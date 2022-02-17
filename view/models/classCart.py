#Die Klasse Cart definiert ein Produkt das zu dem Einkaufswagen hinzugeführt wird.
#Dadruch steht am Ende im Einkaufswagen nur noch die Produkt ID und der Preis inkl. Steuern.
#Somit werden unnötige information im Einkaufswagen weggelassen wie z.B. der Preis ohne Stuern oder der Lagerbestand.

class Cart:
    product_ID = None
    Pricewithtaxes = None

    def __init__(self, product_ID, Pricewithtaxes):
        self.product_ID = product_ID
        self.Pricewithtaxes= Pricewithtaxes

#Die Funktion return_price gibt den Preis inkl. Steuern zurück.
    def return_price(self):
        return self.Pricewithtaxes



