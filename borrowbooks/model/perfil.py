class perfil:
    __listaPerfiles = []
    def __init__(self, id="", descrip="", d_prestamo=""):
        self.id = id
        self.descrip = descrip
        self.d_prestamo = d_prestamo

    def __str__(self):
        return "{0} {1} {2}".format(self.id, self.descrip, self.d_prestamo)
    
    def getLista(self):
        return self.__listaPerfiles
    
    #---- Methods ----
    def addPerfil(self, val):
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

    def filtra_por_descripcion(self, value):
        lista = self.getLista()
        if len(lista) > 0:
            for perfil in lista:
                if perfil.descrip.upper() == value.upper():
                    return perfil

        return None
            
        
