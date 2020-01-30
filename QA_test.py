#!/usr/bin/env python
# coding: utf-8

import time
start_time=time.perf_counter()

print('Importing Modules...')
import os
import QUANTAXIS as QA
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
    n+=1
    
    if QA.QA_fetch_stock_day_adv(stock,'2017-06-15','2020-01-23') is None:
        pass
    
    else:
        df=QA.QA_fetch_stock_day_adv(stock,'2017-06-15','2020-01-23').data
        df['ma5']=ta.SMA(df['close'],5)
        code_list.append(stock)
        max_value.append(df['ma5'].max())
    print(str(n)+' of '+str(len(stock_list))+' finished. Code: '+str(stock))

pd.DataFrame([code_list, max_value],index=['code','max']).T.to_excel('test.xlsx',index=False)

end_time=time.perf_counter()
print('It costs %s seconds.'%(round((end_time-start_time),4)))
