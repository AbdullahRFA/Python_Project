def showBalance(balance):
    """
    This Python program allows users to check balance, deposit funds, withdraw funds, and exit a simple banking system.
    """
    print(f"\nYour Current Balance: {balance:.2f}")

def depositBalance(balance):
    try:
        tempBalance = float(input("Enter deposit amount: "))
        if tempBalance <= 0:
            print("\nDeposit amount can't be less than or equal to ZERO.")
            return 0
        else:
            print(f"\nDeposit Complete,\nYour Current Balance: {balance+tempBalance}")
            return tempBalance
    except ValueError:
        print("\nInvalid input. Please enter a numeric value.")
        return 0

def withdrawBalance(balance):
    try:
        tempBalance = float(input("Enter withdraw amount: "))
        if tempBalance <= 0:
            print("\nWithdraw amount can't be less than or equal to ZERO.")
            return 0
        elif tempBalance > balance:
            print("\nInsufficient funds!")
            print(f"\nYour Current Balance: {balance}")

            return 0
        else:
            print(f"\nWithdraw Complete,\nYour Current Balance: {balance-tempBalance}")
            return tempBalance
    except ValueError:
        print("\nInvalid input. Please enter a numeric value.")
        return 0

def main():
    balance = 0.0
    is_true = True
    while is_true:
        print("\n1. Show Balance")
        print("2. Deposit Balance")
        print("3. Withdraw Balance")
        print("4. Exit")
        
        try:
            result = int(input("Enter your choice (1-4): "))
            
            if result == 1:
                showBalance(balance)
            elif result == 2:
                balance += depositBalance(balance)
            elif result == 3:
                balance -= withdrawBalance(balance)
            elif result == 4:
                is_true = False
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("\nThank you! Have a nice day.\n")


main()

