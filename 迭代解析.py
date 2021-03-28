# a = ['sac','sdc','dc','swg']
# print(len(a))
# url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'
# for i in range(0,1000,20):
#     url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + '{}'.format(i) + '&type=T'
#     url = url.format(i)
#     print(url)
#
# url_get = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='
# for i in range(0, 1000, 20):
#     url_pro = url_get + '{}'.format(i) + '&type=T'
#     url = url_pro.format(i)
#     url_wo = {
#         i: url
#     }
#     a = url_wo.values()
# import time
# import random
# a = random.randint(2,6)
#
# print(a)
# a = 4
# for i in range(0,a):
#    filename = r'C:/Users/周述正/Desktop/笔记/English/语法{}.jpg'.format(i)
#    print(filename)
#
# import random
#
# a = random.uniform(35.4,36.6)
# b = '{:.1f}'.format(a)
# print(b)
from multiprocessing import Pool

people = []
classnums = ['021318117','021318118','021318119','021318131']
passages = ['Aa19973628358','Xq242313','LuangLuang21','123456lL']
for i in range(0,len(classnums),1):
    classnum = classnums[i]
    passage = passages[i]
    get_dict = {
        'classnum': classnum,
        'passage': passage
    }
    people.append(get_dict)
def test(get_dict):
    print(get_dict['classnum'],get_dict['passage'])


if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(test, people)
    pool.close()
    pool.join()
