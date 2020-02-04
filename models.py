from peewee import *


datab = MySQLDatabase(
    'herboristerie',
    user='mickaell', password='cheerfulguys84', host='127.0.0.1')


class BaseModel(Model):
    class Meta:
        database = datab


class Sous_Classe(BaseModel):
    id_Sous_Classe = AutoField (primary_key=True)
    name = CharField(column_name= 'Name')
    name_fr = CharField(column_name='Name_Fr')


class Famille(BaseModel):
    id=AutoField (primary_key=True)
    name = CharField(column_name= 'Name')
    name_fr = CharField(column_name='Name_Fr')
    sous_class_id = ForeignKeyField(Sous_Classe,column_name='Sous_Class_id')

class Plante (BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(column_name= 'nom')
    indication = CharField ()
    used_part = CharField(column_name='partie_utilisee')
    price = DecimalField(max_digits=7, decimal_places=2,column_name='prix')
    famille_id = ForeignKeyField(Famille, column_name='Famille_id')

if __name__ == '__main__':
    result = Plante.select()
    for plante in result:
        print(plante.name)


