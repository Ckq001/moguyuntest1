import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, 'config.ini')
print (proDir)
print (configPath)
ft = open(configPath)
data = ft.read()
print (data[:3])

cf = configparser.ConfigParser()
cf.read(configPath)
secs = cf.sections()
print (secs)

options = cf.options("DATABASE")  # 获取某个section名为Mysql-Database所对应的键
print(options)

items = cf.items("DATABASE")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)

host = cf.get("DATABASE", "host")  # 获取[Mysql-Database]中host对应的值
print(host)