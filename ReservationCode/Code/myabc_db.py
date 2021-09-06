import configparser

import MySQLdb


class MyABC_db():
    def __init__(self, db_config_file, db):
        config = configparser.ConfigParser()
        config.read(db_config_file, encoding='utf-8')
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        password = config[db]['password']
        database = config[db]['database']
        charset = config[db]['charset']

        self.conn = MySQLdb.connect(host=host, port=port, user=user, password=password,
                                    database=database,
                                    charset=charset)
        # self.cursor = self.conn_db.cursor()

    def close(self):
        self.conn.close()

    def select_record(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        c = cursor.fetchall()
        return c

    def insert_record(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            cursor.execute('commit')
        except Exception as e:
            print('插入数据库失败：%s' % e)
            cursor.execute('rollback')
            cursor.close()
            exit()

    def select_record_fetchone(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        c = cursor.fetchone()
        return c
