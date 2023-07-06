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
    
    def agregar_ejemplar(self, libro_isbn, sede_desc, id_n_devol, id_n_prestamo, estado_id):
        start_dao = dao_libro()
        #Carga las sedes desde la base de datos
        dto_sede().listar_sedes()
        location = sede().filtra_por_descripcion(sede_desc)
        loc_id = int(location.id)
        #Transfiere objeto persona a el controlador de base de datos.
        resultado = start_dao.agregar_ejemplar(ejemplar(libro_isbn=libro_isbn, sede_id=loc_id, id_n_devol=id_n_devol, id_n_prestamo=id_n_prestamo, estado_id=estado_id))
        return resultado
    
    def listar_libros(self):
        start_dao = dao_libro()
        lista_db = start_dao.listar_libros()
        start_libro = libro()
        if len(lista_db) == len(start_libro.getLista()):
            return start_libro.getLista()
        
        if lista_db:
          for row in lista_db:
              start_libro.addLibro(libro(*row))

          return start_libro.getLista()
        else:
            return False
        
    
    def listar_ejemplares(self):
        start_dao = dao_libro()
        lista_db = start_dao.listar_ejemplares()
        start_ejemp = ejemplar()
        if len(lista_db) == len(start_ejemp.getLista()):
            return start_ejemp.getLista()
        
        if lista_db:
          for row in lista_db:
              start_ejemp.addEjemplar(ejemplar(*row))

          return start_ejemp.getLista()
        else:
            return False
    
    def agregar_qty_ejemplares(self, isbn, id_sede, qty):
        start_dao = dao_libro()
        total = 1
        for x in range(qty):
            add = start_dao.agregar_ejemplar(ejemplar(isbn, id_sede, 0, 0, 1))
            if add:
                total = total + x
        return total

    def listar_ejempl_disponib_porsede(self, isbn, id_sede):
        start_dao = dao_libro()
        db_list = start_dao.listar_ejemplares_disponibles_por_sede(isbn, id_sede)
        output = []
        if db_list:
            for record in db_list:
                libro = {}
                libro['serial_num'] = record[0]
                libro['isbn'] = record[1]
                libro['titulo'] = record[2]
                output.append(libro)
            return output
        else:
            False

        
