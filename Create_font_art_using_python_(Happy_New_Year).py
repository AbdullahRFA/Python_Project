from colorama import Fore, Style
import pyfiglet

def display_ascci_art(message, color):
    """
    Function to render and display ASCII art in a specified color.

    Args:
        message (str): The text to convert into ASCII art.
        color (str): The color to apply from Colorama's `Fore` module.
    """
    ascii_art = pyfiglet.figlet_format(message)
    print(color+ascii_art+Style.RESET_ALL)

def main():
     display_ascci_art("Happy New Year", Fore.GREEN)
     display_ascci_art("Wish You All The Best", Fore.YELLOW)
     display_ascci_art("Celebrate With Joy!", Fore.CYAN)
     
if __name__ == "__main__":
    main()