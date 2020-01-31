import read as data
import mysql.connector

def ajout_plante():
    newid = input(" quels id voulez vous ajouter ? ")
    newname = input("quel plante voulez vous ajouter ? ")
    newindication = input("quel indication preconisez vous ? ")
    newutilisation = input("quelle partie est utile ? ")
    newprice = input("quel est le prix de cette plante ? ")

    sql = "INSERT INTO plante (id,nom,indication,partie_utilisee,prix) VALUES ('{}','{}','{}','{}','{}')".format(newid, newname,
                                                                                                   newindication,
                                                                                                   newutilisation, newprice)
    mycursor.execute(sql)
    data.get_plantes(mycursor)
    datab.commit()

def update():
    updatesql="UPDATE plante SET partie_utilisee = 'feuilles' WHERE partie_utilisee = 'feuiles'"
    mycursor.execute(updatesql)
    data.get_plantes(mycursor)
    datab.commit()


def del_plantes():
    supp_id = input("quelle est le numero a supprimer ? ")
    supp="DELETE FROM plante WHERE id = '{}' ".format(supp_id)
    mycursor.execute(supp)
    data.get_plantes(mycursor)
    datab.commit()

def main():

    while True:

        choix_utilisateur=input("\n que voulez vous faire ? A pour Ajouter , M pour modifier , L pour lister ,Q pour quitter : ").upper()

        if choix_utilisateur == "A":
            ajout_plante()

        elif choix_utilisateur == "M":
            update()

        elif choix_utilisateur == "L":
            data.get_plantes(mycursor)

        elif choix_utilisateur == "S":
            del_plantes()

        elif choix_utilisateur == "Q":
             break


    datab.close()


if __name__ == "__main__":
    datab = mysql.connector.connect(user='mickaell', password='cheerfulguys84', host='127.0.0.1',
                                  database='herboristerie')

    mycursor = datab.cursor()
    main()
