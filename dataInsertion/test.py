import pyodbc
import pandas


data = pandas.read_csv (r'C:/Users/ekrem/Documents/Database File Upload/test_2.csv')
df = pandas.DataFrame(data,columns = ['Ticker', 'PutRatio', 'CallRatio', 'Date'])


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-UTF7GAF\SQLEXPRESS;'
                      'Database=Trading;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#top10query = "Select TOP 10 * from Option_Volume_Leaders Where Time BETWEEN '2020-12-01' AND '2020-12-05' ORDER BY Volume Desc"
#
#cursor.execute(top10query)
# 
#for row in cursor:
#    print(row)
#

#cursor.execute('CREATE TABLE TradingData (Ticker varchar(255), PutRatio decimal(5, 2), CallRatio decimal(5, 2), Date date)')
#
#conn.commit()

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO [Trading].[dbo].[TradingData] (Ticker, PutRatio, CallRatio, Date)
                VALUES (?,?,?,?)
                ''',
                row.Ticker, 
                row.PutRatio,
                row.CallRatio,
                row.Date
                )
conn.commit()
print("Data Insert is completed")
