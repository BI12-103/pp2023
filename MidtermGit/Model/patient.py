import csv

class Patient:
    def __init__(self, id, name, address, age, condition,creator):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__age = age
        self.__condition = condition
        self.__creator = creator

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


class PatientDatabase:
    patient_list = [Patient]
    patient_list.clear()

    def add_patient(self, patient):
        self.patient_list.append(patient)

    def remove_patient(self, patient):
        if patient in self.patient_list:
            self.patient_list.remove(patient)
            print("Patient removed successfully")
        else:
            print("Patient not found")

    def update_patient(self, id, new_name, new_address, new_age, new_condition,creator):
        for patient in self.patient_list:
            if patient.get_id() == id:
                patient.set_name(new_name)
                patient.set_address(new_address)
                patient.set_age(new_age)
                patient.set_condition(new_condition)
                patient.set_creator(creator)
                print("Patient updated successfully")
                return
        print("Patient not found")

    def find_patient_by_id(self, id):
        for patient in self.patient_list:
            if patient.get_id() == id:
                print("Patient found:")
                print("ID:", patient.get_id())
                print("Name:", patient.get_name())
                print("Address:", patient.get_address())
                print("Age:", patient.get_age())
                print("Condition:", patient.get_condition())
                return
        print("Patient not found")

    def find_patients_by_symptoms(self, symptoms):
        print("Patients with symptoms:")
        for patient in self.patient_list:
            if symptoms in patient.get_condition():
                print("ID:", patient.get_id())
                print("Name:", patient.get_name())
                print("Address:", patient.get_address())
                print("Age:", patient.get_age())
                print("Condition:", patient.get_condition())

    def save_to_csv(self):
        with open("patients.csv", mode='w', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'Address', 'Age', 'Condition','Creator']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for patient in self.patient_list:
                writer.writerow({'ID': patient.get_id(), 'Name': patient.get_name(), 'Address': patient.get_address(), 'Age': patient.get_age(), 'Condition': patient.get_condition(),'Creator':patient.get_creator()})

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
                    patient = Patient(id, name, address, age, condition,creator)
                    self.add_patient(patient)
        except FileNotFoundError:
            f = open("patients.csv","w")
            f.close()

    def print_patients_from_csv(self):
        with open("patients.csv", mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)

    def saveNewPatient(self,patient):
        with open("patients.csv", mode='a', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'Address', 'Age', 'Condition','Creator']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'ID': patient.get_id(), 'Name': patient.get_name(), 'Address': patient.get_address(),
                             'Age': patient.get_age(), 'Condition': patient.get_condition(),'Creator':patient.get_creator()})
            
    def idDub(self,id):
        for patient in self.patient_list:
            if patient.get_id() == id:
                return True
        return False

# Example Usage
def test():
    db = PatientDatabase()
    db.load_from_csv()
    patient1 = Patient(1, "Khoa", "Bac", 21, "COVID-18","Dung")
    db.add_patient(patient1)
    db.save_to_csv()

def addPatient(id, name, address, age, condition,creator):
    db = PatientDatabase()
    newPatient = Patient(id, name, address, age, condition,creator)
    db.add_patient(newPatient)
    db.saveNewPatient(newPatient)

def checkID(id):
    db = PatientDatabase()
    return db.idDub(id)
