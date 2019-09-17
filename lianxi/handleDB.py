# coding: utf-8

from readConfig import ReadConfig
import pymysql.cursors


class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        host = self.data.Database("host")
        user = self.data.Database("user")
        password = self.data.Database("password")
        database = self.data.Database("database")
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, data):
        """执行操作数据的相关sql"""
        self.conn_mysql()
        self.cur.execute(sql, data)
        self.conn.commit()

    def search(self, sql):
        """执行查询sql"""

        self.conn_mysql()

        self.cur.execute(sql)
        return self.cur.fetchall()

    def close_mysql(self):
        """关闭数据库连接"""
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    sql = ReadConfig().Mysql("user_id")
    test = HandleMysql().search(sql)
    print(test)