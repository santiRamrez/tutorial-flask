#Trae la clase de la carpeta model
from model.persona import Persona

#Trae la clase de la carpeta dao
from dao.dao_persona import Dao_Persona

#Here we're going to create the logic for each entity.
class Dto_Persona: 
    def agregar_persona(self, username, email, password):
        dao_persona = Dao_Persona()
        resultado = dao_persona.agregar_persona(Persona(username=username, email=email, password=password))
        return resultado
