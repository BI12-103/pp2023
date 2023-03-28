import csv

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
    def __init__(self):
        # self.__filename = filename
        self.__user_list = [User]
        self.load_from_csv()

    def add_user(self, user):
        self.__user_list.append(user)
        self.save_to_csv()

    # def remove_user(self, user):
    #     self.__user_list.remove(user)
    #     self.save_to_csv()

    # def update_user(self, user, username=None, password=None):
    #     if username:
    #         user.set_username(username)
    #     if password:
    #         user.set_password(password)
    #     self.save_to_csv()

    def save_to_csv(self):
        with open("user.csv", mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for user in self.__user_list:
                writer.writerow([user.get_username(), user.get_password(),user.get_question(),user.get_answer()])

    def load_from_csv(self):
        try:
            with open("user.csv", mode='r') as csv_file:
                reader = csv.reader(csv_file)
                for line in reader:
                    username, password,question,answer = line
                    user = User(username, password,question,answer)
                    self.add_user(user)
        except FileNotFoundError:
            f = open("user.csv","w")
            f.close()

    # def login(self, username, password):
    #     for user in self.__user_list:
    #         if user.get_username() == username and user.get_password() == password:
    #             print("Login successful!")
    #             return
    #     print("Invalid username or password.")

def get_user_info():
    username = input("Enter username: ")
    password = input("Enter password: ")
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    
    user = User(username,password,question,answer)
    data = UserDatabase()
    data.add_user(user)
    

get_user_info()
