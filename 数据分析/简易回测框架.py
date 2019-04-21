import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import datetime
import dateutil

CASH = 10000
START_DATE = '2016-01-07'
END_DATE = '2016-01-15'
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
                                    (trade_cal['calendarDate'] <= end_date)]['calendarDate'].values
        # self.dt = datetime.datetime.strptime('',start_date)
        # self.dt = dateutil.parser.parse(start_date)  # ToDo: start_date 后一个交易日
        self.dt = None


context = Context(CASH, START_DATE, END_DATE)


def set_benckmark(security):  # 只支持一只股票作为基准
    context.benchmark = security


class G:
    pass


g = G()


# 获取历史数据
def attribute_history(security, count, fields=('open', 'close', 'high', 'low', 'volume')):
    end_date = (context.dt - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_date = trade_cal[(trade_cal['isOpen'] == 1) & (trade_cal['calendarDate'] <= end_date)][-count:].iloc[0, :][
        'calendarDate']
    # print(start_date, end_date)
    return attribute_daterange_history(security, start_date, end_date)


def attribute_daterange_history(security, start_date, end_date, fields=('open', 'close', 'high', 'low', 'volume')):
    try:
        f = open(security + '.csv', 'r')
        df = pd.read_csv(f, index_col='date', parse_dates=['date']).loc[start_date:end_date, :]
    except FileNotFoundError:
        df = tushare.get_k_data(security, start_date, end_date)
    df = df[list(fields)]# type:pd.DataFrame
    return df.reset_index( drop=True)


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


def __order(today_data, security, amount):
    p = today_data['close']
    if len(today_data) == 0:
        print('今日停牌')
        return
    if context.cash - amount * p < 0:
        amount = context.cash // p
        print('现金不足,已调整为：%d' % amount)
    if amount % 100 != 0:
        if amount != -context.positions.get(security, 0):
            # 2345
            amount = amount // 100 * 100
            print('不是100的倍数，以调整为%d' % amount)
    # 300   -200
    if context.positions.get(security, 0) < -amount:
        # 卖超过拥有的量
        amount = -context.positions.get(security, 0)
        print('卖出股票不能超过持仓数，已调整为%d' % amount)

    context.positions[security] = context.positions.get(security, 0) + amount
    # 更新余额
    context.cash -= amount * p

    # 如果持仓为0，
    if context.positions[security] == 0:
        del context.positions[security]


# __order(get_today_data('601318'),'601318',1000000)
# print(context.positions)


def order(security, amount):
    today_data = get_today_data(security)
    __order(today_data, security, amount)


def order_target(security, amount):
    if amount < 0:
        print('数量不能为负数，已调整为0')
        amount = 0
    today_data = get_today_data(security)
    hold_amount = context.positions.get(security, 0)
    delta_amount = amount - hold_amount  # 要卖的股票数
    __order(today_data, security, delta_amount)  # ToDo : T+1  closeabel total


def order_value(security, value):
    today_data = get_today_data(security)
    amount = value // today_data['open']
    __order(today_data, security, amount)


def order_target_value(security, value):
    today_data = get_today_data(security)
    if value < 0:
        print('价格不能为负，以调整为0')
        value = 0
    hold_value = context.positions.get(security, 0) * today_data['open']

    delta_value = value - hold_value  # 买卖的价格
    order_value(security, delta_value)


# order('601318',100)
# order_value('601318',30000)
# print(context.positions)


def run():
    plt_df = pd.DataFrame(index=pd.to_datetime(context.date_range), columns=['value'])
    init_value = context.cash

    initialize(context)
    last_prize = {}
    for dt in context.date_range:
        context.dt = dateutil.parser.parse(dt)
        handle_data(context)
        value = context.cash
        for stock in context.positions:
            today_data = get_today_data(stock)
            # 考虑停牌的情况
            if len(today_data) == 0:
                p = last_prize[stock]
            else:
                p = today_data['open']
                last_prize[stock] = p
            value += p * context.positions[stock]
        plt_df.loc[dt, 'value'] = value
    plt_df['ratio'] = (plt_df['value'] - init_value) / init_value
    bm_df = attribute_daterange_history(context.benchmark, context.start_date, context.end_date)
    bm_init = bm_df['open'][0]
    temp =(bm_df['open'] - bm_init) / bm_init
    plt_df['benckmark_ratio'] = temp
    plt_df[['ratio', 'benckmark_ratio']].plot()
    plt.show()


def initialize(context):
    set_benckmark('601318')
    g.p1 = 5
    g.p2 = 60
    g.security = '601318'


def handle_data(context):
    order('601318', 100)
    hist = attribute_history(g.security, g.p2)
    md5 = hist['close'][-g.p1:].mean()
    md60 = hist['close'].mean()

    if md5 > md60 and g.security not in context.positions:
        order_value(g.security, context.cash)
    elif md5 < md60 and g.security in context.positions:
        order_target(g.security, 0)


if __name__ == '__main__':
    run()
