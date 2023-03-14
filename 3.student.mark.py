from math import floor #floor() can not round to 1 decimal place in python 3, so I just import it then use round() instead
import numpy as np


class Student:
    #Hide student's informations
    def __init__(self,n):
        self.__ID = input(f"Input id of student number {n}: ")
        self.__Name = input(f"Input name of student number {n}: ")
        self.__DoB = input(f"Input DoB of student {n}: ")
    
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
    def __init__(self,n):
        self.ID = input(f"Input id of course number {n}: ")
        self.Name = input(f"Input name of course {n}: ")
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
    # def setCourse(self,crse):
    #     self.course.append = crse
    def getID(self):
        return self.__stID
    def getName(self):
        return self.__stName
    def getMark(self):
        return self.__mark
    
    #Dub = false, not dub = true
    # def __IDnotdub__(self,check):
    #     if check in self.course:
    #         return True
    #     else:
    #         return False
        
    def __str__(self,n):
        if n not in self.k:
            self.k.append(n)
            return f"Course: {self.course[n]}\nID: {self.getID()}\nName: {self.getName()}\nMark: {self.getMark()}\n"
        else:
            return f"ID: {self.getID()}\nName: {self.getName()}\nMark: {self.getMark()}\n"


#Input attributes for students
def inputSt(Sts):
    stList = Sts

    #Input number of students
    while True:
        try:
            print("Input number of students: ")
            numSt = int(input())
            while numSt<0:
                print("Error!")
                print("Input number of students: ")
                numSt = int(input())
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
        temp = Student(len(stList)+1)
        for i in range(len(stList)):
            if (stList[i]).__IDdub__(temp.getID()):
                print(f"This ID \"{temp.getID()}\" is taken!\nPlease input a different ID!")
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
def inputCourse(courseList):
    cL  = courseList

    # for i in range(numCourse):
    #     courseList.append(Course())
    
    # Input number of courses
    while True:
        try:
            print("Input number of courses: ")
            numCourse = int(input())
            while numCourse<0:
                print("Error!")
                print("Input number of courses: ")
                numCourse = int(input())
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
        temp = Course(len(cL)+1)
        for i in range(len(cL)):
            if (cL[i]).__IDdub__(temp.ID):
                print(f"This ID \"{temp.ID}\" is taken!\nPlease input a different ID!")
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
def printList(dList):
    for i in range(len(dList)):
        print(dList[i])


#Set marks for a course
def setMarks(courseList,stList,marked):
    #Search for course
    while True:
        #Check variable
        duB = 0
        courseM = input("Input the course ID that needs to enter marks: ")
        
        #Check if the ID is corrected
        for i in range(len(courseList)):
            if (courseList[i]).__IDdub__(courseM):
                duB = 0
                break
            else:
                duB = 1
                pass

        #Check if the course is marked
        for i in range(len(Marks.course)):
            if len(Marks.course) != 0 and courseM in Marks.course:
                duB = 1
                break
        
        if duB == 1:
            pass
        else:
            Marks.course.append(courseM)
            #Marking
            for x in range(len(stList)):
                while True:
                    try:
                        m = round(float(input(f"Input mark for student number {x+1}: ")),1)
                        temp = Marks(stList[x].getID(),stList[x].getName(),m)
                        marked.append(temp)
                        break
                    except ValueError:
                        pass
            return marked

def printMark(markList,numST):
    Marks.k.clear()
    for i in range(len(markList)):
        n = i//numST
        print(markList[i].__str__(n))
    Marks.k.clear()

# def GPA(markList,numCourse,numST):
#     GPA = []
#     GPA.clear()
#     for i in range(numST):
#         GPA.append(markList[i].getMark())
#         for x in range(numCourse-1):
#             GPA[i] = GPA[i] + markList[i+(x+1)*numST].getMark()
#         GPA[i] = round(GPA[i]/numCourse,1)
#     for i in range(numST):
#         print(f"\nID: {markList[i].getID()}\nGPA: {GPA[i]}")


#GPA using numpy
def GPA(markList,numCourse,numST):
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
    sortandPrint(markList,GPAList)


def sortandPrint(markList,GPA):
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
        print(f"\nID: {tempList[i].getID()}\nGPA: {GPA[i]}")

    #Clear cache
    try:
        del(tempList)
        del(temp1)
    except UnboundLocalError:
        pass



def main():
    #Init
    stList = [Student]
    courseList = [Course]
    marked = [Marks]


    stList.clear()
    courseList.clear()
    marked.clear()

    #Input
    stList = inputSt(stList)
    # courseList = inputCourse(courseList)

    # # Dung = Student()
    # # stList.append(Dung)

    # #Marking
    # marked = setMarks(courseList,stList,marked)

    # #Print
    # printList(stList)
    # printList(courseList)

    # printMark(marked,len(stList))


    while True:
        print("\nEnter 1 to update new students")
        print("Enter 2 to update new courses")
        print("Enter 3 to set marks")
        print("Enter 4 to print student list")
        print("Enter 5 to print course list")
        print("Enter 6 to print marks")
        print("Enter 7 to print GPA")
        while True:
            try:
                print("Your choice: ")
                choice = int(input())
                while choice<1 or choice>7:
                    print("Error!")
                    print("Please input choice from 1 to 7: ")
                    choice = int(input())
                break
            except ValueError:
                pass
        if choice == 1:
            stList = inputSt(stList)
        if choice == 2:
            courseList = inputCourse(courseList)
        if choice == 3:
            if len(courseList) == len(Marks.course):
                print("You have marked all courses !")
            else:
                marked = setMarks(courseList,stList,marked)
        if choice == 4:
            printList(stList)
        if choice == 5:
            printList(courseList)
        if choice == 6:
            if len(marked) < len(stList):
                print("You have to update mark for new students first!")
            else:
                printMark(marked,len(stList))
        if choice == 7:
            if len(marked) < len(stList):
                print("You have to update mark for new students first!")
            else:
                GPA(marked,len(courseList),len(stList))
            
    
main()

