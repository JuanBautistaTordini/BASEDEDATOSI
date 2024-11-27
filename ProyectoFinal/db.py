import mysql.connector

def conectar_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root", #Modifcar root por el usuario de la base de datos
            password="root", # Modificar por la contraseña de la base de datos
            database="SistemaDeHospital"
        )
    except mysql.connector.Error as e:
        print(f"error al conectar a la base de datos: {e}")
        return None
