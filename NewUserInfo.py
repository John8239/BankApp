import WritingFiles
from os import path
import csv


first_name = ""
last_name = ""
username = ""


def import_main(x):
    import main

    if x == "a":
        main.startup()


def get_user_name():

    global first_name
    global last_name
    global username

    first_name = input("Welcome! Please enter your first name: ")       # Makes first and last name
    if len(first_name) < 2:
        print("Sorry, first name must be 2 or more characters.")
        get_user_name()
    if 2 <= len(first_name) < 4:
        for x in first_name:
            if len(first_name) <= 4:
                first_name = first_name + "x"
    first_name = first_name.capitalize()
    first_name = first_name.replace("'", "")

    last_name = input("And your last name: ")
    if len(last_name) < 2:
        print("Sorry, first name must be 2 or more characters.")
        get_user_name()
    if 2 <= len(last_name) < 4:
        for x in last_name:
            if len(last_name) <= 4:
                last_name = last_name + "x"
    last_name = last_name.capitalize()
    last_name = last_name.replace("'", "")

    username = first_name[0: 4] + last_name[0: 4]           # Creates username by taking first 4 chars from first and
                                                            # last names.
    confirm_username(username)


def confirm_username(username_v2):

    if path.exists("ClientList.txt") is False:
        with open('ClientList.txt', 'w', newline='') as f:    # Needed this because it is the first time the file will
            pass                                              # be opened
    elif path.exists("ClientList.txt") is True:
        with open('ClientList.txt', 'r') as f:                # Checks to see if username already exists in clients file
            reader = csv.reader(f)
            for row in reader:
                if username_v2 == row[0]:
                    user = len(username_v2)
                    if user == 8:
                        username_v2 = username_v2 + str(1)
                    elif len(username_v2) > 8:
                        user_list = list(username_v2)
                        last_char = len(user_list) - 1
                        str_last_char = str(username_v2[last_char])
                        user_list.pop(last_char)
                        str_last_char = str(int(str_last_char) + 1)
                        username_v2 = ''.join(user_list) + str(str_last_char)

    print("Your new username is: " + username_v2)

    make_user_password(username_v2, first_name, last_name)     # Goes to password function below


def make_user_password(user, first, last):                  # Creates and confirms password

    user_password = input("Please create a password.")
    password_confirmation = input("Please confirm your password.")

    if user_password == password_confirmation:
        if len(user_password) >= 8 and any(c.isdigit() for c in user_password) \
                and any(c.isupper() for c in user_password):
            client = [user, first, last, user_password]
            print("In order to complete your account set-up, please make your first deposit.")
            WritingFiles.make_first_deposit(user, client)     # If both passwords match, we go to the make first deposit
        else:                                                 # function
            print("Your password must contain at least 8 characters long and must contain a capital letter and a number"
                  "\nPlease try again: ")
            make_user_password(username, first_name, last_name)   # If not, the function starts again
    elif user_password != password_confirmation:
        print("Your password didn't match, try again: ")
        make_user_password(username, first_name, last_name)

