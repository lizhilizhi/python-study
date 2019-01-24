import requests
import json
import shuju
url = 'http://fengdun-merchant-dev-api.51xfei.com/rc/api/callService'
head ={"AppName":"912594966","productId":"3359c1a01d4511e994e4b14fa49acab7"}
# global null
# null = ""
data = shuju.data



r = requests.post(url = url ,json = data , headers = head)

print (r.status_code)