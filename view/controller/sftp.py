
import pysftp

srv = pysftp.Connection(host="user13.wp2021.fhws-webprog.de", username="user13",
password="WPCRWZ5rwBDi",port=8080, log="./temp/pysftp.log")

with srv.cd('public'): #chdir to public
    srv.put("C:\Users\Leon\PycharmProjects\LeonFlask\view\ShopWithUi.py") #upload file to nodejs/

# Closes the connection
srv.close()