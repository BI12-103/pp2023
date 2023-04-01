import csv
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Model as Mod



class MenuGUI:
    def mainFrame(self,username):
        #Creator name
        self.user = username

        #Init main window
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Human Health Information Management System")
        self.mainWindow.attributes("-fullscreen",True)
        self.mainWindow.configure(bg="#EAE0DA")
        self.mainWindow.columnconfigure(0,weight=1)
        self.mainWindow.columnconfigure(2,weight=0)
        
        #Limit top level window
        self.popup = False

        # Creating Menubar
        menubar = Menu(self.mainWindow)
        
        # Adding File Menu and commands
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ="File", menu = file)
        file.add_command(label ="New File", command = None)
        file.add_command(label ="Open...", command = None)
        file.add_command(label ="Save", command = None)
        file.add_separator()
        file.add_command(label ="Exit", command = self.on_closing)
        
        # Adding Edit Menu and commands
        edit = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ="Edit", menu = edit)
        edit.add_command(label ="Cut", command = None)
        edit.add_command(label ="Copy", command = None)
        edit.add_command(label ="Paste", command = None)
        edit.add_command(label ="Select All", command = None)
        edit.add_separator()
        edit.add_command(label ="Find...", command = None)
        edit.add_command(label ="Find again", command = None)
        
        # Adding Help Menu
        help_ = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ="Help", menu = help_)
        help_.add_command(label ="About", command = None)

        
        # display Menu
        self.mainWindow.config(menu = menubar)

        #Main frame
        mainFrame = tk.Frame(self.mainWindow,bg="#EAE0DA")

        spaceTop = tk.Label(mainFrame,text="",bg="#EAE0DA")
        spaceTop.grid(column=0,row=0,sticky=tk.N,pady=20)

        title = tk.Label(mainFrame,text="PATIENTS",bg="#2F58CD",fg="#FFFFFF",font=("Franklin Gothic Heavy",25),width=60)
        title.grid(column=0,row=1,pady=5)

        # spaceRight = tk.Label(mainFrame,text="",bg="#EAE0DA")
        # spaceRight.grid(column=0,row=2,sticky=tk.W,rowspan=4)
        

        # idIn = tk.Label(mainFrame,text="ID",bg="#EAE0DA",fg="#333333",font=("Arial",14))
        # idIn.grid(column=0,row=1,sticky=tk.W)

        #Tree view
        Columns = ("ID", "Name", "Address", "Age", "Condition", "Creator")
        self.tv = ttk.Treeview(mainFrame,height=33,columns=Columns,show="headings")
        self.tv.grid(row=2,column=0,sticky="news")

        treescrolly = ttk.Scrollbar(mainFrame,orient="vertical",command=self.tv.yview)
        self.tv.configure(yscrollcommand=treescrolly.set)
        treescrolly.grid(row=2,column=1,sticky=tk.NS)

        #Table title
        self.tv.heading("ID", text="ID")
        self.tv.heading("Name", text="Name")
        self.tv.heading("Address", text="Address")
        self.tv.heading("Age", text="Age")
        self.tv.heading("Condition", text="Condition")
        self.tv.heading("Creator", text="Creator")

        self.tv.column("ID",anchor=CENTER,width=100)
        self.tv.column("Name",anchor=CENTER,width=250)
        self.tv.column("Address",anchor=CENTER,width=280)
        self.tv.column("Age",anchor=CENTER,width=50)
        self.tv.column("Condition",anchor=CENTER,width=280)
        self.tv.column("Creator",anchor=CENTER,width=100)

        #Display data to table
        self.show_data()

        mainFrame.grid(row=0,column=1,sticky="news")

        #Button frame
        buttonFrame = tk.Frame(self.mainWindow,bg="#EAE0DA")

        newBut = tk.Button(buttonFrame,text="New",font=("Arial",12),command=self.newPatient,anchor=CENTER,width=15,height=2,borderwidth=5)
        newBut.grid(column=0,row=0)

        f5But = tk.Button(buttonFrame,text="Refresh",font=("Arial",12),command=self.refresh,anchor=CENTER,width=15,height=2,borderwidth=5)
        f5But.grid(column=0,row=1,pady=5)

        modifyBut = tk.Button(buttonFrame,text="Modify",font=("Arial",12),command=NONE,width=15,height=2,anchor=CENTER,borderwidth=5)
        modifyBut.grid(column=0,row=2)

        delBut = tk.Button(buttonFrame,text="Delete",font=("Arial",12),command=NONE ,width=15,height=2,anchor=CENTER,borderwidth=5)
        delBut.grid(column=0,row=3,pady=5)

        exitBut = tk.Button(buttonFrame,text="Exit",font=("Arial",12),command=self.on_closing,width=15,height=2,anchor=CENTER,borderwidth=5)
        exitBut.grid(column=0,row=4)

        buttonFrame.grid(row=0,column=2,sticky=tk.E,padx=10)

        self.mainWindow.mainloop()

    #Exit
    def on_closing(self):
        # if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):
            exit()

    #Display data
    def show_data(self):
        with open("patients.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    self.tv.insert("","end",values=row)
    
    #Clear everything in the table
    def clear_all(self):
        for item in self.tv.get_children():
            self.tv.delete(item)

    #Refresh table
    def refresh(self):
        self.clear_all()
        self.show_data()

    def newPatient(self):
        self.addwindow = tk.Toplevel(self.mainWindow)
        self.addwindow.title("New")
        self.addwindow.geometry("760x400")
        self.addwindow.configure(bg="#EAE0DA")
        self.addwindow.resizable(FALSE,FALSE)

        # self.addwindow.columnconfigure(1,weight=2)

        self.newPatientID = StringVar()
        self.newPatientName = StringVar()
        self.newPatientAddress = StringVar()
        self.newPatientAge = IntVar()
        self.newPatientCondition = StringVar()
        # self.newPatientCreator = self

        Welcome = tk.Label(self.addwindow,text="Add new patient",bg="#EAE0DA",font=("Arial",20))
        Welcome.grid(column=0,row=0,columnspan=4,sticky="news",pady=10)

        id = tk.Label(self.addwindow,text="ID",bg="#EAE0DA",font=("Arial",14))
        id.grid(column=0,row=1,padx=40,sticky=tk.W)
        self.idEntry = tk.Entry(self.addwindow,width=10,font=("Arial",14),textvariable=self.newPatientID)
        self.idEntry.grid(column=1,row=1,sticky=tk.W)

        age = tk.Label(self.addwindow,text="Age",bg="#EAE0DA",font=("Arial",14))
        age.grid(column=3,row=1,padx=40,sticky=tk.E)
        self.ageEntry = tk.Entry(self.addwindow,width=5,font=("Arial",14),textvariable=self.newPatientAge)
        self.ageEntry.grid(column=4,row=1,sticky=tk.W)

        name = tk.Label(self.addwindow,text="Name",bg="#EAE0DA",font=("Arial",14))
        name.grid(column=0,row=2,sticky=tk.W,padx=40)
        self.nameEntry = tk.Entry(self.addwindow,width=50,font=("Arial",14),textvariable=self.newPatientName)
        self.nameEntry.grid(column=1,row=2,sticky=tk.W,columnspan=4)

        address = tk.Label(self.addwindow,text="Address",bg="#EAE0DA",font=("Arial",14))
        address.grid(column=0,row=3,columnspan=2,sticky=tk.W,padx=40)
        self.addressEntry = tk.Entry(self.addwindow,width=50,font=("Arial",14),textvariable=self.newPatientAddress)
        self.addressEntry.grid(column=1,row=3,columnspan=4)

        condition = tk.Label(self.addwindow,text="Condition",bg="#EAE0DA",font=("Arial",14))
        condition.grid(column=0,row=4,columnspan=2,sticky=tk.W,padx=40)
        self.conditionEntry = tk.Entry(self.addwindow,width=50,font=("Arial",14),textvariable=self.newPatientCondition)
        self.conditionEntry.grid(column=1,row=4,columnspan=4,sticky=tk.W)

        creator = tk.Label(self.addwindow,text="Creator",bg="#EAE0DA",font=("Arial",14))
        creator.grid(column=0,row=5,sticky=tk.W,padx=40)
        self.creatorName = tk.Label(self.addwindow,text=self.user,bg="#EAE0DA",fg="#913175",font=("Arial",14,"bold"))
        self.creatorName.grid(column=1,row=5,sticky=tk.W)
        
        space=tk.Label(self.addwindow,text="",bg="#EAE0DA")
        space.grid(column=0,row=6,pady=30)

        #Button
        addBut = tk.Button(self.addwindow,text="Add",font=("Arial",12),command=self.add,width=10,borderwidth=4)
        addBut.grid(column=0,row=7,columnspan=7)
        cancelBut = tk.Button(self.addwindow,text="Cancel",font=("Arial",12),command=self.cancelAdd,width=10,borderwidth=4)
        cancelBut.grid(column=0,row=8,columnspan=7,pady=10)

        self.addwindow.mainloop()

    def cancelAdd(self):
        self.addwindow.destroy()

    def add(self):
        if len(self.newPatientID.get())<1 or len(self.newPatientID.get())>5:
            messagebox.showerror(title="Invalid ID",message="Length of ID must be between 1 and 5 characters")
            self.addwindow.lift()
        elif Mod.checkID(self.newPatientID.get()):
            messagebox.showerror(title="ID is already existed",message="This ID is taken")
            self.addwindow.lift()
        elif len(self.newPatientName.get())<2 or len(self.newPatientName.get())>100:
            messagebox.showerror(title="Invalid name",message="Length of name must be between 2 and 100 characters")
            self.addwindow.lift()
        elif len(self.newPatientAddress.get())>255:
            messagebox.showerror(title="Invalid address",message="Length of address must be less than 255 characters")
            self.addwindow.lift()
        elif len(self.newPatientCondition.get())<2 or len(self.newPatientCondition.get())>255:
            messagebox.showerror(title="Invalid condition",message="Length of condition must be between 2 and 255 characters")
            self.addwindow.lift()
        elif self.newPatientAge.get()<0 or self.newPatientAge.get()>255:
            messagebox.showerror(title="Invalid age",message="Age must be between 0 and 255")
            self.addwindow.lift()
        else:
            Mod.addPatient(self.newPatientID.get(),self.newPatientName.get(),self.newPatientAddress.get(),
                           self.newPatientAge.get(),self.newPatientCondition.get(),self.user)
            self.idEntry.delete(0,END)
            self.nameEntry.delete(0,END)
            self.addressEntry.delete(0,END)
            self.conditionEntry.delete(0,END)
            self.ageEntry.delete(0,END)


def run(username):
    k=MenuGUI()
    k.mainFrame(username)

# run("Khoa")