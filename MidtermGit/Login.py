# 12) Human Health Information Management System


from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Login:
    def Login(self):
        self.loginWindow = tk.Tk()
        self.loginWindow.title("Human Health Information Management System")
        self.loginWindow.geometry("340x440")
        self.loginWindow.configure(bg="#333333")
        
        #Limit top level window
        self.popup = False

        frame = tk.Frame(self.loginWindow,bg="#333333")

        self.usernameI = StringVar()
        self.passwordI = StringVar()

        Welcome = tk.Label(frame,text="WELCOME!",bg="#333333",fg="#FFFFFF",font=("Arial",20))
        Username = tk.Label(frame,text="Username:",bg="#333333",fg="#FFFFFF",font=("Arial",14))
        Password = tk.Label(frame,text="Password:",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        Username.grid(column=0,row=1)
        Password.grid(column=0,row=2)

        iUser = tk.Entry(frame,width=20,font=("Arial",14),textvariable=self.usernameI)
        iPass = tk.Entry(frame,width=20,show="*",font=("Arial",14),textvariable=self.passwordI)
        
        iUser.grid(column=1,row=1,padx=5)
        iPass.grid(column=1,row=2,padx=5)


        logBut = tk.Button(frame,text="Login",font=("Arial",12),command=self.loginVerify)
        logBut.grid(column=0,row=4,columnspan=2,pady=20)

        fgPassBut = tk.Button(frame,text="Forgot password?",font=("Arial",10,"italic"),command=self.openFgPass ,width=15,bg="#333333",fg="#BBD6B8")
        fgPassBut.grid(column=0,row=3,columnspan=2,sticky=tk.E)

        regisBut = tk.Button(frame,text="Register",font=("Arial",12),command=self.openRegis,width=20)
        regisBut.grid(column=0,row=6,columnspan=2)

        quitBut = tk.Button(frame,text="Exit",font=("Arial",12),command=self.Quit,width=20)
        quitBut.grid(column=0,row=7,columnspan=2,pady=10)

        n = tk.Label(frame,text="",bg="#333333")
        n.grid(column=0,row=5,sticky="news",pady=30)


        frame.pack()
        self.loginWindow.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.loginWindow.mainloop()


    def openRegis(self):
        if self.popup == False:
            self.popup = True
            self.Register()
        else:
            self.fgPassWindow.lift()

    def openFgPass(self):
        if self.popup == False:
            self.popup = True
            self.fgPass()
        else:
            self.regisWindow.lift()

    def fgPass(self):
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

        self.yourUsername = StringVar()

        Welcome = tk.Label(self.frameP,text="Find your account",bg="#333333",fg="#FFFFFF",font=("Arial",20))
        texts = tk.Label(self.frameP,text="Please enter your username",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        self.yourUserEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourUsername)
        
        self.yourUserEntry.grid(column=0,row=2,columnspan=2)

        nextBut = tk.Button(self.frameP,text="Next",font=("Arial",12),command=self.fgPass2)
        nextBut.grid(column=0,row=6,columnspan=2,pady=20)

        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.closeFgPass,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()

    def fgPass2(self):
        if self.yourUserEntry.get() == "Dung":
            self.yourUserEntry.delete(0,END)
            self.frameP.destroy()
            self.openfgPass2()
        else:
            messagebox.showerror(title="Invalid username",message="Username not found")

    def openfgPass2(self):
        self.frameP = tk.Frame(self.fgPassWindow,bg="#333333")
        Welcome = tk.Label(self.frameP,text="Please answer this question",bg="#333333",fg="#FFFFFF",font=("Arial",18))
        texts = tk.Label(self.frameP,text="#Question",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        self.yourAnswer = StringVar()

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        self.yourAnswerEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourAnswer)
        self.yourAnswerEntry.grid(column=0,row=2,columnspan=2)

        nextBut2 = tk.Button(self.frameP,text="Next",font=("Arial",12),command=self.checkAnsFP)
        nextBut2.grid(column=0,row=6,columnspan=2,pady=20)

        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.backFgPass,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()

    def backFgPass(self):
        self.yourAnswerEntry.delete(0,END)
        self.frameP.destroy()
        self.fgPass()

    def checkAnsFP(self):
        if self.yourAnswer.get() == "Dung":
            self.yourAnswerEntry.delete(0,END)
            self.frameP.destroy()
            self.resetPass()
        else:
            messagebox.showerror(title="Incorrect answer",message="Your answer is incorrect")

    def resetPass(self):
        self.frameP = tk.Frame(self.fgPassWindow,bg="#333333")
        Welcome = tk.Label(self.frameP,text="Reset password",bg="#333333",fg="#FFFFFF",font=("Arial",18))
        texts = tk.Label(self.frameP,text="Please enter your new password",bg="#333333",fg="#FFFFFF",font=("Arial",14))

        self.yourPassword = StringVar()

        Welcome.grid(column=0,row=0,columnspan=2,sticky="news",pady=10)
        texts.grid(column=0,row=1,columnspan=2)

        self.yourPassEntry = tk.Entry(self.frameP,width=20,font=("Arial",14),textvariable=self.yourPassword)
        self.yourPassEntry.grid(column=0,row=2,columnspan=2)

        resetBut = tk.Button(self.frameP,text="Reset",font=("Arial",12),command=self.resetComplete)
        resetBut.grid(column=0,row=6,columnspan=2,pady=20)

        backBut = tk.Button(self.frameP,text="Back",font=("Arial",12),command=self.backFgPass2,width=20)
        backBut.grid(column=0,row=7,columnspan=2)

        self.frameP.pack()

        self.fgPassWindow.protocol("WM_DELETE_WINDOW",self.closeFgPass)
        self.fgPassWindow.mainloop()
        pass
        
    def resetComplete(self):
        # self.yourPassword.get()
        self.closeFgPass()

    def backFgPass2(self):
        self.yourPassEntry.delete(0,END)
        self.frameP.destroy()
        self.openfgPass2()

    def closeFgPass(self):
        self.popup = False
        self.fgPassWindow.destroy()

    def closeRegis(self):
        self.popup = False
        self.regisWindow.destroy()

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


    def regisCreat(self):
        if len(self.newUserName.get()) < 4 or len(self.newUserName.get()) > 12:
            messagebox.showerror(title="Invalid username",message="Length of username must between 4 and 12 characters")
        elif len(self.newUserPassword.get()) < 1 or len(self.newUserName.get()) > 20:
            messagebox.showerror(title="Invalid password",message="Length of password must between 1 and 20 characters")
        elif self.newUserPassword.get() != self.confirmPass.get():
            messagebox.showerror(title="Not identical",message="Passwords are not the same")
        else:
            self.creatAcc()

    def creatAcc(self):
        if len(self.Question.get()) != 0:
            #get question and answer
            pass

        self.newUserEntry.delete(0,END)
        self.newPassEntry.delete(0,END)
        self.confirmPEntry.delete(0,END)
        self.Question.current(0)
        self.answerEntry.delete(0,END)
        pass

    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):
            exit()

    def Quit(self):
        self.on_closing()

    def loginVerify(self):
        #Login success
        if self.usernameI.get() == "Dung" and self.passwordI.get() == "Dung":
            self.loginSuccess()
        else:
            messagebox.showerror(title="Invalid login",message="Username or password is incorrect")

    def loginSuccess(self):
        self.loginWindow.destroy()



if __name__ == "__main__":
    login = Login()
    login.Login()