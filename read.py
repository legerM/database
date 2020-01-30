import requests
import mysql.connector

cnx = mysql.connector.connect(user = 'mickaell' ,password = 'cheerfulguys84', host ='127.0.0.1',database = 'herboristerie')


cnx.close()

