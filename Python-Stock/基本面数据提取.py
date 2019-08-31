import tushare as ts


#df=ts.get_stock_basics()
df=ts.get_profit_data(2017,4)
df.to_excel('2017-04盈利能力.xlsx')