#Die Klasse OrderController beinhaltet die Funktion welche Bestellungen erstellen kann.
from models.classOrder import Order
class OrderController:
    Orders=[]

#Diese Funktion erstellt ein Objekt der Klasse Order und fügt dieses der Liste order hinzu.
    def create_orders_Flask(self,Cartprice,Firstname,Lastname,Street,Housenumber,ZIPCode,City,CardOwner,CreditCardNumber,CVV,ValidUntilMonth,ValidUntilYear):
        order=Order(Cartprice=Cartprice,Firstname=Firstname,Lastname=Lastname,Street=Street,Housenumber=Housenumber,ZIPCode=ZIPCode,City=City,CardOwner=CardOwner,CreditCardNumber=CreditCardNumber,CVV=CVV,ValidUntilMonth=ValidUntilMonth,ValidUntilYear=ValidUntilYear)
        self.Orders.append(order)
        return order


