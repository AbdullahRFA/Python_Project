import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice (or type 'exit' to quit): ").strip().lower()
    print(f"You rolled a {roll_dice()}")
    if input("Roll again? (yes/no): ").strip().lower() != "yes":
        break
    


