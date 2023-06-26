#Trae la clase de la carpeta model
from ..model.sede import sede

#Trae la clase de la carpeta dao
from ..dao.dao_sede import dao_sede

#Here we're going to create the logic for each entity.
class dto_sede: 
    def listar_sedes(self):
        s = sede()
        start_dao = dao_sede()
        #Load the data from the database
        db_lista = start_dao.listar_sedes()
        if db_lista:
            for row in db_lista:
                start_perfil = sede()
                start_perfil.addSede(sede(*row))
                          
            return s.getLista()
        else:
            return False
