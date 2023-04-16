from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Controller as Ctrl

class PreLogin:
    BG_COLOR = "#333333"
    def mainFrame(self):
        #Init main window
        self.preLoginWindow = tk.Tk()
        self.preLoginWindow.title("Human Health Information Management System")
        self.preLoginWindow.geometry("340x220")
        self.preLoginWindow.resizable(FALSE,FALSE)
        self.preLoginWindow.configure(bg=self.BG_COLOR)

        #Frame to center everything
        mainFrame = tk.Frame(self.preLoginWindow,bg=self.BG_COLOR)

        title = tk.Label(mainFrame,text="YOU ARE",bg=self.BG_COLOR,fg="#FFFFFF",font=("Franklin Gothic Heavy",25))
        title.grid(column=0,row=0,pady=5)

        #Button
        docBut = tk.Button(mainFrame,text="Doctor",font=("Arial",14),command=self.docPressed,width=15,height=2,anchor=CENTER,borderwidth=3)
        docBut.grid(column=0,row=1,pady=5)

        patientBut = tk.Button(mainFrame,text="Patient",font=("Arial",14),command=self.patPressed,width=15,height=2,anchor=CENTER,borderwidth=3)
        patientBut.grid(column=0,row=2,pady=5)

        mainFrame.pack()

        self.preLoginWindow.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.preLoginWindow.mainloop()

    #Ask and close
    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):
            self.preLoginWindow.destroy()

    #Open doctor GUI
    def docPressed(self):
        self.preLoginWindow.destroy()
        Ctrl.start()

    #Open patient GUI
    def patPressed(self):
        self.preLoginWindow.destroy()
        Ctrl.toPatientGUI()

def run():
    k = PreLogin()
    k.mainFrame()