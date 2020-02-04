import read as data
import mysql.connector

def ajout_plante():
    newid = input(" quels id voulez vous ajouter ? ")
    newname = input("quel plante voulez vous ajouter ? ")
    newindication = input("quel indication preconisez vous ? ")
    newutilisation = input("quelle partie est utile ? ")
    newprice = input("quel est le prix de cette plante ? ")
    famille_id =input("quels est le famille id ?")
    sql = "INSERT INTO plante (id,nom,indication,partie_utilisee,prix,famille_id) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql,(newid, newname,newindication,newutilisation, newprice, famille_id))
    data.get_plantes(mycursor)
    datab.commit()


def update():
    updatesql="UPDATE plante SET partie_utilisee = 'feuilles' WHERE partie_utilisee = 'feuiles'"
    mycursor.execute(updatesql)
    data.get_plantes(mycursor)
    datab.commit()

def search_plantes():
    search=input("quelle plante voulez vous ?")
    mycursor= datab.cursor()
    sql = "SELECT * FROM plante WHERE INSTR (nom, %s) "
    mycursor.execute(sql,(search,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def del_plantes():
    supp_id = input("quelle est le numero a supprimer ? ")
    supp="DELETE FROM plante WHERE id = '{}' ".format(supp_id)
    mycursor.execute(supp)
    data.get_plantes(mycursor)
    datab.commit()

def main():

    while True:

        choix_utilisateur=input("\n que voulez vous faire ?  L pour lister ,A pour Ajouter , M pour modifier ,S pour supprimer ,Q pour quitter : ").upper()

        if choix_utilisateur == "A":
            ajout_plante()

        elif choix_utilisateur == "M":
            update()

        elif choix_utilisateur == "L":
            data.get_plantes(mycursor)

        elif choix_utilisateur == "S":
            del_plantes()

        elif choix_utilisateur == "R":
            search_plantes()
        elif choix_utilisateur == "Q":
             break


    datab.close()


if __name__ == "__main__":
    datab = mysql.connector.connect(user='mickaell', password='cheerfulguys84', host='127.0.0.1',
                                  database='herboristerie')

    mycursor = datab.cursor()
    main()
