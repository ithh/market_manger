#/usr/bin/python3
#-*-coding:utf-8-*-

import pymysql

db = pymysql.connect("localhost", "root", "123456", "shop")

cursor = db.cursor()

cursor.execute("select * from goods")

data = cursor.fetchall()

#打印获取到的数据
print(data)


#关闭游标和数据库的连接
cursor.close()
db.close()