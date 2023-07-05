class escuela_categ:
    __listaCategorias = []
    def __init__(self, id="", descrip=""):
        self.id = id
        self.descrip = descrip

    def __str__(self):
        return "{0} {1} {2}".format(self.id, self.descrip)
    
    def getLista(self):
        return self.__listaCategorias
    
    #---- Methods ----
    def addCategoria(self, val):
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
            for categ in lista:
                if categ.descrip.upper() == value.upper():
                    return categ

        return None