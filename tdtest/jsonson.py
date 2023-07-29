import json
import pandas as pd



with open('C:/PythonClass/tdtest/tdapidataOptCh.json') as read_doc:
    reader = json.load(read_doc)
    
first_data = reader["symbol"]["callExpDateMap"][0]["2021-02-12:5"][0]["35.0"]
print(first_data)    