import click
import os

#Created Packages
from ..conexdb import conexdb

#Downloaded Packages
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


class dao_libro:
    def __init__(self):
        try:
            # Access the environment variables
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_name = os.getenv("DB_NAME")
            #Insert credentials
            self.conn = conexdb.Conex(db_user, db_password, db_name, db_host, db_port)
        except Exception as ex:
            click.echo(ex)
    
    #Getters
    def getConex(self):
         return self.conn.getConex()

    def listar_libros(self):
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute("SELECT * FROM libro")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def listar_ejemplares(self):
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute("SELECT * FROM ejemplar")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def agregar_libro(self, l):
        query = """INSERT INTO libro (isbn, titulo, editorial, year_publicacion, url_img, autores, idioma, escuela_categ_id, estado_libro_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (l.isbn, l.titulo, l.editorial, l.year_publicacion, l.url_img, l.autores, l.idioma, l.escuela_categ_id, 1))
            c.commit()
            result = True
            click.echo("\nHa agregado!\n")

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def agregar_ejemplar(self, ej):
        query = """INSERT INTO ejemplar (libro_isbn, sede_id, id_n_devol, id_n_prestamo, estado_id) 
                    VALUES (%s, %s, %s, %s, %s);"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (ej.libro_isbn, ej.sede_id, ej.id_n_devol, ej.id_n_prestamo, ej.estado_id))
            c.commit()
            result = True
            click.echo("\nHa agregado!\n")

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def listar_ejemplares_disponibles_por_sede(self, isbn, id_sede):
        # -- Estados_Libros ---> Disponible: 1 / Prestado: 2 / Retraso Devolución: 3
        query = """ SELECT serial_num, isbn, titulo, sede_id, estado_id 
                    FROM ejemplar JOIN libro 
                    ON isbn = libro_isbn
                    WHERE sede_id = %s and estado_id = %s and isbn = %s;"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (id_sede, 1, isbn))
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
