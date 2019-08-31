# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from pandas.core.frame import DataFrame

tables = pd.read_html("http://quotes.money.163.com/f10/zycwzb_600366,year.html")
i = 0
for table in tables:
    DataFrame(table).to_excel('网易-股票财务分析-Pandas-' + str(i) + '.xlsx')
    i += 1
