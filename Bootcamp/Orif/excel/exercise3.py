import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

for i in range (1,10):
    ws['B' + str(i)] = "1 * "+str(i)

wb.save('looping.xlsx')