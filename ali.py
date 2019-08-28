from aliyunsdkcore import client
from aliyunsdksaf.request.v20180919 import ExecuteRequestRequest
clt = client.AcsClient('<your-access-key-id>','<your-access-key-secret>','cn-shanghai')
request = ExecuteRequestRequest.ExecuteRequestRequest()
request.set_accept_format('json')
# 产品service请参考[公共参数]文档中的Service字段描述
request.add_query_param('Service', '购买的产品service')
request.add_query_param('ServiceParameters', 'json串')
# 发起请求
response = clt.do_action_with_exception(request)
print(response)
