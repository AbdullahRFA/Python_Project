## WorkFlow of project :
#  1. Input from user (Rock ,papper , scissor)
#  2. computer choose (computer will chose randomly)
#  print the winner

'''
Case 1
User choose Rock:

Rock - Rock = tie
Rock - paper = paper
Rock - scissor = Rock

case 2
user choose papper:

papper - paper = tie
papper - rock = papper
papper - scissor = scissor

case 3
user choose scissor:

scissor - scissor = tie
scissor - rock =rock
scissor - paper = scissor

'''
import random


def play_game(user_input,computer_choice):
    if user_input == computer_choice:
        print("\nBoth choose same, So game TIE!\n")
    elif user_input == 'rock':
        if computer_choice == 'papper':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You lose the game \n")
        elif computer_choice == 'scissor':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You win the game \n")
    elif user_input == 'papper':
        if computer_choice == 'scissor':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You lose the game \n")
        elif computer_choice == 'rock':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You win the game \n")
    elif user_input == 'scissor':
        if computer_choice == 'rock':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You lose the game \n")
        elif computer_choice == 'papper':
            print(f"\nYour moves {user_input} and computer moves {computer_choice} : You win the game \n")



list_item = ['Rock','Papper','Scissor']

is_true = True
while is_true:
    user_input = input("Enter your moves(Rock, Papper, Scissor) or press '0' to quit the gane : ")
    user_input=user_input.lower()
    computer_choice = random.choice(list_item)
    computer_choice = computer_choice.lower()
    play_game(user_input,computer_choice)
    if user_input == '0':
        print('\n Thank you, Have a nice day!\n')
        is_true = False