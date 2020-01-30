#!/usr/bin/env python
# coding: utf-8

import time
start_time=time.perf_counter()

print('Importing Modules...')
import os
import pandas as pd
import talib as ta

print('Checking Existing Stock List...')
fileList = os.listdir()
if 'stock_list.txt' in fileList:
    stock_list=pd.read_csv('stock_list.txt',converters = {u'0':str})['0'].to_list()
else:
    print('Error: No Stock List Found.')

code_list, max_value=[], []

print('Calculating...')
n=0

for stock in stock_list:
    df=pd.read_csv('data/'+str(stock)+'.csv', index_col=0)
    n+=1

    if df is None:
        pass

    else:
        df['ma5']=ta.SMA(df['close'],5)
        code_list.append(stock)
        max_value.append(df['ma5'].max())
    print(str(n)+' of '+str(len(stock_list))+' finished. Code: '+str(stock))

pd.DataFrame([code_list, max_value],index=['code','max']).T.to_excel('test.xlsx',index=False)

end_time=time.perf_counter()
print('It costs %s seconds.'%(round((end_time-start_time),4)))