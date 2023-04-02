# 12) Human Health Information Management System

import csv
import Model as Mod
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import MenuGUI

class Login:
    def Login(self):
        #Main login window
        self.loginWindow = tk.Tk()
        self.loginWindow.title("Human Health Information Management System")
        self.loginWindow.geometry("340x440")
        self.loginWindow.configure(bg="#333333")
        
        #Limit top level window
        self.popup = False

        frame = tk.Frame(self.loginWindow,bg="#333333")

        #Input value
        self.usernameI = StringVar()
        self.passwordI = StringVar()

        #Labels
        Welcome = tk.Label(frame,text="WELCOME!",bg="#333333",fg="#FFFFFF",font=("Arial",20))
        Username = tk.Label(frame,text="Username:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        Password = tk.Label(frame,text="Password:",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        Username.grid(column=0,row=1)
        Password.grid(column=0,row=2)

        #Entries
        iUser = tk.Entry(frame,width=20,font=("Arial",14),textvariable=self.usernameI)
        iPass = tk.Entry(frame,width=20,show="*",font=("Arial",14),textvariable=self.passwordI)
        
        iUser.grid(column=1,row=1,padx=5)
        iPass.grid(column=1,row=2,padx=5)

        #Buttons
        logBut = tk.Button(frame,text="Login",font=("Arial",12),command=self.loginVerify)
        logBut.grid(column=0,row=4,columnspan=2,pady=20)

        fgPassBut = tk.Button(frame,text="Forgot password?",font=("Arial",10,"italic"),command=self.openFgPass ,width=15,bg="#333333",fg="#BBD6B8")
        fgPassBut.grid(column=0,row=3,columnspan=2,sticky=tk.E)

        regisBut = tk.Button(frame,text="Register",font=("Arial",12),command=self.openRegis,width=20)
        regisBut.grid(column=0,row=6,columnspan=2)

        quitBut = tk.Button(frame,text="Exit",font=("Arial",12),command=self.Quit,width=20)
        quitBut.grid(column=0,row=7,columnspan=2,pady=10)

        space = tk.Label(frame,text="",bg="#333333")
        space.grid(column=0,row=5,sticky="news",pady=30)


        frame.pack()
        self.loginWindow.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.loginWindow.mainloop()

    #Check if forgot pass window if exist -> not open register window
    def openRegis(self):
        try:
            if self.popup == False:
                self.popup = True
                self.Register()
            elif self.fgPassWindow.winfo_exists():
                self.fgPassWindow.lift()
        except AttributeError:
            self.regisWindow.lift()

    #Check if register window if exist -> not open forgot pass window
    def openFgPass(self):
        try:
            if self.popup == False:
                self.popup = True
                self.fgPass()
            elif self.regisWindow.winfo_exists():
                self.regisWindow.lift()
        except AttributeError:
            self.fgPassWindow.lift()

    #Open forgot pass 1
    def fgPass(self):
        #This try is useful when come back from forgot pass 2
        try:
            if not self.fgPassWindow.winfo_exists():
                self.fgPassWindow = tk.Toplevel(self.loginWindow)
                self.fgPassWindow.title("Forgotten password")
                self.fgPassWindow.geometry("340x340")
                self.fgPassWindow.configure(bg="#333333")
        except AttributeError:
            self.fgPassWindow = tk.Toplevel(self.loginWindow)
            self.fgPassWindow.title("Forgotten password")
            self.fgPassWindow.geometry("340x340")
            self.fgPassWindow.configure(bg="#333333")
        
        self.frameP = tk.Frame(self.fgPassWindow,bg="#333333")

        #This variable is important !!!
        self.yourUsername = StringVar()

        #Label
        Welcome = tk.Label(self.frameP,text="Find your account",bg="#333333",fg="#FFFFFF",font=("Arial",20))
        texts = tk.Label(self.frameP,text="Please enter your username",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        #Entry
        self.yourUserEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourUsername)
        self.yourUserEntry.grid(column=0,row=2,columnspan=2)

        #Buttons
        nextBut = tk.Button(self.frameP,text="Next",font=("Arial",12),command=self.fgPass2)
        nextBut.grid(column=0,row=6,columnspan=2,pady=20)
        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.closeFgPass,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()

    #Check if username exist -> open forgot pass 2 window
    def fgPass2(self):
        hasName = False
        with open("user.csv", mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                if self.yourUsername.get() == line[0]:
                    hasName = True
                    if len(line[2]) != 0:
                        self.named = self.yourUsername.get()
                        questioned = line[2]
                        self.answered = line[3]
                        self.yourUserEntry.delete(0,END)
                        self.frameP.destroy()
                        self.openfgPass2(questioned)
                        break
                    else:
                        messagebox.showerror(title="Not enough information",message="Can not reset your password due to lack of information")
        if hasName == False:
            messagebox.showerror(title="Invalid username",message="Username not found")

    #Open forgot pass 2 window
    def openfgPass2(self,questioned):
        self.frameP = tk.Frame(self.fgPassWindow,bg="#333333")

        #Labels
        Welcome = tk.Label(self.frameP,text="Please answer this question",bg="#333333",fg="#FFFFFF",font=("Arial",18))
        texts = tk.Label(self.frameP,text=questioned,bg="#333333",fg="#FFFFFF",font=("Arial",14))
        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        #Important variable
        self.yourAnswer = StringVar()

        #Entry
        self.yourAnswerEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourAnswer)
        self.yourAnswerEntry.grid(column=0,row=2,columnspan=2)

        #Buttons
        nextBut2 = tk.Button(self.frameP,text="Next",font=("Arial",12),command=self.checkAnsFP)
        nextBut2.grid(column=0,row=6,columnspan=2,pady=20)
        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.backFgPass,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()

    #Back to forgot pass 1 window
    def backFgPass(self):
        self.yourAnswerEntry.delete(0,END)
        self.frameP.destroy()
        self.fgPass()

    #Check if answer is correct -> go to reset pass window
    def checkAnsFP(self):
        if self.yourAnswer.get() == self.answered:
            self.yourAnswerEntry.delete(0,END)
            self.frameP.destroy()
            self.resetPass()
        else:
            messagebox.showerror(title="Incorrect answer",message="Your answer is incorrect")

    #Reset password
    def resetPass(self):
        self.frameP = tk.Frame(self.fgPassWindow,bg="#333333")

        #Labels
        Welcome = tk.Label(self.frameP,text="Reset password",bg="#333333",fg="#FFFFFF",font=("Arial",18))
        texts = tk.Label(self.frameP,text="Please enter your new password",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        #Important variable
        self.yourPassword = StringVar()

        #Entry
        self.yourPassEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourPassword)
        self.yourPassEntry.grid(column=0,row=2,columnspan=2)

        #Buttons
        resetBut = tk.Button(self.frameP,text="Reset",font=("Arial",12),command=self.resetComplete)
        resetBut.grid(column=0,row=6,columnspan=2,pady=20)
        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.backFgPass2,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()
        pass
        
    #Done reset pass
    def resetComplete(self):
        if len(self.yourPassword.get())<1 or len(self.yourPassword.get())>20:
            messagebox.showerror(title="Invalid password",message="Length of password must be between 1 and 20 characters")
        else:
            Mod.changePassword(self.named,self.yourPassword.get())
            self.yourPassEntry.delete(0,END)
            self.closeFgPass()

    #Back to forgot pass 2 window
    def backFgPass2(self):
        self.yourPassEntry.delete(0,END)
        self.frameP.destroy()
        self.openfgPass2()

    #Back to main login window from forgot pass window
    def closeFgPass(self):
        self.popup = False
        self.fgPassWindow.destroy()

    #Back to main login window from regis window
    def closeRegis(self):
        self.popup = False
        self.regisWindow.destroy()

    #Open register window
    def Register(self):
        self.regisWindow = tk.Toplevel(self.loginWindow)
        self.regisWindow.title("Register")
        self.regisWindow.geometry("340x340")
        self.regisWindow.configure(bg="#333333")

        frame = tk.Frame(self.regisWindow,bg="#333333")

        self.newUserName = StringVar()
        self.newUserPassword = StringVar()
        self.confirmPass = StringVar()
        self.ans = StringVar()

        Welcome = tk.Label(frame,text="Create your account",bg="#333333",fg="#FFFFFF",font=("Arial",20))
        newUsername = tk.Label(frame,text="Username:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        newPassword = tk.Label(frame,text="Password:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        Confirm = tk.Label(frame,text="Confirm:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        quesLabel = tk.Label(frame,text="Question:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        self.Question = ttk.Combobox(frame,values=["","What is your pet's name?","What is your birthday?",
                                                   "What is your best friend's name?"],width=33)
        self.Question.current(0)
        ansLabel = tk.Label(frame,text="Answer:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        self.answerEntry = tk.Entry(frame,width=20,font=("Arial",14),textvariable=self.ans)

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        newUsername.grid(column=0,row=1,sticky=tk.W)
        newPassword.grid(column=0,row=2,sticky=tk.W)
        Confirm.grid(column=0,row=3,sticky=tk.W),
        quesLabel.grid(column=0,row=4,sticky=tk.W)
        self.Question.grid(column=1,row=4)
        ansLabel.grid(column=0,row=5,sticky=tk.W)
        self.answerEntry.grid(column=1,row=5)

        self.newUserEntry = tk.Entry(frame,width=20,font=("Arial",14),textvariable=self.newUserName)
        self.newPassEntry = tk.Entry(frame,width=20,show="*",font=("Arial",14),textvariable=self.newUserPassword)
        self.confirmPEntry = tk.Entry(frame,width=20,show="*",font=("Arial",14),textvariable=self.confirmPass)

        
        self.newUserEntry.grid(column=1,row=1,padx=5)
        self.newPassEntry.grid(column=1,row=2,padx=5)
        self.confirmPEntry.grid(column=1,row=3,padx=5)


        creatBut = tk.Button(frame,text="Create",font=("Arial",12),command=self.regisCreat)
        creatBut.grid(column=0,row=6,columnspan=2,pady=20)

        backBut = tk.Button(frame,text="Back",font=("Arial",12),command=self.closeRegis,width=20)
        backBut.grid(column=0,row=7,columnspan=2)


        frame.pack()

        self.regisWindow.protocol("WM_DELETE_WINDOW",self.closeRegis)
        self.regisWindow.mainloop()

    #Button create is clicked -> check
    def regisCreat(self):
        existName = False
        with open("user.csv", mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                if self.newUserName.get() == line[0]:
                    messagebox.showerror(title="Username is already existed",message="This username is taken!")
                    existName = True
                    break
        if existName == False:
            if len(self.newUserName.get()) < 4 or len(self.newUserName.get()) > 12:
                messagebox.showerror(title="Invalid username",message="Length of username must be between 4 and 12 characters")
            elif len(self.newUserPassword.get()) < 1 or len(self.newUserName.get()) > 20:
                messagebox.showerror(title="Invalid password",message="Length of password must be between 1 and 20 characters")
            elif self.newUserPassword.get() != self.confirmPass.get():
                messagebox.showerror(title="Not identical",message="Passwords are not the same")
            else:
                self.creatAcc()

    #Create account
    def creatAcc(self):
        if len(self.Question.get()) != 0:
            Mod.get_user_info(self.newUserName.get(),self.newUserPassword.get(),self.Question.get(),self.ans.get())
        else:
            Mod.get_user_info(self.newUserName.get(),self.newUserPassword.get(),None,None)

        self.newUserEntry.delete(0,END)
        self.newPassEntry.delete(0,END)
        self.confirmPEntry.delete(0,END)
        self.Question.current(0)
        self.answerEntry.delete(0,END)
        pass

    #Close program
    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):
            exit()

    #Button Quit is clicked
    def Quit(self):
        self.on_closing()

    #Verify username and password
    def loginVerify(self):
        success = False
        with open("user.csv", mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                if self.usernameI.get() == line[0]:
                    if self.passwordI.get() == line[1]:
                        self.loginSuccess(line[0])
                        success = True
                        break
        if success == False:
            messagebox.showerror(title="Invalid login",message="Username or password is incorrect")

    #Go to GUI window
    def loginSuccess(self,username):
        self.loginWindow.destroy()
        MenuGUI.run(username)

if __name__ == "__main__":
    Mod.initPatient()
    Mod.initUser()
    login = Login()
    login.Login()