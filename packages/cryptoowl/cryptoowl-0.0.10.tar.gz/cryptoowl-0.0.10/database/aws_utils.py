import json
import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

from constants import REGION_NAME, SOCIAL_INTELLIGENCE_DB_SECRET_ID, SOCIAL_INTELLIGENCE_READ_DB_SECRET_ID, \
    CACHE_QUERY_SECRET_ID

load_dotenv()


def get_secrets_manager_client():
    print('INFO: In secrets_manager_client')
    try:
        session = boto3.session.Session(aws_access_key_id=os.getenv('ACCESS_KEY'),
                                        aws_secret_access_key=os.getenv('SECRET_KEY'))
        return session.client(service_name='secretsmanager', region_name=REGION_NAME)
    except Exception as e:
        print(f'ERROR: {e}')
        raise e


def get_write_db_secret():
    print('INFO: In get_write_db_secret')
    client = get_secrets_manager_client()
    try:
        get_secret_value_response = client.get_secret_value(SecretId=SOCIAL_INTELLIGENCE_DB_SECRET_ID)
    except ClientError as e:
        print(f'ERROR: {e}')
        raise e

    return json.loads(get_secret_value_response['SecretString'])


def get_read_db_secret():
    print('INFO: In get_read_db_secret')
    client = get_secrets_manager_client()
    try:
        get_secret_value_response = client.get_secret_value(SecretId=SOCIAL_INTELLIGENCE_READ_DB_SECRET_ID)
    except ClientError as e:
        print(f'ERROR: {e}')
        raise e

    return json.loads(get_secret_value_response['SecretString'])


def get_cache_query():
    print('INFO: In get_cache_query')
    client = get_secrets_manager_client()
    try:
        get_secret_value_response = client.get_secret_value(SecretId=CACHE_QUERY_SECRET_ID)
    except ClientError as e:
        print(f'ERROR: {e}')
        raise e

    return json.loads(get_secret_value_response['SecretString'])
