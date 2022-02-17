#Der Cartcontroller beinhaltet alle funktionen, die dafür da sind dem Cart producte hizuzufügen und dieses in der Console auszugeben.
#from models.classProduct import Product
from models.classCart import Cart
from controller.ProductController import ProductController
PC=ProductController()
#Product=Product("P101","NNike Mütze","sschwarze Mütze",110,111.9,440,"MMütze",None)
class CartContoller:
    cart = []

#Die create_product_for_cart bricht wichtigsten Informationen eines Produktes runter und fügt das Produkt der Liste Cart hinzu.
    def create_product_for_cart(self,product_ID,Pricewithtaxes):
        cartp=Cart(product_ID=product_ID,Pricewithtaxes=Pricewithtaxes)
        self.cart.append(cartp)

#Die Check_Stock Funktion prüft ob die Menge an Produkten die der Kunde möchte in unserem Bestand ist.
    def check_stock(self,ID,how_much):
        product = PC.find_product(product_ID=ID)
        if product is not None:
            prductstock=product.Stock
            if prductstock >= how_much:
                return True

#Die add_cart Funktion nimmt die Informationen des Kunden auf.
#Sie findet mittels der find_product Funktion (der Klasse Productkontroller) das gewünschte Product.
#Somit könne die Informationen des Produktes in die create_product_for_cart Funktion übergeben werden.
    def add_cart(self, ID,how_much):
        if self.check_stock(ID,how_much)is True:
            product = PC.find_product(product_ID=ID)
            if product is not None:
                i=0
                while i<=how_much:
                    self.create_product_for_cart(product.product_ID,product.Pricewithtax)
                    i=i+1

#Mit der price_cart wird die Summe des Warenkorbes bestimmt.
#Dazu werden alle Preise der Produkte im Warenkorb in einer neuen Liste als Intiger gespeichert.
#Diese werden anschließend summiert. Die Preise der Produkte werden aus der Klasse classCart mit der retun_price funktion geholt.
    def price_cart(self):
        summ=[]
        for cartp in self.cart:
            price =int(cartp.return_price())
            summ.append(price)
        summe=sum(summ)
        if summe != 0:
            return summe
        else:
            print("You don´t have any products in your cart")

#Diese Funktion wir aufgerufen nachdem eine Bestellung aufgegeben wurde. Bei den Produkten die bei Bestellung noch im Cart
#liegen, wird das Attribut Stock aktualisiert.
    def stock_update(self):
        for product in self.cart:
            ID = product.product_ID
            PC.find_product(ID)
            PC.find_product(ID).Stock=PC.find_product(ID).Stock-1

#Diese Funktion leert den Cart nach einer Bestellung.
    def clear_cart(self):
        self.cart.clear()


