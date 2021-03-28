import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

y0 = []
y1 = []
y2 = []
y3 = []
y4 = []



font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 9,
         }

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         }

figsize = 8, 9
plt.subplots(figsize=figsize)  # 设定整张图片大小

ax1 = plt.subplot(4, 1, 1)
ax1.yaxis.set_major_locator(MultipleLocator(15))  # 设定y轴刻度间距
# 第一条线
x = range(0, len(y0))
plt.plot(x, y0, color='black', label='$DT$', linewidth=0.8)  # 绘制，指定颜色、标签、线宽，标签采用latex格式
plt.ylim(-90, -20)  # 设定y轴范围
hl = plt.legend(loc='upper right', prop=font1, frameon=False)  # 绘制图例，指定图例位置
# set(hl,'Box','off');
# 第二条曲线
x = range(0, len(y1))
plt.plot(x, y1, color='red', label='$M_1$', linewidth=0.8)
plt.legend(loc='upper right', prop=font1, frameon=False)  # 绘制图例，指定图例位置
plt.xticks([])  # 去掉x坐标轴刻度
plt.xlim(0, 580)  # 设定x轴范围