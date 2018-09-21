import openpyxl

wb = openpyxl.load_workbook("looping.xlsx")
act_ws= wb.active

for i in range(1,10):
    act_ws['C'+str(i)]='='
    act_ws['D'+str(i)]=i

wb.save('looping.xlsx')