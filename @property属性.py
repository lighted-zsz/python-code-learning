#@property 在类函数上使用，可以在调用成员函数的时候，直接使用名称即可
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def get_name(self):
        return self._name

def test():
    p = Person("张三",25)
    name = p.get_name
    print(name)

test()
