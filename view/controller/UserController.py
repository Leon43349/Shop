#Die Klasse UserController beinhaltet alle Funktion die einem User sich einzuloggen, einen Account zu erstellen oder seine Accountdaten zu ändern.
from models.classUser import User
class UserController:
    users=[]
#Mit der create_user Funktion können Nutzer einen Account anlegen.
#Dieser wird dann direkt in die Liste users eingefürgt.
#Den Nutzern werden in der View fragen gestellt, die dann die Werte des Accounts bestimmen.
    def create_user(self,firstname, lastname,birthdate, username, password):
        user = User(firstname=firstname,lastname=lastname,birthdate=birthdate,username=username,password=password)
        self.users.append(user)

#Die Funktion login druchsucht alle user in der Liste users.
#Daraufhin schaut sie ob es einen Account mit der mit dem (in der View) eingegebenen Username und Password übereinstimmt.
    def login(self,inputunsername,inputpassword):
        loggedin=0
        if inputunsername == "Admin" and inputpassword == "Adminpassword":
            loggedin=1
            return loggedin
        else:
            for user in self.users:
                if inputunsername == user.username and inputpassword == user.password:
                    loggedin=2
                    return loggedin


#Die Funktion find_user fidet aus der Liste users einen bestimmten Account anhand des Attributes username und gibt den gefundenen Account zurück.
    def find_user(self,username):
        for user in self.users:
            if user.username == username:
                return user

#Die Funtktion update_userdata dient dazu das Nutzer ihre Acccountdaten ändern können.
#Sie ruft die Funktion find_user auf mit dem Übergabewert username.
#Der zurückgegebene Account ist der Account wo änderungen vorgenommen werden sollen.
#Es wir auch gleich der neue Wert der Funktion mitgegeben.
    def update_userdata_Flask(self,username,key,NewValue):
        user = self.find_user(username)
        if user is not None:
          user.change_user_Flask(key,NewValue)


user = User("Leon","Schmitz","19.11.1999","Leon43349","Leon1234")



