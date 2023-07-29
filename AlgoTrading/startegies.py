
"""
This file should be used to define all custom strageties
"""
from ast import Pass, Return
from pickle import TRUE
from decimal import Decimal


def in_consolidation(df, percentange):
    
    last_15days = df[-45:]
    
    max_price = last_15days['Close'].max()
    min_price = last_15days['Close'].min()
    
    delta_perc = (max_price / min_price) / max_price
    
    custom_threshold = 1- (percentange / 100)
    if min_price > (max_price * custom_threshold):
        return True
    
def consolidation_range(df):
    last_15days = df[-15:]
    print(last_15days)

    max_price = round(last_15days['Close'].max(),2)
    min_price = round(last_15days['Close'].min(),2)

    print(max_price, min_price)

    delta_perc = round((max_price - min_price) / min_price,2)

def fib_retracement(df):
    last_45days = df[-45:]
    
    max_price = round(last_45days['Close'].max(),2)
    min_price = round(last_45days['Close'].min(),2)
    
    point50 = round(max_price - (0.5 * (max_price - min_price)),2)
    point618 = round(max_price - (0.618 * (max_price - min_price)),2)
    
    current_price = round(df.iloc[-1, df.columns.get_loc('Close')],2)
    
    inGoldenZone = bool()
    
    if  point618 < current_price < point50:
        inGoldenZone = True
    else: False

    return inGoldenZone
    
    # if current_price in range(point50, point618):
    #     print("Yes")
        # print(current_price, point618, point50)
    
