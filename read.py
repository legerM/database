import requests
import mysql.connector



def get_plantes (mycursor) :
        mycursor.execute("SELECT * FROM plante")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)


if __name__ == "__main__":
    datab = mysql.connector.connect(user='mickaell', password='cheerfulguys84', host='127.0.0.1',
                                  database='herboristerie')

    mycursor = datab.cursor()
    get_plantes(mycursor)

