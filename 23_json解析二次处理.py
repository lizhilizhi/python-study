import  numpy as np
import json
import yuanshishuju
import jsonpath

a =[1,2,3,33,2,8]
#输出中位数
f = np.sum(a)
print(f)
date = yuanshishuju.data
#取出json中total_amount值
total_amount_list = jsonpath.jsonpath(date,"$..total_amount")
for i in total_amount_list:
    print(i)
sum_total_amount = np.sum(total_amount_list)
print('total_amount之和')
print (sum_total_amount)
print('median_total_amount')
median_total_amount = np.median(total_amount_list)
print(median_total_amount)
#取出sms_cnt
sms_cnt_list= jsonpath.jsonpath(date,"$..sms_cnt")
for i in sms_cnt_list:
    print(i)
sum_sms_cnt = np.sum(sms_cnt_list)
print('sms_cnt之和')
print (sum_sms_cnt)
print('sms_cnt中位数')
median_sms_cnt = np.median(sms_cnt_list)
print(median_total_amount)
print('1111111111111111')
#call_time_detail
#1m时间段内，时长在1min内的通话次数占总通话次数比例
item_1m_list = jsonpath.jsonpath(date,"$.moxie.call_time_detail.[item_1m]")
item_im_list = jsonpath.jsonpath(date,"$.moxie.call_time_detail.[?(@.app_point_zh == '时长在1min内的通话次数')].item_1m")
print(item_im_list)
#1m时间段内，时长在1min内的通话次数
item_1m_list_1s = item_1m_list[2]
item_1m_list_1s = np.array(item_1m_list_1s,dtype='float_')
#1m时间段内，时长在1min内的通话次数总和
item_1m_list_sum = item_1m_list[2:6]
item_1m_list_sum = np.array(item_1m_list_sum,dtype='float_')
item_1m_list_sum = np.sum(item_1m_list_sum)
print('duration_1min_within_1m =', np.true_divide(item_1m_list_1s,item_1m_list_sum))
print(item_1m_list_sum)
print(item_1m_list)


#5位长度的号码发送短信的个数
class 







