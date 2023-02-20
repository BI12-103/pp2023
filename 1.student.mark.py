stID = []
stName =[]
stDoB = []
courseID = []
courseName = []
stList = []
markList = []

def InputFunc():
    global numSt
    global numCourse
    global dub
    
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

    for x in range(numSt):
        #Input student information: id, name, DoB
        #Check if the ID is exist
        if x==0:
            print("Input student number",x+1, "ID: ")
            dub = str(input())
        elif x>0:
            try:
                print("Input student number",x+1, "ID: ")
                dub = str(input())
                stID.index(dub)
                while True:
                    try:
                        print("This student ID is already exist!")
                        print("Input student number",x+1, "ID: ")
                        dub = str(input())
                        stID.index(dub)
                        pass
                    except ValueError:
                        break
            except ValueError:
                pass
        stID.append(dub)
        print("Input student number",x+1, "name: ")
        stName.append(str(input()))
        print("Input student number",x+1, "DoB: ")
        stDoB.append(str(input()))

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

    for x in range(numCourse):
        #Input course information: id, name
        #Check if the ID is exist
        if x==0:
            print("Input course number",x+1, "ID: ")
            dub = str(input())
        elif x>0:
            try:
                print("Input course number",x+1, "ID: ")
                dub = str(input())
                courseID.index(dub)
                while True:
                    try:
                        print("This course ID is already exist!")
                        print("Input course number",x+1, "ID: ")
                        dub = str(input())
                        courseID.index(dub)
                        pass
                    except ValueError:
                        break
            except ValueError:
                pass
        courseID.append(dub)
        print("Input course number",x+1, "name: ")
        courseName.append(str(input()))

    for x in range(numSt):
        tupleList = (stID[x],stName[x],stDoB[x])
        stList.append(tupleList,)


    #Enter mark for a course
    #search for course
    if numCourse>0:
        try:
            print("Input the course ID that needs to enter marks: ")
            courseM = str(input())
            search = courseID.index(courseM)
        except ValueError:
            while True:
                try:
                    print("That course ID does not exist")
                    print("Input the course ID that needs to enter marks: ")
                    courseM = str(input())
                    search = courseID.index(courseM) #course index
                    break
                except ValueError:
                    pass

        markList.append(courseName[search])
        for x in range(numSt):
            print("Input mark for student number",x+1,":")
            mark = (stID[x],int(input()))
            markList.append(mark)

def ListFunc():
    #Student list
    print("Student list:")
    for x in range(numSt):
        print(stList[x])

    #Course list
    print("Course list:")
    for x in range(numCourse):
        print(courseID[x],courseName[x])

    #Mark list
    print("Mark list:")
    if numCourse>0:
        for x in range(numSt+1):
            if x==0:
                print("Course:",markList[x])
            else:
                print(markList[x])

InputFunc()
ListFunc()

