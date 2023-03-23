import Model as Mod


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
        temp = Mod.Student(len(stList)+1,stdscr)
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
        temp = Mod.Course(len(cL)+1,stdscr)
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
        for i in range(len(Mod.Marks.course)):
            if len(Mod.Marks.course) != 0 and courseM in Mod.Marks.course:
                duB = 1
                stdscr.clear()
                stdscr.addstr("This course is marked!\nPress any key to try again!")
                stdscr.refresh()
                stdscr.getch()
                break
        
        if duB == 1:
            pass
        else:
            Mod.Marks.course.append(courseM)
            #Marking
            for x in range(len(stList)):
                while True:
                    try:
                        stdscr.clear()
                        stdscr.addstr(f"Input mark for student number {x+1}: ")
                        stdscr.refresh()
                        m = stdscr.getstr().decode()
                        m = round(float(m),1)
                        temp = Mod.Marks(stList[x].getID(),stList[x].getName(),m)
                        marked.append(temp)
                        break
                    except ValueError:
                        pass
            return marked