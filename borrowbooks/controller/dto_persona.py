import click
#Trae la clase de la carpeta model
from ..model.persona import persona
from ..model.perfil import perfil
from ..model.sede import sede

#Trae la clase de la carpeta dao
from ..dao.dao_persona import dao_persona

#Here we're going to create the logic for each entity.
class dto_persona: 
    def agregar_persona(self, nombre, apellido_pat, apellido_mat, run, fono, fecha_nacim, email, perfil_desc, sede_id, password):
        Dao_Persona = dao_persona()
        cargo = perfil().filtra_por_descripcion(perfil_desc)
        #Transfiere objeto persona a el controlador de base de datos.
        resultado = Dao_Persona.agregar_persona(persona(run=run, nombre=nombre, a_paterno=apellido_pat, a_materno=apellido_mat, telefono=fono, fecha_nacimiento=fecha_nacim, email=email, perfil_id=cargo.id, sede_id=sede_id, passwrd=password))
        return resultado
    
    def login_persona(self, run, passwrd):
        Dao_Persona = dao_persona()
        record = Dao_Persona.login_persona(persona(run=run, passwrd=passwrd))
        if record:
            return persona(*record)
        else:
            record

    
    def carga_personas_memoria(self):
        Dao_Persona = dao_persona()
        info_db = Dao_Persona.listarPersonas()
        if info_db:
            start_persona = persona()
            for record in info_db:
                per = persona(*record)
                start_persona.cargaPersona(per)
            return start_persona.getLista()
        else:
            return False
        
    def listar_beneficiarios(self):
        Dao_Persona = dao_persona()
        info_db = Dao_Persona.listar_beneficiarios()
        output = []
        if info_db:
            for record in info_db:
                output.append(persona(*record))
            return output
        else:
            return False


  