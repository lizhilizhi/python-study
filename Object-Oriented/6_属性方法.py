




class  Dog():
    def __init__(self,name):
        self.name  = name
    @property
    def eat(cls):
        pass
    # 在属性方法中添加参数
    @eat.setter
    def eat(self,food):
        pass
    @eat.deleter
    def eat(self):
         del pass

    def sing(self):
        pass



# 值


# 属性方法 将一个方法变成一个静态属性
# 方法调用错误
# d = Dog(1)
# d.eat()
# 属性的调用
d = Dog(1)
d.eat
