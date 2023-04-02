import Model as Mod
import Login

if __name__ == "__main__":
    Mod.initPatient()
    Mod.initUser()
    login = Login.Login()
    login.Login()