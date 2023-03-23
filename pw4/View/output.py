from math import floor #floor() can not round to 1 decimal place in python 3, so I just import it then use round() instead
import numpy as np


#Print any list
def printList(dList,stdscr):
    stdscr.clear()
    for i in range(len(dList)):
        stdscr.addstr((dList[i]).__str__())
        stdscr.refresh()
    stdscr.addstr("\nPress any key to return!")
    stdscr.refresh()
    stdscr.getch()


def printMark(markList,numST,stdscr):
    stdscr.clear()
    for i in range(len(markList)):
        n = i//numST
        stdscr.addstr(markList[i].__str__(n))
        stdscr.refresh()
    stdscr.addstr("\nPress any key to return!")
    stdscr.refresh()
    stdscr.getch()


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
