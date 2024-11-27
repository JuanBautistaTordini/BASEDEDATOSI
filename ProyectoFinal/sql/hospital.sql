-- Creación de la base de datos
CREATE DATABASE HospitalDB;
USE SistemaDeHospital;

-- Creación de tablas

-- Tabla de Pacientes
CREATE TABLE Pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    direccion VARCHAR(255) NOT NULL,
    CONSTRAINT chk_fecha_nacimiento CHECK (fecha_nacimiento < CURDATE())  
);

-- Tabla de Médicos
CREATE TABLE Medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL UNIQUE, 
    email VARCHAR(100) NOT NULL UNIQUE     
);

-- Tabla de Turnos
CREATE TABLE Turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    fecha DATE NOT NULL,
    horario TIME NOT NULL,
    estado_turno VARCHAR(50) DEFAULT 'Pendiente',
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id) ON DELETE CASCADE,
    FOREIGN KEY (medico_id) REFERENCES Medicos(id) ON DELETE CASCADE,
    CONSTRAINT chk_fecha_turno CHECK (fecha >= CURDATE())
);

-- Creación de índices
CREATE INDEX idx_turnos_fecha_hora ON Turnos(fecha, horario);
CREATE INDEX idx_medicos_especialidad ON Medicos(especialidad);
CREATE INDEX idx_turnos_estado ON Turnos(estado_turno);
CREATE INDEX idx_pacientes_telefono ON Pacientes(telefono);

-- Inserción de datos iniciales
-- Inserción de pacientes
INSERT INTO Pacientes (nombre, apellido, fecha_nacimiento, telefono, email, direccion)
VALUES
('Juan', 'Pérez', '1980-05-15', '123456789', 'juan.perez@example.com', 'Calle Falsa 123'),
('Ana', 'López', '1995-08-20', '987654321', 'ana.lopez@example.com', 'Avenida Siempre Viva 456');

-- Inserción de médicos
INSERT INTO Medicos (nombre, apellido, especialidad, telefono, email)
VALUES
('Laura', 'Gómez', 'Cardiología', '555123456', 'laura.gomez@example.com'),
('Mario', 'Rodríguez', 'Pediatría', '555987654', 'mario.rodriguez@example.com');

-- Inserción de turnos
INSERT INTO Turnos (paciente_id, medico_id, fecha, horario, estado_turno)
VALUES
(1, 1, '2024-11-28', '10:00:00', 'Pendiente'),
(2, 2, '2024-11-29', '11:00:00', 'Confirmado');