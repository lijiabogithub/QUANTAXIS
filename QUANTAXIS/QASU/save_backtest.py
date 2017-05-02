# coding:utf-8


"""
message={
'header':{
'source':'account',
'cookie':self.account_cookie,
'session':{
'user':update_message['user'],
'strategy':update_message['strategy']
}

},
'body':{
'account':{
'init_assest':self.total_assest[0],
'portfolio':self.portfolio,
'history':self.history_trade,
'assest_now':self.assets,
'assest_history':self.total_assest,
'assest_free':self.assets_free,
'assest_fix':self.assets_market_hold_value,
'profit':self.portfit,
'total_profit':self.total_profit,
'cur_profit_present':self.cur_profit_present,
'hold':self.hold
},
'bid':update_message['bid'],
'market':update_message['market'],
'time':datetime.datetime.now(),
'date_stamp':str(datetime.datetime.now().timestamp())


}
}
"""


def QA_SU_save_account_message(message, client):
    header=message['header']
    body=message['body']
    coll=client.quantaxis.backtest_history
    print(message)
    coll.insert({
        'time':message['body']['time'],
        'total_date':message['body']['account']['total_date'],
        'time_stamp':message['body']['date_stamp'],
        "cookie":message['header']['cookie'],
        'user':message['header']['session']['user'],
        'strategy':message['header']['session']['strategy'],
        'init_assest':message['body']['account']['init_assest'],
        'portfolio':message['body']['account']['portfolio'],
        'history':message['body']['account']['history'],
        'assest_now':message['body']['account']['assest_now'],
        'assest_history':message['body']['account']['assest_history'],
        'assest_free':message['body']['account']['assest_free'],
        'assest_fix':message['body']['account']['assest_fix'],
        'profit':message['body']['account']['profit'],
        'total_profit':message['body']['account']['total_profit'],
        'cur_profit_present':message['body']['account']['cur_profit_present'],
        'cur_profit_present_total':message['body']['account']['cur_profit_present_total'],
        'hold':message['body']['account']['hold'],
        'bid':message['body']['bid'],
        'market':message['body']['market']
    })
def QA_SU_save_backtest_message(message,client):
    coll=client.quantaxis.backtest_info
    coll.insert(message)