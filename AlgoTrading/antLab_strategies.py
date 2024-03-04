
"""
This file should be used to define all custom strageties
"""


def in_consolidation(df, percentange):
    
    last_15days = df[-45:]
    
    max_price = last_15days['Close'].max()
    min_price = last_15days['Close'].min()
    
    custom_threshold = 1- (percentange / 100)
    if min_price > (max_price * custom_threshold):
        return True
    
def consolidation_range(df):
    last_15days = df[-15:]

    max_price = round(last_15days['Close'].max(),2)
    min_price = round(last_15days['Close'].min(),2)

    # print(max_price, min_price)

    delta_perc = round((max_price - min_price) / min_price,2)

    return delta_perc


def fib_retracement_test(df):
    last_45days = df[-45:]
    
    max_price = round(last_45days['High'].max(), 2)
    min_price = round(last_45days['Low'].min(), 2)
    
    point50 = round(max_price - 0.5 * (max_price - min_price), 2)
    point618 = round(max_price - ((1 - 0.618) * (max_price - min_price)), 2)
    
    current_price = round(df.iloc[-1, df.columns.get_loc('Close')], 2)
    
    in_golden_zone = point618 > current_price > point50
    # print("0.618:", point618, "--", current_price, "--", "0.5", point50, "max: ", max_price, "--", "min: ", min_price )
    
    return in_golden_zone
    
