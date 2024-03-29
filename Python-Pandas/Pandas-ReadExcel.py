import pandas as pd

'''
code,代码 name,名称 industry,所属行业 area,地区 pe,市盈率 outstanding,流通股本(亿)
totals,总股本(亿) totalAssets,总资产(万) liquidAssets,流动资产 fixedAssets,固定资产
reserved,公积金 reservedPerShare,每股公积金 esp,每股收益 bvps,每股净资 pb,市净率
timeToMarket,上市日期 undp,未分利润 perundp, 每股未分配 rev,收入同比(%) profit,利润同比(%)
gpr,毛利率(%) npr,净利润率(%) holders,股东人数
'''

data = pd.read_excel(u'../股票分析/数据-下载/股票基本面-201805.xlsx')
# 选择板块为'浙江'
# print(data[(data['area'].isin(['浙江']))])

# 选择板块除'浙江'以外的
# print(data[(~data['area'].isin(['浙江']))])

# 选择pe>10的
# print(data[(data['pe']>10)])

# 选择pe>10和bvps>5的
data[(data['pe'] > 10) & (data['bvps'] > 5)].to_excel(u'../股票分析/数据-分析/股票基本面-PE和bvps-201805.xlsx')
