import input as Ip
import Model as Mod
import View
import curses
from curses import wrapper
import mangement as mng


def main(stdscr):
    #Print input to the terminal
    curses.echo()

    #Init
    stList = [Mod.Student]
    courseList = [Mod.Course]
    marked = [Mod.Marks]

    stList.clear()
    courseList.clear()
    marked.clear()

    #Decompress and load data if exist
    mng.extractAndLoad(stList,courseList,marked)

    #Input
    if len(stList)==0:
        stList = Ip.inputSt(stList,stdscr)


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
            stdscr.addstr(8,10,"Enter 8 to exit and save data")
            stdscr.addstr(9,10,"Enter 9 to exit without saving data")
            stdscr.addstr(10,10,"Enter 10 to exit and delete all existing data")
            stdscr.refresh()
            while True:
                try:
                    stdscr.addstr(11,7,"Your choice: ")
                    choice = stdscr.getstr(2)
                    choice = int(choice)
                    while choice<1 or choice>10:
                        stdscr.addstr("\nError!")
                        stdscr.addstr("\nPlease input choice from 1 to 10: ")
                        choice = stdscr.getstr(2)
                        choice = int(choice)
                    break
                except ValueError:
                    pass
            if choice == 1:
                if len(Mod.Marks.course) == 0:
                    stList = Ip.inputSt(stList,stdscr)
                else:
                    stdscr.clear()
                    stdscr.addstr("If you enter new students, you have to input marks again!\nDo you wish to continue? Y/N ")
                    stdscr.refresh()
                    while True:
                        key = stdscr.getkey()
                        if key == "y":
                            #Clear marked courses to input again bcs of new students
                            Mod.Marks.course.clear()
                            marked.clear()
                            mng.clearMarks()
                            stList = Ip.inputSt(stList,stdscr)
                            break
                        elif key == "n":
                            break                
            if choice == 2:
                courseList = Ip.inputCourse(courseList,stdscr)
            if choice == 3:
                if len(courseList) == len(Mod.Marks.course):
                    stdscr.clear()
                    stdscr.addstr("You have marked all courses !\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    marked = Ip.setMarks(courseList,stList,marked,stdscr)
            if choice == 4:
                View.printList(stList,stdscr)
            if choice == 5:
                View.printList(courseList,stdscr)
            if choice == 6:
                if len(marked) < len(stList):
                    stdscr.clear()
                    stdscr.addstr("You have to update mark for new students first!\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    Mod.Marks.k.clear()
                    View.printMark(marked,len(stList),stdscr)
                    Mod.Marks.k.clear()
            if choice == 7:
                if len(marked) < len(stList):
                    stdscr.clear()
                    stdscr.addstr("You have to update mark for new students first!\nPress any key to return!")
                    stdscr.refresh()
                    stdscr.getch()
                else:
                    View.GPA(marked,len(stList),stdscr)
            if choice == 8:
                mng.zipFile()
                exit()
            if choice == 9:
                mng.clearAllTexts()
                exit()
            if choice == 10:
                mng.deleteData()
                exit()
    except curses.error:
        pass #not enough space in terminal window

# main()
wrapper(main)

