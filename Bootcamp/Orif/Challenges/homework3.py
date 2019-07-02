car_list = ["Toyota","Volkswagen Group","General Motors","Ford","Nissan","Honda","Fiat Chrysler","Renault",
"Groupe PSA","Suzuki","SAIC","Daimler", "BMW", "Geetly", "Great Wall"]

result = []
result_no_t=[]
#index=0

for make in car_list:
    yes_it_contains_t= False

    for letter in make:
        if letter=="t" or letter=="T":
            yes_it_contains_t=True
            
            
    if yes_it_contains_t:      
        result.append(make)
    else:
        result_no_t.append(make)
            
print("All makes with letter t",result)
print("All makes without letter t",result_no_t)