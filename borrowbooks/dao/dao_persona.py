import click
import os

#Created Packages
from ..conexdb import conexdb

#Downloaded Packages
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


class dao_persona:
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

    def listarPersonas(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.cursor()
            cursor.execute("SELECT * FROM persona WHERE perfil_id = 1")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result
    
    def agregar_persona(self, per):
        query = """INSERT INTO persona (run, nombre, apellido_pat, apellido_mat, telefono, fecha_nacimien, perfil_id, sede_sede_id, passwrd, email) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (per.run, per.nombre, per.a_paterno, per.a_materno, per.telefono, per.fecha_nacimiento, per.perfil_id, per.sede_id, per.passwrd, per.email))
            c.commit()
            result = True
            click.echo("\nHa agregado!\n")

        # except (Exception, psycopg2.Error) as error:
        #     print("Error while inserting data to PostgreSQL:", error)

        except Exception as ex:
            click.echo(ex)
            result = False

        finally:
            cursor.close()
            c.close()
        
        return result
    

    def login_persona(self, per):
        query = "SELECT * FROM persona WHERE run = %s and passwrd = %s;"
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute(query, (per.run, per.passwrd))
            result = cursor.fetchone()
            c.commit()
        
        except Exception as ex:
            click.echo(ex)
            result = False

        finally:
            cursor.close()
            c.close()
        
        return result