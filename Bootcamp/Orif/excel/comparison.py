import openpyxl

#Open the workbook
first = openpyxl.load_workbook('first.xlsx')
first_ws = first.active

second = openpyxl.load_workbook('second.xlsx')
second_ws = second.active

comparison_cells = ['B1', 'B2', 'B3']

flag_no_issues = True

for ref in comparison_cells:
    first_val = first_ws[ref].value
    second_val = second_ws[ref].value
    if first_val != second_val:
        flag_no_issues = False
        print("Non-matchin value!", ref, first_val, second_val)

print("Comparison finished")

if flag_no_issues:
    print("No issues found.")
else:
    print("Issues found.")


