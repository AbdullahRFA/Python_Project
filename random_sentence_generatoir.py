import random

"""
    The function generates a random sentence by selecting a subject, verb, and object from predefined lists and concatenating them together.
"""

subjects = ["The cat", "A robot", "My friend", "The teacher"]
verbs = ["jumps", "runs", "sings", "dances"]
objects = ["in the park", "on the roof", "during the night", "on the street"]
sentence=''
def sentence_generator():
    global sentence
    sentence += f"{random.choice(subjects)} "
    sentence += f"{random.choice(verbs)} "
    sentence += f"{random.choice(objects)}."

sentence_generator()
    
print("Random Sentence Is : ",sentence)

    