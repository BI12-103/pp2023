from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Model as Mod
import Controller as Ctrl


class PatientGUI:
    BG_COLOR_F = "#333333"
    BG_COLOR_SEARCH = "#EAE0DA"
    FG_COLOR_SEARCH = "#913175"
    def mainFrame(self):
        #Init main window
        self.patientWindow = tk.Tk()
        self.patientWindow.title("Human Health Information Management System")
        self.patientWindow.geometry("340x270")
        self.patientWindow.resizable(FALSE,FALSE)
        self.patientWindow.configure(bg=self.BG_COLOR_F)

        title = tk.Label(self.patientWindow,text="WELCOME!",bg=self.BG_COLOR_F,fg="#FFFFFF",font=("Franklin Gothic Heavy",25))
        title.grid(column=0,row=0,pady=5,columnspan=2,sticky="news",padx=90)

        #ID and entry
        self.Id = StringVar()
        id = tk.Label(self.patientWindow,text="Your ID",bg=self.BG_COLOR_F,fg="#FFFFFF",font=("Arial",16,"bold"))
        id.grid(column=0,row=1,padx=20,pady=10,sticky=tk.W)
        self.idEntry = tk.Entry(self.patientWindow,width=24,font=("Arial",16),textvariable=self.Id)
        self.idEntry.grid(column=0,row=2,sticky=tk.W,columnspan=2,padx=20)

        #Button
        checkBut = tk.Button(self.patientWindow,text="Check",font=("Arial",14),command=self.checkPressed,width=7,anchor=CENTER,borderwidth=3)
        checkBut.grid(column=0,row=3,pady=20,columnspan=2,padx=90)

        backBut = tk.Button(self.patientWindow,text="Back",font=("Arial",14),command=self.backPressed,width=7,anchor=CENTER,borderwidth=3)
        backBut.grid(column=0,row=4,columnspan=2,padx=90)

        self.patientWindow.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.patientWindow.mainloop()

    #Back to preloginWindow
    def backPressed(self):
        self.patientWindow.destroy()
        Ctrl.toPreLogin()

    #Ask and close
    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):
            self.patientWindow.destroy()

    #Check ID
    def checkPressed(self):
        if Mod.checkID(self.Id.get()):
            self.findByID2(self.Id.get())
        else:
            messagebox.showerror(title="Not found",message="Wrong ID")

    #GUI patientInfoWindow
    def findByID2(self,searchedID):
        #Create window
        self.patientInfoWindow = tk.Toplevel(self.patientWindow)
        self.patientInfoWindow.title("Find ID")
        self.patientInfoWindow.geometry("760x440")
        self.patientInfoWindow.configure(bg=self.BG_COLOR_SEARCH)
        self.patientInfoWindow.resizable(FALSE,FALSE)

        searchedName,searchedAddress,searchedAge,searchedCondition,searchedCreator,searchedAdvice = Mod.IDFindFull(searchedID)
        
        Welcome = tk.Label(self.patientInfoWindow,text="Your information",bg=self.BG_COLOR_SEARCH,font=("Arial",20,"bold"))
        Welcome.grid(column=3,row=0,columnspan=5,sticky="news",pady=10,ipadx=50)

        id = tk.Label(self.patientInfoWindow,text="ID",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        id.grid(column=0,row=1,padx=40,sticky=tk.W)
        IDValue = tk.Label(self.patientInfoWindow,text=searchedID,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14))
        IDValue.grid(column=1,row=1,sticky=tk.W)

        age = tk.Label(self.patientInfoWindow,text="Age",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        age.grid(column=3,row=1,padx=40,sticky=tk.E)
        ageValue = tk.Label(self.patientInfoWindow,text=searchedAge,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14))
        ageValue.grid(column=4,row=1,sticky=tk.W)

        name = tk.Label(self.patientInfoWindow,text="Name",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        name.grid(column=0,row=2,sticky=tk.W,padx=40,columnspan=2)
        nameValue = tk.Label(self.patientInfoWindow,text=searchedName,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14))
        nameValue.grid(column=1,row=2,sticky=tk.W,columnspan=4)

        address = tk.Label(self.patientInfoWindow,text="Address",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        address.grid(column=0,row=3,columnspan=2,sticky=tk.W,padx=40)
        addressValue = tk.Label(self.patientInfoWindow,text=searchedAddress,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14))
        addressValue.grid(column=1,row=3,sticky=tk.W,columnspan=4)

        condition = tk.Label(self.patientInfoWindow,text="Condition",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        condition.grid(column=0,row=4,columnspan=2,sticky=tk.W,padx=40)
        conditionValue = tk.Label(self.patientInfoWindow,text=searchedCondition,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14))
        conditionValue.grid(column=1,row=4,columnspan=4,sticky=tk.W)

        creator = tk.Label(self.patientInfoWindow,text="Creator",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        creator.grid(column=0,row=5,sticky=tk.W,padx=40)
        creatorName = tk.Label(self.patientInfoWindow,text=searchedCreator,bg=self.BG_COLOR_SEARCH,fg=self.FG_COLOR_SEARCH,font=("Arial",14,"bold"))
        creatorName.grid(column=1,row=5,sticky=tk.W)

        #Advice text
        advice = tk.Label(self.patientInfoWindow,text="Advice",bg=self.BG_COLOR_SEARCH,font=("Arial",14))
        advice.grid(column=0,row=6,columnspan=2,sticky=tk.W,padx=40)
        adviceEntry = tk.Text(self.patientInfoWindow,width=60,height=5,font=("Arial",14))
        adviceEntry.grid(column=0,row=7,columnspan=5,sticky="news",padx=40)

        #Insert text and make it read-only
        adviceEntry.insert("1.0",searchedAdvice)
        adviceEntry.config(state=DISABLED)

        # Button
        backBut = tk.Button(self.patientInfoWindow,text="Back",font=("Arial",12),command=self.backInfo,width=10,borderwidth=4,anchor=CENTER)
        backBut.grid(column=0,row=8,columnspan=5,pady=30)

        self.patientInfoWindow.protocol("WM_DELETE_WINDOW",self.backInfo)
        self.patientInfoWindow.mainloop()

    def backInfo(self):
        self.patientInfoWindow.destroy()


def run():
    k = PatientGUI()
    k.mainFrame()