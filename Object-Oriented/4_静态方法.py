





class Dog():
    def __init__(self,name):
        self.name = name
    @staticmethod #实际上和类没什么关系 静态方法，通过类直接调用，不需要创建对象，不会隐式传递self
    def eat():
        print("11")



    # 调用不了实例的变量了 函数已经和类没关系了
    # @staticmethod
    # def eat(self):
    # 报错



