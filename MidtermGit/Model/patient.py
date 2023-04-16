import csv
import threading

class Patient:
    def __init__(self, id, name, address, age, condition,creator,advice):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__age = age
        self.__condition = condition
        self.__creator = creator
        self.__advice = advice

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_condition(self):
        return self.__condition
    def get_creator(self):
        return self.__creator
    def get_advice(self):
        return self.__advice
    
    def set_id(self,id):
        self.__id = id
    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_age(self,age):
        self.__age = age
    def set_condition(self,condition):
        self.__condition = condition
    def set_creator(self,creator):
        self.__creator = creator
    def set_advice(self,advice):
        self.__advice = advice


class PatientDatabase:
    patient_list = [Patient]
    patient_list.clear()
    undoTemp = [Patient]

    def add_patient(self, patient):
        self.patient_list.append(patient)

    def remove_patient(self, patient):
        if patient in self.patient_list:
            self.patient_list.remove(patient)

    def update_patient(self, id, new_name, new_address, new_age, new_condition,creator,advice):
        for patient in self.patient_list:
            if patient.get_id() == str(id):
                patient.set_name(new_name)
                patient.set_address(new_address)
                patient.set_age(new_age)
                patient.set_condition(new_condition)
                patient.set_creator(creator)
                patient.set_advice(advice)

    def find_patient_by_id(self, id):
        for patient in self.patient_list:
            if patient.get_id() == str(id):
                return patient

    # def find_patients_by_symptoms(self, symptoms):
    #     print("Patients with symptoms:")
    #     for patient in self.patient_list:
    #         if symptoms in patient.get_condition():
    #             print("ID:", patient.get_id())
    #             print("Name:", patient.get_name())
    #             print("Address:", patient.get_address())
    #             print("Age:", patient.get_age())
    #             print("Condition:", patient.get_condition())

    def save_to_csv(self):
        with open("patients.csv", mode='w', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'Address', 'Age', 'Condition','Creator','Advice']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for patient in self.patient_list:
                writer.writerow({'ID': patient.get_id(), 'Name': patient.get_name(), 'Address': patient.get_address(), 'Age': patient.get_age(),
                                 'Condition': patient.get_condition(),'Creator':patient.get_creator(),'Advice':patient.get_advice()})

    def load_from_csv(self):
        try:
            with open("patients.csv", mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    id = row['ID']
                    name = row['Name']
                    address = row['Address']
                    age = int(row['Age'])
                    condition = row['Condition']
                    creator = row['Creator']
                    advice = row['Advice']
                    patient = Patient(id, name, address, age, condition,creator,advice)
                    self.add_patient(patient)
        except FileNotFoundError:
            with open("patients.csv", mode='w', newline='') as csv_file:
                fieldnames = ['ID', 'Name', 'Address', 'Age', 'Condition','Creator','Advice']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

    # def print_patients_from_csv(self):
    #     with open("patients.csv", mode='r') as csv_file:
    #         reader = csv.reader(csv_file)
    #         for row in reader:
    #             print(row)

    def saveNewPatient(self,patient):
        with open("patients.csv", mode='a', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'Address', 'Age', 'Condition','Creator','Advice']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'ID': patient.get_id(), 'Name': patient.get_name(), 'Address': patient.get_address(), 'Age': patient.get_age(),
                            'Condition': patient.get_condition(),'Creator':patient.get_creator(),'Advice':patient.get_advice()})
            
    def idDub(self,id):
        for patient in self.patient_list:
            if patient.get_id() == str(id):
                return True
        return False

    def sortByAge(self):
        for x in range(len(self.patient_list)-1):
            for i in range(len(self.patient_list)-1):
                if self.patient_list[i].get_age() < self.patient_list[i+1].get_age():
                    self.patient_list[i],self.patient_list[i+1] = swap(self.patient_list[i],self.patient_list[i+1])

    def getPatient4TreeView(self,patient):
        return patient.get_id(), patient.get_name(), patient.get_address(), patient.get_age(), patient.get_condition(), patient.get_creator()


def undo():
    db = PatientDatabase()
    try:
        if db.idDub(db.undoTemp[0].get_id()):
            return "idDub"
        db.add_patient(db.undoTemp[0])
        db.saveNewPatient(db.undoTemp[0])
    except TypeError:
        return "Nothg"


def swap(a,b):
    return b,a

def initPatient():
    db = PatientDatabase()
    db.load_from_csv()

def addPatient(id, name, address, age, condition,creator,advice):
    db = PatientDatabase()
    newPatient = Patient(id, name, address, age, condition,creator,advice)
    db.add_patient(newPatient)
    db.saveNewPatient(newPatient)

def checkID(id):
    db = PatientDatabase()
    return db.idDub(id)

def modify(id,new_name,new_address,new_age,new_condition,creator,advice):
    db = PatientDatabase()
    db.update_patient(id,new_name,new_address,new_age,new_condition,creator,advice)
    threading.Thread(target=db.save_to_csv).start()

def removeAPatient(id):
    db = PatientDatabase()
    remvPat = db.find_patient_by_id(id)
    db.undoTemp.clear()
    db.undoTemp.append(remvPat)
    db.remove_patient(remvPat)
    threading.Thread(target=db.save_to_csv).start()

def IDFind(id):
    db = PatientDatabase()
    searched = db.find_patient_by_id(id)
    return searched.get_name(),searched.get_address(),searched.get_age(),searched.get_condition(),searched.get_creator()

def IDFindFull(id):
    db = PatientDatabase()
    searched = db.find_patient_by_id(id)
    return searched.get_name(),searched.get_address(),searched.get_age(),searched.get_condition(),searched.get_creator(),searched.get_advice()

def sort():
    db = PatientDatabase()
    db.sortByAge()
    threading.Thread(target=db.save_to_csv).start()

def displayData(patient):
    db = PatientDatabase()
    return db.getPatient4TreeView(patient)

