import json
import boto3
from botocore.exceptions import ClientError

SERVICE_NAME = 'secretsmanager'


class SecretManager:

    def __init__(self, access_key, secret_key, region_name):
        self.region_name = region_name
        self.access_key = access_key
        self.secret_key = secret_key

    def get_secrets_manager_client(self, ):
        print('INFO: In secrets_manager_client')
        try:
            session = boto3.session.Session(aws_access_key_id=self.access_key,
                                            aws_secret_access_key=self.secret_key)
            return session.client(service_name=SERVICE_NAME, region_name=self.region_name)
        except Exception as e:
            print(f'Exception while creating secrets_manager_client: {e}')
            raise e

    # Retrieves the secret value for the given secret name from AWS Secrets Manager.
    def get_secret_key_value(self, secret_name):
        print(f"INFO: In get_secret_key_value for: {secret_name}")
        client = self.get_secrets_manager_client()
        try:
            get_secret_key_value_response = client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            print(f"An error occurred while retrieving the secret for {secret_name}: {e}")
            raise e

        return json.loads(get_secret_key_value_response['SecretString'])
