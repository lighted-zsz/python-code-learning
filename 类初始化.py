class Student:
    def __init__(self):  # 类似于c++中的默认构造函数
        self.name = None  #这里的name和grade是属性值
        self.grade = None

    def print_grade(self):
        print("%s grade is %s" % (self.name, self.grade))


s1 = Student()  # 创建对象s1
s1.name = "Tom"
s1.grade = 8

s2 = Student()  # 创建对象s2
s2.name = "Jerry"
s2.grade = 7

s1.print_grade()
s2.print_grade()



#传多个参数
class Student_Grade:
    def __init__(self, name, grade):  #类似于C++中的有参构造函数
        self.name = name
        self.grade = grade

    def print_grade(self):
        print("%s grade is %s" % (self.name,self.grade))

s1 = Student("Tom", 8)  # 创建对象s1
s2 = Student("Jerry", 7)  # 创建对象s2

s1.print_grade()
s2.print_grade()





    
