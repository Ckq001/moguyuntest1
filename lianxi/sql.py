#!/usr/bin/python3

import pymysql

# 打开数据库连接

db = pymysql.connect("192.168.0.2","admin268xue","admin268xue","pg_test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询

sql = """SELECT
        rd.project_id AS projectId,
        rd.audit_type AS auditType,
        u.userName,
        u.mobile,
        rd.is_accept AS isAccept 
    FROM
        report_distribution rd
        INNER JOIN sysuser u ON u.id = rd.user_id 
        AND u.`status` = 1 
    WHERE
        rd.STATUS = 1 
        AND rd.project_id = 15274021 
    ORDER BY
        rd.audit_type;"""
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % (data,))
for r in range(len(data)):
    print(list(data)[3])

# 使用 fetchall() 方法获取所有数据.
rs=cursor.fetchall()
for r in rs:
    print(r)

# 关闭数据库连接
db.close()