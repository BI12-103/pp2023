import csv

class Patient:
    def __init__(self, name, address, age, condition):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__condition = condition

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_condition(self):
        return self.__condition

class PatientDatabase:
    def __init__(self):
        self.__patient_list = []

    def add_patient(self, patient):
        self.__patient_list.append(patient)

    def remove_patient(self, patient):
        if patient in self.__patient_list:
            self.__patient_list.remove(patient)
            print("Patient removed successfully")
        else:
            print("Patient not found")

    def update_patient(self, patient, new_name, new_address, new_age, new_condition):
        if patient in self.__patient_list:
            patient._Patient__name = new_name
            patient._Patient__address = new_address
            patient._Patient__age = new_age
            patient._Patient__condition = new_condition
            print("Patient updated successfully")
        else:
            print("Patient not found")

    def save_to_csv(self, file_name):
        with open(file_name, mode='w', newline='') as csv_file:
            fieldnames = ['Name', 'Address', 'Age', 'Condition']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for patient in self.__patient_list:
                writer.writerow({'Name': patient.get_name(), 'Address': patient.get_address(), 'Age': patient.get_age(), 'Condition': patient.get_condition()})

    def load_from_csv(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                name = row['Name']
                address = row['Address']
                age = row['Age']
                condition = row['Condition']
                patient = Patient(name, address, age, condition)
                self.add_patient(patient)

    def print_patients_from_csv(self, filename):
        with open(filename, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)

# Example usage:
db = PatientDatabase()

# Create and add patients
patient1 = Patient(" hai", "bac ninh", 20, "covid-19")
db.add_patient(patient1)

patient2 = Patient("dung", "ha noi", 20, "Headache")
db.add_patient(patient2)

# Save patient data to CSV file
#db.save_to_csv("patients.csv")

# Load patient data from CSV file
#db.load_from_csv("patients.csv")

# Update patient information
#db.update_patient(patient1, "John Smith", "123 Main St.", 36, "Fever")

# Remove patient
#db.remove_patient(patient2)

# Save updated patient data to CSV file
#db.save_to_csv("patients.csv")
#db.print_patients_from_csv('patients.csv')
