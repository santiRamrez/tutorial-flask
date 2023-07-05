class libro:
    __lista_libros = []
    def __init__(self, isbn="", titulo="", editorial="", year_publicacion="", url_img="", autores="", idioma="", escuela_categ_id="", estado_libro_id=""):
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial
        self.year_publicacion = year_publicacion
        self.url_img = url_img
        self.autores = autores
        self.idioma = idioma
        self.escuela_categ_id = escuela_categ_id
        self.estado_libro_id = estado_libro_id

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} ".format(self.isbn, self.titulo, self.editorial, self.year_publicacion, self.url_img, self.autores)

    def getLista(self):
        return self.__lista_libros
    
    def addLibro(self, val):
        lista = self.getLista()
        found = False
        if len(lista) > 0:
          for obj in lista:
              if val.titulo.upper() == obj.titulo.upper():
                  found = True
          if found:
              return
          else:
              return lista.append(val)
        else:
          return lista.append(val)
   
    def filtra_por_descripcion(self, libro):
        lista = self.getLista()
        if len(lista) > 0:
            for obj in lista:
                if obj.titulo.upper() == libro.titulo.upper():
                    return obj

        return None