import random
import string

def random_password_generator(length=12):
    """
    The function `random_password_generator` generates a random password of a specified length using a combination of letters, digits, and punctuation characters.
    
    :param length: The `length` parameter in the `random_password_generator` function specifies the length of the password to be generated. By default, if no length is provided when calling the function, it will generate a password of length 12 characters. You can also specify a different length when calling the function if you, defaults to 12 (optional)
    :return: The function `random_password_generator` returns a randomly generated password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

print("Your Secure Password : ",random_password_generator())


