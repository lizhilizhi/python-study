#!/usr/local/Cellar/python/3.7.2/bin/python3
import  pymysql

db = pymysql.connect("rm-bp1710pt8uc479581go.mysql.rds.aliyuncs.com","tianli","@tianli123456TL","risk_control_saas_dev")

cursor = db.cursor()

sql = input()
cursor.execute(sql)
date = cursor.fetchall()


for i in date:
    print (i)

db.close()
