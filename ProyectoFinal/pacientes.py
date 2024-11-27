from db import conectar_db

# registrar paciente:
def RegistrarPaciente():
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese la edad del paciente: ")
    dni = input("Ingrese el DNI del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente: ")
    telefono = input("Ingrese el telefono del paciente: ")
    email = input("Ingrese el email del paciente: ")
    direccion = input("Ingrese la direccion del paciente: ")
    
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = connection.cursor()
            Cursor.execute("""
                INSERT INTO Pacientes (nombre, apellido, DNI, fecha_nacimiento, telefono, email, direccion)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, dni, fecha_nacimiento, telefono, email, direccion))
            Connection.commit()
            print("Paciente registrado con exito")

        except EXCEPTION as e:
            if "1062" in str(e):
                print("Error: El paciente ya se encuentra registrado")
            else:
                print(f"Error: {e}")
        
        finally:
            Connection.close()
            
def VerPacientes():
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor= Connection.cursor()
            Cursor.execute("SELECT * FROM Pacientes")
            pacientes = Cursor.fetchall()
            
            for paciente in pacientes:
                print(paciente)
        except EXCEPTION as e:
            print(f"Error: {e}")
        finally:
            Connection.close()

def ActualizarPaciente():
    #Elegir paciente por id
    id_paciente = input("Ingrese el id del paciente a actualizar: ")
    
    #Datos a actualizar
    nombre = input("Ingrese el nuevo nombre del paciente: ")
    apellido = input("Ingrese la nueva edad del paciente: ")
    dni = input("Ingrese el DNI del paciente: ")
    fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del paciente: ")
    telefono = input("Ingrese el nuevo telefono del paciente: ")
    email = input("Ingrese el nuevo email del paciente: ")
    direccion = input("Ingrese la nueva direccion del paciente: ")
    
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("""
                UPDATE Pacientes SET nombre = %s, apellido = %s, DNI = %s, fecha_nacimiento = %s, telefono = %s, email = %s, direccion = %s
                WHERE id_paciente = %s
            """ , (nombre, apellido, dni, fecha_nacimiento, telefono, email, direccion, id_paciente))
            
            Connection.commit()
            print(f"Paciente con id {id_paciente} actualizado con exito")
            
        except EXCEPTION as e:
            print(f"Error: {e}")
        
        finally:
            Connection.close()

def EliminarPaciente():
    id_paciente = input("Ingrese el id del paciente a eliminar: ")
    
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("DELETE FROM Pacientes WHERE id_paciente = %s", (id_paciente,))
            Connection.commit()
            print(f"Paciente con id {id_paciente} eliminado con exito")
        except EXCEPTION as e:
            print(f"Error: {e}")
        finally:
            Connection.close()
            