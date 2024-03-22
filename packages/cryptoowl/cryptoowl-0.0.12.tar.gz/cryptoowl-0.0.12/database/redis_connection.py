import redis
from aws_secret_manager import SecretManager


class RedisConnection:
    def __init__(self, access_key, secret_key, region_name, redis_secret_name):
        self.region_name = region_name
        self.access_key = access_key
        self.secret_key = secret_key
        self.redis_secret_name = redis_secret_name

    def conn(self):
        aws_secret_manager = SecretManager(self.region_name, self.access_key, self.secret_key)
        redis_values = aws_secret_manager.get_secret_key_value(self.redis_secret_name)
        host = redis_values.get('host')
        port = redis_values.get('port')

        try:
            red_conn = redis.StrictRedis(host=host, port=port)
            return red_conn
        except redis.ConnectionError as e:
            print(f"Redis Connection Error: {e}")
        except redis.RedisError as e:
            print(f"Redis Error: {e}")

    def get(self, key):
        conn = self.conn()
        return conn.get(key)

    def set(self, key, data, ex_time):
        conn = self.conn()
        conn.set(key, data, ex=ex_time)