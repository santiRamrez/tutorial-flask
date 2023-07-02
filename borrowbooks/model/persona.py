class persona:
    __listaUsuarios = []
    def __init__(self, id="", run="", nombre="", a_paterno="", a_materno="", telefono="", fecha_nacimiento="", perfil_id="", sede_id="", passwrd="", email=""):
        self.id = id
        self.run = run
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.perfil_id = perfil_id
        self.sede_id = sede_id
        self.passwrd = passwrd
        

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.run, self.nombre, self.a_paterno, self.telefono, self.fecha_nacimiento, self.perfil_id, self.email, self.sede_id)

   
    def getLista(self):
        return self.__listaUsuarios
    
    def cargaPersona(self, persona):
        self.getLista().append(persona)
    
    