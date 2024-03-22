import boto3
import pymysql
import redis

from config import Config


class Database:
    def __init__(self, user, password, host, port):
        """ Initialize the connection and create the cursor object """
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conn(self):
        return pymysql.connect(user=self.user, password=self.password, host=self.host, port=self.port)

    @staticmethod
    def cursor(conn):
        """ Return the cursor object """
        return conn.cursor()

    def execute_query(self, query, values=''):
        """ Execute the query """
        conn = self.conn()
        try:
            cursor = self.cursor(conn=conn)
            cursor.execute(query, values)
            conn.commit()
            return cursor
        finally:
            conn.close()

    def fetchall(self, query, values=None):
        """ Execute the query and fetch all data """
        try:
            cursor = self.execute_query(query=query, values=values)
            return cursor.fetchall()
        except Exception as e:
            print(f'ERROR: {str(e)}')
            return []


class Redis:
    def __init__(self, host, port):
        """ Initialize the connection and create the cursor object """
        self.host = host
        self.port = port

    def conn(self):
        try:
            red_conn = redis.StrictRedis(host=self.host, port=self.port)
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


read_db = Database(user=Config.DATABASE_USER, password=Config.DATABASE_PASS, host=Config.DATABASE_READ_HOST,
                   port=Config.DATABASE_PORT)

write_db = Database(user=Config.DATABASE_USER, password=Config.DATABASE_PASS, host=Config.DATABASE_WRITE_HOST,
                    port=Config.DATABASE_PORT)

ts_session = boto3.Session(aws_access_key_id=Config.ACCESS_KEY_ID, aws_secret_access_key=Config.SECRET_ACCESS_KEY,
                           region_name=Config.REGION_NAME)

redis_db = Redis(host=Config.REDIS_ENDPOINT, port=Config.REDIS_PORT)