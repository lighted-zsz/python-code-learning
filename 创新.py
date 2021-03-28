# 导入相关库
import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 可以在画图时正常显示出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 设置token
token = '5cbbc9bbd236fcad420d342a6628bb7833d5022fd3a5e5dbe1cdc5b7'
pro = ts.pro_api(token)
# 获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code, symbol, name, area, industry, list_date')
# 查看前五行数据
print(data.head(5))

# 获取万科日行情数据并查看前五条数据信息
wk = pro.daily(ts_code='000002.SZ', start_date='20200101',
               end_date='20200416')
print(wk.head())

# 指数数据：pro.index_daily()
def get_index_data(indexs):
    '''indexs是字典格式'''
    index_data = {}
    for name, code in indexs.items():
        df = pro.index_daily(ts_code=code)
        df.index = pd.to_datetime(df.trade_date)
        index_data[name] = df.sort_index()
    return index_data

# 获取常见股票指数行情
indexs = {'上证综指': '000001.SH', '深证成指': '399001.SZ',
          '沪深300': '000300.SH', '创业板指': '399006.SZ',
          '上证50': '000016.SH', '中证500': '000905.SH',
          '中小板指': '399005.SZ', '上证180': '000010.SH'}
index_data = get_index_data(indexs)
print(index_data['上证综指'].head())

# 对股价走势进行可视化分析
subjects = list(index_data.keys())
# 每个子图的title
plot_pos = [421, 422, 423, 424, 425, 426, 427, 428]  # 每个子图的位置
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

fig = plt.figure(figsize=(25, 25))
fig.suptitle('A股股指走势', fontsize=18)
for pos in np.arange(len(plot_pos)):
    ax = fig.add_subplot(plot_pos[pos])
    y_data = index_data[subjects[pos]]['close']
    b = ax.plot(y_data, color=new_colors[pos])
    ax.set_title(subjects[pos])
    # 将右上边的两条边颜色设置为空，相当于抹掉这两条边
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
plt.savefig('A股重要指数基金.png')
plt.show()

# 定义获取多只股票函数：
def get_stocks_data(stocklist, start, end):
    all_data = {}
    for code in stocklist:
        all_data[code] = pro.daily(ts_code=code, start_date=start, end_date=end)
    return all_data

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
stocklist = list(data['ts_code'][:20]) # 取前20只股票
print(stocklist)
start = '20200101' # 开始时间
end = '20200401' # 截至时间
all_data = get_stocks_data(stocklist, start, end)
print(all_data)
print(all_data['000002.SZ'].tail())

# 保存本地
def save_data(all_data):
    for code, data in all_data.items():
        data.to_('C:/Users/86188/Desktop/研究生学习/股票数据/'+code+'.csv', header=True, index=False)
# 将数据保存到本地
save_data(all_data)
