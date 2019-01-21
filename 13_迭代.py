#一个循环
for i in range(5):
    print(i)
#一个循环
for i in range(1,10):
    print (i)
# 定义一个数组
def table(n):
    uu =[]
    for i in range(n):
        uu.append(i*i)
    return uu
table =table(4)

print (table[:9])