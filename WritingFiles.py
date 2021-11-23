import csv
from os import path
from datetime import datetime


def make_first_deposit(username, client):
    deposit = input("Type in how much you would like to deposit: $")    # Asks how much to deposit
    date_and_time = datetime.now()                                      # Gets date and time
    user = str(username)

    if path.exists("ClientFiles/" + user) is True:
        raise Exception("Sorry, an error has occurred: \n"
                        "Error 1 - a file has already been created for this account")
    elif path.exists("ClientFiles/" + user) is False:
        with open("ClientFiles/" + user, 'w') as f:
            f.write(str(date_and_time) + " - ACCOUNT CREATED - First Deposit:+$" + deposit)
            f.close()
            info_processor(client, deposit)


def make_deposit(username):
    deposit = input("Type in how much you would like to deposit: $")
    date_and_time = datetime.now()
    user = str(username)

    with open('ClientList.txt', 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        for row in lines:
            if row[0] == user:
                total = float(row[4])
                total = total + float(deposit)
                row[4] = str(total)
                with open('ClientList.txt', 'w') as f2:
                    writer2 = csv.writer(f2)
                    writer2.writerows(lines)
                with open("ClientFiles/" + user, 'a', newline='') as f3:
                    f3.write("\n" + str(date_and_time) + " - Deposit:+$" + deposit + " - Total=" + str(total))
                    print("You have deposited: " + deposit + "\n"
                          "Your total is: " + row[4])
                f.close()
                f2.close()
                f3.close()
                import_welcome_back(username)
            # elif row[0] != user:
            #     raise Exception("Sorry, an error has occurred: \n"
            #                     "Error 1 - a file has already been created for this account")


def make_withdrawal(username):
    withdrawal = input("Type in how much you would like to withdraw: $")
    date_and_time = datetime.now()

    with open('ClientList.txt', 'r', newline='') as f:
        reader = csv.reader(f)
        lines = list(reader)
        for row in lines:                    # initially had a 'user' variable to make a string of username
            if row[0] == username:
                x = row
                if float(withdrawal) > float(x[4]):
                    print("Sorry, your account balance is: $" + x[4] + ".\n"
                          "You do not have enough funds to make this withdrawal.")
                    inp = input("Would you like to make another withdrawal? Type 'Yes' or 'No': ")
                    if inp == "Yes":
                        make_withdrawal(username)
                    elif inp == "No":
                        import_welcome_back(username)
                    else:
                        print("Sorry, invalid answer. You are returning to the welcome back screen - - -")
                        import_welcome_back(username)
                elif float(withdrawal) <= float(x[4]):
                    total = float(x[4])
                    total = total - float(withdrawal)
                    x[4] = str(total)
                    with open('ClientList.txt', 'w') as f2:
                        writer2 = csv.writer(f2)
                        writer2.writerows(lines)
                    with open("ClientFiles/" + username, 'a', newline='') as f3:
                        f3.write("\n" + str(date_and_time) + " - Withdrawal:-$" + withdrawal + " - Total=" + str(total))
                        print("You have withdrawn: " + withdrawal + "\n"
                              "Your total is: " + x[4])
                    f.close()
                    f2.close()
                    f3.close()
                    import_welcome_back(username)
            # elif row[0] != username:
            #     raise Exception("Sorry, an error has occurred: \n"
            #                     "Error 1 - a file has already been created for this account")


def account_balance(username):
    with open('ClientList.txt', 'r', newline='') as f:
        reader = csv.reader(f)
        lines = list(reader)
        for row in lines:
            if row[0] == username:
                x = row
                print("Your current account balance is: $" + str(x[4]))
                import_welcome_back(username)


def write_file(client):                     # Checks if ClientList.txt file exists and then writes to it
    if path.exists("ClientList.txt") is True:
        with open('ClientList.txt', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(client)
        f.close()
    if path.exists("ClientList.txt") is False:
        with open('ClientList.txt', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(client)
        f.close()


def import_welcome_back(x):
    import WelcomeBack
    WelcomeBack.welcome_back(x)


def info_processor(process_client, deposit):
    process_client.append(deposit)
    write_file(process_client)
    print("You have successfully been added to our system! You will now be taken to our welcome back screen - - -")
    import_welcome_back(process_client[0])
