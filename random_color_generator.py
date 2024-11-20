import random

def random_color():
    """
    The function `random_color()` generates a random hexadecimal color code.
    :return: A random hexadecimal color code in the format "#RRGGBB", where RR, GG, and BB are two-digit hexadecimal values representing the red, green, and blue components of the color, respectively.
    """
    return f"#{random.randint(0, 0xFFFFFF):06x}"

print("Random Colors:")
for _ in range(5):
    print(random_color())