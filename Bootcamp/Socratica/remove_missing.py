# Remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "",
"Ecuador", "", "", "Venezuela"]

print(list(filter(None, countries)))