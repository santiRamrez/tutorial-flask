import click

#Trae clases de la carpeta model
from ..model.nota_prestamo import nota_prestamo
from ..model.persona import persona
from ..model.libro import libro
from ..model.ejemplar import ejemplar

#Trae clases de la carpeta dao
from ..dao.dao_libro import dao_libro


#Here we're going to create the logic for each entity.
class dto_prestamo: 
    def agregar_prestamo(self, ):
        start_dao = dao_libro()
        #Transfiere objeto persona a el controlador de base de datos.
        # resultado = start_dao.agregar_libro(libro())
        # return resultado
    
    # def agregar_ejemplar(self, libro_isbn, sede_desc, id_n_devol, id_n_prestamo, estado_id):
    #     start_dao = dao_libro()
    #     #Carga las sedes desde la base de datos
    #     dto_sede().listar_sedes()
    #     location = sede().filtra_por_descripcion(sede_desc)
    #     loc_id = int(location.id)
    #     #Transfiere objeto persona a el controlador de base de datos.
    #     resultado = start_dao.agregar_ejemplar(ejemplar(libro_isbn=libro_isbn, sede_id=loc_id, id_n_devol=id_n_devol, id_n_prestamo=id_n_prestamo, estado_id=estado_id))
    #     return resultado
    
    # def listar_libros(self):
    #     start_dao = dao_libro()
    #     lista_db = start_dao.listar_libros()
    #     start_libro = libro()
    #     if len(lista_db) == len(start_libro.getLista()):
    #         return start_libro.getLista()
        
    #     if lista_db:
    #       for row in lista_db:
    #           start_libro.addLibro(libro(*row))

    #       return start_libro.getLista()
    #     else:
    #         return False
        
    
    # def listar_ejemplares(self):
    #     start_dao = dao_libro()
    #     lista_db = start_dao.listar_ejemplares()
    #     start_ejemp = ejemplar()
    #     if len(lista_db) == len(start_ejemp.getLista()):
    #         return start_ejemp.getLista()
        
    #     if lista_db:
    #       for row in lista_db:
    #           start_ejemp.addEjemplar(ejemplar(*row))

    #       return start_ejemp.getLista()
    #     else:
    #         return False
    
    # def agregar_qty_ejemplares(self, isbn, id_sede, qty):
    #     start_dao = dao_libro()
    #     total = 1
    #     for x in range(qty):
    #         add = start_dao.agregar_ejemplar(ejemplar(isbn, id_sede, 0, 0, 1))
    #         if add:
    #             total = total + x
    #     return total