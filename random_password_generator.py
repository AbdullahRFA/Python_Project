# import random
# import string

# def random_password_generator(length=12):
#     """
#     The function `random_password_generator` generates a random password of a specified length using a combination of letters, digits, and punctuation characters.
    
#     :param length: The `length` parameter in the `random_password_generator` function specifies the length of the password to be generated. By default, if no length is provided when calling the function, it will generate a password of length 12 characters. You can also specify a different length when calling the function if you, defaults to 12 (optional)
#     :return: The function `random_password_generator` returns a randomly generated password of the specified length.
#     """
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password=''.join(random.choice(characters) for _ in range(length))
#     return password

# print("Your Secure Password : ",random_password_generator())




# The code snippet you provided is generating a random password of length 20 characters using a combination of uppercase letters, lowercase letters, digits, and punctuation characters. Here is a breakdown of what the code does:
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password=""
for _ in range(20):
    password+=random.choice(characters)
    
print("Your Secure Passrowd : ",password)

