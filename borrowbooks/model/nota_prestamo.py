class nota_prestamo:
    __listaPrestamos = []
    def __init__(self, fecha_prestamo="", fecha_devol="", renov="", prest_id=""):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devol = fecha_devol
        self.renov = renov
        self.prest_id = prest_id

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.fecha_prestamo, self.fecha_devol, self.renov, self.prest_id)
    
    def getLista(self):
        return self.__listaPerfiles
    
    #---- Methods ----
    def addPrestamo(self, prest):
        lista = self.getLista()
        found = False
        if len(lista) > 0:
          for obj in lista:
              if prest.prest_id == obj.prest_id:
                  found = True
          if found:
              return
          else:
              return lista.append(prest)
        else:
          return lista.append(prest)

    def filtra_por_descripcion(self, value):
        lista = self.getLista()
        if len(lista) > 0:
            for perfil in lista:
                if perfil.descrip.upper() == value.upper():
                    return perfil

        return None