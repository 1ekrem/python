import openpyxl

wb = openpyxl.load_workbook("magento2.xlsx")
ws = wb.active

if ws["A1"].value == "username":
    username = ws["A2"]

if ws["B1"].value == "firstname":
    firstname = ws["B2"]

if ws["C1"].value == "lastname":
    lastname = ws["C2"]

if ws["D1"].value == "company":
    company = ws["D2"]

if ws["E1"].value == "street":
    street = ws["E2"]

if ws["F1"].value == "city":
    city = ws["F2"]

if ws["G1"].value == "state":
    state = ws["G2"]

if ws["H1"].value == "postcode":
    postcode = ws["H2"]

if ws["I1"].value == "country_id":
    country_id = ws["I2"]

if ws["J1"].value == "telephone":
    phonenumber = ws["J2"]

