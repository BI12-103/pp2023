class Student:
    #Hide student's informations
    def __init__(self,n,stdscr):
        stdscr.clear()
        stdscr.addstr(f"Input id of student number {n}: ")
        stdscr.refresh()
        self.__ID = stdscr.getstr(10).decode()

        stdscr.addstr(f"Input name of student number {n}: ")
        stdscr.refresh()
        self.__Name = stdscr.getstr(100).decode()

        stdscr.addstr(f"Input DoB of student {n}: ")
        stdscr.refresh()
        self.__DoB = stdscr.getstr(30).decode()
    
    def __str__(self):
        return f"ID: {self.getID()}\nName: {self.getName()}\nDate of birth: {self.getDoB()}\n"
    
    #Function check for dublicating
    #Dub = True, not dub = false
    def __IDdub__(self,check):
        if self.getID() == check:
            return True
        else:
            return False
    
    #Get student's informations
    def getID(self):
        return self.__ID
    def getName(self):
        return self.__Name
    def getDoB(self):
        return self.__DoB

class Course:
    def __init__(self,n,stdscr):
        stdscr.clear()
        stdscr.addstr(f"Input id of course number {n}: ")
        stdscr.refresh()
        self.ID = stdscr.getstr(10).decode()

        stdscr.addstr(f"Input name of course {n}: ")
        stdscr.refresh()
        self.Name = stdscr.getstr(100).decode()
    def __str__(self):
        return f"Course ID: {self.ID}\nCourse name: {self.Name}\n"
    def __IDdub__(self,check):
        if self.ID == check:
            return True
        else:
            return False

    
class Marks:
    course = []
    k = [] #Print course name at the beginning
    def __init__(self,ID,Name,mark):
        self.__stID = ID
        self.__stName = Name
        self.__mark = mark

    def getID(self):
        return self.__stID
    def getName(self):
        return self.__stName
    def getMark(self):
        return self.__mark
    

    def __str__(self,n):
        if n not in self.k:
            self.k.append(n)
            return f"\nCourse: {self.course[n]}\nID: {self.getID()}\nName: {self.getName()}\nMark: {self.getMark()}\n"
        else:
            return f"ID: {self.getID()}\nName: {self.getName()}\nMark: {self.getMark()}\n"