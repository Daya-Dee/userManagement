#CURRENT PROJECT

from tkinter import *
from tkinter import font
import json
import os
from PIL import ImageTk, Image

if not os.path.exists("./user.json"):
    with open("./user.json", "w+") as f:
        f.write("{}")
        
class C:
    
    def __init__(self):
        with open("user.json", "r") as reader:
            try:
                self.userdata = json.load(reader)
            except Exception as e:
                self.userdata = {}

    def register_user(self):
        
        username_info = self.username.get()
        password_info = self.password.get()
        first_name_info = self.first_name.get()
        last_name_info = self.last_name.get()
        birthday_info = self.bday.get()
        
        self.userdata[username_info] = {
                "Username": username_info,  
                "Password":password_info,
                "First name":first_name_info,
                "Last name":last_name_info,
                "Birthday":birthday_info
            }
        with open("user.json", "w") as f:
            json.dump(self.userdata, f)
        
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.fname_entry.delete(0, END)
        self.lname_entry.delete(0, END)
        self.bday_entry.delete(0, END)
        
        Label(self.screen1, text = "Registration Success", fg = "green", font=("Lucida Calligraphy", 11)).pack()
    
    
    def register(self):
        self.screen1 = Toplevel(self.screen)
        self.screen1.title("Register")
        self.screen1.geometry("400x350")
        
        self.username = StringVar()
        self.password = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.bday = StringVar()
        #TITLE OF SCREEN
        Label(self.screen1, text = "Please enter your details below").pack()
        Label(self.screen1, text = "").pack()
        #FIRST NAME
        Label(self.screen1, text = "First Name * ").pack()
        self.fname_entry = Entry(self.screen1, textvariable = self.first_name)
        self.fname_entry.pack()
        #LAST NAME
        Label(self.screen1, text = "Last Name * ").pack()
        self.lname_entry = Entry(self.screen1, textvariable = self.last_name)
        self.lname_entry.pack()
        #BIRTHDAY
        Label(self.screen1, text = "Birthday (MM/DD/YYYY) * ").pack()
        self.bday_entry = Entry(self.screen1, textvariable = self.bday)
        self.bday_entry.pack()
        #USERNAME
        Label(self.screen1, text = "Username * ").pack()
        self.username_entry = Entry(self.screen1, textvariable = self.username)
        self.username_entry.pack()
        #PASSWORD
        Label(self.screen1, text = "Password * ").pack()
        self.password_entry = Entry(self.screen1, textvariable = self.password)
        self.password_entry.pack()
        
        Label(self.screen1, text = "").pack()
        Button(self.screen1, text = "Register", width = 10, height = 1, command = self.register_user).pack()
    
    def login(self):
        self.screen1 = Toplevel(self.screen)
        self.screen1.title("Login")
        self.screen1.geometry("300x250")
        
        self.username = StringVar()
        self.password = StringVar()
        #TITLE OF SCREEN
        Label(self.screen1, text = "Please enter your details below").pack()
        Label(self.screen1, text = "").pack()
        #USERNAME
        Label(self.screen1, text = "Username * ").pack()
        self.username_entry = Entry(self.screen1, textvariable = self.username)
        self.username_entry.pack()
        #PASSWORD
        Label(self.screen1, text = "Password * ").pack()
        self.password_entry = Entry(self.screen1, textvariable = self.password)
        self.password_entry.pack()
    
        Label(self.screen1, text = "").pack()
        Button(self.screen1, text = "Login", width = 10, height = 1, command = self.runLoginChecks).pack()

    def postlogin(self):
        self.screen2 = Toplevel(self.screen)
        self.screen2.title("You're logged in! :D")
        self.screen2.geometry("500x500")
        
        img = Image.open("cat.png")
        img = img.resize((300,300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        
        l1 = Label(self.screen2, image=test)
        l1.image = test
        l1.pack()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username not in self.userdata:
            return False
        success = self.userdata[username]["Password"]==password
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        return success
    
    def runLoginChecks(self):
        if not self.check_login():
            #if we're here, this failed login
            return
        Label(self.screen1, text = "Login Success", fg = "green", font=("Lucida Calligraphy", 11)).pack()
        self.postlogin()
        
    def main_screen(self):
        self.screen = Tk()
        self.screen.geometry("300x250")
        
        self.screen.title("User System 1.1")
        Label(text = "User System 1.1", bg = "light grey", width = "300", height = "2", font=("Lucida Calligraphy", 13)).pack()   
        Label(text = "").pack()
        Button(text = "Login", fg = "black", bg = "light grey", height = "2", width = "30", command = self.login).pack()
        Label(text = "").pack()
        Button(text = "Register", fg = "black", bg = "light grey", height = "2", width = "30", command = self.register).pack()
    
        self.screen.mainloop()
        
win = C()
win.main_screen()