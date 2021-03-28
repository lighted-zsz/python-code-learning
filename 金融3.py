# 先引入后面可能用到的包（package）
#振德医疗股票
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts


# 正常显示画图时出现的中文
from pylab import mpl
# 这里使用微软雅黑字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 画图时显示负号
mpl.rcParams['axes.unicode_minus'] = False


# 直接在行内显示图形
# codes = ['600519', '601398', '601939', '601318']

sh1 = ts.get_k_data('603301', ktype='M',
autype='qfq', start='2018-12-20')#振德医疗股票代码为603301
sh1.head(5)
sh1.index = pd.to_datetime(sh1.date)


sh1_csv = pd.DataFrame(sh1)
sh1_csv.to_csv('D:\creat.csv')
    # 画出上证指数收盘价的走势
print(sh1)

# print(sh['close'])
sh1['close'].plot(color='r',figsize=(12, 6))
plt.title('股票走势图')
plt.xlabel('日期')
plt.show()
