from db import conectar_db

def reporte_turnos():
    connection = conectar_db()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT Medicos.nombre, Medicos.apellido, COUNT(*) AS cantidad_turnos
                FROM Turnos
                JOIN Medicos ON Turnos.medico_id = Medicos.id
                GROUP BY Turnos.medico_id
                ORDER BY cantidad_turnos DESC
                LIMIT 3
            """)
            turnos = cursor.fetchall()
            
            if turnos:
                print("\n=== Reporte de los 3 medicos con mas turnos ===")
                print(f"{'Nombre':<20}{'Apellido':<20}{'Cantidad de Turnos':<20}")
                print("-" * 60)
                for medico in turnos:
                    nombre, apellido, cantidad = medico
                    print(f"{nombre:<20}{apellido:<20}{cantidad:<20}")
                print("-" * 60)
            else:
                print("No hay datos suficientes para generar el reporte.")
        
        except Exception as e:
            print(f"Error al generar el reporte: {e}")
        
        finally:
            connection.close()
