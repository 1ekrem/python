# List all the car manufacturer containing 't' in their name.

    # OPTION 1
car_list = ["Toyota","Volkswagen Group","Hyundai / Kia","General Motors","Ford","Nissan","Honda","Fiat Chrysler","Renault","Groupe PSA","Suzuki","SAIC","Daimler",
"BMW","Changan", "Mazda", "BAIC", "Dongfeng Motor", "Geely", "Great Wall"]

car_list_with_t = []

# for i in car_list:
#     if i.__contains__("t"):
#     #if i.find('t')!=-1:
#         car_list_with_t = car_list_with_t + i + " " 
# print("Names having 't' :", car_list_with_t)   

no_t=[]
# OPTION 2
for name in car_list:
    if name.find('t') > -1:
        car_list_with_t.append(name)
    else:
        no_t.append(name)


print(car_list_with_t) 
print(no_t)  


# for i in car_list:
#     print(i)

