#Trae la clase de la carpeta model
from ..model.escuela_categ import escuela_categ

#Trae la clase de la carpeta dao
from ..dao.dao_escuela_categ import dao_escuela_categ

#Here we're going to create the logic for each entity.
class dto_escuela_categ: 
    def listar_categorias(self):
        cat = escuela_categ()
        start_dao = dao_escuela_categ()
        lista = start_dao.listar_categorias()
        if len(cat.getLista()) == len(lista):
            return cat.getLista()
        #Transfiere objeto persona a el controlador de base de datos.
        if lista:
            for row in lista:
                record = escuela_categ(*row)
                cat.addCategoria(record)

            return cat.getLista()
        else:
            return False