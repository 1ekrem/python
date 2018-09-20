# Open an existing worksheet
# Add a value
# add other values
# save

import openpyxl

wb = openpyxl.load_workbook("ekrem_info2.xlsx")

ws_ekrem = wb['Ekrem']

first_cell=ws_ekrem["A1"]
ws_ekrem.append([])

print(first_cell.value)
