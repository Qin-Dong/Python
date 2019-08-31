import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
import time
import Chinese as fnt

fnt.set_ch('YH', 12)
df_jbcwzb = pd.read_excel('./数据-下载/html-201806-网易-主要财务指标-年度.xlsx')
data_reportDate = df_jbcwzb.ix[0, 1:].sort_index(ascending=False)

plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)

plt.subplot(311)
# 基本每股收益
data_jbmgsy = df_jbcwzb.ix[1, 1:].replace('--', '0').sort_index(ascending=False)
plt.plot(data_reportDate, data_jbmgsy.astype(float), label='a')
plt.legend()
plt.xticks(rotation=90)
# plt.xlabel('年报日期')
plt.ylabel('每股收益')
plt.title('600366-每股收益')

plt.subplot(312)
# 基本每股收益
data_kfjlr = df_jbcwzb.ix[11, 1:].replace('--', '0').sort_index(ascending=False)
plt.plot(data_reportDate, data_kfjlr.astype(float), label='a')
plt.legend()
plt.xticks(rotation=90)
plt.xlabel('年报日期')
plt.ylabel('扣非净利润')
plt.title('600366-扣非净利润')

plt.show()
