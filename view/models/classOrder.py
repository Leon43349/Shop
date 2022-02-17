#Die Klasse classOrder definiert eine Bestellung.
from controller.CartController import CartContoller

CC = CartContoller()
class Order:
    Cartprice = None
    Firstname = None
    Lastname = None
    Street = None
    Housenumber = None
    ZIPCode = None
    City = None
    CardOwner = None
    CreditCardNumber = None
    CVV = None
    ValidUntilMonth = None
    ValidUntilYear = None

    def __init__(self,Cartprice,Firstname,Lastname,Street,Housenumber,ZIPCode,City,CardOwner,CreditCardNumber,CVV,ValidUntilMonth,ValidUntilYear):
        self.Cartprice = Cartprice
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Street = Street
        self.Housenumber = Housenumber
        self.ZIPCode = ZIPCode
        self.City = City
        self.CardOwner = CardOwner
        self.CreditCardNumber = CreditCardNumber
        self.CVV = CVV
        self.ValidUntilMonth = ValidUntilMonth
        self.ValidUntilYear = ValidUntilYear


