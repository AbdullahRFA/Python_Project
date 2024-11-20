import random

def monty_hall_simulation():
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)
    
    player_choice = random.randint(0, 2)
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
    host_opens = random.choice(remaining_doors)
    
    switch_choice = [i for i in range(3) if i != player_choice and i != host_opens][0]
    
    return "Switching Wins" if doors[switch_choice] == 1 else "Staying Wins"

results = {"Switching Wins": 0, "Staying Wins": 0}
for _ in range(1000):
    result = monty_hall_simulation()
    results[result] += 1

print("Simulation Results (1000 Trials):")
print(results)