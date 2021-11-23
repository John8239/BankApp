import NewUserInfo
import ReturningUserInfo


def startup():
    first_question = input("Welcome, are you a new or returning member? Type 'New' or 'Returning'.")
    if first_question == "Returning":
        ReturningUserInfo.returning_user_info_check()
    elif first_question == "New":
        NewUserInfo.get_user_name()
    else:
        print("Sorry, an error has occurred, please try again.")
        startup()


startup()
