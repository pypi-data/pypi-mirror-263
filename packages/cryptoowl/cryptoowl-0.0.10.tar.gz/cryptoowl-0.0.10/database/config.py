import os

from dotenv import load_dotenv

from aws_utils import get_write_db_secret, get_read_db_secret, get_cache_query

load_dotenv()

write_db_secret = get_write_db_secret()
read_db_secret = get_read_db_secret()
cache_query_secret = get_cache_query()


class Config:
    """ All the configurations and variable related to the script """
    DATABASE_USER = write_db_secret.get('username')
    DATABASE_PASS = write_db_secret.get('password')
    DATABASE_PORT = write_db_secret.get('port')
    DATABASE_WRITE_HOST = write_db_secret.get('host')
    DATABASE_READ_HOST = read_db_secret.get('host')

    ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
    REGION_NAME = os.getenv('REGION_NAME')

    REDIS_ENDPOINT = os.getenv('REDIS_ENDPOINT')
    REDIS_PORT = os.getenv('REDIS_PORT')

    PAIR_DATA_QUERY = cache_query_secret.get('pairs_query')