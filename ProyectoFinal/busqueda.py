from db import conectar_db

def BuscarPaciente():
    
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            
            #Buscar paciente por nombre
            nombre = input("Ingrese el nombre del paciente a buscar: ")
            Cursor.execute("SELECT * FROM Pacientes WHERE nombre = %s", (nombre,))
            resultado = Cursor.fetchall()

            if resultado:
                for paciente in resultado:
                    print(paciente)
            else:
                print("Paciente no encontrado")
        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            Connection.close()

def BuscarMedico():
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            
            #Buscar medico por nombre
            nombre = input("Ingrese el nombre del medico a buscar: ")
            Cursor.execute("SELECT * FROM Medicos WHERE nombre = %s", (nombre,))
            resultado = Cursor.fetchall()

            if resultado:
                for medico in resultado:
                    print(medico)
            else:
                print("Medico no encontrado")
        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            Connection.close()

    