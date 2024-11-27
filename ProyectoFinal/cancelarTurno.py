#CancelarTurno.py

from db import conectar_db

def CancelarTurnoPorFecha(fecha):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("DELETE FROM Turnos WHERE fecha = %s", (fecha,))
            Connection.commit()
            print("Turnos cancelados con exito")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            Connection.close()

def CancelarTurnoPorMedico(id_medico):
    Connection = conectar_db()
    
    if Connection:
        try:
            Cursor = Connection.cursor()
            Cursor.execute("DELETE FROM Turnos WHERE id_medico = %s")
            Connection.commit()
            print("Turnos para el medico cancelados")
        except EXCEPTION as e:
            print(f"Error: {e}")
        finally:
            Connection.close()
            