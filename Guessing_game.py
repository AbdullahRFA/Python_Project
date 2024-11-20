import random
number_to_be_guessed = random.randint(1,100)
print("Guessing number is in between 1 and 100 ")
attempts=0
def guess_number(number_to_be_guessed):
    # """
    # The function `guess_number` allows a user to guess a number and provides feedback on whether the guess is too high or too low until the correct number is guessed.
    
    # :param number_to_be_guessed: It looks like the code you provided is a function called `guess_number` that allows a user to guess a number until they guess the correct number. The function takes the `number_to_be_guessed` as a parameter, which is the number that the user needs to guess
    # """
    global attempts
    while True:
        attempts +=1
        number = int(input("Enter your guessing numner : "))
        if number > number_to_be_guessed:
            print("Guessed number too high")
        elif number < number_to_be_guessed:
            print("Guessing number is too low")
        else:
            print(f"Congratulations\nYou guessed the number in {attempts} attempts")
            break
            
guess_number(number_to_be_guessed)