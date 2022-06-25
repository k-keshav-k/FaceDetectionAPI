import psycopg2

# Class containing utilities for coonection to a database
class connectionClass:
    # method to establish connection
    def __init__(self):
        self.conn = psycopg2.connect(
            database="facesdb", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
        )
        # Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

        # Executing an MYSQL function using the execute() method
        self.cursor.execute("select version()")

        # Fetch a single row using fetchone() method.
        data = self.cursor.fetchone()
        print("Connection established to: ",data)

    # method to close Connection
    def closeConn(self):
        self.conn.close()

    # method to commit changes to database
    def commitToDb(self):
        self.conn.commit()
