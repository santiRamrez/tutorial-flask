import click
import os

#Created Packages
from ..conexdb import conexdb

#Downloaded Packages
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


class dao_prestamo:
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

    def listar_prestamos(self):
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute("SELECT * FROM nota_prestamo")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def listar_persona_notaprest(self):
        #Relaciona la persona con la nota de préstamo
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute("SELECT * FROM persona_notaprest")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def agregar_nota_prestamo(self, prest):
        query = """INSERT INTO nota_prestamo (fecha_prestamo, fecha_devol, renov) 
                    VALUES (%s, %s, %s);"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (prest.fecha_prestamo, prest.fecha_devol, prest.renov))
            c.commit()
            result = True
            click.echo("\nHa agregado!\n")

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def agregar_persona_notaprest(self, rec):
        query = """INSERT INTO persona_notaprest (per_id, nota_prestamo_prest_id) 
                    VALUES (%s, %s);"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (rec.per_id, rec.nota_prestamo_prest_id))
            c.commit()
            result = True
            click.echo("\nHa agregado!\n")

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result