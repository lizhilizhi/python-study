



class School():
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        self.student=[]
        self.teacher =[]

    def enroll(self,stu_obj):
        self.student.append(stu_obj)


class StudentMember():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        
        pass
class Teacher(StudentMember):

    def __init__(self,name,age,sex):
        super(Teacher,self).__init__(name,age,sex)

