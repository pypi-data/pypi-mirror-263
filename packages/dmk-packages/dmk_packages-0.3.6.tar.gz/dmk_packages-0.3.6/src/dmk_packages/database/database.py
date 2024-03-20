import os

import psycopg2
from dotenv import find_dotenv, load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv(dotenv_path=find_dotenv())


def __get_db_info(target: str):
    host = os.environ.get(f"{target}_DB_HOST")
    port = os.environ.get(f"{target}_DB_PORT")
    database = os.environ.get(f"{target}_DB_NAME")
    username = os.environ.get(f"{target}_DB_USERNAME")
    password = os.environ.get(f"{target}_DB_PASSWORD")

    if None in (host, port, database, username, password):
        raise Exception(f"{target}에 대한 환경변수를 제대로 입력해주세요.")

    return host, port, database, username, password


def get_conn(target: str):
    try:
        host, port, database, username, password = __get_db_info(target=target)

        return psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=username,
            password=password,
        )
    except Exception as error:
        logger.error(error)


def get_engine(target: str, drivername: str = "postgresql+psycopg2"):
    try:
        host, port, database, username, password = __get_db_info(target=target)

        dsn = URL.create(
            host=host,
            port=port,
            database=database,
            username=username,
            password=password,
            drivername=drivername,
        )
        return create_engine(dsn)
    except Exception as error:
        logger.error(error)
