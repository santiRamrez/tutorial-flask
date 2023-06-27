import click
import os

#Created Packages
from ..conexdb import conexdb

#Downloaded Packages
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


class dao_sede:
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
    
    def listar_sedes(self):
        c = self.getConex()
        cursor = c.cursor()
        result = None
        try:
            cursor.execute("SELECT * FROM sede;")
            result = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            c.close()

        return result