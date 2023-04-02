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

        newBut = tk.Button(buttonFrame,text="New",font=("Arial",12),command=self.openAdd,anchor=CENTER,width=15,height=2,borderwidth=5)
        newBut.grid(column=0,row=0)

        f5But = tk.Button(buttonFrame,text="Refresh",font=("Arial",12),command=self.refresh,anchor=CENTER,width=15,height=2,borderwidth=5)
        f5But.grid(column=0,row=1,pady=5)

        modifyBut = tk.Button(buttonFrame,text="Modify",font=("Arial",12),command=self.openModify,width=15,height=2,anchor=CENTER,borderwidth=5)
        modifyBut.grid(column=0,row=2)

        delBut = tk.Button(buttonFrame,text="Delete",font=("Arial",12),command=self.deleteData ,width=15,height=2,anchor=CENTER,borderwidth=5)
        delBut.grid(column=0,row=3,pady=5)

        exitBut = tk.Button(buttonFrame,text="Exit",font=("Arial",12),command=self.on_closing,width=15,height=2,anchor=CENTER,borderwidth=5)
        exitBut.grid(column=0,row=4)

        buttonFrame.grid(row=0,column=2,sticky=tk.E,padx=10)

        self.mainWindow.mainloop()

    #Open modify condition
    def openModify(self):
        try:
            if self.popup == False:
                self.popup = True
                self.modify()
            elif self.addwindow.winfo_exists():
                self.addwindow.lift()
        except AttributeError:
            self.modifyWindow.lift()

    def openAdd(self):
        try:
            if self.popup == False:
                self.popup = True
                self.newPatient()
            elif self.modifyWindow.winfo_exists():
                self.modifyWindow.lift()
        except AttributeError:
            self.addwindow.lift()

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

        self.newPatientID = StringVar()
        self.newPatientName = StringVar()
        self.newPatientAddress = StringVar()
        self.newPatientAge = IntVar()
        self.newPatientCondition = StringVar()

        Welcome = tk.Label(self.addwindow,text="Add new patient",bg="#EAE0DA",font=("Arial",20,"bold"))
        Welcome.grid(column=0,row=0,columnspan=10,sticky="news",pady=10)

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

        self.addwindow.protocol("WM_DELETE_WINDOW",self.cancelAdd)
        self.addwindow.mainloop()

    def cancelAdd(self):
        self.popup = False
        self.addwindow.destroy()

    def add(self):
        try:
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
                self.refresh()
        except tk.TclError:
            messagebox.showerror(title="Invalid age",message="Age must be an interger")
            self.addwindow.lift()

    def modify(self):
        try:
            #Check first
            selectedItem = self.tv.selection()
            self.modifyPatientID = self.tv.item(selectedItem)['values'][0]
            
            #Create window if check ok
            self.modifyWindow = tk.Toplevel(self.mainWindow)
            self.modifyWindow.title("Modify")
            self.modifyWindow.geometry("760x600")
            self.modifyWindow.configure(bg="#EAE0DA")
            self.modifyWindow.resizable(FALSE,FALSE)
            
            self.modifyPatientName = StringVar()
            self.modifyPatientAddress = StringVar()
            self.modifyPatientAge = IntVar()
            self.modifyPatientCondition = StringVar()

            #Welcome
            Welcome = tk.Label(self.modifyWindow,text="Current",bg="#EAE0DA",font=("Arial",20,"bold"))
            Welcome.grid(column=0,row=0,columnspan=5,sticky="news",pady=10,ipadx=50)

            #Old data
            id = tk.Label(self.modifyWindow,text="ID",bg="#EAE0DA",font=("Arial",14))
            id.grid(column=0,row=1,padx=40,sticky=tk.W)
            idEntry = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][0],bg="#EAE0DA",font=("Arial",14))
            idEntry.grid(column=1,row=1,sticky=tk.W)

            age = tk.Label(self.modifyWindow,text="Age",bg="#EAE0DA",font=("Arial",14))
            age.grid(column=3,row=1,padx=40,sticky=tk.W)
            ageEntry = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][3],bg="#EAE0DA",font=("Arial",14))
            ageEntry.grid(column=4,row=1,sticky=tk.W)

            name = tk.Label(self.modifyWindow,text="Name",bg="#EAE0DA",font=("Arial",14))
            name.grid(column=0,row=2,sticky=tk.W,padx=40,columnspan=2)
            nameEntry = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][1],bg="#EAE0DA",font=("Arial",14))
            nameEntry.grid(column=1,row=2,sticky=tk.W,columnspan=4)

            address = tk.Label(self.modifyWindow,text="Address",bg="#EAE0DA",font=("Arial",14))
            address.grid(column=0,row=3,columnspan=2,sticky=tk.W,padx=40)
            addressEntry = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][2],bg="#EAE0DA",font=("Arial",14))
            addressEntry.grid(column=1,row=3,columnspan=4,sticky=tk.W)

            condition = tk.Label(self.modifyWindow,text="Condition",bg="#EAE0DA",font=("Arial",14))
            condition.grid(column=0,row=4,columnspan=2,sticky=tk.W,padx=40)
            conditionEntry = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][4],bg="#EAE0DA",font=("Arial",14))
            conditionEntry.grid(column=1,row=4,columnspan=4,sticky=tk.W)

            creator = tk.Label(self.modifyWindow,text="Creator",bg="#EAE0DA",font=("Arial",14))
            creator.grid(column=0,row=5,sticky=tk.W,padx=40)
            creatorName = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][5],bg="#EAE0DA",font=("Arial",14))
            creatorName.grid(column=1,row=5,sticky=tk.W)
            
            space=tk.Label(self.modifyWindow,text="",bg="#EAE0DA")
            space.grid(column=0,row=6,pady=10)

            #New data
            Welcome2 = tk.Label(self.modifyWindow,text="Update",bg="#EAE0DA",font=("Arial",20,"bold"))
            Welcome2.grid(column=0,row=7,columnspan=5,sticky="news",pady=10,ipadx=50)

            id2 = tk.Label(self.modifyWindow,text="ID",bg="#EAE0DA",font=("Arial",14))
            id2.grid(column=0,row=8,padx=40,sticky=tk.W)
            self.idEntry2 = tk.Label(self.modifyWindow,text=self.tv.item(selectedItem)['values'][0],bg="#EAE0DA",font=("Arial",14))
            self.idEntry2.grid(column=1,row=8,sticky=tk.W)

            age2 = tk.Label(self.modifyWindow,text="Age",bg="#EAE0DA",font=("Arial",14))
            age2.grid(column=3,row=8,padx=40,sticky=tk.W)
            self.ageEntry2 = tk.Entry(self.modifyWindow,width=5,font=("Arial",14),textvariable=self.modifyPatientAge)
            self.ageEntry2.grid(column=4,row=8,sticky=tk.W)

            name2 = tk.Label(self.modifyWindow,text="Name",bg="#EAE0DA",font=("Arial",14))
            name2.grid(column=0,row=9,sticky=tk.W,padx=40,columnspan=2)
            self.nameEntry2 = tk.Entry(self.modifyWindow,width=50,font=("Arial",14),textvariable=self.modifyPatientName)
            self.nameEntry2.grid(column=1,row=9,sticky=tk.W,columnspan=4)

            address2 = tk.Label(self.modifyWindow,text="Address",bg="#EAE0DA",font=("Arial",14))
            address2.grid(column=0,row=10,columnspan=2,sticky=tk.W,padx=40)
            self.addressEntry2 = tk.Entry(self.modifyWindow,width=50,font=("Arial",14),textvariable=self.modifyPatientAddress)
            self.addressEntry2.grid(column=1,row=10,columnspan=4,sticky=tk.W)

            condition2 = tk.Label(self.modifyWindow,text="Condition",bg="#EAE0DA",font=("Arial",14))
            condition2.grid(column=0,row=11,columnspan=2,sticky=tk.W,padx=40)
            self.conditionEntry2 = tk.Entry(self.modifyWindow,width=50,font=("Arial",14),textvariable=self.modifyPatientCondition)
            self.conditionEntry2.grid(column=1,row=11,columnspan=4,sticky=tk.W)

            creator2 = tk.Label(self.modifyWindow,text="Creator",bg="#EAE0DA",font=("Arial",14))
            creator2.grid(column=0,row=12,sticky=tk.W,padx=40)
            creatorName2 = tk.Label(self.modifyWindow,text=self.user,bg="#EAE0DA",fg="#913175",font=("Arial",14,"bold"))
            creatorName2.grid(column=1,row=12,sticky=tk.W)

            space=tk.Label(self.modifyWindow,text="",bg="#EAE0DA")
            space.grid(column=0,row=13,pady=10)

            #Button
            updateBut = tk.Button(self.modifyWindow,text="Update",font=("Arial",12),command=self.update,width=10,borderwidth=4)
            updateBut.grid(column=1,row=14,sticky="news")
            cancelBut = tk.Button(self.modifyWindow,text="Cancel",font=("Arial",12),command=self.cancelModify,width=10,borderwidth=4)
            cancelBut.grid(column=3,row=14,sticky="news")
            
            self.modifyWindow.protocol("WM_DELETE_WINDOW",self.cancelModify)
            self.modifyWindow.mainloop()
        except IndexError:
            self.popup = False
            messagebox.showerror(title="Error",message="Please select a patient's data to modify")

    def update(self):
        try:
            if len(self.modifyPatientName.get())<2 or len(self.modifyPatientName.get())>100:
                messagebox.showerror(title="Invalid name",message="Length of name must be between 2 and 100 characters")
                self.modifyWindow.lift()
            elif len(self.modifyPatientAddress.get())>255:
                messagebox.showerror(title="Invalid address",message="Length of address must be less than 255 characters")
                self.modifyWindow.lift()
            elif len(self.modifyPatientCondition.get())<2 or len(self.modifyPatientCondition.get())>255:
                messagebox.showerror(title="Invalid condition",message="Length of condition must be between 2 and 255 characters")
                self.modifyWindow.lift()
            elif self.modifyPatientAge.get()<0 or self.modifyPatientAge.get()>255:
                messagebox.showerror(title="Invalid age",message="Age must be between 0 and 255")
                self.modifyWindow.lift()
            else:
                Mod.modify(self.modifyPatientID,self.modifyPatientName.get(),self.modifyPatientAddress.get(),
                            self.modifyPatientAge.get(),self.modifyPatientCondition.get(),self.user)
                self.nameEntry2.delete(0,END)
                self.addressEntry2.delete(0,END)
                self.conditionEntry2.delete(0,END)
                self.ageEntry2.delete(0,END)
                self.refresh()
        except tk.TclError:
            messagebox.showerror(title="Invalid age",message="Age must be an interger")
            self.addwindow.lift()

    def cancelModify(self):
        self.popup = False
        self.modifyWindow.destroy()

    def deleteData(self):
        if self.popup == False:
            try:
                #Check first
                selectedItem = self.tv.selection()
                deletePatientID = self.tv.item(selectedItem)['values'][0]

                #Delete item selected
                Mod.removeAPatient(deletePatientID)
                self.refresh()
            except IndexError:
                messagebox.showerror(title="Error",message="Please select a patient's data to remove")


def run(username):
    k=MenuGUI()
    k.mainFrame(username)

# run("Trung")