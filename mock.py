# /usr/bin/env python
# -*- coding:utf-8 -*-


from flask import  jsonify, Flask

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

tasks = {
    "success": "true",
    "resultMsg": "请求成功",
    "result": "1000"
}

@app.route('/task', methods=['GET','POST'])
def get_task():

    return jsonify(tasks)


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 6868,
        debug = True
    )
