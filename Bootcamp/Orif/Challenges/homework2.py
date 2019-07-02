# OPTION 1

car_list = ["Toyota","Volkswagen Group","Hyundai / Kia","General Motors","Ford","Nissan","Honda","Fiat Chrysler","Renault","Groupe PSA","Suzuki","SAIC","Daimler",
"BMW","Changan", "Mazda", "BAIC", "Dongfeng Motor", "Geely", "Great Wall"]

car_list_with_t = []
index=0

while True:
    make =car_list[index]


    if make.find('t') > -1:
        car_list_with_t.append(make)

    index=index+1
    if index >= len(car_list):
        break

print(car_list_with_t)