import pandas as pd
from pandas.io.json import json_normalize


new_dict = {
    "symbol": "PLTR",
    "status": "SUCCESS",
    "underlying": None,
    "strategy": "SINGLE",
    "interval": 0.0,
    "isDelayed": 'false',
    "isIndex": 'false',
    "interestRate": 0.1,
    "underlyingPrice": 32.18,
    "volatility": 29.0,
    "daysToExpiration": 0.0,
    "numberOfContracts": 13,
    "putExpDateMap": {},
    "callExpDateMap": {
        "2021-02-19:6": {
            "35.0": [
                {
                    "putCall": "CALL",
                    "symbol": "PLTR_021921C35",
                    "description": "PLTR Feb 19 2021 35 Call",
                    "exchangeName": "OPR",
                    "bid": 1.86,
                    "ask": 1.99,
                    "last": 1.9,
                    "mark": 1.93,
                    "bidSize": 1,
                    "askSize": 14,
                    "bidAskSize": "1X14",
                    "lastSize": 0,
                    "highPrice": 2.77,
                    "lowPrice": 1.65,
                    "openPrice": 0.0,
                    "closePrice": 1.91,
                    "totalVolume": 18495,
                    "tradeDate": None,
                    "tradeTimeInLong": 1613163599494,
                    "quoteTimeInLong": 1613163599967,
                    "netChange": -0.68,
                    "volatility": 167.504,
                    "delta": 0.396,
                    "gamma": 0.05,
                    "theta": -0.193,
                    "vega": 0.018,
                    "rho": 0.002,
                    "openInterest": 55448,
                    "timeValue": 1.9,
                    "theoreticalOptionValue": 1.906,
                    "theoreticalVolatility": 29.0,
                    "optionDeliverablesList": None,
                    "strikePrice": 35.0,
                    "expirationDate": 1613768400000,
                    "daysToExpiration": 6,
                    "expirationType": "R",
                    "lastTradingDay": 1613782800000,
                    "multiplier": 100.0,
                    "settlementType": " ",
                    "deliverableNote": "",
                    "isIndexOption": None,
                    "percentChange": -35.54,
                    "markChange": 0.02,
                    "markPercentChange": 0.99,
                    "nonStandard": 'false',
                    "mini": 'false',
                    "inTheMoney": 'false'
                }
            ]
        },
        "2021-02-26:13": {
            "35.0": [
                {
                    "putCall": "CALL",
                    "symbol": "PLTR_022621C35",
                    "description": "PLTR Feb 26 2021 35 Call (Weekly)",
                    "exchangeName": "OPR",
                    "bid": 2.71,
                    "ask": 2.75,
                    "last": 2.67,
                    "mark": 2.73,
                    "bidSize": 25,
                    "askSize": 1,
                    "bidAskSize": "25X1",
                    "lastSize": 0,
                    "highPrice": 3.65,
                    "lowPrice": 2.45,
                    "openPrice": 0.0,
                    "closePrice": 2.73,
                    "totalVolume": 2550,
                    "tradeDate": None,
                    "tradeTimeInLong": 1613163589287,
                    "quoteTimeInLong": 1613163595017,
                    "netChange": -0.68,
                    "volatility": 155.772,
                    "delta": 0.438,
                    "gamma": 0.039,
                    "theta": -0.13,
                    "vega": 0.025,
                    "rho": 0.004,
                    "openInterest": 2936,
                    "timeValue": 2.67,
                    "theoreticalOptionValue": 2.731,
                    "theoreticalVolatility": 29.0,
                    "optionDeliverablesList": None,
                    "strikePrice": 35.0,
                    "expirationDate": 1614373200000,
                    "daysToExpiration": 13,
                    "expirationType": "S",
                    "lastTradingDay": 1614387600000,
                    "multiplier": 100.0,
                    "settlementType": " ",
                    "deliverableNote": "",
                    "isIndexOption": None,
                    "percentChange": -25.05,
                    "markChange": 0.0,
                    "markPercentChange": -0.04,
                    "nonStandard": 'false',
                    "mini": 'false',
                    "inTheMoney": 'false'
                }
            ]
        }
    }
}

x = pd.json_normalize(new_dict['callExpDateMap']['2021-02-26:13']['35.0'])

print(x)

for key, value in new_dict['callExpDateMap'].items():
    print(key)