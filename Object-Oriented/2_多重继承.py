

class People():
    def __init__(self,name):
        self.name = name



class Re():
    def frienf(self,obj):
        print("%s %s" %(self.name,obj.name))


class Man(People,Re):
    def __init__(self,name,mokey):
        super(Man,self).__init__(name)
        self.mokey =mokey
class Woman(People,Re):
    def __init__(self,name,beauty):
        super(Woman,self).__init__(name)
        self.beauty =beauty



m1 = Man(1,10)
w1 = Woman(2,100)
print(m1.name)


m1.frienf(w1)
