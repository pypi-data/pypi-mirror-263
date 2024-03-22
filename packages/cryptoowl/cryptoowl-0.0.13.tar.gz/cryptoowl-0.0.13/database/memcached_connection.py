import ssl
import json

from pymemcache.client.base import Client
from aws_secret_manager import SecretManager

context = ssl.create_default_context()


class MemcachedConnection:
    def __init__(self, access_key, secret_key, region_name, memcached_secret_name):
        self.region_name = region_name
        self.access_key = access_key
        self.secret_key = secret_key
        self.memcached_secret_name = memcached_secret_name

    def get_client(self):
        aws_secret_manager = SecretManager(self.region_name, self.access_key, self.secret_key)
        memcached_values = aws_secret_manager.get_secret_key_value(self.memcached_secret_name)
        host = memcached_values.get('host')
        port = memcached_values.get('port')
        return Client((host, port), tls_context=context)

    def set_data_into_memcache(self, key, data, ttl):
        client = self.get_client()
        json_data = json.dumps(data, default=str)

        client.set(key, json_data, expire=ttl)
        print(f"INFO: Data set to memcached: {data}")

    def get_data_from_memcached(self, key):
        client = self.get_client()
        cached_data = client.get(key)

        if cached_data:
            data = json.loads(cached_data)
            print(f"INFO: Data got from memcached: {data}")
            return data, True

        return None, None
