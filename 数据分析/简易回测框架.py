import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import datetime
import dateutil

CASH = 10000
START_DATE = '2016-01-07'
END_DATE = '2017-12-31'
# trade_cal = tushare.trade_cal()
# trade_cal.to_csv('trade_cal.csv')
trade_cal = pd.read_csv('trade_cal.csv')


class Context:
    def __init__(self, cash, start_date, end_date):
        self.cash = cash
        self.start_date = start_date
        self.end_date = end_date
        self.positions = {}
        self.benchmark = None
        self.date_range = trade_cal[(trade_cal['isOpen'] == 1) &
                                    (trade_cal['calendarDate'] >= start_date) &
                                    (trade_cal['calendarDate'] <= end_date)]
        # self.dt = datetime.datetime.strptime('',start_date)
        self.dt = dateutil.parser.parse(start_date)  # ToDo: start_date 后一个交易日


context = Context(CASH, START_DATE, END_DATE)


# print(context.date_range)

class G:
    pass


g = G()


# 获取历史数据
def attribute_history(security, count, fields=('open', 'close', 'high', 'low', 'volume')):
    end_date = (context.dt - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = trade_cal[(trade_cal['isOpen'] == 1) & (trade_cal['calendarDate'] <= end_date)][-count:].iloc[0, :][
        'calendarDate']
    print(start_date, end_date)
    return attribute_daterange_history(security, start_date, end_date)


def attribute_daterange_history(security, start_date, end_date, fields=('open', 'close', 'high', 'low', 'volume')):
    try:
        f = open(security + '.csv')
        df = pd.read_csv(f, index_col='date', parse_dates=['date']).loc[start_date:end_date, :]
    except:
        df = tushare.get_k_data(security, start_date, end_date)
    return df[list(fields)]


#  下单函数
def get_today_data(security):
    today = context.dt.strftime('%Y-%m-%d')
    try:
        f = open(security + '.csv')
        data = pd.read_csv(f, index_col='date', parse_dates=['date']).loc[today, :]
    except FileNotFoundError:
        data = tushare.get_k_data(security, today, today).iloc[0, :]

    # 非交易日、停牌
    except KeyError:
        data = pd.Series()
    return data


print(get_today_data('601318'))


def __order(today_data, security, amount):
    p = today_data['close']
    if len(today_data) == 0:
        print('今日停牌')
        return
    if context.cash - amount * p < 0:
        amount = context.cash // p
        print('现金不足,已调整为：%d' % amount)
    if amount % 100 != 0:
        if amount != -context.positions.get(security,0):
            # 2345
            amount = amount // 100 * 100
            print('不是100的倍数，以调整为%d' % amount)
    # 300   -200
    if context.positions.get(security,0) < -amount:
        # 卖超过拥有的量
        amount = -context.positions[security]
        print('卖出股票不能超过持仓数，已调整为%d' % amount)

    context.positions[security] = context.positions.get(security, 0) + amount
    # 更新余额
    context.cash -= amount * p

    # 如果持仓为0，
    if context.positions[security] == 0:
        del context.positions[security]

__order(get_today_data('601318'),'601318',100)
print(context.positions)