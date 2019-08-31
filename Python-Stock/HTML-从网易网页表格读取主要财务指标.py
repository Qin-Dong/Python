import pandas as pd
from pandas.core.frame import DataFrame
import time

tables = pd.read_html("http://quotes.money.163.com/f10/zycwzb_600366,year.html")
i = 0
for table in tables:
    if i == 4:
        df_tmp = DataFrame(table)
        df_tmp.insert(0, '分类',
                      ['报告日期', '基本每股收益(元)', '每股净资产(元)', '每股经营活动产生的现金流量净额(元)', '主营业务收入(万元)', '主营业务利润(万元)', '营业利润(万元)',
                       '投资收益(万元)', '营业外收支净额(万元)', '利润总额(万元)', '净利润(万元)', '净利润(扣除非经常性损益后)(万元)', '经营活动产生的现金流量净额(万元)',
                       '现金及现金等价物净增加额(万元)', '总资产(万元)', '流动资产(万元)', '总负债(万元)', '流动负债(万元)', '股东权益不含少数股东权益(万元)',
                       '净资产收益率加权(%)'])
        df_tmp.to_excel('./数据-下载/html-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-年度.xlsx')
    elif i == 5:
        DataFrame(table).to_excel('./数据-下载/html-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-盈利能力.xlsx')
    elif i == 6:
        DataFrame(table).to_excel('./数据-下载/html-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-偿还能力.xlsx')
    elif i == 7:
        DataFrame(table).to_excel('./数据-下载/html-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-成长能力.xlsx')
    elif i == 8:
        DataFrame(table).to_excel('./数据-下载/html-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-营运能力.xlsx')
    i += 1
