import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import datetime
import dateutil

CASH = 10000
START_DATE = '2016-01-01'
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
        self.dt = dateutil.parser.parse(start_date)


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
    return atttibute_daterange_history(security, start_date, end_date)


def atttibute_daterange_history(security, start_date, end_date, fields=('open', 'close', 'high', 'low', 'volume')):
    try:
        f = open(security + '.csv')
        df = pd.read_csv(f, index_col='date', parse_dates=['date']).loc[start_date:end_date, :]
    except:
        df = tushare.get_k_data(security, start_date, end_date)
    return df[list(fields)]
