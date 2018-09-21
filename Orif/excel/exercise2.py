# Open an existing worksheet
# Add a value
# add other values
# save

import openpyxl

wb = openpyxl.load_workbook("ekrem_info2.xlsx")

ws_ekrem = wb['Ekrem']

first_cell=ws_ekrem["A1"]
print(first_cell.value)

ws_ekrem.append([10,20,30])

wb.save('ekrem_info2.xlsx')
