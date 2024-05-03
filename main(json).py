from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passowrd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(symbols)for _ in range(randint(2, 4))]
    symbols_list = [choice(numbers)for _ in range(randint(2, 4))]
    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("E:/Python/Course/password-manager/data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("E:/Python/Course/password-manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("E:/Python/Course/password-manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

            # with open("E:/Python/Course/password-manager/data.json", "w") as data_file:
            # json.dump(new_data,data_file,indent=4) #writing

            # data = json.load(new_data) #reading
            # print(data)
            # print(type(data))

            # with open("E:/Python/Course/password-manager/data.json", "r") as data_file:
            #     #Reading old data
            #     data = json.load(new_data) #updating
            #     #Updating old data with new data
            #     data.update(new_data)
            # with open("E:/Python/Course/password-manager/data.json", "w") as data_file:
            #     #Opening in write mode and saving the updated data
            #     json.dump(data,data_file,indent=4)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    website = website_input.get()
    try:
        with open("", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email:{email}\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(
                title="Error", message="No details for the website found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)


# LABELS
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# ENTRIES

website_input = Entry(width=21)
website_input.focus()  # focus on the website input box when app starts up so user can start typing right away without clicking it first
website_input.grid(column=1, row=1)


email_input = Entry(width=41)
email_input.insert(END, "")
email_input.grid(column=1, row=2, columnspan=2)


password_input = Entry(width=21)
password_input.grid(column=1, row=3)


# BUTTONS

button = Button(text="Generate Password", width=15, command=generate_passowrd)
button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=15, command=search_password)
search.grid(column=2, row=1)


window.mainloop()
