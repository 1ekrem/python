import pandas as pd

people = {"first" : ["Ekrem", "Test"],
          "last" : ["Ers", "testLast"],
          "email" : ["ers@gmail.com", "test@gmail.com"]          
          }

#print(people["email"])

df = pd.DataFrame(people)

#iloc searches by integer
var_iloc = df.iloc[[0,1], 2]
print(var_iloc)

#loc searches by actual label
var_loc = df.loc[[0,1], ['last','email']]
print(var_loc)

test_filt =(df["first"] == 'Test') & (df['last']=='testLast')

print(~test_filt)

df.columns = [x.lower() for x in df.columns]
df.columns = df.columns.str.replace("l", "__")
print(df)

