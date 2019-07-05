const fs = require('fs')
const container = []
const tmplate = `{
    "applyTime": "2019-05-14 11:21:08",
    "borrowerModel": "550",
    "createTime": "2019-05-14 11:21:08",
    "instalments": [
        {
            "createTime": "2019-05-14 11:21:08",
            "dueTime": "2019-05-14 11:21:08",
            "lateFee": "0",
            "overdue": "false",
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
    "orderId": "3687f612-2e3b-4da5-8ba6-c357b670879a",
    "realName": "James",
    "updateTime": "2019-05-14 11:21:08"
}`

function randomString(len) {
    const length = len || 32
    const chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    const maxPos = chars.length
    let pwd = ''
    for (let i = 0; i < length; i++) {
        pwd += chars.charAt(Math.floor(Math.random() * maxPos))
    }
    return pwd
}

for(let i = 0; i< 5000; i++) {
    const item = JSON.parse(tmplate)
    item.orderId = randomString(36)
    container.push(item)
}

const outPut = {
    "result": container,
    "resultMsg": "请求成功",
    "success": "true"
}

fs.writeFileSync('./output.json', JSON.stringify(outPut))