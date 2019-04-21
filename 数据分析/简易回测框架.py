import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare

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


# context = Context(1000, '2016-01-01', '2017-01-01')
# print(context.date_range)

class G:
    pass


g = G()
