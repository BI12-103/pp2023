import zipfile
import Model as Mod


def clearAllTexts():
    f = open("students.txt","w")
    f.close()
    f = open("courses.txt","w")
    f.close()
    f = open("marks.txt","w")
    f.close()

def updateStudent(newStudent):
    f = open("students.txt","a")
    f.write(newStudent.__str__()+"\n")
    f.close()

def updateCourses(newCourses):
    f = open("courses.txt","a")
    f.write(newCourses.__str__()+"\n")
    f.close()

def updateMarks(Course,stID,stName,Mark):
    f = open("marks.txt","a")
    f.write(f"Course: {Course}\nID: {stID}\nName: {stName}\nMark: {Mark}\n\n")
    f.close()

def clearMarks():
    f = open("marks.txt","w")
    f.close()

def zipFile():
    with zipfile.ZipFile("students.zip","w",compression=zipfile.ZIP_DEFLATED) as dat:
        dat.write("students.txt")
        dat.write("courses.txt")
        dat.write("marks.txt")

def extractAndLoad(stList,cList,mList):
    try:
        with zipfile.ZipFile("students.zip","r") as dat:
            dat.extractall()
        loadData(stList,cList,mList)
    except FileNotFoundError:
        pass

def deleteData():
    with zipfile.ZipFile("students.zip","w") as z:
        pass
    clearAllTexts()

def loadData(stList,cList,mList):
    loadStudents(stList)
    loadCourses(cList)
    loadMarks(mList)

def loadStudents(stList):
    with open("students.txt","r",buffering=-1) as f:
        check_id = False
        for line in f:
            if "ID: " in line and check_id == False:
                id = line.replace("ID: ","").rstrip("\n")
                check_id = True
                check_name = False
            elif "Name: " in line and check_name == False:
                name = line.replace("Name: ","").rstrip("\n")
                check_name = True
            elif "Date of birth: " in line:
                dob = line.replace("Date of birth: ","").rstrip("\n")
                check_id = False
                try:
                    temp = Mod.Student(id,name,dob)
                    stList.append(temp)
                    del(temp)
                except UnboundLocalError:
                    pass

def loadCourses(cList):
    with open("courses.txt","r",buffering=-1) as f:
        check_id = False
        for line in f:
            if "Course ID: " in line and check_id == False:
                id = line.replace("Course ID: ","").rstrip("\n")
                check_id = True
                check_name = False
            elif "Course name: " in line and check_name == False:
                name = line.replace("Course name: ","").rstrip("\n")
                check_name = True
                check_id = False
                try:
                    temp = Mod.Course(id,name)
                    cList.append(temp)
                    del(temp)
                except UnboundLocalError:
                    pass

def loadMarks(mList):
    with open("marks.txt","r",buffering=-1) as f:
        check_c = False
        for line in f:
            if "Course: " in line and check_c == False:
                course = line.replace("Course: ","").rstrip("\n")
                if course not in Mod.Marks.course:
                    Mod.Marks.course.append(course)
                else:
                    pass
                check_c = True
                check_id = False
            elif "ID: " in line and check_id == False:
                id = line.replace("ID: ","").rstrip("\n")
                check_id = True
                check_name = False
            elif "Name: " in line and check_name == False:
                name = line.replace("Name: ","").rstrip("\n")
                check_name = True
            elif "Mark: " in line:
                mark = float(line.replace("Mark: ","").rstrip("\n"))
                check_c = False
                try:
                    temp = Mod.Marks(id,name,mark)
                    mList.append(temp)
                    del(temp)
                except UnboundLocalError:
                    pass


