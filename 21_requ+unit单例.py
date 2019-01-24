import unittest
import requests
import json
url1 = 'http://192.168.30.61:7001/rc/v1/merchant/message/read/:msgId'
head = {"Authorization":"test-env"}
data ={}



class ApiTestCase(unittest.TestCase):
    # def __init__(self):
    #     global  url2,head2,data2
    #     url2 = url1
    #     head2 = head
    #     data2 = data
    def testgetmsgid(self):
        r = requests.get(url1)
        print (r.status_code)

if __name__ == '__main__':
    unittest.main(verbosity=2)




