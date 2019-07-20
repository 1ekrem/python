number_list = [1,2,2,3,4,4,5,5,6,7]
alpha_numeric_list = ['a','s','g', 'g', 'q', 'c', 'p', 'p',
                        3,4,5,6,7,3,9,'c','%','$','%']

class functions:

    def __init__(self, array_list):
        self.array_list = array_list

    def find_duplicates(self):
        duplicates = []
        for i in range(len(self.array_list)):
            for k in range(i+1, len(self.array_list)):
                if self.array_list[i] == self.array_list[k] and (self.array_list[i]) not in duplicates:
                    duplicates.append(self.array_list[i])
        
        print("Duplicated Values:", duplicates)
        
    def count_duplicated_elements(self):
        countvalues = {}
        duplicates = {}
        for i in (set(self.array_list)):
            countvalues[i]=self.array_list.count(i)
            if self.array_list.count(i) > 1:
                duplicates[i]=self.array_list.count(i)
        print("Values counted: ", countvalues)
        print("Duplicated Values after counting", duplicates)

obj = functions(alpha_numeric_list)
obj.find_duplicates()
obj.count_duplicated_elements()


