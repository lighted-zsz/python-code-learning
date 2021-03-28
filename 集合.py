a = {1020,'1020',28,80}
b = {67,1,28,1020,83,20,80}

#集合的交集，并集，补集，差集
print(a-b)
print(a|b)
print(a&b)
print(a^b)


#set函数可以将任何数据集合变换为集合类型
c = [1,2,3,4,5]
c = set(c)
print(c)
d = ['a','d','e','o','pxp']
print(d*3) #复制三次