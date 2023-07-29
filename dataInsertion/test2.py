import pyodbc
import pandas


data = pandas.read_csv (r'C:/Users/ekrem/Downloads/most-active-options-12-06-2020.csv')
df = pandas.DataFrame(data,columns = ['Symbol'
                                      ,'Name'
                                      ,'Last'
                                      ,'Change'
                                      ,'Change_per'
                                      ,'Options_Volume'
                                      ,'Put_Options_Per'
                                      ,'Call_Options_Per'
                                      ,'Put_Call_Ratio'
                                      ,'Effective_Date'
                                      ,'IV_Rank'])

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-UTF7GAF\SQLEXPRESS;'
                      'Database=Trading;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

"""Create table"""
#table_creation_query = 'CREATE TABLE most_active_options2 (Symbol varchar(255),Name varchar(255),Last decimal(6, 2),Change decimal(5, 2),Change_per decimal(5, 2),Options_Volume nvarchar(255),Put_Options_Per decimal(5, 2),Call_Options_Per decimal(5, 2),Put_Call_Ratio decimal(5, 2),Effective_Date date)'
#cursor.execute(table_creation_query)
#conn.commit()

"""Insert Data"""
#insert_query = '''INSERT INTO [Trading].[dbo].[Option_History] (Symbol, Name, Last, Change, Change_per,  Options_Volume, Put_Options_Per, Call_Options_Per, Put_Call_Ratio, Effective_Date)
#                VALUES (Symbol, Name, Last, Change, Change_per, Options_Volume, Put_Options_Per, Call_Options_Per, Put_Call_Ratio, Effective_Date, IV_Rank)'''

for row in df.itertuples():
    cursor.execute(
        '''INSERT INTO [Trading].[dbo].[Option_History] (Symbol, Name, Last, Change, Change_per, Options_Volume, Put_Options_Per, Call_Options_Per, Put_Call_Ratio, Effective_Date, IV_Rank)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                    row.Symbol,
                    row.Name,
                    row.Last,
                    row.Change,
                    row.Change_per,
                    row.Options_Volume,
                    row.Put_Options_Per,
                    row.Call_Options_Per,
                    row.Put_Call_Ratio,
                    row.Effective_Date,
                    row.IV_Rank
)
conn.commit()