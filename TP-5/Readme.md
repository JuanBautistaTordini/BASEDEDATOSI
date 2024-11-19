### Ejercicio: Talleres de Autos

**Esquema de Base de Datos:**  
`TALLER <codigoSucursal, domicilioSucursal, telefonoSucursal, codigoFosa, largoFosa, anchoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente, nombreCliente, celularCliente, dniMecanico, nombreMecanico, emailMecanico>`

---

### **Restricciones:**

1. **Sobre las sucursales:**  
   Cada `codigoSucursal` identifica una sucursal específica, con su domicilio, teléfono, fosas y mecánicos asociados.

2. **Sobre las fosas:**  
   Cada fosa tiene un `codigoFosa`, que es un número secuencial dentro de la sucursal. Esto significa que el mismo código puede repetirse en diferentes sucursales, pero siempre se distinguirá por el `codigoSucursal`. También se registran las dimensiones (`largoFosa` y `anchoFosa`) de cada fosa.

3. **Relación entre autos y fosas:**  
   Cada fosa puede registrar los autos que se repararon allí. De los autos, guardamos su patente (`patenteAuto`), marca, modelo y el cliente que lo trajo al taller.

4. **Sobre los clientes:**  
   Un cliente tiene un único `dniCliente`, pero puede poseer varios autos. Registramos su nombre y celular.

5. **Sobre los mecánicos:**  
   Cada mecánico tiene un `dniMecanico`, un nombre y un email.

---

### **Paso 1: Dependencias Funcionales (DFs)**

Con base en el esquema y las restricciones, identificamos las siguientes dependencias funcionales:

- `codigoSucursal -> domicilioSucursal, telefonoSucursal`  
  (Una sucursal tiene un único domicilio y teléfono).

- `codigoFosa -> largoFosa, anchoFosa`  
  (Cada fosa tiene dimensiones específicas).

- `patenteAuto -> marcaAuto, modeloAuto, dniCliente`  
  (La patente identifica de manera única al auto, su marca, modelo y propietario).

- `dniCliente -> nombreCliente, celularCliente`  
  (Cada cliente tiene un nombre y un celular únicos).

- `dniMecanico -> nombreMecanico, emailMecanico`  
  (Cada mecánico tiene un nombre y un correo únicos).

---

### **Paso 2: Claves Candidatas**

Para encontrar las claves candidatas, buscamos un conjunto mínimo de atributos que identifique de forma única cada registro en la tabla `TALLER`.  

Las claves candidatas son:  
`(codigoFosa, patenteAuto, dniMecanico, codigoSucursal)`  

Justificación:
- `codigoFosa` identifica una fosa dentro de una sucursal.
- `patenteAuto` identifica el auto en cuestión.
- `dniMecanico` señala qué mecánico realizó el trabajo.
- `codigoSucursal` diferencia fosas con el mismo código en distintas sucursales.

---

### **Paso 3: Normalización a Tercera Forma Normal (3FN)**

Para alcanzar la 3FN, eliminamos las dependencias transitivas y nos aseguramos de que cada atributo no clave dependa únicamente de la clave primaria completa. Esto implica dividir la tabla original en varias tablas relacionadas.  

El diseño normalizado incluye las siguientes tablas:

#### **1. Tabla `Taller`:**
Relación entre fosas, autos, mecánicos y sucursales.  
- **Atributos:**  
  `codigoFosa`, `patenteAuto`, `dniMecanico`, `codigoSucursal`  
- **Clave primaria compuesta:**  
  `(codigoFosa, patenteAuto, dniMecanico, codigoSucursal)`  

#### **2. Tabla `Fosa`:**
Información sobre las fosas dentro de las sucursales.  
- **Atributos:**  
  `codigoFosa`, `codigoSucursal`, `largoFosa`, `anchoFosa`  
- **Clave primaria compuesta:**  
  `(codigoFosa, codigoSucursal)`  

#### **3. Tabla `Auto`:**
Datos de los vehículos que ingresan al taller.  
- **Atributos:**  
  `patenteAuto`, `marcaAuto`, `modeloAuto`, `dniCliente`  
- **Clave primaria:**  
  `patenteAuto`  

#### **4. Tabla `Cliente`:**
Información de los propietarios de los vehículos.  
- **Atributos:**  
  `dniCliente`, `nombreCliente`, `celularCliente`  
- **Clave primaria:**  
  `dniCliente`  

#### **5. Tabla `Mecanico`:**
Datos de los mecánicos que trabajan en el taller.  
- **Atributos:**  
  `dniMecanico`, `nombreMecanico`, `emailMecanico`  
- **Clave primaria:**  
  `dniMecanico`  

#### **6. Tabla `Sucursal`:**
Información de las sucursales.  
- **Atributos:**  
  `codigoSucursal`, `domicilioSucursal`, `telefonoSucursal`  
- **Clave primaria:**  
  `codigoSucursal`  

### **Ventajas del Diseño Normalizado:**
- **Reducción de redundancia:** Eliminamos datos duplicados entre las tablas.  
- **Consistencia:** Garantizamos que cada atributo depende de una clave primaria.  
- **Escalabilidad:** Podemos agregar o modificar datos en una tabla sin afectar a otras.  