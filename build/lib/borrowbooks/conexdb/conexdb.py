import psycopg2

class Conex:
    def __init__(self, user, password, dbname, host, port):
        try:
            # Connect to an existing database
            self.__connex = psycopg2.connect(user=user, password=password, host=host, port=port, dbname=dbname)                         

        except psycopg2.Error as ex:
            self.__connex.rollback()
            return None

    def getConex(self):
        return self.__connex

    def closeConex(self):
        return self.__connex.close()

