import psycopg2



# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
...      (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

class Conex:

    def __init__(self,  host="localhost", port=5432 user, password, db_name):
        try:
            # Connect to an existing database
            self.__connex = psycopg2.connect(user=user, password=password, host=host, port=port database=db_name)
                                             
        except psycopg2.Error as ex:
            print(ex.pgerror)
            self.__connex.rollback()
            return None

    def closeConex(self):
        self.__myconn.close()

    def getConex(self):
        return self.__myconn