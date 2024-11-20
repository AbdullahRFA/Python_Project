import random

def random_walk(steps):
    x, y = 0, 0
    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
    return x, y

steps = int(input("Enter the number of steps: "))
final_position = random_walk(steps)
print(f"The final position is: {final_position}")