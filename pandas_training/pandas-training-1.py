from pprint import pprint
from traceback import print_tb
import pandas as pd

df = pd.read_csv('C:/Users/ekrem/Documents/PandasTraining/stackoverflow/survey_results_public.csv', index_col="ResponseId")

schema_df = pd.read_csv('C:/Users/ekrem/Documents/PandasTraining/stackoverflow/survey_results_schema.csv', index_col="qname")

#df = pd.set_option('display.max_columns',85)

#print(df['Age'].value_counts())

#print(df.loc[0:4,"Country"])

#print(schema_df.loc['MentalHealth','question'])

schema_df = schema_df.sort_index(ascending=False)

#print(schema_df)

filt = (df['Country'].loc == 'Netherlands')

#print(filt,"TEST")

#Find who makes the highest salary
high_salary = (df['CompTotal'] < 1)

high_sal = df.loc[high_salary, ['Country', 'LanguageHaveWorkedWith', 'CompTotal']]
print(high_sal)

countries = ['Slovakia', 'South Korea', 'Germany', 'Canada', 'United Kingdom']
countries_only= df['Country'].isin(countries)
#print(countries_only)

language_filter = df['LanguageHaveWorkedWith'].str.contains("Python", na=False)
x = df.loc[language_filter, 'LanguageHaveWorkedWith']
#print(x)

print(df['CompTotal'].idxmax())