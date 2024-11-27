from pacientes import RegistrarPaciente, VerPacientes, ActualizarPaciente, EliminarPaciente
from medicos import AgregarMedico, ActualizarMedico, VerDetallesMedico
from turnos import ProgramarTurno, ActualizarTurno, CancelarTurno, VerTurnos
from reportes import reporte_turnos

def menu_pacientes():
    while True:
        print("\n=== Menú de Pacientes ===")
        print("1. Registrar Paciente")
        print("2. Ver Pacientes")
        print("3. Actualizar Paciente")
        print("4. Eliminar Paciente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            RegistrarPaciente()
        elif opcion == "2":
            VerPacientes()
        elif opcion == "3":
            ActualizarPaciente()
        elif opcion == "4":
            EliminarPaciente()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_medicos():
    while True:
        print("\n=== Menú de Médicos ===")
        print("1. Agregar Médico")
        print("2. Ver Detalles de Médicos")
        print("3. Actualizar Médico")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            especialidad = input("Especialidad: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            AgregarMedico(nombre, apellido, especialidad, telefono, email)
        elif opcion == "2":
            VerDetallesMedico()
        elif opcion == "3":
            id_medico = input("ID del médico: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            especialidad = input("Nueva Especialidad: ")
            telefono = input("Nuevo Teléfono: ")
            email = input("Nuevo Email: ")
            ActualizarMedico(id_medico, nombre, apellido, especialidad, telefono, email)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_turnos():
    while True:
        print("\n=== Menú de Turnos ===")
        print("1. Programar Turno")
        print("2. Ver Turnos")
        print("3. Actualizar Turno")
        print("4. Cancelar Turno")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora (HH:MM): ")
            id_paciente = input("ID del Paciente: ")
            id_medico = input("ID del Médico: ")
            estado_turno = input("Estado del Turno (Ej: Confirmado, Pendiente): ")
            ProgramarTurno(fecha, hora, id_paciente, id_medico, estado_turno)
        elif opcion == "2":
            VerTurnos()
        elif opcion == "3":
            id_turno = input("ID del Turno: ")
            nueva_fecha = input("Nueva Fecha (YYYY-MM-DD): ")
            nueva_hora = input("Nueva Hora (HH:MM): ")
            ActualizarTurno(id_turno, nueva_fecha, nueva_hora)
        elif opcion == "4":
            id_turno = input("ID del Turno: ")
            CancelarTurno(id_turno)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_reportes():
    while True:
        print("\n=== Menú de Reportes ===")
        print("1. Generar Reporte de Turnos por Médico")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_turnos()
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Turnos")
        print("4. Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
