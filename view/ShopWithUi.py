
from flask import Flask, render_template, request, session
from controller.UserController import UserController
from controller.ProductController import ProductController
from controller.CartController import CartContoller
from controller.CostumerEvaluationConstroller import CostumerEvaluationController
from controller.OrderController import OrderController

app = Flask(__name__, template_folder="../templates")
UC = UserController()
OC = OrderController()
PC = ProductController()
CC = CartContoller()
KC = CostumerEvaluationController()
app.secret_key = "asdfghjkl"

@app.route("/")
def helloworld():
    return render_template("LoginMask.html")

#Diese Funktion schick den User vom Regestrieungsprozess zurück auf die Startseite wenn er den Prozess nicht abschließen möchte.
@app.route("/GoToLoginMask",methods=["POST"])
def GoToLoginMask():
    return render_template("LoginMask.html")

#Diese Funktion wird ausgeführt wenn der User einen Account erstellen will. Er wird auf die Seite weitergeleitet,
#bei der er seine Daten eigeben muss.
@app.route("/createAccount")
def show_create_account():
    return render_template("createAccount.html")


#Diese Funktion nimmt die Inputs von dem User und erstellt einen Account. Dann wird der User zurück auf die Anmeldemaske geleitet.
@app.route("/createAccount", methods=["POST"])
def create_account():
    Firstname = request.form.get("Firstname")
    Lastname = request.form.get("Lastname")
    Birthday = request.form.get("Birthday")
    Username = request.form.get("Username")
    Password = request.form.get("Password")
    UC.create_user(firstname=Firstname, lastname=Lastname, birthdate=Birthday, username=Username,
                              password=Password)
    return render_template("LoginMask.html")


#Der User gibt in der Maske seine Anmeldedaten ein. Wenn er ein Admin ist wird er in das Admin Menu geschickt.
#Fall er ein Kunde ist kommt er auf die Kunden Menu Seite, dabei werden seine Anmeldedaten in der Session gespeichert.
#Falls seine Daten nicht korrekt sind bleibt er auf der Seite und muss erneut seine Daten eingeben oder einen Account erstellen.
@app.route("/login", methods=["POST"])
def login():
    inputusername = request.form.get("username")
    inputpassword = request.form.get("password")
    UC.login(inputusername, inputpassword)
    if UC.login(inputusername, inputpassword) == 1:
        return render_template("LoggedInAdminMenu.html")
    elif UC.login(inputusername, inputpassword) == 2:
        session["username"] = inputusername
        session["password"] = inputpassword
        return render_template("LoggedInUserMenu.html")
    else:
        print("no account with this combination")
        return render_template("LoginMask.html")

#Bei der Logout Funktion wird der User wieder zurück auf die Anmeldemaske geleitet.
#Es wird der Cart und die Session gelöscht.
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    CC.clear_cart()
    return render_template("LoginMask.html")

#Bei dieser Funktion wir der User der Aktuell in der Session eingeloggt ist ausgegeben.
@app.route("/ViewAccount", methods=["POST"])
def ViewAccount():
    username = session["username"]
    user = UC.find_user(username)
    return render_template("ViewAccount.html", User=user)

#In dieser Funktion wird auf die Seite verwiesen bei der der User einen Input tätigen kann was er an seinem Account verändern möchte.
#Dabei wird der Seite ChangeAccount.html der User mitgegeben.
@app.route("/GoToChangeAccount", methods=["POST"])
def GoToChangeAccount():
    username = session["username"]
    us = UC.find_user(username)
    return render_template("ChangeAccount.html",us=us)

#In dieser Funktion werden die neuen Account Daten gegen die alten Ausgetauscht.
#Es wird geschaut bei welchem Feld ein Input getätigt wurde. Dieses wird dann durch den neuen Wert ausgetasucht.
#Handelt es sich um eine Änderung von Username oder Password dann wird die Session dementsprechend angepasst.
@app.route("/ChangeAccount", methods=["POST", "SET"])
def ChangeAccount():
    newfirstname = request.form.get("newfirstname")
    newlastname = request.form.get("newlastname")
    newbirthday = request.form.get("newbirthday")
    newusername = request.form.get("newusername")
    newpassword = request.form.get("newpassword")
    SessionUsername = request.form.get("getUsername")
    if newfirstname !="":
        WhatChange = "Firstname"
        UC.update_userdata_Flask(SessionUsername, WhatChange, newfirstname)
    if newlastname !="":
        newlastname = request.form.get("newlastname")
        WhatChange = "Lastname"
        UC.update_userdata_Flask(SessionUsername, WhatChange, newlastname)
    if newbirthday !="":
        newbirthday = request.form.get("newbirthday")
        WhatChange = "Birthdate"
        UC.update_userdata_Flask(SessionUsername, WhatChange, newbirthday)
    if newusername !="":
        newusername = request.form.get("newusername")
        WhatChange = "Username"
        UC.update_userdata_Flask(SessionUsername, WhatChange, newusername)
        session["username"] = newusername
    if newpassword !="":
        newpassword = request.form.get("newpassword")
        WhatChange = "Password"
        UC.update_userdata_Flask(SessionUsername, WhatChange, newpassword)
        session["password"] = newpassword
    return render_template("LoggedInUserMenu.html")

#Falls der User doch nichts ändern will, kann er durch einen Button zurück in das Menu wechseln.
@app.route("/BackToMenu", methods=["POST"])
def BackToMenu():
    return render_template("LoggedInUserMenu.html")

#Der HTMl Seite wird die Liste aller Produkte mitgegeben, die dann auf der Seite als Tabelle ausgegeben werden.
@app.route("/ViewProduct", methods=["POST"])
def ViewProduct():
    Products = PC.Products
    return render_template("ViewProduct.html", Products=Products)

#In dieser Funktion werden werden die Daten an die add_cart funktion übergeben.
@app.route("/AddToCart", methods=["POST"])
def AddToCart():
    ID = request.form.get("getProductID")
    how_much = request.form.get("HowMuch")
    howmuch = int(how_much)
    howmuch2= howmuch-1
    CC.add_cart(ID, howmuch2)
    return render_template("LoggedInUserMenu.html", ID=ID)

#Diese Funktion übergiebt den Inhalt der Liste Cart auf die Seite ViewCart.html. Dort würd der Cart als Liste ausgegeben.
@app.route("/ViewCart", methods=["POST"])
def ViewCart():
    Cart = CC.cart
    return render_template("ViewCart.html", Cart=Cart)

#Diese Funktion verweißt auf eine Seite wo der User eine Produkt ID eingeben kann.
@app.route("/ViewReviewsID", methods=["POST"])
def ViewReviewsID():
    return render_template("ViewReviewsID.html")

#Mit der eingegebenen Produkt ID werden dann alle dazu passenden Reviews ausgegeben.
#Die Reviews werden in die Liste ReviewsToDeleteInFlask gespeichert.
@app.route("/ViewReviews", methods=["POST"])
def ViewReviews():
    RID = request.form.get("RID")
    KC.get_all_reviews(RID)
    Reviews = KC.ReviewsToDeleteInFlask
    return render_template("ViewReviews.html", RID=RID, Reviews=Reviews)

#In dieser Funktion wird das selbe gemacht wie in der Vorherigen.
#Es wird die Produkt ID automatisch weitergeben, über den Button auf der Seite ViewProduct.html.
@app.route("/ViewReviewsInProduct", methods=["POST"])
def ViewReviewsInProduct():
    RID = request.form.get("getProductRID")
    KC.get_all_reviews(RID)
    Reviews = KC.ReviewsToDeleteInFlask
    return render_template("ViewReviewsInProduct.html", RID=RID, Reviews=Reviews)

#Diese Funktion wird aufgerufen wenn ein Nutzer sich eine Review angeschat hat und zurück zu den Produkten möchte.
#Die erstellte Liste wird wieder geleert damit wenn der User sich eine andere Review anschauen möchte auch nur diese ausgegeben wird.
@app.route("/ViewProductAfterViewReview", methods=["POST"])
def ViewProductAfterViewReview():
    Products = PC.Products
    KC.ReviewsToDeleteInFlask.clear()
    return render_template("ViewProductAfterViewReview.html", Products=Products)

#Diese Funktion wird aufgerufen wenn ein Nutzer sich eine Review angeschat hat und zurück zum Menu möchte.
#Die erstellte Liste wird wieder geleert damit wenn der User sich eine andere Review anschauen möchte auch nur diese ausgegeben wird.
@app.route("/BackToMenuAfterReview", methods=["POST"])
def BackToMenuAfterReview():
    KC.ReviewsToDeleteInFlask.clear()
    return render_template("LoggedInUserMenu.html")

#Diese Funktion leitet den User zum Formular weiter in dem er eine Review schrieben kann.
#Nachdem der User den Button write review gedrückt hat.
@app.route("/WriteReviewRoute", methods=["POST"])
def WriteReviewRoute():
    return render_template("WriteReviewInfo.html")

#Die eingebenen Infos werden zu einer Review zusammengefügt und gespeichert.
@app.route("/WriteReviewInfo", methods=["POST"])
def WriteReviewInfo():
    RID = request.form.get("RID")
    reviewhead = request.form.get("reviewhead")
    reviewbody = request.form.get("reviewbody")
    KC.create_new_reviews(RID=RID,head=reviewhead,reviews=reviewbody)
    return render_template("LoggedInUserMenu.html")

#Diese Funktion leitet den User auf die Seite Checkout.html weiter.
#Nachdem er auf den Button Checkout gedrückt hat.
@app.route("/RouteToCheckOut", methods=["POST"])
def RouteToCheckOut():
    return render_template("Checkout.html")

#Bei dieser Funktion wird aus den Inputs eine Order erstellt, welche dann gespeichet wird.
#Der Nutzer wird auf eine Übersicht der Bestellung weitergeleitet. Dort kann er die Bestellung dann bestätigen.
@app.route("/Checkout", methods=["POST"])
def Checkout():
    CartPrice = CC.price_cart()
    Firstname = request.form.get("Firstname")
    Lastname = request.form.get("Lastname")
    Street = request.form.get("Street")
    Housenumber = request.form.get("Housenumber")
    ZIPCode = request.form.get("ZIPCode")
    City = request.form.get("City")
    Cardowner = request.form.get("Cardowner")
    CreditCardNumber = request.form.get("CreditCardNumber")
    CVV = request.form.get("CVV")
    ValidUntilMonth = request.form.get("ValidUntilMonth")
    ValidUntilYear = request.form.get("ValidUntilYear")
    CO = OC.create_orders_Flask(CartPrice, Firstname, Lastname, Street, Housenumber, ZIPCode, City, Cardowner,
                                CreditCardNumber, CVV, ValidUntilMonth, ValidUntilYear)
    return render_template("CheckoutOverview.html", CO=CO)

#Nach der Bestätigung wir der Stock angepasst und der Cart geleert.
@app.route("/FinishOrder", methods=["POST"])
def FinishOrder():
    CC.stock_update()
    CC.clear_cart()
    return render_template("LoggedInUserMenu.html")

#Diese Funktion schick den Admin zurück zum Admin Menu.
@app.route("/BackToMenuAdmin", methods=["POST"])
def BackToMenuAdmin():
    return render_template("LoggedInAdminMenu.html")

#Diese Funktion loggt den Admin aus und der Nutzer des Systems ist wieder auf der Anmeldemaske.
#Der Unterschied zur logout Funktion für den User ist das keine Session und kein Cart geleert wird.
@app.route("/logoutadmin", methods=["POST"])
def logoutadmin():
    return render_template("LoginMask.html")

#Mit dieser Funktion kann der Admin sich alle Orders die getätigt wurden anschauen(wenn es schon welche gibt).
#Die Liste Orders wird an die ViewOrdersAdmin.html Seite übergeben wo diese dann in einer Tabelle aufgelistet sind.
@app.route("/ViewOrdersAdmin", methods=["POST"])
def ViewOrdersAdmin():
    Orders = OC.Orders
    return render_template("ViewOrdersAdmin.html",Orders=Orders)

#Mit dieser Funktion kann der Admin sich noch alle Accounts anzeigen lassen.
#Die Liste der Account wird an die Seite ViewAllUsersAdmin.html übergeben, wo diese dann als Tabelle dargestellt wird.
@app.route("/ViewAllUsersAdmin", methods=["POST"])
def ViewAllUsersAdmin():
    users = UC.users
    return render_template("ViewAllUsersAdmin.html",Users=users)

#Diese Funktion leitet den Admin auf die Seite AddProduct.html weiter.
@app.route("/AddProductRoute", methods=["POST"])
def AddProductRoute():
    return render_template("AddProduct.html")

#Auf der Seite AddPRoduct.html kann der Admin die Daten eingeben aus denen dann eien neues Produkt generiert wird
@app.route("/AddProduct", methods=["POST"])
def AddProduct():
    product_ID = request.form.get("product_ID")
    Name = request.form.get("Name")
    Description = request.form.get("Description")
    Pricewithouttax = request.form.get("Pricewithouttax")
    Pricewithtax = request.form.get("Pricewithtax")
    Stock = request.form.get("Stock")
    Stock = int(Stock)
    Category = request.form.get("Category")
    PC.create_productadmin(product_ID=product_ID,Name=Name,Description=Description,Pricewithouttax=Pricewithouttax,
                           Pricewithtax=Pricewithtax,Stock=Stock,Category=Category,Kundenbewertungen=None)
    return render_template("LoggedInAdminMenu.html")

#Diese Funktion zeigt dem Admin alle Produkte, dafür werden die Produkte der Seite ViewProductAdmin.html übergeben und als Tabelle dargestellt.
@app.route("/ViewProductAdmin", methods=["POST"])
def ViewProductAdmin():
    Products = PC.Products
    return render_template("ViewProductAdmin.html", Products=Products)

#Mit dieser Funktion kann der Admin auf die Seite ViewReviewsIDAdmin.html geleitet werden wo er dann eine Produkt ID eigeben kann.
@app.route("/ViewReviewsIDAdmin", methods=["POST"])
def ViewReviewsIDAdmin():
    return render_template("ViewReviewsIDAdmin.html")

#Zu der eingebenen Produkt ID werden dem Amin dann alle Reviews ausgegeben.
@app.route("/ViewReviewsAdmin", methods=["POST"])
def ViewReviewsAdmin():
    RID = request.form.get("RID")
    KC.get_all_reviews(RID)
    Reviews = KC.ReviewsToDeleteInFlask
    return render_template("ViewReviewsAdmin.html", RID=RID, Reviews=Reviews)

#Diese Funktion wird aufgerufen wenn ein Admin sich eine Review angeschat hat und zurück zum Menu möchte.
#Die erstellte Liste wird wieder geleert, damit wenn der Admin sich eine andere Review anschauen möchte auch nur diese ausgegeben wird.
@app.route("/BackToMenuAfterReviewAdmin", methods=["POST"])
def BackToMenuAfterReviewAdmin():
    KC.ReviewsToDeleteInFlask.clear()
    return render_template("LoggedInAdminMenu.html")


app.run(debug=True)
