from math import floor #floor() can not round to 1 decimal place in python 3, so I just import it then use round() instead
import numpy as np
import curses
from curses import wrapper


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


#Input attributes for students
def inputSt(Sts,stdscr):
    stList = Sts

    #Input number of students
    while True:
        try:
            stdscr.clear()
            stdscr.addstr("Input number of students: ")
            stdscr.refresh()
            numSt = stdscr.getstr(4)
            numSt = int(numSt)
            while numSt<0:
                stdscr.clear()
                stdscr.addstr("Error!")
                stdscr.addstr("\nInput number of students: ")
                stdscr.refresh()
                numSt = stdscr.getstr(4)
                numSt = int(numSt)
            break
        except ValueError:
            pass
    
    #Limit
    newNumST = len(stList) + numSt

    #Loop checking ID
    while True:
        #End loop
        if len(stList) == newNumST:
            break
        #Input and check if ID is dub
        temp = Student(len(stList)+1,stdscr)
        for i in range(len(stList)):
            if (stList[i]).__IDdub__(temp.getID()):
                stdscr.addstr(f"This ID \"{temp.getID()}\" is taken!\nPlease input a different ID!\nPress any key to input again!")
                stdscr.refresh()
                stdscr.getch()
                del(temp)
                break
        try:
            stList.append(temp)
        except UnboundLocalError:
            pass
    
    #Update list
    Sts = stList
    del(stList)
    return Sts


#Input attributes for courses
def inputCourse(courseList,stdscr):
    cL  = courseList


    # Input number of courses
    while True:
        try:
            stdscr.clear()
            stdscr.addstr("Input number of courses: ")
            stdscr.refresh()
            numCourse = stdscr.getstr(2)
            numCourse = int(numCourse)
            while numCourse<0:
                stdscr.clear()
                stdscr.addstr("\nError!")
                stdscr.addstr("\nInput number of courses: ")
                stdscr.refresh()
                numCourse = stdscr.getstr(2)
                numCourse = int(numCourse)
            break
        except ValueError:
            pass
    
    #Limit
    newNumCourse = len(cL) + numCourse

    #Loop checking ID
    while True:
        #End loop condition
        if len(cL) == newNumCourse:
            break
        #Input and check if ID is dub
        temp = Course(len(cL)+1,stdscr)
        for i in range(len(cL)):
            if (cL[i]).__IDdub__(temp.ID):
                stdscr.addstr(f"This ID \"{temp.ID}\" is taken!\nPlease input a different ID!\nPress any key to input again!")
                stdscr.refresh()
                stdscr.getch()
                del(temp)
                break
        try:
            cL.append(temp)
        except UnboundLocalError:
            pass
    
    #Update courses list
    courseList = cL
    del(cL)
    return courseList

#Print any list
def printList(dList,stdscr):
    stdscr.clear()
    for i in range(len(dList)):
        stdscr.addstr((dList[i]).__str__())
        stdscr.refresh()
    stdscr.addstr("\nPress any key to return!")
    stdscr.refresh()
    stdscr.getch()


#Set marks for a course
def setMarks(courseList,stList,marked,stdscr):
    #Search for course
    while True:
        #Check variable
        duB = 0

        stdscr.clear()
        stdscr.addstr("Input the course ID that needs to enter marks: ")
        stdscr.refresh()
        courseM = stdscr.getstr(10).decode()
        
        #Check if the ID is corrected
        for i in range(len(courseList)):
            if (courseList[i]).__IDdub__(courseM):
                duB = 0
                break
            else:
                duB = 1
                pass
        if duB == 1:
            stdscr.clear()
            stdscr.addstr("Invalid course's ID!\nPress any key to try again!")
            stdscr.refresh()
            stdscr.getch()

        #Check if the course is marked
        for i in range(len(Marks.course)):
            if len(Marks.course) != 0 and courseM in Marks.course:
                duB = 1
                stdscr.clear()
                stdscr.addstr("This course is marked!\nPress any key to try again!")
                stdscr.refresh()
                stdscr.getch()
                break
        
        if duB == 1:
            pass
        else:
            Marks.course.append(courseM)
            #Marking
            for x in range(len(stList)):
                while True:
                    try:
                        stdscr.clear()
                        stdscr.addstr(f"Input mark for student number {x+1}: ")
                        stdscr.refresh()
                        m = stdscr.getstr().decode()
                        m = round(float(m),1)
                        temp = Marks(stList[x].getID(),stList[x].getName(),m)
                        marked.append(temp)
                        break
                    except ValueError:
                        pass
            return marked

def printMark(markList,numST,stdscr):
    stdscr.clear()
    Marks.k.clear()
    for i in range(len(markList)):
        n = i//numST
        stdscr.addstr(markList[i].__str__(n))
        stdscr.refresh()
    stdscr.addstr("\nPress any key to return!")
    stdscr.refresh()
    stdscr.getch()
    Marks.k.clear()


#GPA using numpy
def GPA(markList,numST,stdscr):
    GPA = []
    GPA.clear()
    for i in range(len(markList)):
        GPA.append(markList[i].getMark())
    GPA = np.array(GPA)

    GPAList = []
    GPAList.clear()
    for i in range(numST):
        GPAList.append(round(np.average(GPA[i::numST]),1))
        # print(f"\nID: {markList[i].getID()}\nGPA: {np.average(GPA[i::numST])}") #Can add weights for number credits here
    sortandPrint(markList,GPAList,stdscr)


def sortandPrint(markList,GPA,stdscr):
    stdscr.clear()
    tempList = markList
    #Sorting
    for i in range(len(GPA)-1):
        for x in range(len(GPA)-1):
            if GPA[i] < GPA[i+1]:
                temp = GPA[i]
                GPA[i] = GPA[i+1]
                GPA[i+1] = temp
                temp1 = tempList[i]
                tempList[i] = tempList[i+1]
                tempList[i+1] = temp1
    
    #Printing
    for i in range(len(GPA)):
        stdscr.addstr(f"\nID: {tempList[i].getID()}\nGPA: {GPA[i]}")
        stdscr.refresh()
    stdscr.addstr("\nPress any key to return!")
    stdscr.refresh()
    stdscr.getch()
    #Clear cache
    try:
        del(tempList)
        del(temp1)
    except UnboundLocalError:
        pass



def main(stdscr):
    curses.echo()
    #Init
    stList = [Student]
    courseList = [Course]
    marked = [Marks]


    stList.clear()
    courseList.clear()
    marked.clear()

    #Input
    stList = inputSt(stList,stdscr)


    try:
        while True:
            stdscr.clear()
            stdscr.addstr(1,10,"Enter 1 to update new students")
            stdscr.addstr(2,10,"Enter 2 to update new courses")
            stdscr.addstr(3,10,"Enter 3 to set marks")
            stdscr.addstr(4,10,"Enter 4 to print student list")
            stdscr.addstr(5,10,"Enter 5 to print course list")
            stdscr.addstr(6,10,"Enter 6 to print marks")
            stdscr.addstr(7,10,"Enter 7 to print GPA")
            stdscr.refresh()
            while True:
                try:
                    stdscr.addstr(8,7,"Your choice: ")
                    choice = stdscr.getkey()
                    choice = int(choice)
                    while choice<1 or choice>7:
                        stdscr.addstr("\nError!")
                        stdscr.addstr("\nPlease input choice from 1 to 7: ")
                        choice = stdscr.getkey()
                        choice = int(choice)
                    break
                except ValueError:
                    pass
            if choice == 1:
                if len(Marks.course) == 0:
                    stList = inputSt(stList,stdscr)
                else:
                    stdscr.clear()
                    stdscr.addstr("If you enter new students, you have to input marks again!\nDo you wish to continue? Y/N ")
                    stdscr.refresh()
                    while True:
                        key = stdscr.getkey()
                        if key == "y":
                            #Clear marked courses to input again bcs of new students
                            Marks.course.clear()
                            marked.clear()
                            stList = inputSt(stList,stdscr)
                            break
                        elif key == "n":
                            break                
            if choice == 2:
                courseList = inputCourse(courseList,stdscr)
            if choice == 3:
                if len(courseList) == len(Marks.course):
                    stdscr.clear()
                    stdscr.addstr("You have marked all courses !\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    marked = setMarks(courseList,stList,marked,stdscr)
            if choice == 4:
                printList(stList,stdscr)
            if choice == 5:
                printList(courseList,stdscr)
            if choice == 6:
                if len(marked) < len(stList):
                    stdscr.clear()
                    stdscr.addstr("You have to update mark for new students first!\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    printMark(marked,len(stList),stdscr)
            if choice == 7:
                if len(marked) < len(stList):
                    stdscr.clear()
                    stdscr.addstr("You have to update mark for new students first!\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    GPA(marked,len(stList),stdscr)
    except curses.error:
        pass #not enough space in terminal window

# main()
wrapper(main)

