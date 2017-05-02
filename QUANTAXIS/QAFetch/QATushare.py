# coding: utf-8

import tushare as QATs
import json
from QUANTAXIS.QAUtil import QA_util_date_stamp


def QA_fetch_get_stock_day(name,startDate,endDate):
    if (len(name)!=6):
        name=str(name)[0:6]
    return QATs.get_k_data(name,startDate,endDate,ktype='D')

def QA_fetch_get_stock_info(name):
    if (len(name)!=6):
        name=str(name)[0:6]
    return QATs.get_stock_basics()

def QA_fetch_get_stock_tick(name,date):
    if (len(name)!=6):
        name=str(name)[0:6]
    return QATs.get_tick_data(name,date)
    

def QA_fetch_get_stock_list():
    df=QATs.get_stock_basics()
    return list(df.index)

def QA_fetch_get_trade_date(endDate, exchange):
    data=QATs.trade_cal()
    da=data[ data.isOpen>0 ]    
    data_json=json.loads(da.to_json(orient='records'))
    message=[]
    for i in range(0,len(data_json)-1,1):
        date=data_json[i]['calendarDate']
        num=i+1
        exchangeName='SSE'
        data_stamp=QA_util_date_stamp(date)
        mes={'date':date,'num':num,'exchangeName':exchangeName,'date_stamp':data_stamp}
        message.append(mes)
    return message

#test

#print(get_stock_day("000001",'2001-01-01','2010-01-01'))
#print(get_stock_tick("000001.SZ","2017-02-21"))