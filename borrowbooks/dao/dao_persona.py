from conexdb import conex
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Use the variables in your Flask app as needed
# app.config["SECRET_KEY"] = secret_key
# app.config["SQLALCHEMY_DATABASE_URI"] = database_url

import traceback

class DaoPersona:
    def __init__(self):
        try:
            # Insert crdentials as env variables.
            self.__conn = conex(db_user, db_password, db_name, db_host, db_port)
        except Exception as ex:
            print(ex)
    
    #Getters
    def getConex(self):
        return self.__conn

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
