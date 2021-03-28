#先引入后面可能用到的包（package）
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文
from pylab import mpl
#这里使用微软雅黑字体
mpl.rcParams['font.sans-serif']=['SimHei']
#画图时显示负号
mpl.rcParams['axes.unicode_minus']=False
import tushare as ts
#Jupyter Notebook特有的magic命令
#直接在行内显示图形
codes = ['600519','601398','601939','601318']
for code in codes:
  sh=ts.get_k_data(code,ktype='D',
   autype='qfq', start='2000-12-20')
  sh.head(5)
  # 将数据列表中的第0列'date'设置为索引
  sh.index = pd.to_datetime(sh.date)
  # 画出上证指数收盘价的走势
  # print(sh)
  print(sh['close'])
  sh['close'].plot(figsize=(12, 6))
  plt.title('股票走势图')
  plt.xlabel('日期')
  plt.show()
