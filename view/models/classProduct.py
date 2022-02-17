#Die Klasse Product definiert ein Produkt.
from controller.CostumerEvaluationConstroller import CostumerEvaluationController
KC= CostumerEvaluationController()

class Product:
    product_ID= None
    Name = None
    Description = None
    Pricewithouttax = None
    Pricewithtax= None
    Stock= None
    Category= None
    Kundenbewertungen= None

    def __init__(self,product_ID,Name,Description,Pricewithouttax,Pricewithtax,Stock,Category,Kundenbewertungen):
        self.product_ID=product_ID
        self.Name=Name
        self.Description=Description
        self.Pricewithouttax=Pricewithouttax
        self.Pricewithtax=Pricewithtax
        self.Stock=Stock
        self.Category=Category
        self.Kundenbewertungen=Kundenbewertungen









