import openpyxl as xl

wb = xl.Workbook()
ws = wb.active

data = [
    ["PID", "Total Amount"],
    ["IA1", 145],
    ["IA5", 25],
    ["IO1", 800],
    ["IO2", 200],
    ["IO7", 400],
    ["OO1", 250]
]

for i in data:
    ws.append(i)

ws.auto_filter.ref="A1:B7"
ws.auto_filter.add_filter_column(0, ["IO7"])
ws.auto_filter.add_sort_condition("B2:B7", False)
wb.save("C:\\PythonClass\\excel_pda_np\\pid_formating.xlsx")
print("Done!")

