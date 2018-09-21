#Get the total of the values

import openpyxl

wb = openpyxl.load_workbook("car.xlsx")
ws = wb.active

grouping_cells=['A1']

for value in ws['B']:

