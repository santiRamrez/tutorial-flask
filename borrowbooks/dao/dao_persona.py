#Created Packages
from conexdb import conex

#Downloaded Packages
from dotenv import load_dotenv
import os
import click


class Dao_Persona:
    def __init__(self):
        try:
            # Load environment variables from the .env file
            load_dotenv()

            # Access the environment variables
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_name = os.getenv("DB_NAME")
            # Insert crdentials as env variables.
            self.__conn = conex(db_user, db_password, db_name, db_host, db_port)
        except Exception as ex:
            print(ex)
    
    #Getters
    def getConex(self):
         self.__conn
         return click.echo('Conected to the local database.')

    #Methods
    def listarUsuarios(self):
        conn = self.getConex()
        result = None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM persona WHERE perfil_id = 1")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            conn.close()

        return result
