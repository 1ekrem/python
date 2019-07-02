
car_list = ["Toyota","Volkswagen Group","Hyundai / Kia","General Motors","Ford","Nissan","Honda","Fiat Chrysler","Renault","Groupe PSA","Suzuki","SAIC","Daimler",
"BMW","Changan", "Mazda", "BAIC", "Dongfeng Motor", "Geely", "Great Wall"]

car_list_with_t = []

for name in car_list:
    if name.find('t') > -1:
        car_list_with_t.append(name)
print(car_list_with_t)   


for i in car_list:
    print(i)