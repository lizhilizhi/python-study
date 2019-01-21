import json

data = {
    'no':1,
    'acc':2
}
#json.dumps(): 对数据进行编码
#json.loads(): 对数据进行解码


json_str = json.dumps(data)
print(data)
print(json_str)

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
# 写入 JSON 数据
# with open('data.json', 'w') as f:
# #     json.dump(data, f)
# #
# # # 读取数据
# # with open('data.json', 'r') as f:
# #     data = json.load(f)