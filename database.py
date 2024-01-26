import sqlite3

class database:
    def __init__(self):
        # Change this with your database name
        self.DBname = 'database.db'

    # Connecting to the database
    def connect(self):
        conn = None
        try:
            conn = sqlite3.connect(self.DBname)
        except Exception as e:
            # Error handling
            print(e)
        return conn
    
    # Getting data from the database (GET Request)
    def query(self, command, parameters=[]):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(command, parameters)

        result = cur.fetchall()
        self.disconnect(conn)
        return result

    # Updating the databse (POST, SET, DELETE Request etc.)
    def update(self, command, parameters=[]):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(command, parameters)

        conn.commit()
        result = cur.fetchall()
        self.disconnect(conn)
        return result

    # Disconnecting from the database
    def disconnect(self, conn):
        conn.close()