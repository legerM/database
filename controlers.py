import models as mod
from peewee import *

def average_price():
    plantes = (mod.Plante
               .select(mod.Plante.indication, fn.AVG(mod.Plante.price).alias("avg"))
               .order_by(mod.Plante.indication)
               .group_by(mod.Plante.indication)
               )

    for plante in plantes:
        print(plante.indication, plante.avg)


def 


average_price()


