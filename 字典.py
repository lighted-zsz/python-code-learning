a = {"1":"zsz",'2':'zse','3':'zsa','4':'zsaq','5':'zsda'}
b = a.keys() #dict_keys(['1', '2', '3', '4', '5'])
print(b)

c = a.values() #dict_values(['zsz', 'zse', 'zsa', 'zsaq', 'zsda'])
print(c)

d = a.items()#dict_items([('1', 'zsz'), ('2', 'zse'), ('3', 'zsa'), ('4', 'zsaq'), ('5', 'zsda')])
print(d)

e = a.get('5',None) #键值’5‘存在，所以返回其对应的值，否则会返回None
print(e)

f = a.pop('1','不存在') #zsz
print(a)              # {'2': 'zse', '3': 'zsa', '4': 'zsaq', '5': 'zsda'}
print(f)              #将’1‘对于的键值对删除  将’1‘对应的键值对显示出来
print(a)

print(a.popitem())  #随机取出一个键值对
