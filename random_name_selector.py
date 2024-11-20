import random

def random_name_picker(names):
    return random.choice(names)

names = input("Enter names separated by space: ").split(" ")
print("Names are : ",names)
print("Selected Name:", random_name_picker(names))