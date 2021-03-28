class fun:
    # self.属性名1 = 形参1
    # self.属性名2 = 形参2
    #只要有某个self.属性名 = 形参的定义，那么就可以使用这形参，传形参
    def __init__(self):
        pass
    def first(self,name,age):  #其中name，age是共有的属性参数
        self.name = name
        self.age = age
    def qulification(self):
        print("{}今年{}岁".format(self.name,self.age)) #不能传入其他的self形参,否则报错
    def detail(self,sex,number,teacher):  #也可以在普通的一般方法中有自己的形参变量
        self.sex = sex
        self.number = number
        self.teacher = teacher
        print("性别：{}，班号为{}，老师是{}".format(self.sex,self.number,self.teacher))
b = fun()
b.first('zsz',19)
b.qulification()
b.detail('男','','')
