# s =  'NcDF,vacldn,ajcjnv'
# print(s[0:4])
# print(s[:-4])

#   0
# N = input("请输入值：")
# N = float(N)
# print(N**32)
#   1
# story  = input("请输入一段句子：")
# for i in story:
#     print(i)
#   2
# number = input("请输入:")
# number = int()
# print(number)
#   3
# N = input("请输入:")
# N = int(N)
# sum = 0
# for i in range(1,N+1):
#     sum += i + 1
# print("1到{}的和为{}".format(N,sum))
#   4 实部和虚部
# x = 3
# y = 4
# c = '{}+{}j'.format(x,y)
# print(c)
# b = 3+4j
# b_real = b.real
# b_imag = b.imag
# print(b_real)
# print(b_imag)


# x = 30
# y = 5.3
# c = x//y  #整数商
# print(c)


#需要单引号又需要双引号时  要用到\转义符

#chr  uincode-->单字符
#ord 单字符-->uincode

# def split(s):
#     return s.split('a')
# if __name__ == '__main__':
#     s = 'an bad bay day'
#     a = s.split()
#     print(a)
b = []
def gys(x, y):
    """该函数返回两个数的最大公约数"""
    global b
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0 :
            print('')
        print(max(i))
# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print('{}和{}的最大公约数为{}'.format(num1,num2,gys(num1,num2)))
