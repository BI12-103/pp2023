import Model as Mod
import Login
import PreLogin
import PatientGUI

def init():
    Mod.initPatient()
    Mod.initUser()

def reLogin():
    Login.run()

def start():
    Login.run()

def toPreLogin():
    PreLogin.run()

def toPatientGUI():
    PatientGUI.run()
