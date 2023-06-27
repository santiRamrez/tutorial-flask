class sede:
    __listaSedes = []
    def __init__(self, id="", descrip="", calle="", num="", comuna_id=""):
        self.id = id
        self.descrip = descrip
        self.calle = calle
        self.num = num
        self.comuna_id = comuna_id

    def __str__(self):
        return "{0} {1} {2}".format(self.id, self.descrip, self.calle, self.num)
    
    def getLista(self):
        return self.__listaSedes
    
    #---- Methods ----
    def addSede(self, val):
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

    def filtra_por_id(self, value):
        lista = self.getLista()
        if len(lista) > 0:
            for sede in lista:
                if sede.id == value:
                    return sede

        return None