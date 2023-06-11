# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Tom", 5) 
cat2 = Cat("Garfield", 12) 
cat3 = Cat("Bola de nieve", 6)

cat_list = [cat1.age, cat2.age, cat3.age]
print(cat_list)
    
def get_oldest():
    print(f"The oldest cat is {max(cat_list)} years old!")

get_oldest()


    

