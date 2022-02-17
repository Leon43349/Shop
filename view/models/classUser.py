#Die Klasse User definiert einen User der vom nutzer angelegt werde kann.

class User:
    firstname = None
    lastname = None
    birthdate = None
    username = None
    password = None

    def __init__(self, firstname, lastname, birthdate, username, password):
        self.firstname=firstname
        self.lastname=lastname
        self.birthdate=birthdate
        self.username=username
        self.password=password

#Die Methode change_user kann Eigenschaften an einem User ändern.
#Durch den Schlüssel what wird bestimmt was geändert werden soll.
#New_value erstezt dann das Attribut was verändert werden soll.

    def change_user_Flask(self, what,NewValue):
        if what=="Firstname":
            self.firstname= NewValue
        if what=="Lastname":
            self.lastname= NewValue
        if what=="Birthdate":
            self.birthdate= NewValue
        if what=="Username":
            self.username= NewValue
        if what=="Password":
            self.password= NewValue





