class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1, dog2, dog3 = Dog("Pedro", 23), Dog("Luis", 10), Dog("Poncho", 3)
list1 = [dog1.age, dog2.age, dog3.age]
dog_name =[dog1.name, dog2.name, dog3.name]


def age_calc():
    print(f'the oldest dog is {max(list1)} years old!')

def find_pedro():
    for name in dog_name:
        if name == "Pedro":
            print("Pedro esta aquí")



age_calc()
find_pedro()