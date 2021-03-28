#classmethod方法
#直接接在class下为类属性，用@classmethod，其他是def中的对象方法
class animal:
    ability = ''
    def __init__(self,name,averge_age,attack):
        self.name = name
        self.averge_age = averge_age
        self.attack = attack
    def dog(self):
        if self.name == str:
            print("狗名{}正确".format(self.name))
        else:print("错误")
        if self.averge_age>10 and self.attack<10:
            print("{}是一个可以寿命可以到达{}年，并且可以家养的狗".format(self.name,self.averge_age))
        else:print("{}不适合饲养".format(self.name))
    def monkey(self):
        if self.name == str:
            print("猴名{}正确".format(self.name))
        else:
            print("错误")
        if int(self.averge_age) > 10 and int(self.attack) < 10:
            print("{}是一个可以寿命可以到达{}年，并且可以家养的猴".format(self.name, self.averge_age))
        else:
            print("{}不适合饲养".format(self.name))
    @classmethod
    def synthesis(cls):  #cls为类中参数，不会引入前面对象中的原有参数
        print(cls.ability)
a = input("请输入年龄：")
b = input("请输入攻击力:")
c = animal('汪汪','a','b')
c.dog()

