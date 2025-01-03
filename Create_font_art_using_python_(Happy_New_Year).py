# pip install colorama
# pip install pyfiglet

from colorama import Fore, Style
import pyfiglet
import time
def display_ascii_art(message, color, delay=0.5):
    """
    Function to render and display ASCII art in a specified color.

    Args:
        message (str): The text to convert into ASCII art.
        color (str): The color to apply from Colorama's `Fore` module.
    """
    ascii_art = pyfiglet.figlet_format(message)
    for lines in ascii_art.splitlines():
        print(color + lines + Style.RESET_ALL)
        time.sleep(delay)
    
def main():
    print(f"{Fore.RED}Starting The Celebration...")
    time.sleep(1)
    display_ascii_art("Happy New Year 2025", Fore.GREEN , delay=0.2)
    time.sleep(1)
    display_ascii_art("Wish You All The Best", Fore.YELLOW, delay=0.2)
    time.sleep(1)
    display_ascii_art("Celebrate With Joy!", Fore.CYAN, delay=0.1)
    time.sleep(1)
     
if __name__ == "__main__":
    main()