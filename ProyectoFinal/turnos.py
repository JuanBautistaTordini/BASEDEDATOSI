from db import conectar_db
import datetime

#programar turno:

def ProgramarTurno(fecha, hora, id_paciente, id_medico, estado_turno):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            
            Cursor.execute("""
                INSERT INTO Turnos (fecha, hora, id_paciente, id_medico, estado_turno)
                VALUES (%s, %s, %s, %s, %s)
            """, (fecha, hora, id_paciente, id_medico, estado_turno))
            
            Connection.commit()
            print("Turno programado correctamente")
        except Exception as e:
            print(f"Error al programar turno: {e}")
        
        finally:
            Connection.close()

#actualizar turno
def ActualizarTurno(id_turno, nueva_fecha, nueva_hora):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            
            Cursor.execute("""
                UPDATE Turnos
                SET fecha = %s, hora = %s
                WHERE id_turno = %s
            """, (nueva_fecha, nueva_hora, id_turno))
            
            Connection.commit()
            print("turno actualizado correctamente")
        except Exception as e:
            print(f"Error al actualizar turno: {e}")
        finally:
            Connection.close()
            
#cancelar turno
def CancelarTurno(id_turno):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            
            Cursor.execute("DELETE FROM Turnos WHERE id_turno = %s", (id_turno,))
            Connection.commit()
            print("Turno cancelado correctamente")
        except Exception as e:
            print(f"Error al cancelar turno: {e}")
        finally:
            Connection.close()
    
#ver turnos
def VerTurnos():
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("SELECT * FROM Turnos")
            turnos = Cursor.fetchall()
            
            for turno in turnos:
                print(turno)
        except Exception as e:
            print(f"Error al ver turnos: {e}")
        finally:
            Connection.close()