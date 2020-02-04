while True:

    try:
        ammountcredit = int(input("quels est le montant de votre emprunt ? "))
        year = int(input(" sur combien d'année ? "))
        caculcredit = ammountcredit / year
    except ValueError :
        print ("Merci de saisir un chiffre ")
    except ZeroDivisionError:
        print ("La durée ne doit pas être égale à 0")

