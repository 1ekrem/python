from ta_BulkRunner_Function import bulkRunner
from NDX100 import NDX100
from SPX import SPX

file_path = 'C:\\Users\\Ekrem.Ersayin\\Documents\\pythonwork\\USTickers\\USMarketTicker-2023-07-19-Capture.csv'


# with open(file_path, 'r') as file:
#     # Assuming each value is on a separate line in the file
#     for line_number, line in enumerate(file, start=1):
#         value = line.strip()  # Remove leading/trailing whitespaces and newlines
#         try:
#             bulkRunner(value)
#         except IndexError:
#             pass    

for ticker in NDX100:
    try:
        bulkRunner(ticker)
    except IndexError:
        pass    