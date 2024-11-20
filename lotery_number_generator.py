import random

def lotery_number():
    return sorted(random.sample(range(1, 100),10))

print("Lotery Numbers : ",lotery_number())
