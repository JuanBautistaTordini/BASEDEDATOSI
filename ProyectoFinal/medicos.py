from db import conectar_db

def AgregarMedico(nombre, apellido, especialidad, telefono, email):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("""
                INSERT INTO Medicos (nombre, apellido, especialidad, telefono, email)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, apellido, especialidad, telefono, email))
            Connection.commit()
            print("Médico agregado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al agregar médico: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            Connection.close()

def ActualizarMedico(id, nombre, apellido, especialidad, telefono, email):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("""
                UPDATE Medicos
                SET nombre = %s, apellido = %s, especialidad = %s, telefono = %s, email = %s
                WHERE id_medico = %s
            """, (nombre, apellido, especialidad, telefono, email, id))
            Connection.commit()
            print("Médico actualizado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar médico: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            Connection.close()

def VerDetallesMedico():
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("SELECT id_medico, nombre, apellido, especialidad, telefono, email FROM Medicos")
            
            print("Detalles de médicos:")
            for medico in Cursor.fetchall():
                print(f"ID: {medico[0]}, Nombre: {medico[1]}, Apellido: {medico[2]}, Especialidad: {medico[3]}, Teléfono: {medico[4]}, Email: {medico[5]}")
        except mysql.connector.Error as e:
            print(f"Error al obtener detalles de médicos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            Connection.close()
