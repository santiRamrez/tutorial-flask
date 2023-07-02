class ejemplar:
    __listaEjemplares = []
    def __init__(self, n_serie="", libro_isbn="", sede_id="", id_n_devol="", id_n_prestamo="", estado_id=""):
        self.n_serie = n_serie
        self.libro_isbn = libro_isbn
        self.sede_id = sede_id
        self.id_n_devol = id_n_devol
        self.id_n_prestamo = id_n_prestamo
        self.estado_id = estado_id

    def __str__(self):
        return "{0} {1} {2}".format(self.n_serie, self.libro_isbn, self.sede_id)
    
    def getLista(self):
        return self.__listaEjemplares
    
    #---- Methods ----
    def addEjemplar(self, val):
        lista = self.getLista()
        found = False
        if len(lista) > 0:
          for obj in lista:
              if val.descrip.upper() == obj.descrip.upper():
                  found = True
          if found:
              return
          else:
              return lista.append(val)
        else:
          return lista.append(val)

    # def filtra_por_descripcion(self, value):
    #     lista = self.getLista()
    #     if len(lista) > 0:
    #         for ejemp in lista:
    #             if ejemp.descrip.upper() == value.upper():
    #                 return ejemp

    #     return None