import csv
import WelcomeBack


def returning_user_info_check():
    ent_user = input("Please enter your username: ")
    ent_pass = input("And your password: ")
    with open('ClientList.txt', newline='') as f:
        reader = csv.reader(f)
        counter = count_clients_in_file()
        count = 0
        for line in reader:
            count += 1
            if line[0] == ent_user:
                x = line
                if x[3] == ent_pass:
                    f.close()
                    WelcomeBack.welcome_back(ent_user)
                    break
                else:
                    print("Username or password is incorrect, try again.")
                    returning_user_info_check()
                    break
            elif line[0] != ent_user and count != counter:
                pass
            elif line[0] != ent_user and count != counter + 1:
                print("Username or password is incorrect, try again.")
                returning_user_info_check()


def count_clients_in_file():
    with open('ClientList.txt', newline='') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            counter += 1
        f.close()
        return counter

