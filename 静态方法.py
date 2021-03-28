class sample:
    age = 13  #可以通过外部类方法改变age值，sample.age = 30
    _age = 15 #只能通过改变类方法中的值修改_age
    def __init__(self,name):
        self.name = name
        print("年龄为{}".format(self.age))
    @classmethod
    def fir(cls):
        cls._age = 30 #
        print("年龄为{}".format(cls.age))
sample.age = 20








