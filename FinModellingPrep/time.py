from cgi import print_arguments
import datetime 


now = datetime.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(dt_string)


x = datetime.datetime.now().strftime("%m-%d-%Y")

print(x)