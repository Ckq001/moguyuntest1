#  -*- coding:utf-8 -*-
import pymysql
from readConfig import ReadConfig


mysql = ReadConfig()


#db = pymysql.connect(host,user,passwd,database,charset="utf8")

class MysqlDb:
    def __init__(self):
        self.host = mysql.Database("host")
        self.user = mysql.Database("user")
        self.passwd = mysql.Database("passwd")
        self.database = mysql.Database("database")
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.database,charset="utf8")

    def user_id(self):
        cursor = self.db.cursor()
        sql = mysql.Mysql("user_id")
        cursor.execute(sql)                    #db.commit()提交到数据库执行
        data = cursor.fetchone()               #cursor
        return data