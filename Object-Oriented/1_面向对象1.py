

# 构造函数
# class dog():
#     n = 300
#     n_list =[]
#     def __init__(self,name):
#         self.name = name
#     def bulk(self):
#         print("%s 叫" %self.name)
#
# r1 = dog(1)
#
# r1 = dog(1)
#
# r1.n_list.append("123")
# r1.n_list=[]
# r2 = dog(1)
#
# r2.n_list.append("456")
#
#
# print(r1.n_list,r2.n_list,dog.n_list)


# 析构函数：在实例释放，销毁的时候执行的，通常用于做一些扫尾工作，关闭一些数据库连接，打开的临时文件
class dog():
    n = 300
    n_list =[]
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("%s 叫" %self.name)
    def __del__(self):
        print("析构函数")
    def bulk1(self):
        print("%s 叫" %self.name)

r1 = dog(1)

r1.bulk1()
