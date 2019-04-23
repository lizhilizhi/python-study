# 字典

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "国贸":["hp","cicc"]
        }
    },
    '杭州':{
        "西湖区":{
            "滨江":["yaxin","test"]
        }
    }
}


while True:
    for i in data:
        print(i)

    choice = input("选择进入>>:")
    if choice in data:
        while True:
            for j in data[choice]:
                print("\t", j)
                choice2 = input("选择进入>>:")
                if choice2 in data[choice]:
                    for e in data[choice][choice2]:
                        print("\t", e)





