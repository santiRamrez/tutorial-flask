#Trae la clase de la carpeta model
from ..model.perfil import perfil

#Trae la clase de la carpeta dao
from ..dao.dao_perfil import dao_perfil

#Here we're going to create the logic for each entity.
class dto_perfil: 
    def listar_perfiles_usuarios(self):
        output = []
        start_dao = dao_perfil()
        p = perfil()
        #Load the data from the database
        db_lista = start_dao.listar_perfiles()
        if db_lista:
            for row in db_lista:
                start_perfil = perfil()
                record = perfil(*row)
                start_perfil.addPerfil(record)
              
        
            #filter the local list to only ENCARGADO - ASISTENTE
            output.append(p.filtra_por_descripcion('ENCARGADO'))
            output.append(p.filtra_por_descripcion('ASISTENTE'))
            
            return output
        else:
            return False