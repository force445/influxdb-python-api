import psycopg2

from config import POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT

class Posgres():
    def __init__(self, POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT):
        self.POSGRES_HOST = POSGRES_HOST
        self.POSGRES_USER = POSGRES_USER
        self.POSGRES_PASSWORD = POSGRES_PASSWORD
        self.POSGRES_DB = POSGRES_DB
        self.POSGRES_PORT = POSGRES_PORT

        try:
            self.connection = psycopg2.connect(
                host=self.POSGRES_HOST,
                user=self.POSGRES_USER,
                password=self.POSGRES_PASSWORD,
                database=self.POSGRES_DB,
                port=self.POSGRES_PORT
            )
            self.cursor = self.connection.cursor()
            print("Connection to PostgreSQL DB successful")

        except Exception as e:
            raise Exception(f"Connection to PostgreSQL DB failed: {e}")

    def create_table(self):
        try:
            create_table_query = '''
            CREATE TABLE IoT_Controller (
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            DevEUI CHAR(100) NOT NULL,
            Device_Address CHAR(100),
            Network_Session_Key CHAR(100),
            Application_Session_Key CHAR(100),
            Serial_Number CHAR(100),
            Model CHAR(10),
            Class CHAR(10),
            Measurement CHAR(50)
            );'''
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
    
    def add_column(self):
        try:
            add_column_query = '''ALTER TABLE Environment_Monitoring_Sensor ADD COLUMN App_ID CHAR(100);'''
            self.cursor.execute(add_column_query)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")

    def select_device(self):
        try:
            select_query = '''SELECT * FROM IoT_Controller'''
            self.cursor.execute(select_query)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")



print(POSGRES_DB, POSGRES_HOST, POSGRES_PASSWORD, POSGRES_PORT, POSGRES_USER)
posgres = Posgres(POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT)
# posgres.create_table()
# posgres.add_column()
posgres.select_device()
