import csv
import threading

class User:
    def __init__(self, username, password, question, answer):
        self.__username = username
        self.__password = password
        self.__question = question
        self.__answer = answer

    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_question(self):
        return self.__question
    def get_answer(self):
        return self.__answer

    def set_username(self, username):
        self.__username = username
    def set_password(self, password):
        self.__password = password
    def set_question(self, question):
        self.__question = question
    def set_answer(self, answer):
        self.__answer = answer

class UserDatabase:
    userList = [User]

    def addAndSave(self,user):
        self.userList.append(user)
        self.save_to_csv(user)

    def remove_user(self, user):
        self.userList.remove(user)
        self.saveall_to_csv()

    def searchUser(self,username):
        for user in self.userList:
            if user.get_username() == username:
                return user
        return None

    def save_to_csv(self,user):
        with open("user.csv", mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([user.get_username(), user.get_password(),user.get_question(),user.get_answer()])

    def saveall_to_csv(self):
        with open("user.csv", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for user in self.userList:
                writer.writerow([user.get_username(), user.get_password(), user.get_question(), user.get_answer()])

    def load_from_csv(self):
        try:
            with open("user.csv", mode='r') as csv_file:
                reader = csv.reader(csv_file)
                for line in reader:
                    username,password,question,answer = line
                    user = User(username,password,question,answer)
                    self.userList.append(user)
        except FileNotFoundError:
            f = open("user.csv","w")
            f.close()

    def changePass(self,name,pas):
        for user in self.userList:
            if user.get_username() == name:
                user.set_password(pas)
                break

def deleteUser(username):
    data = UserDatabase()
    remv = data.searchUser(username)
    data.remove_user(remv)

def set_user_info(uN,pW,qT,aW):
    data = UserDatabase()
    user = User(uN,pW,qT,aW)
    data.addAndSave(user)

def initUser():
    load = UserDatabase()
    UserDatabase.userList.clear()
    load.load_from_csv()

def changePassword(username,password):
    search = UserDatabase()
    search.changePass(username,password)
    threading.Thread(target=search.saveall_to_csv).start()

##If password is correct return True, else return false
def checkPassword(username,password):
    k = UserDatabase()
    search = k.searchUser(username)
    if search != None and search.get_password() == password:
        return True
    else:
        return False
    
#If username exist return True, else return false
def checkUsername(username):
    k = UserDatabase()
    search = k.searchUser(username)
    if search != None:
        return True
    else:
        return False

#Return question and answer
def getQuesAns(username):
    k = UserDatabase()
    search = k.searchUser(username)
    if search != None:
        return search.get_question(),search.get_answer()

