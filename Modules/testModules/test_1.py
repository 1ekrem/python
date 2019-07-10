import random

# import sys
# sys.path.append(".")

from Modules.module1.multiplier import multiplier
from Modules.module2.subtractor import subtractor

x=random.randint(5,10)
y=random.randint(5,10)

m = multiplier
s = subtractor

print("First Number:", x,"\n", 
        "Second Number:",y,"\n", 
            "Mutiply: ", m(x,y), "\n",
            "Subtract: ", s(x,y))