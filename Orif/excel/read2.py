import openpyxl

wb = openpyxl.load_workbook("sample.xlsx")
ws = wb.active

first_cell = ws["A2"]

print(first_cell.value)