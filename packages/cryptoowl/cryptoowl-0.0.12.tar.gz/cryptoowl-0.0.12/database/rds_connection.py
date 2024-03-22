import pymysql
from aws_secret_manager import SecretManager


class RdsConnection:
    def __init__(self, access_key, secret_key, region_name, db_secret_name):
        self.region_name = region_name
        self.access_key = access_key
        self.secret_key = secret_key
        self.db_secret_name = db_secret_name

    def conn(self):
        aws_secret_manager = SecretManager(self.region_name, self.access_key, self.secret_key)
        database_values = aws_secret_manager.get_secret_key_value(self.db_secret_name)

        user = database_values.get('username')
        password = database_values.get('password')
        host = database_values.get('host')
        port = database_values.get('port')
        return pymysql.connect(user=user, password=password, host=host, port=port)

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