import base64
import hashlib
import hmac
import json

import pendulum
import requests
from loguru import logger
from sqlalchemy import text

from dmk_packages import database as db


class NaverSearchVolumeCrawler:
    DATALAB_URL = "https://openapi.naver.com/v1/datalab/search"
    SEARCHAD_URL = "https://api.naver.com/keywordstool"
    LESS_THAN_10 = "< 10"
    DEFAULT_DT = pendulum.yesterday(tz="Asia/Seoul")

    def __init__(self, date_from=None, date_until=None, target="MADERI_AUTH"):
        self._engine = db.get_engine(target)
        self._datalab_key = self.__get_datalab_key()
        self._searchad_key = self.__get_searchad_key()

        self._target_dt_range = []
        self._target_dt_from = (
            pendulum.parse(date_from) if date_from else self.DEFAULT_DT
        )
        self._target_dt_until = (
            pendulum.parse(date_until) if date_until else self.DEFAULT_DT
        )
        self._target_kwds = None
        self._target_kwds_bundle = None

    def __get_searchad_key(self):
        # TODO: 사용 가능한 key가 없을 때 어떻게 반환되는지 확인 및 반영 필요
        query = """
        SELECT id, customer_id, access_license, private_key
        FROM t_auth_naver_searchad_key_v2
        WHERE is_valid
        ORDER BY RANDOM()
        LIMIT 1;
        """

        with self._engine.begin() as connection:
            result = connection.execute(text(query))

        key_id, customer_id, access_license, private_key = result.fetchone()

        return {
            "key_id": key_id,
            "customer_id": customer_id,
            "access_license": access_license,
            "private_key": private_key,
        }

    def __get_datalab_key(self):
        # TODO: 사용 가능한 key가 없을 때 어떻게 반환되는지 확인 및 반영 필요
        query = """
        SELECT id, client_id, client_secret
        FROM t_auth_naver_datalab_key_v2
        WHERE is_auth AND is_active
        ORDER BY RANDOM()
        LIMIT 1;
        """

        with self._engine.begin() as connection:
            result = connection.execute(text(query))

        key_id, client_id, client_secret = result.fetchone()

        return {
            "key_id": key_id,
            "client_id": client_id,
            "client_secret": client_secret,
        }

    # NOTE: 검색광고 API에 대해서는 제한량이 없다고 하여 사용이 안될 수 있다.
    # TODO: 하지만 만약 그외의 이유로 키를 사용하지 못하게 될 경우를 대비해야한다.
    def __update_searchad_key(self, pk_id, feather):
        try:
            if self._engine is None:
                raise Exception("인증 정보 DB에 접근할 수 없습니다.")

            if feather not in ["valid"]:
                raise Exception("사용할 수 없는 feather입니다.")

            query = f"""
                    UPDATE t_auth_naver_searchad_key_v2
                    SET is_{feather} = FALSE, failed_{feather}_at = CURRENT_DATE
                    WHERE id = {pk_id};
                    """

            with self._engine.begin() as connection:
                connection.execute(text(query))

        except Exception as error:
            raise Exception(error)

    def __update_datalab_key(self, pk_id, feather):
        try:
            if self._engine is None:
                raise Exception("인증 정보 DB에 접근할 수 없습니다.")

            if feather not in ["valid"]:
                raise Exception("사용할 수 없는 feather입니다.")

            query = f"""
                    UPDATE t_auth_naver_datalab_key_v2
                    SET is_{feather} = FALSE, failed_{feather}_date = CURRENT_DATE
                    WHERE id = {pk_id};
                    """

            with self._engine.begin() as connection:
                connection.execute(text(query))

        except Exception as error:
            raise Exception(error)

    def _set_date_range(self, target_date):
        try:
            # NOTE: 30일전 날짜를 구해야한다.
            # 타겟날짜도 포함하기에 코드에서는 29일을 차감한다.
            date_thirty_days_ago = target_date.subtract(days=29)

            self._target_dt_range.append([date_thirty_days_ago, target_date])

            if self._target_dt_from < date_thirty_days_ago:
                return self._set_date_range(date_thirty_days_ago.subtract(days=1))
        except Exception as error:
            logger.error(error)

    def _set_kwds(self, keywords):
        self._target_kwds = keywords

    def _set_kwds_bundle(self, keywods: list[str]):
        try:
            keywods_bundle = [keywods[i : i + 5] for i in range(0, len(keywods), 5)]
            self._target_kwds_bundle = keywods_bundle
        except Exception as error:
            logger.error(error)

    def get_kwds(self):
        """해당 메서드를 오버라이딩하여 키워드를 불러온다."""

        return []

    # TODO: keywords_bundle이 5개 이상이면 에러 배출하기
    # TODO: 반환 타입 넣어주기 - [{'relKeyword': '룰루', 'monthlyPcQcCnt': 1030, 'monthlyMobileQcCnt': 5300}, {'relKeyword': '호롤', 'monthlyPcQcCnt': 10, 'monthlyMobileQcCnt': 30}]
    def get_searchad_data(self, keywords_bundle: list[str]):
        """
        네이버 검색광고 API 데이터 가져오기

        API 문서: https://naver.github.io/searchad-apidoc/#/tags/RelKwdStat
        """
        try:
            hint_keywords = ",".join(
                [k.replace(" ", "").upper() for k in keywords_bundle]
            )
            hint_keywords_map = {k.replace(" ", "").upper(): k for k in keywords_bundle}

            timestamp = str(round(pendulum.now().timestamp() * 1000))
            signature = base64.b64encode(
                hmac.new(
                    bytes(self._searchad_key["private_key"], "UTF-8"),
                    bytes(f"{timestamp}.GET./keywordstool", "UTF-8"),
                    digestmod=hashlib.sha256,
                ).digest()
            )

            headers = {
                "Content-Type": "application/json; charset=UTF-8",
                "X-Timestamp": timestamp,
                "X-API-KEY": self._searchad_key["access_license"],
                "X-Customer": self._searchad_key["customer_id"],
                "X-Signature": signature,
            }

            response = requests.get(
                url=self.SEARCHAD_URL,
                headers=headers,
                params={"hintKeywords": hint_keywords},
            )

            if not response.ok:
                raise Exception(response.json().get("title"))

            target_keyword_hits = 0
            searchad_data = []
            result = response.json()

            for kwd in result.get("keywordList"):
                if kwd["relKeyword"] in hint_keywords_map:

                    kwd["monthlyPcQcCnt"] = (
                        kwd["monthlyPcQcCnt"]
                        if kwd["monthlyPcQcCnt"] != self.LESS_THAN_10
                        else 9
                    )
                    kwd["monthlyMobileQcCnt"] = (
                        kwd["monthlyMobileQcCnt"]
                        if kwd["monthlyMobileQcCnt"] != self.LESS_THAN_10
                        else 9
                    )

                    searchad_data.append(
                        {
                            "keyword": hint_keywords_map[kwd["relKeyword"]],
                            "monthlyPcQcCnt": kwd["monthlyPcQcCnt"],
                            "monthlyMobileQcCnt": kwd["monthlyMobileQcCnt"],
                        }
                    )

                    target_keyword_hits += 1
                    if target_keyword_hits == len(keywords_bundle):
                        break
            return searchad_data
        except Exception as error:
            logger.error(error)

    # TODO: keywords_bundle이 5개 이상이면 에러 배출하기
    def get_datalab_data(self, keywords_bundle: list[str], start_dt, end_dt):
        """
        네이버 데이터랩 API 데이터 가져오기

        API 문서: https://developers.naver.com/docs/serviceapi/datalab/search/search.md#python
        """
        try:
            datalab_data = []

            headers = {
                "X-Naver-Client-Id": self._datalab_key["client_id"],
                "X-Naver-Client-Secret": self._datalab_key["client_secret"],
                "Content-Type": "application/json",
            }
            body = {
                "startDate": start_dt,
                "endDate": end_dt,
                "timeUnit": "date",
                "keywordGroups": [
                    {"groupName": k, "keywords": [k]} for k in keywords_bundle
                ],
            }
            response = requests.post(
                url=self.DATALAB_URL, headers=headers, data=json.dumps(body)
            )

            if response.status_code == 401:
                # NOTE: 인증 실패시 업데이트
                self.__update_datalab_key(self._datalab_key["key_id"], "auth")
                return self.get_datalab_data(keywords_bundle, start_dt, end_dt)
            elif response.status_code == 429:
                #  NOTE: 호출 한도 초과시 업데이트
                self.__update_datalab_key(self._datalab_key["key_id"], "active")
                return self.get_datalab_data(keywords_bundle, start_dt, end_dt)

            results = response.json().get("results")
            for result in results:
                keyword = result.get("title", "")
                data = result.get("data", [])

                temp_data = data.copy()
                existing_dates = {d["period"] for d in data}

                start_date = pendulum.from_format(start_dt, "YYYY-MM-DD")
                end_date = pendulum.from_format(end_dt, "YYYY-MM-DD")

                current_date = start_date
                while current_date <= end_date:
                    current_date_str = current_date.strftime("%Y-%m-%d")
                    if current_date_str not in existing_dates:
                        temp_data.append({"period": current_date_str, "ratio": 0.0})
                    current_date = current_date.add(days=1)

                temp_data.sort(key=lambda x: x["period"])
                datalab_data.append({"keyword": keyword, "data": temp_data})
            return datalab_data
        except Exception as error:
            logger.error(error)

    def calc_search_volume(self, keywords_bundle, searchad_data, datalab_data):
        try:
            search_volume = []

            for kwd in keywords_bundle:
                target_searchad_datum = [
                    d for d in searchad_data if d["keyword"] == kwd
                ]
                target_datalab_datum = [d for d in datalab_data if d["keyword"] == kwd]

                if target_searchad_datum and target_datalab_datum:
                    monthly_pc_volume = target_searchad_datum[0].get("monthlyPcQcCnt")
                    monthly_mo_volume = target_searchad_datum[0].get(
                        "monthlyMobileQcCnt"
                    )

                    total_volume = monthly_pc_volume + monthly_mo_volume
                    total_ratio = sum(
                        [d["ratio"] for d in target_datalab_datum[0].get("data")]
                    )

                    volume_per_ratio = (
                        total_volume / total_ratio if total_ratio > 0 else 0
                    )

                    for d in target_datalab_datum[0].get("data"):
                        new_data = {
                            "keyword_text": kwd,
                            "keyword_date": pendulum.parse(
                                d["period"], tz="Asia/Seoul"
                            ),
                            "keyword_volume": int(d["ratio"] * volume_per_ratio),
                            "collected_at": pendulum.today(),
                        }
                        search_volume.append(new_data)
            return search_volume
        except Exception as error:
            logger.error(error)

    def get_search_volume(self):
        try:
            results = []

            self._set_date_range(target_date=self._target_dt_until)

            self._set_kwds(self.get_kwds())
            self._set_kwds_bundle(keywods=self._target_kwds)

            for kwds_bundle in self._target_kwds_bundle:
                searchad_data = self.get_searchad_data(kwds_bundle)

                for date_range in self._target_dt_range:
                    start_dt, end_dt = [d.strftime("%Y-%m-%d") for d in date_range]
                    datalab_data = self.get_datalab_data(kwds_bundle, start_dt, end_dt)

                    search_volume = self.calc_search_volume(
                        kwds_bundle, searchad_data, datalab_data
                    )
                    results.extend(search_volume)
            return results
        except Exception as error:
            logger.error(error)


if __name__ == "__main__":
    naver_search_volume_crawler = NaverSearchVolumeCrawler()
    search_volume = naver_search_volume_crawler.get_search_volume()

    for vol in search_volume:
        logger.debug(vol)
