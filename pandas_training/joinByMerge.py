import pandas as pd

traders = {'Trader_ID': [111,222,333,444,555],
           'Trader_Name': ['Ekrem Ersayin', 'John Hello', 'Pupsik Yahsiyan', 'Ronaldinho Barca', 'Fernando Torres']
}

df1 = pd.DataFrame(traders, columns = ['Trader_ID', 'Trader_Name'])
print(df1)

countries = {'Trader_ID': [111,222,333,444,777],
             'Trader_Country': ['TR','Canada','Spain','China','Brazil']
             }

df2 = pd.DataFrame (countries, columns = ['Trader_ID', 'Trader_Country'])
print(df2)


inner_join = pd.merge(df1,df2, how='inner', on=['Trader_ID', 'Trader_ID'])
print(inner_join)

outer_join = pd.merge(df1,df2, how='outer', on=['Trader_ID', 'Trader_ID'])
print(outer_join)

left_join = pd.merge(df1,df2, how='left', on=['Trader_ID', 'Trader_ID'])
print(left_join)