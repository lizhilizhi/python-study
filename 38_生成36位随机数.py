data = {
    "success":"true",
    "resultMsg":"请求成功",
    "result":[
        {
            "orderId":"3687f612-2e3b-4da5-8ba6-c357b670879a",
            "mobile":"13329215678",
            "realName":"James",
            "borrowerModel":"550",
            "applyTime":"2019-05-14 11:21:08",
            "loanAmount":"1000",
            "loanStatus":1,
            "loanTime":"2019-05-14 11:21:08",
            "instalments":[
                {
                    "period":1,
                    "dueTime":"2019-05-14 11:21:08",
                    "overdue":"true",
                    "repayAmount":"1000",
                    "lateFee":"0",
                    "repayTime":"2019-05-15 11:21:08",
                    "createTime":"2019-05-14 11:21:08",
                }
            ],
            "createTime":"2019-05-14 11:21:08",
            "updateTime":"2019-05-14 11:21:08"
        },
        {
            "applyTime": "2019-05-14 11:21:08",
            "borrowerModel": "550",
            "createTime": "2019-05-14 11:21:08",
            "instalments": [
                {
                    "createTime": "2019-05-14 11:21:08",
                    "dueTime": "2019-05-14 11:21:08",
                    "lateFee": "0",
                    "overdue": "true",
                    "period": 1,
                    "repayAmount": "1000",
                    "repayTime": "2019-05-15 11:21:08",
                    "updateTime": "2019-05-14 11:21:08"
                }
            ],
            "loanAmount": "1000",
            "loanStatus": 1,
            "loanTime": "2019-05-14 11:21:08",
            "mobile": "13329215678",
            "orderId": "3687f612-2e3b-4da5-8ba6-c357b6708793",
            "realName": "James",
            "updateTime": "2019-05-14 11:21:08"
        }
    ]
}


import json
import codecs

j = json.dumps(data,ensure_ascii=False)

with codecs.open('./Gongzai1.json', "w", "utf-8") as f:
    f.write(j)


