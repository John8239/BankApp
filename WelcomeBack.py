import WritingFiles


def welcome_back(username):
    choice = input("Welcome back! What would you like to do? \n"
                   "Please type: 'Account Balance', 'Deposit', 'Withdraw', or 'Quit'")
    if choice == "Account Balance":
        WritingFiles.account_balance(username)

    elif choice == "Deposit":
        WritingFiles.make_deposit(username)

    elif choice == "Withdraw":
        WritingFiles.make_withdrawal(username)

    elif choice == "Quit":
        quit()

    else:
        print("I'm sorry there seems to have been an error.\n"
              "make sure to print your choice exactly as the options are written.")
        welcome_back(username)
