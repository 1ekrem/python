# dynamic number of values
# all available cells


import openpyxl

wb = openpyxl.load_workbook('multiplication_result.xlsx')
ws = wb.active
for row in ws.iter_rows():
    row_cells = []
    for cell in row:
        row_cells.append(cell.value)
    
    print(row_cells)