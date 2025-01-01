from colorama import Fore, Style
import pyfiglet

def display_ascii_art(message, color):
    """
    Function to render and display ASCII art in a specified color.

    Args:
        message (str): The text to convert into ASCII art.
        color (str): The color to apply from Colorama's `Fore` module.
    """
    ascii_art = pyfiglet.figlet_format(message)
    print(color+ascii_art+Style.RESET_ALL)

def main():
     display_ascii_art("Happy New Year", Fore.GREEN)
     display_ascii_art("Wish You All The Best", Fore.YELLOW)
     display_ascii_art("Celebrate With Joy!", Fore.CYAN)
     
if __name__ == "__main__":
    main()