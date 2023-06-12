class Persona:
    def __init__(self, id, run, nombre, a_paterno, a_materno, telefono, fecha_nacimiento, perfil_id):
        self.__id = id
        self.__run = run
        self.__nombre = nombre
        self.__a_paterno = a_paterno
        self.__a_materno = a_materno
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__perfil_id = perfil_id
        

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} ".format(self.id, self.__run, self.__nombre, self.__a_paterno, self.__telefono, self.__fecha_nacimiento, self.__perfil_id)

    #Getters

    #Methods or Setters