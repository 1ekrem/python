import pandas as pd

csv_file = 'C:\\Users\\ekrem\\Documents\\PandasTraining\\csv files\\calc_stats.csv'

df = pd.read_csv(csv_file)

print(df)

#Step 3: Use Pandas to Calculate Stats from an Imported CSV File
"""
Mean salary
Total sum of salaries
Maximum salary
Minimum salary
Count of salaries
Median salary
Standard deviation of salaries
Variance of of salaries
"""

# df['Mean Salary'] = df['Salary'].mean()
# df['Total sum of salaries'] = df['Salary'].sum()
# df['Maximum Salary'] = df['Salary'].max()
# df['Minimum Salary'] = df['Salary'].min()
# df['Count of salaries'] = df['Salary'].count()
# df['Median salary'] = df['Salary'].median()
# df['Standard deviation of salaries'] = df['Salary'].std()
# df['Variance of of salaries'] = df['Salary'].var()

#Block2
sum1 = df['Salary'].sum()
count1 = df['Salary'].count()

groupby_sum1 = df.groupby(['Country']).sum()
groupby_count1 = df.groupby(['Country']).count()

#print(groupby_sum1)

#print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Country: ' + str(groupby_count1))

df.loc[df['Country'] == 'USA', 'Match?'] = True
df.loc[df['Country'] != 'USA', 'Match?'] = False
df['Country Match-2?'] = df['Country'].apply(lambda x: 'Match2' if x == 'USA' else 'Different Country')

print(df)