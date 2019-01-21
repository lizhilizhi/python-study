import  pymysql
import xlwt


db = pymysql.connect("rm-bp1710pt8uc479581go.mysql.rds.aliyuncs.com","tianli","@tianli123456TL","risk_control_saas_dev")

cursor = db.cursor()

sql ="select * from admin_role where id = 30 "
cursor.execute(sql)
date = cursor.fetchall()

for row in date:
    id = row[0]
    role = row[1]
    enable = row[2]
    desc = row[3]
    created = row[4]
    update = row[5]
print(row)
print(row[5])

sqlresult = xlwt.Workbook()

sheet = sqlresult.add_sheet('id')
for r in range(10):
    if r <= 5:
        sheet.write(r,r,row[r])
    else:
        print('wancheng')


sqlresult.save('id1.xls')

