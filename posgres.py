import psycopg2


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

    def add_column(self):
        try:
            add_column_query = '''ALTER TABLE sound_level_sensor ADD COLUMN App_ID CHAR(100);'''
            self.cursor.execute(add_column_query)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")

    def select_device_env_monitoring(self):
        try:
            select_query = '''SELECT * FROM Environment_Monitoring_Sensor;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}
            
            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
        
    def select_device_pir(self):
        try:
            select_query = '''SELECT * FROM PIR;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}


            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
    
    def select_device_sound_level(self):
        try:
            select_query = '''SELECT * FROM Sound_Level_Sensor;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}

            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
        
    def select_device_magnetic(self):
        try:
            select_query = '''SELECT * FROM Magnetic_Contract_Switch;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}

            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
        
    def select_device_smart_button(self):
        try:
            select_query = '''SELECT * FROM Smart_Button;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}

            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data

        
    def select_device_portable_socket(self):
        try:
            select_query = '''SELECT * FROM Portable_Socket;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}


            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
        
        
    def select_device_iot_controller(self):
        try:
            select_query = '''SELECT * FROM IoT_Controller;'''
            self.cursor.execute(select_query)
            records = self.cursor.fetchall()
            for row in records:
                data = {'name': row[1], 'deveui': row[2], 'device_address': row[3], 'app_id': row[10]}

            cleaned_data = {key: value.strip() for key, value in data.items()}

        except Exception as e:
            raise Exception(f"Table creation failed: {e}")
        
        return cleaned_data
