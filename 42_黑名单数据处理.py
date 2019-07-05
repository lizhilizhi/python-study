
# coding:utf-8
import re 
import json,requests
import sqlite3

class getbalklist():

    def getphone():
        
        f = open('/Users/apple/Desktop/b.txt').read()
        ret = re.findall(r'1[3567]\d{9}',f)
        return ret


    def getres(ret):
        headers = {'Content-Type':'application/json','appname':'331099344'}
        url = "http://admin-beta.lifengkong.com/rc/api/blacklist-query"
        for row in ret:
            phone = row
            print(phone)
            date = {
                "mobile": phone
                    }
            r = requests.post(url,data=json.dumps(date),headers=headers)  

a = getbalklist.getphone() 
b = getbalklist.getres(a)
