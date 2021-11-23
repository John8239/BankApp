from tkinter import *

root = Tk()
root.title("Sample Bank System!")
root.geometry("300x250")


def func():
    welcome_lab.grid_forget()


welcome_lab = Label(root, text="Welcome to SampleBank's online banking app! \n are you a new or returning member?")

new_member_button = Button(root, text="New")
return_member_button = Button(root, text="Returning", command=func)


welcome_lab.grid(row=0, column=0, columnspan=2)
new_member_button.grid(row=1, column=0)
return_member_button.grid(row=1, column=1)


root.mainloop()
