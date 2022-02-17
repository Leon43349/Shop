#Die ProductController erstellt die product die von Start es Programmes exsetieren. Außerdem beinhaltet sie
from controller.CostumerEvaluationConstroller import CostumerEvaluationController
from models.classProduct import Product
KC = CostumerEvaluationController()
class ProductController:
    Products = []

    Product1=Product("P1","Haifischnike","Shoes",100,119,8,"Shoes",KC.find_reviews(RID=Product.product_ID))
    Product2=Product("P2","Levi´s ","blue pants straight fit",200,238,5,"Pants",KC.find_reviews(RID=Product.product_ID))
    Product3=Product("P3","Polo Pulli", "green Pullover", 300, 357, 1,"Top",KC.find_reviews(RID=Product.product_ID))
    Product4=Product("P4", "North Face rain jacked","black rain jacked",400,476,50,"Jacked",KC.find_reviews(RID=Product.product_ID))
    Product5=Product("P5", "Adidas sports jacked","blue sports jacked",50,59.5,100,"Jacked",KC.find_reviews(RID=Product.product_ID))
    Product6=Product("P6","Adidas shoes","black shoes",250, 297.5,20,"shoes",KC.find_reviews(RID=Product.product_ID))
    Product7=Product("P7","winter jacked","blue winter jacked",1000,1190,5, "Jacked",KC.find_reviews(RID=Product.product_ID))
    Product8=Product("P8","Nike T-Shirt", "white T-Shirt",10,11.90,50,"T-Shirt",KC.find_reviews(RID=Product.product_ID))
    Product9=Product("P9","Nike sports pants","black sport pants",40,47.6,40,"Pants",KC.find_reviews(RID=Product.product_ID))
    Product10=Product("P10","Nike cap","black cap",10,11.9,40,"cap",KC.find_reviews(RID=Product.product_ID))
    Products.append(Product1)
    Products.append(Product2)
    Products.append(Product3)
    Products.append(Product4)
    Products.append(Product5)
    Products.append(Product6)
    Products.append(Product7)
    Products.append(Product8)
    Products.append(Product9)
    Products.append(Product10)

#Mittels dieser Funktion kann der Admin neue Producte hinzufügen, welche direkt in der Liste Products gespeichert werden.
    def create_productadmin(self, product_ID, Name, Description, Pricewithouttax, Pricewithtax, Stock, Category,Kundenbewertungen):
        product=Product(product_ID=product_ID,Name=Name,Description=Description,Pricewithouttax=Pricewithouttax,Pricewithtax=Pricewithtax,Stock=Stock,Category=Category,Kundenbewertungen=Kundenbewertungen)
        self.Products.append(product)

#Diese Funktion gibt ein bestimmtes Produkt zurück das anhand der Produkt ID gefunden wird.
    def find_product(self,product_ID):
        for product in self.Products:
            if product.product_ID == product_ID :
                return product


product = Product("P101","NNike Mütze","sschwarze Mütze",110,111.9,440,"MMütze",None)




