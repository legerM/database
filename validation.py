class Vehicule:
    cap_essence_max = None


    def __init__(self,name):
        self.name = name
        self.reservoir = self.cap_essence_max

    def start(self):
        self.etat = True
        print("le véhicule démarre")

    def accelerate(self,vitesse,distance):
        if self.etat:
            essence_utilise = vitesse*distance / 100
            self.reservoir -= essence_utilise
            if self.reservoir <= 0:
                self.Eteindre()

    def Eteindre(self):
        self.etat = False
        print(" le vehicule s'eteint")





class Voiture (Vehicule):
    etat = False
    vitesse_max =130
    cap_essence_max = 50


class Camion(Vehicule):
    etat = False
    vitesse_max = 90
    cap_essence_max = 100

    def start(self):
        super().start()
        self.reservoir -= 5
        print(self.reservoir)




class Scooter(Vehicule):
    etat = False
    vitesse_max = 50
    cap_essence_max = 5


# twingo = Voiture("twingo")
# twingo.start()
# twingo.accelerate(50,200)

mercedes = Camion("mercedes")
mercedes.start()
mercedes.accelerate(90,100)

# scooter=