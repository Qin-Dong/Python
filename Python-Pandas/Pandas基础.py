import numpy as np
import pandas as pd

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006], "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32], "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ], "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})



#df.to_excel('f:/temp/pandas_to_excel.xlsx')
#print(df[df['price'] > 0])
df_inner=pd.merge(df,df1,how='inner')
df_left=pd.merge(df,df1,how='left')
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')
print(df_inner)