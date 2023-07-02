import click

#Trae la clase de la carpeta model
from ..model.libro import libro
from ..model.ejemplar import ejemplar
from ..model.sede import sede

#Trae la clase de la carpeta dao
from ..dao.dao_libro import dao_libro

from .dto_sede import dto_sede

#Here we're going to create the logic for each entity.
class dto_libro: 
    def agregar_libro(self, isbn, titulo, editorial, year_publicacion, url_img, autores, idioma, escuela_categ_id, estado_libro_id):
        start_dao = dao_libro()
        #Transfiere objeto persona a el controlador de base de datos.
        resultado = start_dao.agregar_libro(libro(isbn=isbn, titulo=titulo, editorial=editorial, year_publicacion=year_publicacion, url_img=url_img, autores=autores, idioma=idioma, escuela_categ_id=escuela_categ_id, estado_libro_id=estado_libro_id))
        return resultado
    
    def agregar_ejemplar(self, n_serie, libro_isbn, sede_desc, id_n_devol, id_n_prestamo, estado_id):
        start_dao = dao_libro()
        #Carga las sedes desde la base de datos
        dto_sede().listar_sedes()
        location = sede().filtra_por_descripcion(sede_desc)
        loc_id = int(location.id)
        #Transfiere objeto persona a el controlador de base de datos.
        resultado = start_dao.agregar_ejemplar(ejemplar(n_serie=n_serie, libro_isbn=libro_isbn, sede_id=loc_id, id_n_devol=id_n_devol, id_n_prestamo=id_n_prestamo, estado_id=estado_id))
        return resultado
    
    def listar_libros(self):
        start_dao = dao_libro()
        #Transfiere objeto persona a el controlador de base de datos.
        lista = start_dao.listar_libros()
        resultado = []
        if lista:
          for row in lista:
              record = libro(*row)
              resultado.append(record)

          return resultado
        else:
            return False