class Fruit(object):
    
    def __init__(self):
        print("Fruit_Class - Function 1 - Init")
    
    def nutrition_main(self):
        print("Fruit_Class - Function 2 - Nutrition")

    def fruit_shape_main(self):
        print("Fruit_Class - Function 3 - Fruit_Shape")

class Apple(Fruit):
    
    def __init__(self):
        print("Child Class - Function 1 - Init")

    def nutrition_child(self):
        print("Child Class - Function 2 - Apple contains 9 percent of sugar")

    def color_child(self):
        print("Child Class - Function 3 - Apple is red")

f = Fruit()
f.nutrition_main()
f.fruit_shape_main()

a = Apple()
a.nutrition_child()
a.color_child()

a.nutrition_main()
a.fruit_shape_main()