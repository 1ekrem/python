import pyodbc
import pandas
import time


df = pandas.read_csv ('most-active-stocks-options-03-29-2021.csv')

# df = pandas.DataFrame(data,columns = ['Symbol'
#                                       ,'Name'
#                                       ,'Last'
#                                       ,'Change'
#                                       ,'Change_per'
#                                       ,'IV_Rank'
#                                       ,'Options_Volume'
#                                       ,'Put_Options_Per'
#                                       ,'Call_Options_Per'
#                                       ,'Put_Call_Ratio'
#                                       ,'Effective_Date'])

# Rename columns
df['Change_per'] = df['%Chg'] = [float(str(i).replace("%", "")) for i in df['%Chg']]
df['IV_Rank'] = df['IV Rank'] = [float(str(i).replace("%", "")) for i in df['IV Rank']]
df['Options_Volume'] = df['Options Vol']
df['Put_Options_Per'] = df['% Put'] = [float(str(i).replace("%", "")) for i in df['% Put']]
df['Call_Options_Per'] = df['% Call'] = [float(str(i).replace("%", "")) for i in df['% Call']]
df['Put_Call_Ratio'] = df['Put/Call Vol']= [float(str(i).replace("%", "")) for i in df['Put/Call Vol']]
df['Effective_Date'] = df['Time']


df.fillna(0)
print(df)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-UTF7GAF\SQLEXPRESS;'
                      'Database=Trading;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

"""Create table"""
# table_creation_query = 'CREATE TABLE most_active_options2 (Symbol varchar(255),Name varchar(255),Last decimal(6, 2),Change decimal(5, 2),Change_per decimal(5, 2),IV_Rank decimal(5, 2),Options_Volume nvarchar(255),Put_Options_Per decimal(5, 2),Call_Options_Per decimal(5, 2),Put_Call_Ratio decimal(5, 2),Effective_Date date)'
# cursor.execute(table_creation_query)
# conn.commit()

# print("Table is created")


"""Insert Data"""
insert_query = '''INSERT INTO [Trading].[dbo].[most_active_options2] (Symbol, Name, Last, Change, Change_per, IV_Rank, Options_Volume, Put_Options_Per, Call_Options_Per, Put_Call_Ratio, Effective_Date)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
for row in df.itertuples():
    cursor.execute('''INSERT INTO [Trading].[dbo].[most_active_options2] (Symbol, Name, Last, Change, Change_per, IV_Rank, Options_Volume, Put_Options_Per, Call_Options_Per, Put_Call_Ratio, Effective_Date)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                    row.Symbol,
                    row.Name,
                    row.Last,
                    row.Change,
                    row.Change_per,
                    row.IV_Rank,
                    row.Options_Volume,
                    row.Put_Options_Per,
                    row.Call_Options_Per,
                    row.Put_Call_Ratio,
                    row.Effective_Date
)
conn.commit()

print("Inserted")