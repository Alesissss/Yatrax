-- Primero eliminamos los procedimientos por si existen
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_DARBAJA_CLIENTE;
DROP PROCEDURE IF EXISTS SP_EDITAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ASIGNAR_DMENU;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_EDITAR_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_DARBAJA_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_DMENU;
DROP PROCEDURE IF EXISTS SP_ASIGNAR_DCLAIM;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_DCLAIM;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_CAMBIAR_CLAVE;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_EDITAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ACTIVAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_ABREVIATURA_CIUDAD;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_SUCURSAL;
DROP PROCEDURE IF EXISTS SP_EDITAR_SUCURSAL;
DROP PROCEDURE IF EXISTS SP_DARBAJA_SUCURSAL;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_SUCURSAL;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_HORARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_HORARIO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_HORARIO;
DROP PROCEDURE IF EXISTS SP_ACTIVAR_HORARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_HORARIO;
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_METODO_PAGO;
DROP PROCEDURE IF EXISTS SP_EDITAR_METODO_PAGO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_METODO_PAGO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_METODO_PAGO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_PERSONAL;
DROP PROCEDURE IF EXISTS SP_EDITAR_TIPO_PERSONAL;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPO_PERSONAL;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_PERSONAL;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_DOCUMENTO;
DROP PROCEDURE IF EXISTS SP_EDITAR_TIPO_DOCUMENTO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPO_DOCUMENTO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_DOCUMENTO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_PERSONAL;
DROP PROCEDURE IF EXISTS SP_EDITAR_PERSONAL;
DROP PROCEDURE IF EXISTS SP_DARBAJA_PERSONAL;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PERSONAL;
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PERSONAL_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_DARBAJA_PERSONAL_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_PERSONAL_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_EDITAR_PERSONAL_INCIDENCIA;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_CLIENTE;

DROP PROCEDURE IF EXISTS SP_ELIMINAR_ASIENTO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_ASIENTO;
DROP PROCEDURE IF EXISTS SP_EDITAR_ASIENTO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_ASIENTO;

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_COMPROBANTE;

DROP PROCEDURE IF EXISTS SP_INSERTAR_SERVICIO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_SERVICIO;
DROP PROCEDURE IF EXISTS SP_BAJA_SERVICIO;
DROP PROCEDURE IF EXISTS SP_DELETE_SERVICIO;

DROP PROCEDURE IF EXISTS SP_INSERTAR_MICROSERVICIO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_MICROSERVICIO;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_MICROSERVICIO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_MICROSERVICIO;

-- Eliminar procedimientos almacenados si existen
DROP PROCEDURE IF EXISTS SP_INSERTAR_VEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_VEHICULO;
DROP PROCEDURE IF EXISTS SP_BAJA_VEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_VEHICULO;

-- Eliminar procedimientos existentes (si los hay)
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPOVEHICULO;

-- Eliminar procedimientos existentes (si los hay)
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE_JURIDICO;

DROP PROCEDURE IF EXISTS SP_EDITAR_CLIENTE_NATURAL;
DROP PROCEDURE IF EXISTS SP_EDITAR_CLIENTE_JURIDICO;

DROP PROCEDURE IF EXISTS SP_DARBAJA_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_VERIFICAR_CORREO_CLIENTE;

-- Eliminar procedimientos si existen
DROP PROCEDURE IF EXISTS SP_INSERTAR_NIVEL;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_NIVEL;
DROP PROCEDURE IF EXISTS SP_DARBAJA_PISO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_NIVEL;

DROP PROCEDURE IF EXISTS SP_REGISTRAR_MARCA;
DROP PROCEDURE IF EXISTS SP_EDITAR_MARCA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_MARCA;
DROP PROCEDURE IF EXISTS SP_DARBAJA_MARCA;

DROP PROCEDURE IF EXISTS SP_REGISTRAR_RUTA;
DROP PROCEDURE IF EXISTS SP_EDITAR_RUTA;
DROP PROCEDURE IF EXISTS SP_DARBAJA_RUTA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_RUTA;

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_METODOPAGO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_METODOPAGO;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_METODOPAGO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_METODOPAGO;

DROP PROCEDURE IF EXISTS SP_REGISTRAR_TERMINOS_CONDICIONES;
DROP PROCEDURE IF EXISTS SP_EDITAR_TERMINOS_CONDICIONES;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TERMINOS_CONDICIONES;
DROP PROCEDURE IF EXISTS SP_ACTIVAR_TERMINOS_CONDICIONES;

DROP PROCEDURE IF EXISTS SP_REGISTRAR_PREGUNTA_FRECUENTE;
DROP PROCEDURE IF EXISTS SP_EDITAR_PREGUNTA_FRECUENTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PREGUNTA_FRECUENTE;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_PREGUNTA_FRECUENTE;

DROP PROCEDURE IF EXISTS SP_INSERTAR_PASAJE;
DROP PROCEDURE IF EXISTS SP_MODIFICAR_PASAJE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PASAJE;
DROP PROCEDURE IF EXISTS SP_CAMBIAR_ESTADO_PASAJE;

DROP PROCEDURE IF EXISTS SP_CAMBIAR_CLAVE;

-- Eliminar procedimientos de reclamo y tipo_reclamo
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_RECLAMO;
DROP PROCEDURE IF EXISTS SP_MODIFICAR_TIPO_RECLAMO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_RECLAMO;

DROP PROCEDURE IF EXISTS SP_INSERTAR_RECLAMO;
DROP PROCEDURE IF EXISTS SP_MODIFICAR_RECLAMO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_RECLAMO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE;
DROP PROCEDURE IF EXISTS SP_DARBAJA_RECLAMO;


DROP PROCEDURE IF EXISTS SP_REGISTRAR_PROMOCION;
DROP PROCEDURE IF EXISTS SP_EDITAR_PROMOCION;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PROMOCION;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_PROMOCION;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPO_RECLAMO;
DROP PROCEDURE IF EXISTS SP_INSERTAR_RECLAMO;
DROP PROCEDURE IF EXISTS SP_MODIFICAR_RECLAMO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_RECLAMO;

-- Eliminar tablas si existen
DROP TABLE IF EXISTS conf_general;
DROP TABLE IF EXISTS reclamo;
DROP TABLE IF EXISTS tipo_reclamo;
DROP TABLE IF EXISTS detalle_personal;
DROP TABLE IF EXISTS detalle_pasaje;
DROP TABLE IF EXISTS pasaje;
DROP TABLE IF EXISTS detalle_viaje_asiento;
DROP TABLE IF EXISTS detalle_viaje;
DROP TABLE IF EXISTS pasajero;
DROP TABLE IF EXISTS viaje;
DROP TABLE IF EXISTS venta;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS tipo_cliente;
DROP TABLE IF EXISTS estado_viaje;
DROP TABLE IF EXISTS personal_incidencia;
DROP TABLE IF EXISTS incidencia;
DROP TABLE IF EXISTS servicio_microservicio;
DROP TABLE IF EXISTS microservicio;
DROP TABLE IF EXISTS escala;
DROP TABLE IF EXISTS conf_plantillas;
DROP TABLE IF EXISTS conf_dclaims;
DROP TABLE IF EXISTS conf_dmenus;
DROP TABLE IF EXISTS conf_claims;
DROP TABLE IF EXISTS conf_menus;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS tipo_usuario;
DROP TABLE IF EXISTS sucursal;
DROP TABLE IF EXISTS horario;
DROP TABLE IF EXISTS asiento;
DROP TABLE IF EXISTS ubigeo;
DROP TABLE IF EXISTS metodo_pago;
DROP TABLE IF EXISTS personal;
DROP TABLE IF EXISTS nivel_herramienta;
DROP TABLE IF EXISTS nivel;
DROP TABLE IF EXISTS vehiculo;
DROP TABLE IF EXISTS tipo_vehiculo;
DROP TABLE IF EXISTS servicio;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS ruta;
DROP TABLE IF EXISTS ciudad;
DROP TABLE IF EXISTS pais;
DROP TABLE IF EXISTS herramienta;
DROP TABLE IF EXISTS tipo_herramienta;
DROP TABLE IF EXISTS tipo_metodoPago;
DROP TABLE IF EXISTS terminos_condiciones;
DROP TABLE IF EXISTS preguntas_frecuentes;
DROP TABLE IF EXISTS promocion;
DROP TABLE IF EXISTS tipo_personal;
DROP TABLE IF EXISTS tipo_comprobante;
DROP TABLE IF EXISTS tipo_documento;

-- Crear tabla preguntas_frecuentes
CREATE TABLE preguntas_frecuentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta VARCHAR(255) NOT NULL,
    respuesta TEXT NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

-- Crear tabla terminos_condiciones
CREATE TABLE terminos_condiciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    archivo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(255) NOT NULL
);

-- Crear tabla pais
CREATE TABLE pais(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    name VARCHAR(255),
    iso2 VARCHAR(255),
    iso3 VARCHAR(255),
    phone_code VARCHAR(255),
    continente VARCHAR(255)
);

-- Crear tabla incidencia
CREATE TABLE incidencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (255) NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    duracion_sancion INT NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(255) NOT NULL

);

-- Crear tabla tipo_servicio
CREATE TABLE microservicio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

CREATE TABLE servicio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    imagen TEXT
);

CREATE TABLE servicio_microservicio (
    idServicio INT NOT NULL,
    idMicroservicio INT NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null,
    FOREIGN KEY (idServicio) REFERENCES servicio (id),
    FOREIGN KEY (idMicroservicio) REFERENCES microservicio (id),
    PRIMARY KEY (idServicio, idMicroservicio)
);

-- Crear tabla tipo_comprobante
CREATE TABLE tipo_comprobante (
    idTipoComprobante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
    );
    CREATE TABLE tipo_herramienta(
    id int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario varchar(100)
);

-- Crear tabla ubigeo
create table ubigeo(
    ubigeo char(6) PRIMARY KEY,
    departamento varchar(50) NOT NULL,
    provincia varchar(50) NOT NULL,
    distrito varchar(50) NOT NULL
);

-- Crear tabla tipo_personal
CREATE TABLE tipo_personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

CREATE TABLE tipo_documento(
    id int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    abreviatura varchar(10) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla tipo_cliente
CREATE TABLE tipo_cliente (
    idTipoCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla tipo_usuario
CREATE TABLE tipo_usuario (
    id int AUTO_INCREMENT PRIMARY key,
    nombre varchar(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    id_tipousuario INT NOT NULL,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null,
    FOREIGN KEY (id_tipousuario) REFERENCES tipo_usuario(id)
);

CREATE TABLE ciudad(
    id int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    abreviatura CHAR(3) NOT NULL
);

CREATE TABLE horario (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    horario_entrada time NOT NULL,
    horario_salida time NOT NULL,
    estado char(1) NOT NULL,
    fecha_registro datetime NOT NULL DEFAULT current_timestamp()
);

-- Crear tabla sucursal
CREATE TABLE sucursal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_sucursal CHAR(6) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    latitud DECIMAL(8,6) NOT NULL,
    longitud DECIMAL(9,6) NOT NULL,
    estado TINYINT NOT NULL DEFAULT 1,
    abreviatura CHAR(3) NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

-- Crear tabla ruta
CREATE TABLE ruta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    distancia_estimada DECIMAL(9,2),
    tiempo_estimado DECIMAL(9,2),
    tipo VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

-- Crear tabla escala
CREATE TABLE escala (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nro_orden INT NOT NULL,
    idSucursal INT NOT NULL,
    idRuta INT NOT NULL,
    distancia_estimada DECIMAL(9,2),
    tiempo_estimado DECIMAL(9,2),
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idSucursal) REFERENCES sucursal (id),
    FOREIGN KEY (idRuta) REFERENCES ruta (id)
);

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_documento VARCHAR(11), -- Se recomienda especificar una longitud
    nombre VARCHAR(255),
    ape_paterno VARCHAR(50),
    ape_materno VARCHAR(50),
    razon_social VARCHAR(255), -- Para clientes jurídicos
    sexo BOOLEAN,
    f_nacimiento DATE,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(255),
    password VARCHAR(255),
    estado BOOLEAN,
    id_pais INT,
    id_tipo_cliente INT,
    id_tipo_doc INT,
    fechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NULL,
    -- Claves foráneas
    CONSTRAINT fk_pais FOREIGN KEY (id_pais) REFERENCES PAIS(id),
    CONSTRAINT fk_tipo_cliente FOREIGN KEY (id_tipo_cliente) REFERENCES TIPO_CLIENTE(idTipoCliente),
    CONSTRAINT fk_tipo_doc FOREIGN KEY (id_tipo_doc) REFERENCES TIPO_DOCUMENTO(id)
);

-- Crear tabla conf_general
CREATE TABLE conf_general (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarifaBase DECIMAL(9,2) NOT NULL,
    igv DECIMAL(9,2) NOT NULL,
    max_pasajes_venta INT NOT NULL,
    viajesReprogramables BOOLEAN NOT NULL
);

-- Crear tabla menus
CREATE TABLE conf_menus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    idPadre INT NULL,
    FOREIGN KEY (idPadre) REFERENCES conf_menus(id)
);

-- Crear tabla detalle_menu
CREATE TABLE conf_dmenus (
    idMenu INT,
    idTipoUsuario INT,
    PRIMARY KEY (idMenu, idTipoUsuario),
    FOREIGN KEY (idMenu) REFERENCES conf_menus (id),
    FOREIGN KEY (idTipoUsuario) REFERENCES tipo_usuario (id)
);

-- Crear tabla claims
CREATE TABLE conf_claims (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    idPadre INT NULL,
    FOREIGN KEY (idPadre) REFERENCES conf_menus(id)
);

-- Crear tabla detalle_claim
CREATE TABLE conf_dclaims (
    idClaim INT,
    idTipoUsuario INT,
    PRIMARY KEY (idClaim, idTipoUsuario),
    FOREIGN KEY (idClaim) REFERENCES conf_claims (id),
    FOREIGN KEY (idTipoUsuario) REFERENCES tipo_usuario (id)
);

-- Crear tabla conf_plantillas
CREATE TABLE conf_plantillas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    color_header VARCHAR(255) NOT NULL,
    color_footer VARCHAR(255) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

CREATE TABLE tipo_vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    id_marca INT NULL,
    id_servicio INT NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    CONSTRAINT fk_tipo_vehiculo_marca FOREIGN KEY (id_marca) REFERENCES marca(id),
    FOREIGN KEY (id_servicio) REFERENCES servicio(id)
);

CREATE TABLE vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10),
    anio INT,
    color VARCHAR(30),
    estado BOOLEAN NOT NULL,
    id_tipo_vehiculo INT NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_tipo_vehiculo)
    REFERENCES tipo_vehiculo(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE nivel(
    id int AUTO_INCREMENT primary key,
    nroPiso int not null,
    id_tipo_vehiculo int not null,
    x_dimension int not null,
    y_dimension int not null,
    precio DECIMAL(10,2) not null,
    estado BOOLEAN not null,
    foreign key (id_tipo_vehiculo) references tipo_vehiculo(id)
);
-- Crear tabla tipo metodo pago
CREATE TABLE tipo_metodoPago (
    idTipoMetodoPago INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla metodo_pago
CREATE TABLE metodo_pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    id_tipo_metodoPago INT NOT NULL,
    qr VARCHAR(255) NULL,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null,
    foreign key (id_tipo_metodoPago) references tipo_metodoPago(idTipoMetodoPago) -- Relación con tipo_metodoPago
);

-- Crear tabla personal

CREATE TABLE personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    id_tipopersonal INT NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_tipopersonal) REFERENCES tipo_personal(id) -- Relación con tipo_personal
);

-- Crear tabla personal_incidencia
CREATE TABLE personal_incidencia (
    personalid INT NOT NULL,
    incidenciaid INT NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha_fin DATETIME NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(255) NOT NULL,
    PRIMARY KEY (personalid, incidenciaid),
    FOREIGN KEY (personalid) REFERENCES personal(id),
    FOREIGN KEY (incidenciaid) REFERENCES incidencia(id)
);

CREATE TABLE herramienta(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(60),
    icono varchar(200),
    id_tipo INT NOT NULL,
    FOREIGN KEY (id_tipo) REFERENCES tipo_herramienta(id)
);

CREATE TABLE nivel_herramienta(
        id int AUTO_INCREMENT PRIMARY KEY,
        id_herramienta int NOT NULL,
        id_nivel int NOT NULL,
        x_dimension int not null,
        y_dimension int not null,
        FOREIGN KEY (id_nivel) REFERENCES nivel(id),
        FOREIGN KEY (id_herramienta) REFERENCES herramienta(id)
    );

CREATE TABLE estado_viaje (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR (100) NOT NULL  
    );

CREATE TABLE viaje (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idRuta INT NOT NULL,
    idVehiculo INT NOT NULL,
    estado BOOLEAN NOT NULL, -- 1: vigente, 0: no vigente
    idEstadoViaje INT NOT NULL,
    esReprogramado BOOLEAN DEFAULT 0,
    fechaHoraSalida DATETIME NOT NULL,
    fechaHoraLlegada DATETIME NOT NULL,
    -- Auditoría
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES vehiculo(id),
    FOREIGN KEY (idRuta) REFERENCES ruta(id),
    FOREIGN KEY (idEstadoViaje) REFERENCES estado_viaje(id)
);

CREATE TABLE pasajero(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ape_paterno VARCHAR(100) NOT NULL,
    ape_materno VARCHAR(100) NOT NULL,
    idTipoDocumento INT NOT NULL,
    numero_documento VARCHAR(12) NOT NULL, -- Se recomienda especificar una longitud
    sexo TINYINT NOT NULL, -- 1: masculino, 0: femenino
    f_nacimiento DATE NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idTipoDocumento) REFERENCES tipo_documento(id)
);
CREATE TABLE detalle_viaje (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idViaje INT NOT NULL,
    idSucursalOrigen INT NOT NULL,
    idSucursalDestino INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    fechaSalida DATETIME NOT NULL,
    fechaSalidaReal DATETIME NULL,
    fechaLlegadaEstimada DATETIME NOT NULL,
    fechaLlegadaReal DATETIME NULL,
    -- Auditoría
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idViaje) REFERENCES viaje(id)
);
CREATE TABLE asiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(5) NOT NULL,
    id_vehiculo INT NOT NULL,
    id_nivel_herramienta INT NOT NULL,
    estado TINYINT NOT NULL CHECK (estado IN (0, 1, 2, 3)),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id),
    FOREIGN KEY (id_nivel_herramienta) REFERENCES nivel_herramienta(id)
);
CREATE TABLE detalle_viaje_asiento(
    id INT AUTO_INCREMENT PRIMARY KEY,
    idDetalle_Viaje INT NOT NULL ,
    idAsiento INT NULL, -- Puede ser NULL si el viaje es libre
    esDisponible BOOLEAN NOT NULL DEFAULT 1, -- 1: disponible, 0: no disponible
    -- Auditoría
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idDetalle_Viaje) REFERENCES detalle_viaje(id),
    FOREIGN KEY (idAsiento) REFERENCES asiento(id)
);
CREATE TABLE detalle_personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idPersonal INT NOT NULL,
    idTipoPersonal INT NOT NULL,
    idViaje INT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idPersonal) REFERENCES personal(id),
    FOREIGN KEY (idViaje) REFERENCES viaje(id)
);
CREATE TABLE promocion (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre varchar(100) NOT NULL, 
    estado TINYINT NOT NULL, 
    fecha_inicio date NOT NULL, 
    fecha_fin date NOT NULL, 
    codigo char(8) NOT NULL, 
    monto_promo DECIMAL(9, 2) NOT NULL
);
CREATE TABLE venta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    subTotal DECIMAL(10,2) NOT NULL,
    igv DECIMAL(10,2) NOT NULL,
    idPromocion INT NULL,
    idMetodoPago INT NOT NULL,
    idTipoComprobante INT NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES cliente(id),
    FOREIGN KEY (idMetodoPago) REFERENCES metodo_pago(id),
    FOREIGN KEY (idTipoComprobante) REFERENCES tipo_comprobante(idTipoComprobante),
    FOREIGN KEY (idPromocion) REFERENCES promocion(id)
);

CREATE TABLE pasaje(
    id INT AUTO_INCREMENT PRIMARY KEY,
    idDetalleViajeAsiento INT NOT NULL,
    numeroComprobante char(13) NULL, -- Ej: A001-00000001
    -- operaciones con pasaje
    esPasajeNormal TINYINT NULL DEFAULT 0, -- 1: es pasaje normal, 0: no es pasaje normal
    esPasajeLibre TINYINT NULL DEFAULT 0, -- 1: es pasaje libre, 0: no es pasaje libre
    esTransferencia TINYINT NULL DEFAULT 0, -- 1: es transferencia, 0: no es transferencia
    esReserva TINYINT NULL DEFAULT 0, -- 1: es pasaje reserva, 0: no es pasaje reserva
    esCambioRuta TINYINT NULL DEFAULT 0, -- 1: es cambio de ruta, 0: no es cambio de ruta
    idVenta INT NOT NULL,
    codigo CHAR(8) NOT NULL, -- AA0202
    enTransaccion TINYINT NULL DEFAULT 0, -- 1: en transacción, 0: no en transacción
    idPasaje INT NULL, -- Para operaciones con pasajes
    FOREIGN KEY (idDetalleViajeAsiento) REFERENCES detalle_viaje_asiento(id),
    FOREIGN KEY (idVenta) REFERENCES venta(id)
);

CREATE TABLE detalle_pasaje (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idPasajero INT NOT NULL,
    idPasaje INT NOT NULL,
    esMenorEdad TINYINT NOT NULL, -- 1: es menor de edad, 0: no es menor de edad
    viajeEnBrazos TINYINT NOT NULL, -- 1: viaja en brazos, 0: no viaja en brazo
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idPasajero) REFERENCES pasajero(id),
    FOREIGN KEY (idPasaje) REFERENCES pasaje(id)
);

CREATE TABLE tipo_reclamo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estado TINYINT NOT NULL
);

CREATE TABLE reclamo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo_reclamo INT NOT NULL,
    detalle TEXT NOT NULL,
    monto NUMERIC(9,2),
    idPasaje INT NOT NULL,
    motivo TEXT NOT NULL,
    estado TINYINT NOT NULL,
    FOREIGN KEY (idPasaje) REFERENCES pasaje (id),
    FOREIGN KEY (id_tipo_reclamo) REFERENCES tipo_reclamo (id)
);

INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Qué medios de pago
aceptan para comprar pasajes en línea?','Aceptamos tarjetas de crédito y débito Visa, así como billeteras digitales como
Yape y Plin.','1','2025-06-07 11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Puedo comprar pasajes
para cualquier destino?','No. Solo se pueden comprar pasajes para los destinos que aparecen disponibles en la
programación','1','2025-06-07 11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Puedo transferir mi
pasaje a otra persona?','Sí. Puedes solicitar la transferencia de tu pasaje hasta 4 horas antes del viaje, con un costo
adicional de S/ 10.00. El trámite debe ser realizado por el titular del pasaje.','1','2025-06-07
11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿La empresa realiza
reembolsos?','Solo se realiza reembolso si la empresa no cumple con brindar el servicio. No se hace reembolso si el
pasajero no se presenta o no aborda el bus a tiempo.','1','2025-06-07 11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Puedo cambiar la ruta
de mi pasaje?','Sí. El cambio de ruta debe solicitarse con al menos 6 horas de anticipación y está sujeto a
disponibilidad. Si la nueva ruta cuesta más, deberás pagar la diferencia. Si cuesta menos, no se hace
reembolso.','1','2025-06-07 11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Qué sucede si no llego
a tiempo para mi viaje?','El pasajero debe presentarse al embarque 30 minutos antes de la salida. Si no llega a tiempo,
pierde el pasaje sin derecho a reclamo ni reembolso.','1','2025-06-07 11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Qué documentos debo
presentar para abordar el bus?','Es obligatorio presentar el DNI físico del pasajero. En el caso de menores de edad,
también se debe presentar una carta notarial de autorización de viaje y el DNI o partida original.','1','2025-06-07
11:34:18','ander@gmail.com');
INSERT INTO preguntas_frecuentes (pregunta, respuesta, estado, fecha_registro, usuario) VALUES ('¿Qué es un pasaje libre
y cómo funciona?','Es un pasaje que puede ser activado en otra fecha dentro de los 90 días posteriores a la compra,
sujeto a disponibilidad. Puedes convertir tu pasaje normal a pasaje libre hasta 6 horas antes del viaje pagando S/
5.00.','1','2025-06-07 11:34:18','ander@gmail.com');

INSERT INTO sucursal (`cod_sucursal`, `ciudad`, `nombre`, `direccion`, `latitud`, `longitud`, `estado`, `abreviatura`,
`fecha_registro`, `usuario`)
VALUES ('CIX-01', 'Chiclayo', 'BALTA', 'Emtrafesa, 110, Avenida José Balta, Urbanizacion Santa Victoria, Chiclayo,
Lambayeque, 14001, Perú', '-6.776610', '-79.838656', '1', 'CIX', '2025-06-02 11:34:18', 'edgar@gmail.com'),
('CIX-02', 'Chiclayo', 'CHAVEZ', 'Calle Francisco de Orellana, Chiclayo, Lambayeque, 14001, Perú', '-6.764886',
'-79.830315', '1', 'CIX', '2025-06-02 11:37:36', 'edgar@gmail.com'),
('CIX-03', 'Chiclayo', 'CATOLICA', 'Universidad Católica Santo Toribio de Mogrovejo, Panamericana Norte, Ciudad El
Chofer, Chiclayo, Lambayeque, 14013, Perú', '-6.759932', '-79.862134', '1', 'CIX', '2025-06-02 11:39:17',
'edgar@gmail.com'),
('IMA-01', 'Lima', 'PLAZA NORTE', 'Plaza Norte, 1400, Avenida Tomás Valle, Urbanización Mesa Redonda, Independencia,
Lima, Lima Metropolitana, Lima, 15028, Perú', '-12.006144', '-77.058837', '1', 'IMA', '2025-06-02 11:39:59',
'edgar@gmail.com'),
('IMA-02', 'Lima', 'PLAZA SAN MIGUEL', 'Plaza San Miguel, 2000, Avenida La Marina, Virgen de Fatima, San Miguel, Lima,
Lima Metropolitana, Lima, 15088, Perú', '-12.076740', '-77.082720', '1', 'IMA', '2025-06-02 11:40:35',
'edgar@gmail.com'),
('CJA-01', 'Cajamarca', 'CUMBE', 'El Cumbe, Avenida San Martín de Porres, Urbanización Ramon Castilla, Mollepampa,
Cajamarca, 06002, Perú', '-7.164035', '-78.510006', '1', 'CJA', '2025-06-02 11:42:04', 'edgar@gmail.com'),
('HUA-01', 'Huamanga', 'SAN JUAN BAUTISTA', 'Terminal San Juan Bautista, Avenida Venezuela, Asociación La Victoria, San
Juan Bautista, Huamanga, Ayacucho, 05002, Perú', '-13.170961', '-74.214658', '1', 'HUA', '2025-06-02 11:43:48',
'edgar@gmail.com'),
('AQP-01', 'Arequipa', 'FLORES HERMANOS', 'Avenida Pedro P. Diaz, Urbanización Campiña, Arequipa, 04002, Perú',
'-16.422245', '-71.543607', '1', 'AQP', '2025-06-02 11:45:18', 'edgar@gmail.com'),
('PUN-01', 'Puno', 'EL SOL', 'Avenida El Sol, Laykakota, Puno, 05151, Perú', '-15.849338', '-70.018838', '1', 'PUN',
'2025-06-02 11:46:46', 'edgar@gmail.com'),
('COR-01', 'Coronel Portillo', 'GUSBET', 'Gran Hotel Gusbet, Tupac Amaru, Area Metropolitana de Pucallpa, Las Palmeras,
Yarinacocha, Coronel Portillo, Ucayali, 25004, Perú', '-8.360615', '-74.579561', '1', 'COR','2025-06-02 11:50:16',
'edgar@gmail.com'),
('HUU-01', 'Huánuco', 'PLAZA REY', 'Rey Tours, 1215, Jirón 28 de Julio, Huánuco, 10003, Perú', '-9.927278',
'-76.237774', '1', 'HUU', '2025-06-02 11:51:14', 'edgar@gmail.com');

INSERT INTO ruta (`id`,`nombre`, `distancia_estimada`, `tiempo_estimado`, `tipo`, `estado`, `fecha_registro`, `usuario`)
VALUES (1,'COSTA COMPLETA IDA', '1766.48', '1477.55', 'ESCALA', '1', '2025-06-02 12:02:38', 'edgar@gmail.com'),
(2,'COSTA COMPLETA VUELTA', '1767.03', '1506.97', 'ESCALA', '1', '2025-06-02 12:04:19', 'edgar@gmail.com'),
(3,'SIERRA COMPLETA IDA', '2595.83', '2366.86', 'ESCALA', '1', '2025-06-02 12:05:35', 'edgar@gmail.com'),
(4,'SIERRA COMPLETA VUELTA', '2595.10', '2371.92', 'ESCALA', '1', '2025-06-02 12:06:08', 'edgar@gmail.com'),
(5,'COSTA NORTE IDA', '763.92', '685.04', 'DIRECTO', '1', '2025-06-02 12:08:42', 'edgar@gmail.com'),
(6,'COSTA NORTE VUELTA', '765.10', '713.35', 'DIRECTO', '1', '2025-06-02 12:08:56', 'edgar@gmail.com'),
(7,'COSTA SUR IDA', '1002.56', '792.50', 'DIRECTO', '1', '2025-06-02 12:09:18', 'edgar@gmail.com'),
(8,'COSTA SUR VUELTA', '1001.93', '793.63', 'DIRECTO', '1', '2025-06-02 12:09:40', 'edgar@gmail.com');

INSERT INTO `escala` (`nro_orden`, `idSucursal`, `idRuta`, `distancia_estimada`, `tiempo_estimado`, `fecha_registro`,
`usuario`)
VALUES ('1', '2', '1', '0.00', '0.00', '2025-06-10 19:28:47', 'edgar@gmail.com'),
('2', '5', '1', '763.92', '685.04', '2025-06-10 19:28:47', 'edgar@gmail.com'),
('3', '8', '1', '1002.56', '792.51', '2025-06-10 19:28:47', 'edgar@gmail.com'),
('1', '8', '2', '0.00', '0.00', '2025-06-10 19:29:54', 'edgar@gmail.com'),
('2', '5', '2', '1001.93', '793.63', '2025-06-10 19:29:54', 'edgar@gmail.com'),
('3', '2', '2', '765.10', '713.35', '2025-06-10 19:29:54', 'edgar@gmail.com'),
('1', '6', '3', '0.00', '0.00', '2025-06-10 19:30:28', 'edgar@gmail.com'),
('2', '11', '3', '956.70', '814.19', '2025-06-10 19:30:28', 'edgar@gmail.com'),
('3', '7', '3', '654.96', '609.86', '2025-06-10 19:30:28', 'edgar@gmail.com'),
('1', '7', '4', '0.00', '0.00', '2025-06-10 19:30:40', 'edgar@gmail.com'),
('2', '11', '4', '654.29', '608.78', '2025-06-10 19:30:40', 'edgar@gmail.com'),
('3', '6', '4', '956.94', '830.52', '2025-06-10 19:30:40', 'edgar@gmail.com'),
('1', '2', '5', '0.00', '0.00', '2025-06-10 19:30:48', 'edgar@gmail.com'),
('2', '6', '5', '264.05', '213.81', '2025-06-10 19:30:48', 'edgar@gmail.com'),
('1', '6', '6', '0.00', '0.00', '2025-06-10 19:30:57', 'edgar@gmail.com'),
('2', '2', '6', '263.84', '213.50', '2025-06-10 19:30:57', 'edgar@gmail.com'),
('1', '5', '7', '0.00', '0.00', '2025-06-10 19:31:10', 'edgar@gmail.com'),
('2', '8', '7', '1002.56', '792.51', '2025-06-10 19:31:10', 'edgar@gmail.com'),
('1', '8', '8', '0.00', '0.00', '2025-06-10 19:32:46', 'edgar@gmail.com'),
('2', '5', '8', '1001.93', '793.63', '2025-06-10 19:32:46', 'edgar@gmail.com');


-- INSERTS terminos y condicones
INSERT INTO terminos_condiciones(id, nombre, archivo, estado, fecha_registro, usuario) VALUES
(1,'TyC-v2025-001','TyC_v2025-001.txt',1,'2025-05-29 01:51:30','ander@gmail.com');
INSERT INTO terminos_condiciones(id, nombre, archivo, estado, fecha_registro, usuario) VALUES (2,'Versión
guía','versionPreliminar.txt',0,'2025-05-29 01:51:30','ander@gmail.com');

-- INSERTS estado_viaje
INSERT INTO estado_viaje (id, nombre) VALUES (1, 'PENDIENTE');
INSERT INTO estado_viaje (id, nombre) VALUES (2, 'EN CURSO');
INSERT INTO estado_viaje (id, nombre) VALUES (3, 'FINALIZADO');

-- INSERTS tipo_personal
INSERT INTO tipo_personal (id, nombre, estado, usuario) VALUES (1, 'CHOFER', 1, 'SYSTEM');
INSERT INTO tipo_personal (id, nombre, estado, usuario) VALUES (2, 'TRIPULANTE', 1, 'SYSTEM');

-- INSERTS personal
INSERT INTO personal (id, nombre, imagen, estado, id_tipopersonal) VALUES (1, 'Louis Requejo Chirinos',
"/Static/img/trabajadores/default-user.png", 1, 1);
INSERT INTO personal (id, nombre, imagen, estado, id_tipopersonal) VALUES (2, 'Anderson Baca Chuquimanco',
"/Static/img/trabajadores/default-user.png", 1, 1);
INSERT INTO personal (id, nombre, imagen, estado, id_tipopersonal) VALUES (3, 'Edgar Alarcón Chapoñan',
"/Static/img/trabajadores/default-user.png", 1, 2);
INSERT INTO personal (id, nombre, imagen, estado, id_tipopersonal) VALUES (4, 'Luis Cruz Chinchay',
"/Static/img/trabajadores/default-user.png", 1, 2);

-- INSERT TIPO CLIENTE
INSERT INTO tipo_cliente (nombre, estado, usuario)
VALUES
('Bebé', TRUE, 'admin'),
('Niño', TRUE, 'admin'),
('Adulto', TRUE, 'admin'),
('Empresa', TRUE, 'admin');

-- INSERT TIPO DOCUMENTO
INSERT INTO tipo_documento (nombre, abreviatura, estado, usuario)
VALUES ('DOCUMENTO NACIONAL DE IDENTIFICACION', 'DNI', TRUE, 'admin');
INSERT INTO tipo_documento (nombre, abreviatura, estado, usuario)
VALUES ('REGISTRO UNICO DE CONTRIBUYENTE', 'RUC', TRUE, 'admin');
INSERT INTO tipo_documento (nombre, abreviatura, estado, usuario)
VALUES ('CARNET DE EXTRANJERIA', 'CE', TRUE, 'admin');

-- INSERT SERVICIO
insert into servicio values (1,'Premium','Los autobuses más modernos y lujosos del mercado. Asientos cama,
entretenimiento a bordo, snacks incluidos, aire acondicionado y cargadores USB. Ideal para viajes de largo
trayecto.',1,'2025-05-25 19:30:00','Alexis','/Static/img/servicios/busPremium.png');
insert into servicio values (2,'Económico','Autobuses cómodos y seguros a precios accesibles. Pensado para usuarios que
priorizan economía sin perder calidad.',1,'2025-05-25 19:32:00','Alexis','/Static/img/servicios/busEconomico.png');
insert into servicio values (3,'Exprés','Servicios rápidos con pocas paradas. Unidades modernas y seguras para viajeros
que buscan llegar en el menor tiempo posible.',1,'2025-05-25 19:40:00','Alexis','/Static/img/servicios/busExpress.png');

-- INSERT MARCA

INSERT INTO `marca` (`id`,`nombre`, `logo`, `estado`, `fecha_registro`, `usuario`)
VALUES (1,'Mercedes-Benz', '/Static/img/marca/MercedesBenz.png', '1', '2025-05-26 11:40:29', 'edgar@gmail.com'),
(2,'Dodge', '/Static/img/marca/Dodge.png', '1', '2025-05-26 11:40:50', 'edgar@gmail.com'),
(3,'Volkswagen','/Static/img/marca/Volkswagen.png', '1', '2025-05-26 11:41:09', 'edgar@gmail.com'),
(4,'Hyundai','/Static/img/marca/Hyundai.png', '1', '2025-05-26 11:41:28', 'edgar@gmail.com');

-- INSERT TIPO_VEHICULO
INSERT INTO `tipo_vehiculo` (`id`, `nombre`, `id_marca`, `id_servicio`, `estado`, `fecha_registro`, `usuario`)
VALUES (1, 'Solati H350', '4', '1', '1', '2025-05-26 11:57:29', 'edgar@gmail.com'),
(2, 'County bus', '4', '1', '1', '2025-05-26 11:58:51', 'edgar@gmail.com'),
(3, 'Volksbus', '3', '2', '1', '2025-05-26 12:01:43', 'edgar@gmail.com'),
(4, 'eCitaro fuel cell', '1', '1', '1', '2025-05-26 12:04:08', 'edgar@gmail.com'),
(5, 'eCitaro', '1', '2', '1', '2025-05-26 12:04:42', 'edgar@gmail.com'),
(6, 'Citaro', '1', '2', '1', '2025-05-26 12:05:05', 'edgar@gmail.com'),
(7, 'Citaro U', '1', '3', '1', '2025-05-26 12:05:38', 'edgar@gmail.com'),
(8, 'Intouro', '1', '3', '1', '2025-05-26 12:05:50', 'edgar@gmail.com'),
(9, 'Tourismo', '1', '3', '1', '2025-05-26 12:08:52', 'edgar@gmail.com');

-- INSERT TIPO_HERRAMIENTA

INSERT INTO tipo_herramienta (id, nombre) VALUES (1, 'Asientos');
INSERT INTO tipo_herramienta (id, nombre) VALUES (2, 'Acceso');
INSERT INTO tipo_herramienta (id, nombre) VALUES (3, 'Seguridad');
INSERT INTO tipo_herramienta (id, nombre) VALUES (4, 'Multimedia');

-- INSERT HERRAMIENTA

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (1, 'Asiento a 140°','img/herramienta/asiento_140.png',1);
INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (2, 'Asiento a 160°','img/herramienta/asiento_160.png',1);
INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (3, 'Asiento cama','img/herramienta/asiento_180.png',1);

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (4, 'Televisor','img/herramienta/tv.png',4);

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (5, 'Baño','img/herramienta/toilet.png',3);
INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (6, 'Extintor','img/herramienta/extintor.png',3);

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (7, 'Puerta','img/herramienta/puerta.png',2);

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (8, 'Subida','img/herramienta/escalera_hacia_arriba.png',2);

INSERT INTO herramienta (id, nombre, icono,id_tipo) VALUES (9, 'Bajada','img/herramienta/escalera_hacia_abajo.png',2);

-- INSERTS PAIS
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(1,'Afganistán','Afghanistan','AF','AFG','93','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(2,'Albania','Albania','AL','ALB','355','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(3,'Alemania','Germany','DE','DEU','49','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(4,'Algeria','Algeria','DZ','DZA','213','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(5,'Andorra','Andorra','AD','AND','376','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(6,'Angola','Angola','AO','AGO','244','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (7,'Anguila','Anguilla','AI','AIA','1
264','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(8,'Antártida','Antarctica','AQ','ATA','672','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (9,'Antigua y Barbuda','Antigua and
Barbuda','AG','ATG','1 268','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (10,'Antillas Neerlandesas','Netherlands
Antilles','AN','ANT','599','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (11,'Arabia Saudita','Saudi
Arabia','SA','SAU','966','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(12,'Argentina','Argentina','AR','ARG','54','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(13,'Armenia','Armenia','AM','ARM','374','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(14,'Aruba','Aruba','AW','ABW','297','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(15,'Australia','Australia','AU','AUS','61','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(16,'Austria','Austria','AT','AUT','43','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(17,'Azerbayán','Azerbaijan','AZ','AZE','994','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(18,'Bélgica','Belgium','BE','BEL','32','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (19,'Bahamas','Bahamas','BS','BHS','1
242','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(20,'Bahrein','Bahrain','BH','BHR','973','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(21,'Bangladesh','Bangladesh','BD','BGD','880','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (22,'Barbados','Barbados','BB','BRB','1
246','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(23,'Belice','Belize','BZ','BLZ','501','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(24,'Benín','Benin','BJ','BEN','229','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(25,'Bhután','Bhutan','BT','BTN','975','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(26,'Bielorrusia','Belarus','BY','BLR','375','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(27,'Birmania','Myanmar','MM','MMR','95','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(28,'Bolivia','Bolivia','BO','BOL','591','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (29,'Bosnia y Herzegovina','Bosnia and
Herzegovina','BA','BIH','387','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(30,'Botsuana','Botswana','BW','BWA','267','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(31,'Brasil','Brazil','BR','BRA','55','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(32,'Brunéi','Brunei','BN','BRN','673','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(33,'Bulgaria','Bulgaria','BG','BGR','359','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (34,'Burkina Faso','Burkina
Faso','BF','BFA','226','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(35,'Burundi','Burundi','BI','BDI','257','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (36,'Cabo Verde','Cape
Verde','CV','CPV','238','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(37,'Camboya','Cambodia','KH','KHM','855','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(38,'Camerún','Cameroon','CM','CMR','237','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(39,'Canadá','Canada','CA','CAN','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(40,'Chad','Chad','TD','TCD','235','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(41,'Chile','Chile','CL','CHL','56','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(42,'China','China','CN','CHN','86','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(43,'Chipre','Cyprus','CY','CYP','357','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (44,'Ciudad del Vaticano','Vatican City
State','VA','VAT','39','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(45,'Colombia','Colombia','CO','COL','57','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(46,'Comoras','Comoros','KM','COM','269','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(47,'Congo','Congo','CG','COG','242','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(48,'Congo','Congo','CD','COD','243','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (49,'Corea del Norte','North
Korea','KP','PRK','850','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (50,'Corea del Sur','South
Korea','KR','KOR','82','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (51,'Costa de Marfil','Ivory
Coast','CI','CIV','225','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (52,'Costa Rica','Costa
Rica','CR','CRI','506','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(53,'Croacia','Croatia','HR','HRV','385','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(54,'Cuba','Cuba','CU','CUB','53','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(55,'Dinamarca','Denmark','DK','DNK','45','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (56,'Dominica','Dominica','DM','DMA','1
767','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(57,'Ecuador','Ecuador','EC','ECU','593','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(58,'Egipto','Egypt','EG','EGY','20','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (59,'El Salvador','El
Salvador','SV','SLV','503','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (60,'Emiratos Árabes Unidos','United Arab
Emirates','AE','ARE','971','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(61,'Eritrea','Eritrea','ER','ERI','291','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(62,'Eslovaquia','Slovakia','SK','SVK','421','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(63,'Eslovenia','Slovenia','SI','SVN','386','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(64,'España','Spain','ES','ESP','34','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (65,'Estados Unidos de América','United
States of America','US','USA','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(66,'Estonia','Estonia','EE','EST','372','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(67,'Etiopía','Ethiopia','ET','ETH','251','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(68,'Filipinas','Philippines','PH','PHL','63','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(69,'Finlandia','Finland','FI','FIN','358','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(70,'Fiyi','Fiji','FJ','FJI','679','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(71,'Francia','France','FR','FRA','33','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(72,'Gabón','Gabon','GA','GAB','241','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(73,'Gambia','Gambia','GM','GMB','220','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(74,'Georgia','Georgia','GE','GEO','995','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(75,'Ghana','Ghana','GH','GHA','233','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(76,'Gibraltar','Gibraltar','GI','GIB','350','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (77,'Granada','Grenada','GD','GRD','1
473','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(78,'Grecia','Greece','GR','GRC','30','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(79,'Groenlandia','Greenland','GL','GRL','299','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(80,'Guadalupe','Guadeloupe','GP','GLP','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (81,'Guam','Guam','GU','GUM','1
671','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(82,'Guatemala','Guatemala','GT','GTM','502','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (83,'Guayana Francesa','French
Guiana','GF','GUF','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(84,'Guernsey','Guernsey','GG','GGY','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(85,'Guinea','Guinea','GN','GIN','224','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (86,'Guinea Ecuatorial','Equatorial
Guinea','GQ','GNQ','240','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(87,'Guinea-Bissau','Guinea-Bissau','GW','GNB','245','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(88,'Guyana','Guyana','GY','GUY','592','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(89,'Haití','Haiti','HT','HTI','509','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(90,'Honduras','Honduras','HN','HND','504','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (91,'Hong kong','Hong
Kong','HK','HKG','852','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(92,'Hungría','Hungary','HU','HUN','36','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(93,'India','India','IN','IND','91','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(94,'Indonesia','Indonesia','ID','IDN','62','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(95,'Irán','Iran','IR','IRN','98','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(96,'Irak','Iraq','IQ','IRQ','964','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(97,'Irlanda','Ireland','IE','IRL','353','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (98,'Isla Bouvet','Bouvet
Island','BV','BVT','','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (99,'Isla de Man','Isle of
Man','IM','IMN','44','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (100,'Isla de Navidad','Christmas
Island','CX','CXR','61','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (101,'Isla Norfolk','Norfolk
Island','NF','NFK','','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(102,'Islandia','Iceland','IS','ISL','354','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (103,'Islas Bermudas','Bermuda
Islands','BM','BMU','1 441','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (104,'Islas Caimán','Cayman
Islands','KY','CYM','1 345','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (105,'Islas Cocos (Keeling)','Cocos
(Keeling) Islands','CC','CCK','61','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (106,'Islas Cook','Cook
Islands','CK','COK','682','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (107,'Islas de Åland','Åland
Islands','AX','ALA','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (108,'Islas Feroe','Faroe
Islands','FO','FRO','298','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (109,'Islas Georgias del Sur y Sandwich
del Sur','South Georgia and the South Sandwich Islands','GS','SGS','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (110,'Islas Heard y McDonald','Heard
Island and McDonald Islands','HM','HMD','','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (111,'Islas
Maldivas','Maldives','MV','MDV','960','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (112,'Islas Malvinas','Falkland Islands
(Malvinas)','FK','FLK','500','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (113,'Islas Marianas del Norte','Northern
Mariana Islands','MP','MNP','1 670','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (114,'Islas Marshall','Marshall
Islands','MH','MHL','692','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (115,'Islas Pitcairn','Pitcairn
Islands','PN','PCN','870','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (116,'Islas Salomón','Solomon
Islands','SB','SLB','677','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (117,'Islas Turcas y Caicos','Turks and
Caicos Islands','TC','TCA','1 649','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (118,'Islas Ultramarinas Menores de
Estados Unidos','United States Minor Outlying Islands','UM','UMI','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (119,'Islas Vírgenes Británicas','Virgin
Islands','VG','VG','1 284','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (120,'Islas Vírgenes de los Estados
Unidos','United States Virgin Islands','VI','VIR','1 340','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(121,'Israel','Israel','IL','ISR','972','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(122,'Italia','Italy','IT','ITA','39','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (123,'Jamaica','Jamaica','JM','JAM','1
876','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(124,'Japón','Japan','JP','JPN','81','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(125,'Jersey','Jersey','JE','JEY','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(126,'Jordania','Jordan','JO','JOR','962','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(127,'Kazajistán','Kazakhstan','KZ','KAZ','7','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(128,'Kenia','Kenya','KE','KEN','254','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(129,'Kirgizstán','Kyrgyzstan','KG','KGZ','996','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(130,'Kiribati','Kiribati','KI','KIR','686','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(131,'Kuwait','Kuwait','KW','KWT','965','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(132,'Líbano','Lebanon','LB','LBN','961','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(133,'Laos','Laos','LA','LAO','856','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(134,'Lesoto','Lesotho','LS','LSO','266','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(135,'Letonia','Latvia','LV','LVA','371','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(136,'Liberia','Liberia','LR','LBR','231','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(137,'Libia','Libya','LY','LBY','218','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(138,'Liechtenstein','Liechtenstein','LI','LIE','423','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(139,'Lituania','Lithuania','LT','LTU','370','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(140,'Luxemburgo','Luxembourg','LU','LUX','352','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(141,'México','Mexico','MX','MEX','52','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(142,'Mónaco','Monaco','MC','MCO','377','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(143,'Macao','Macao','MO','MAC','853','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(144,'Macedônia','Macedonia','MK','MKD','389','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(145,'Madagascar','Madagascar','MG','MDG','261','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(146,'Malasia','Malaysia','MY','MYS','60','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(147,'Malawi','Malawi','MW','MWI','265','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(148,'Mali','Mali','ML','MLI','223','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(149,'Malta','Malta','MT','MLT','356','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(150,'Marruecos','Morocco','MA','MAR','212','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(151,'Martinica','Martinique','MQ','MTQ','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(152,'Mauricio','Mauritius','MU','MUS','230','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(153,'Mauritania','Mauritania','MR','MRT','222','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(154,'Mayotte','Mayotte','YT','MYT','262','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (155,'Micronesia','Estados Federados
de','FM','FSM','691','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(156,'Moldavia','Moldova','MD','MDA','373','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(157,'Mongolia','Mongolia','MN','MNG','976','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(158,'Montenegro','Montenegro','ME','MNE','382','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(159,'Montserrat','Montserrat','MS','MSR','1 664','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(160,'Mozambique','Mozambique','MZ','MOZ','258','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(161,'Namibia','Namibia','NA','NAM','264','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(162,'Nauru','Nauru','NR','NRU','674','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(163,'Nepal','Nepal','NP','NPL','977','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(164,'Nicaragua','Nicaragua','NI','NIC','505','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(165,'Niger','Niger','NE','NER','227','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(166,'Nigeria','Nigeria','NG','NGA','234','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(167,'Niue','Niue','NU','NIU','683','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(168,'Noruega','Norway','NO','NOR','47','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (169,'Nueva Caledonia','New
Caledonia','NC','NCL','687','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (170,'Nueva Zelanda','New
Zealand','NZ','NZL','64','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(171,'Omán','Oman','OM','OMN','968','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (172,'Países
Bajos','Netherlands','NL','NLD','31','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(173,'Pakistán','Pakistan','PK','PAK','92','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(174,'Palau','Palau','PW','PLW','680','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(175,'Palestina','Palestine','PS','PSE','','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(176,'Panamá','Panama','PA','PAN','507','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (177,'Papúa Nueva Guinea','Papua New
Guinea','PG','PNG','675','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(178,'Paraguay','Paraguay','PY','PRY','595','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(179,'Perú','Peru','PE','PER','51','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (180,'Polinesia Francesa','French
Polynesia','PF','PYF','689','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(181,'Polonia','Poland','PL','POL','48','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(182,'Portugal','Portugal','PT','PRT','351','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (183,'Puerto Rico','Puerto
Rico','PR','PRI','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(184,'Qatar','Qatar','QA','QAT','974','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (185,'Reino Unido','United
Kingdom','GB','GBR','44','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (186,'República Centroafricana','Central
African Republic','CF','CAF','236','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (187,'República Checa','Czech
Republic','CZ','CZE','420','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (188,'República Dominicana','Dominican
Republic','DO','DOM','1 809','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(189,'Reunión','Réunion','RE','REU','','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(190,'Ruanda','Rwanda','RW','RWA','250','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(191,'Rumanía','Romania','RO','ROU','40','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(192,'Rusia','Russia','RU','RUS','7','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (193,'Sahara Occidental','Western
Sahara','EH','ESH','','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(194,'Samoa','Samoa','WS','WSM','685','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (195,'Samoa Americana','American
Samoa','AS','ASM','1 684','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (196,'San Bartolomé','Saint
Barthélemy','BL','BLM','590','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (197,'San Cristóbal y Nieves','Saint
Kitts and Nevis','KN','KNA','1 869','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (198,'San Marino','San
Marino','SM','SMR','378','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (199,'San Martín (Francia)','Saint Martin
(French part)','MF','MAF','1 599','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (200,'San Pedro y Miquelón','Saint Pierre
and Miquelon','PM','SPM','508','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (201,'San Vicente y las
Granadinas','Saint Vincent and the Grenadines','VC','VCT','1 784','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (202,'Santa Elena','Ascensión y Tristán
de Acuña','SH','SHN','290','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (203,'Santa Lucía','Saint
Lucia','LC','LCA','1 758','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (204,'Santo Tomé y Príncipe','Sao Tome
and Principe','ST','STP','239','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(205,'Senegal','Senegal','SN','SEN','221','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(206,'Serbia','Serbia','RS','SRB','381','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(207,'Seychelles','Seychelles','SC','SYC','248','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (208,'Sierra Leona','Sierra
Leone','SL','SLE','232','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(209,'Singapur','Singapore','SG','SGP','65','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(210,'Siria','Syria','SY','SYR','963','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(211,'Somalia','Somalia','SO','SOM','252','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (212,'Sri lanka','Sri
Lanka','LK','LKA','94','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (213,'Sudáfrica','South
Africa','ZA','ZAF','27','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(214,'Sudán','Sudan','SD','SDN','249','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(215,'Suecia','Sweden','SE','SWE','46','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(216,'Suiza','Switzerland','CH','CHE','41','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(217,'Surinám','Suriname','SR','SUR','597','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (218,'Svalbard y Jan Mayen','Svalbard and
Jan Mayen','SJ','SJM','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(219,'Swazilandia','Swaziland','SZ','SWZ','268','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(220,'Tadjikistán','Tajikistan','TJ','TJK','992','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(221,'Tailandia','Thailand','TH','THA','66','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(222,'Taiwán','Taiwan','TW','TWN','886','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(223,'Tanzania','Tanzania','TZ','TZA','255','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (224,'Territorio Británico del Océano
Índico','British Indian Ocean Territory','IO','IOT','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (225,'Territorios Australes y Antárticas
Franceses','French Southern Territories','TF','ATF','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (226,'Timor Oriental','East
Timor','TL','TLS','670','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(227,'Togo','Togo','TG','TGO','228','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(228,'Tokelau','Tokelau','TK','TKL','690','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(229,'Tonga','Tonga','TO','TON','676','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (230,'Trinidad y Tobago','Trinidad and
Tobago','TT','TTO','1 868','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(231,'Tunez','Tunisia','TN','TUN','216','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(232,'Turkmenistán','Turkmenistan','TM','TKM','993','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(233,'Turquía','Turkey','TR','TUR','90','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(234,'Tuvalu','Tuvalu','TV','TUV','688','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(235,'Ucrania','Ukraine','UA','UKR','380','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(236,'Uganda','Uganda','UG','UGA','256','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(237,'Uruguay','Uruguay','UY','URY','598','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(238,'Uzbekistán','Uzbekistan','UZ','UZB','998','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(239,'Vanuatu','Vanuatu','VU','VUT','678','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(240,'Venezuela','Venezuela','VE','VEN','58','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(241,'Vietnam','Vietnam','VN','VNM','84','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (242,'Wallis y Futuna','Wallis and
Futuna','WF','WLF','681','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(243,'Yemen','Yemen','YE','YEM','967','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(244,'Yibuti','Djibouti','DJ','DJI','253','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(245,'Zambia','Zambia','ZM','ZMB','260','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES
(246,'Zimbabue','Zimbabwe','ZW','ZWE','263','África');

-- INSERTS IATA CIUDAD
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Arequipa','AQP');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Callao','LIM');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Chiclayo','CIX');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Cusco','CUZ');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Iquitos','IQT');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Juliaca','JUL');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Piura','PIU');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Pucallpa','PCL');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Puerto Maldonado','PEM');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Talara','TYL');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Tacna','TCQ');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Trujillo','TRU');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Andahuaylas','ANS');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Ayacucho','AYP');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Chimbote','CHM');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Huaraz','ATA');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Chachapoyas','CHH');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Cajamarca','CJA');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Jaén','JAE');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Huánuco','HUU');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Tingo María','TGI');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Pisco','PIO');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Jauja','JAU');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Mazamari','MZA');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Yurimaguas','YMS');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Ilo','ILQ');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Tarapoto','TPP');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Punta Sal','PTL');
INSERT INTO ciudad (nombre, abreviatura) VALUES ('Tumbes','TBP');

-- Tabla Tipo Usuario
INSERT INTO tipo_usuario (id,nombre, estado, fecha_registro, usuario) VALUES (1,'ADMINISTRADOR', 1, '2025-03-06
20:02:56','SYSTEM');

-- Tabla Usuario
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,fecha_registro,usuario) VALUES
(1,'Alexis','alexis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
'/Static/img/trabajadores/alexis.jpeg', 1, 1,'2025-03-06 20:06:14','SYSTEM');
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,fecha_registro,usuario) VALUES
(2,'Edgar','edgar@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
'/Static/img/trabajadores/edgar.png', 1, 1,'2025-03-06 20:06:14','SYSTEM');
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,fecha_registro,usuario) VALUES
(3,'Ander','ander@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
'/Static/img/trabajadores/ander.jpg', 1, 1,'2025-03-06 20:06:14','SYSTEM');
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,fecha_registro,usuario) VALUES
(4,'Luis','luis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
'/Static/img/trabajadores/luis.jpg', 1, 1,'2025-03-06 20:06:14','SYSTEM');

-- Tabla de configuración general
INSERT INTO conf_general (id, igv, tarifaBase, max_pasajes_venta, viajesReprogramables) VALUES (1, 0.18, 10, 4, 0);

-- Tabla menus
INSERT INTO conf_menus (id, nombre, estado) VALUES (1, 'M_USUARIOS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (2, 'M_CONFIGURACION', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (3, 'M_VENTAS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (4, 'M_VIAJES', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (5, 'M_PERSONAL', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (6, 'M_ATENCION', 1);

-- Submenús de USUARIOS
-- Gestionar usuarios
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (10, 'Gestionar usuarios', 1, 1);
-- Claims de Gestionar usuarios (Menú 10)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (1, 'Registrar usuario', 1, 10);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (2, 'Editar usuario', 1, 10);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (3, 'Eliminar usuario', 1, 10);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (4, 'Ver usuario', 1, 10);

-- Gestionar tipos de usuarios
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (11, 'Gestionar tipos de usuarios', 1, 1);
-- Claims de Gestionar tipos de usuarios (Menú 11)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (5, 'Registrar tipo de usuario', 1, 11);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (6, 'Editar tipo de usuario', 1, 11);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (7, 'Eliminar tipo de usuario', 1, 11);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (8, 'Ver tipo de usuario', 1, 11);

-- Submenús de CONFIGURACIÓN
-- Gestionar permisos
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (20, 'Gestionar permisos', 1, 2);
-- Claims de Gestionar permisos (Menú 20)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (9, 'Editar permisos', 1, 20);

-- Gestionar plantillas
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (21, 'Gestionar plantillas', 1, 2);
-- Claims de Gestionar plantillas (Menú 21)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (10, 'Registrar plantilla', 1, 21);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (11, 'Editar plantilla', 1, 21);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (12, 'Eliminar plantilla', 1, 21);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (13, 'Ver plantilla', 1, 21);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (14, 'Activar plantilla', 1, 21);

-- Gestionar métodos de pago
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (22, 'Gestionar métodos de pago', 1, 2);
-- Claims de Gestionar métodos de pago (Menú 22)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (15, 'Registrar método de pago', 1, 22);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (16, 'Editar método de pago', 1, 22);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (17, 'Eliminar método de pago', 1, 22);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (18, 'Ver método de pago', 1, 22);

-- Submenús de VENTAS
-- Gestionar tipo de comprobante
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (30, 'Gestionar tipo comprobante', 1, 3);
-- Claims de Gestionar tipo de comprobante (Menú 30)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (19, 'Registrar tipo comprobante', 1, 30);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (20, 'Editar tipo comprobante', 1, 30);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (21, 'Eliminar tipo comprobante', 1, 30);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (22, 'Ver tipo comprobante', 1, 30);

-- Gestionar tipo de cliente
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (31, 'Gestionar tipo cliente', 1, 3);
-- Claims de Gestionar tipo cliente (Menú 31)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (23, 'Registrar tipo cliente', 1, 31);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (24, 'Editar tipo cliente', 1, 31);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (25, 'Eliminar tipo cliente', 1, 31);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (26, 'Ver tipo cliente', 1, 31);

-- Gestionar cliente
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (32, 'Gestionar cliente', 1, 3);
-- Claims de Gestionar cliente (Menú 32)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (27, 'Registrar tipo cliente', 1, 32);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (28, 'Editar tipo cliente', 1, 32);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (29, 'Eliminar tipo cliente', 1, 32);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (30, 'Ver tipo cliente', 1, 32);

-- Gestionar servicios
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (33, 'Gestionar servicio', 1, 3);
-- Claims de Gestionar servicio (Menú 34)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (31, 'Registrar servicio', 1, 33);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (32, 'Editar servicio', 1, 33);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (33, 'Eliminar servicio', 1, 33);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (34, 'Ver servicio', 1, 33);

-- Gestionar tipo de servicio
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (34, 'Gestionar microservicio', 1, 3);
-- Claims de Gestionar tipo servicio (Menú 33)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (35, 'Registrar microservicio', 1, 34);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (36, 'Editar microservicio', 1, 34);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (37, 'Eliminar microservicio', 1, 34);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (38, 'Ver microservicio', 1, 34);

-- Gestionar tipo de documento
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (35, 'Gestionar tipo documento', 1, 3);
-- Claims de Gestionar tipo documento (Menú 35)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (39, 'Registrar tipo documento', 1, 35);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (40, 'Editar tipo documento', 1, 35);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (41, 'Eliminar tipo documento', 1, 35);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (42, 'Ver tipo documento', 1, 35);

-- Submenús de VIAJES
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (40, 'Gestionar horarios', 1, 4);

-- Gestionar tipo de vehículo
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (41, 'Gestionar tipo vehículo', 1, 4);
-- Claims de Gestionar tipo vehículo (Menú 41)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (43, 'Registrar tipo vehículo', 1, 41);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (44, 'Editar tipo vehículo', 1, 41);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (45, 'Eliminar tipo vehículo', 1, 41);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (46, 'Ver tipo vehículo', 1, 41);

-- Gestionar vehículos
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (42, 'Gestionar vehículo', 1, 4);
-- Claims de Gestionar vehículo (Menú 42)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (47, 'Registrar vehículo', 1, 42);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (48, 'Editar vehículo', 1, 42);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (49, 'Eliminar vehículo', 1, 42);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (50, 'Ver vehículo', 1, 42);

-- Gestionar niveles
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (43, 'Gestionar niveles', 1, 4);
-- Claims de Gestionar niveles (Menú 43)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (51, 'Registrar niveles', 1, 43);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (52, 'Editar niveles', 1, 43);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (53, 'Eliminar niveles', 1, 43);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (54, 'Ver niveles', 1, 43);

-- Gestionar asientos
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (44, 'Gestionar asientos', 1, 4);

-- Gestionar sucursales
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (45, 'Gestionar sucursales', 1, 4);
-- Claims de Gestionar sucursales (Menú 44)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (55, 'Registrar sucursales', 1, 45);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (56, 'Editar sucursales', 1, 45);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (57, 'Eliminar sucursales', 1, 45);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (58, 'Ver sucursales', 1, 45);

-- Gestionar marcas
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (46, 'Gestionar marcas', 1, 4);
-- Claims de Gestionar marcas (Menú 45)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (59, 'Registrar marcas', 1, 46);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (60, 'Editar marcas', 1, 46);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (61, 'Eliminar marcas', 1, 46);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (62, 'Ver marcas', 1, 46);

-- Gestionar rutas
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (47, 'Gestionar rutas', 1, 4);
-- Claims de Gestionar rutas (Menú 46)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (63, 'Registrar rutas', 1, 47);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (64, 'Editar rutas', 1, 47);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (65, 'Eliminar rutas', 1, 47);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (66, 'Ver rutas', 1, 47);

-- Programar viajes
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (48, 'Programar viajes', 1, 4);

-- Submenús de PERSONAL
-- Gestionar tipo de personal
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (50, 'Gestionar tipo personal', 1, 5);
-- Claims de Gestionar tipo personal (Menú 50)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (67, 'Registrar tipo personal', 1, 50);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (68, 'Editar tipo personal', 1, 50);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (69, 'Eliminar tipo personal', 1, 50);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (70, 'Ver tipo personal', 1, 50);

INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (51, 'Gestionar personal', 1, 5);
-- Claims de Gestionar tipo personal (Menú 50)
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (71, 'Registrar personal', 1, 51);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (72, 'Editar personal', 1, 51);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (73, 'Eliminar personal', 1, 51);
INSERT INTO conf_claims(id, nombre, estado, idPadre) VALUES (74, 'Ver personal', 1, 51);

-- Submenús de ATENCIÓN AL CLIENTE
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (60, 'Ejemplo', 1, 6);

-- Tabla dmenus
-- Módulos principales
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (1, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (2, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (3, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (4, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (5, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (6, 1);
-- Submenús de "USUARIOS"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (10, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (11, 1);
-- Submenús de "CONFIGURACIÓN"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (20, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (21, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (22, 1);
-- Submenús de "VENTAS"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (30, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (31, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (32, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (33, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (34, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (35, 1);
-- Submenús de "VIAJES"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (40, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (41, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (42, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (43, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (44, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (45, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (46, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (47, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (48, 1);
-- Submenús de "PERSONAL"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (50, 1);
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (51, 1);
-- Submenús de "ATENCIÓN AL CLIENTE"
INSERT INTO conf_dmenus (idMenu, idTipoUsuario) VALUES (60, 1);

-- Todos los claims al administrador
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (1,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (2,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (3,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (4,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (5,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (6,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (7,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (8,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (9,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (10,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (11,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (12,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (13,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (14,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (15,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (16,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (17,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (18,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (19,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (20,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (21,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (22,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (23,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (24,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (25,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (26,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (27,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (28,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (29,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (30,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (31,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (32,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (33,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (34,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (35,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (36,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (37,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (38,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (39,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (40,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (41,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (42,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (43,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (44,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (45,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (46,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (47,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (48,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (49,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (50,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (51,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (52,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (53,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (54,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (55,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (56,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (57,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (58,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (59,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (60,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (61,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (62,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (63,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (64,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (65,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (66,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (67,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (68,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (69,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (70,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (71,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (72,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (73,1);
INSERT INTO conf_dclaims (idClaim, idTipoUsuario) VALUES (74,1);

-- Tabla apariencia
INSERT INTO conf_plantillas (id, nombre, color_header, color_footer, logo, estado, fecha_registro, usuario) VALUES (1,
'YATRAX', '#0c336e', '#000000', '/Static/img/plantillas/logo_yatusa.png', 1, '2025-03-06 20:06:14', 'SYSTEM');

INSERT INTO cliente (
    numero_documento, nombre, ape_paterno, ape_materno, sexo, f_nacimiento, direccion, telefono, email, password, estado,
    id_pais, id_tipo_cliente, id_tipo_doc, usuario
) VALUES
-- Clientes con RUC
('20481234567', 'EMPRESA ALPHA SAC', NULL, NULL, NULL, NULL, 'AV. PERÚ 101', '987654321', 'contacto@alpha.com', SHA2('123', 256), 1, 1, 1, 2, 'ADMIN'),
('20553334441', 'SERVICIOS BETA SRL', NULL, NULL, NULL, NULL, 'CALLE LIMA 202', '912345678', 'contacto@beta.com', SHA2('123', 256), 1, 1, 1, 2, 'ADMIN'),
('20661234589', 'CONSULTORA GAMMA EIRL', NULL, NULL, NULL, NULL, 'JR. CUSCO 303', '923456789', 'info@gamma.com', SHA2('123', 256), 1, 1, 1, 2, 'ADMIN'),
('20771234987', 'CONSTRUCTORA DELTA S.A.', NULL, NULL, NULL, NULL, 'AV. AREQUIPA 404', '934567890', 'delta@construct.com', SHA2('123', 256), 1, 1, 1, 2, 'ADMIN'),
('20881234500', 'COMERCIAL EPSILON S.A.C.', NULL, NULL, NULL, NULL, 'AV. BRASIL 505', '945678901', 'epsilon@comercial.com', SHA2('123', 256), 1, 1, 1, 2, 'ADMIN'),

-- CLIENTES CON DNI
('12345678', 'JUAN', 'PÉREZ', 'LOPEZ', 1, '1990-05-10', 'MZ A LT 5', '956789012', 'juanp@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN'),
('87654321', 'ANA', 'GARCÍA', 'TORRES', 0, '1992-08-22', 'JR. AYACUCHO 123', '967890123', 'ana@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN'),
('11223344', 'CARLOS', 'RAMIREZ', 'PAREDES', 1, '1988-03-15', 'AV. GRAU 456', '978901234', 'carlosr@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN'),
('44332211', 'MARÍA', 'LÓPEZ', 'ROJAS', 0, '1995-12-01', 'JR. JUNÍN 789', '989012345', 'maria@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN'),
('55667788', 'LUIS', 'TORRES', 'GÓMEZ', 1, '1991-09-30', 'AV. SALAVERRY 101', '990123456', 'luist@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN'),
('60594837', 'SEBASTIAN', 'CELIZ', 'GUERRERO', 1, '2010-09-30', 'AV. BRASIL 101', '94435638', 'sebastian@gmail.com', SHA2('123', 256), 1, 1, 1, 1, 'ADMIN');

INSERT INTO `tipo_comprobante` (`nombre`, `estado`, `usuario`)
VALUES ('boleta', 1, 'alexis@gmail.com');

INSERT INTO `tipo_comprobante` (`nombre`, `estado`, `usuario`)
VALUES ('factura', 1, 'alexis@gmail.com');

INSERT INTO `tipo_metodopago` (`nombre`, `estado`, `usuario`)
VALUES ('Efectivo', 1, 'alexis@gmail.com');

INSERT INTO `metodo_pago`
(`nombre`, `logo`, `estado`, `id_tipo_metodoPago`, `qr`, `usuario`)
VALUES
(
'Efectivo',
'/static/img/efectivo.png',
1,
1,
'/static/img/efectivo.png',
'alexis@gmail.com'
);

-- Crear procedimiento SP_REGISTRAR_PERSONAL_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_PERSONAL_INCIDENCIA(
    IN P_PERSONAL_ID INT,
    IN P_INCIDENCIA_ID INT,
    IN P_DESCRIPCION VARCHAR(255),
    IN P_ESTADO BOOLEAN, 
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cIncidencia INT DEFAULT 0;
    DECLARE duracion INT DEFAULT 0;
    DECLARE fecha_fin DATETIME;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    -- Verificar si ya existe la incidencia para ese personal
    SELECT COUNT(*) INTO cIncidencia 
    FROM personal_incidencia 
    WHERE personalid = P_PERSONAL_ID AND incidenciaid = P_INCIDENCIA_ID;

    IF cIncidencia > 0 THEN
        SET @MSJ2 = 'Ya se encuentra registrada esa sanción para ese personal';
    ELSE
        -- Recuperar la duración de la sanción en días
        SELECT duracion_sancion INTO duracion
        FROM incidencia 
        WHERE id = P_INCIDENCIA_ID;

        -- Calcular la fecha de fin sumando los días a la fecha actual
        SET fecha_fin = DATE_ADD(NOW(), INTERVAL duracion DAY);

        -- Insertar el registro en la tabla
        INSERT INTO personal_incidencia (
            personalid, incidenciaid, descripcion, fecha_fin, estado, usuario
        ) VALUES (
            P_PERSONAL_ID, P_INCIDENCIA_ID, P_DESCRIPCION, fecha_fin, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Sanción registrada al personal correctamente';
    END IF;

END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_PERSONAL_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_PERSONAL_INCIDENCIA(
    IN P_PERSONAL_ID INT,
    IN P_INCIDENCIA_ID INT,
    IN P_DESCRIPCION VARCHAR(255),
    IN P_ESTADO BOOLEAN, 
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cPersonal INT;
    DECLARE cIncidencia INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPersonal FROM personal_incidencia WHERE personalid = P_PERSONAL_ID;
    SELECT COUNT(*) INTO cIncidencia FROM personal_incidencia WHERE incidenciaid = P_INCIDENCIA_ID;

    IF cPersonal <= 0 AND cIncidencia <= 0 THEN
        SET @MSJ2 = 'El personal que intenta sancionar editar no existe';
    ELSEIF cIncidencia != 0 AND cPersonal != 0 THEN
        SET @MSJ2 = 'La sanción que intenta aplicarle al personal ya existe';
    ELSE
        UPDATE personal_incidencia 
        SET descripcion = P_DESCRIPCION, estado = P_ESTADO 
        WHERE personalid = P_PERSONAL_ID AND incidenciaid = P_INCIDENCIA_ID;
        SET @MSJ = 'Se modificó correctamente la sanción al personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_PERSONAL_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_PERSONAL_INCIDENCIA(
    IN P_INCIDENCIA_ID INT,
    IN P_PERSONAL_ID INT
)
BEGIN
    DECLARE cIncidencia INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN 
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cIncidencia 
    FROM personal_incidencia 
    WHERE incidenciaid = P_INCIDENCIA_ID AND personalid = P_PERSONAL_ID;

    IF cIncidencia <= 0 THEN
        SET @MSJ2 = 'La sanción al personal que intenta dar de baja no existe';
    ELSE
        UPDATE personal_incidencia 
        SET estado = 0 
        WHERE personalid = P_PERSONAL_ID AND incidenciaid = P_INCIDENCIA_ID;
        SET @MSJ = 'Se dio de baja correctamente la sanción al personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_PERSONAL_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_PERSONAL_INCIDENCIA(
    IN P_PERSONAL_ID INT,
    IN P_INCIDENCIA_ID INT
)
BEGIN
    DECLARE cIncidencia INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN 
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cIncidencia 
    FROM personal_incidencia 
    WHERE incidenciaid = P_INCIDENCIA_ID AND personalid = P_PERSONAL_ID;

    IF cIncidencia <= 0 THEN
        SET @MSJ2 = 'La sanción al personal que intenta eliminar no existe';
    ELSE
        DELETE FROM personal_incidencia 
        WHERE personalid = P_PERSONAL_ID AND incidenciaid = P_INCIDENCIA_ID;

        SET @MSJ = 'Se eliminó correctamente la sanción del personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_INCIDENCIA(
    IN P_NOMBRE VARCHAR(255),
    IN P_DESCRIPCION VARCHAR(255),
    IN P_DURACION_SANCION INT,
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre 
    FROM incidencia 
    WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'La incidencia que intenta registrar ya está registrada';
    ELSE
        INSERT INTO incidencia (
            nombre, descripcion, duracion_sancion, estado, usuario
        ) VALUES (
            P_NOMBRE, P_DESCRIPCION, P_DURACION_SANCION, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Incidencia registrada correctamente';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_INCIDENCIA(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_DESCRIPCION VARCHAR(255),
    IN P_DURACION_SANCION INT,
    IN P_ESTADO BOOLEAN
)
BEGIN 
    DECLARE cNombre INT;
    DECLARE cID INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cID 
    FROM incidencia 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM incidencia 
    WHERE nombre = P_NOMBRE;

    IF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre de incidencia ya existe';
    ELSE
        UPDATE incidencia 
        SET nombre = P_NOMBRE,
            descripcion = P_DESCRIPCION,
            duracion_sancion = P_DURACION_SANCION,
            estado = P_ESTADO 
        WHERE id = P_ID;

        SET @MSJ = 'Se editó correctamente la incidencia';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_INCIDENCIA(
    IN P_ID INT
)
BEGIN
    DECLARE cID INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cID FROM incidencia WHERE id = P_ID;

    IF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta dar de baja no existe';
    ELSE
        UPDATE incidencia SET estado = 0 WHERE id = P_ID;
        SET @MSJ = 'Se dio de baja correctamente la incidencia';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_INCIDENCIA
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_INCIDENCIA(
    IN P_ID INT
)
BEGIN
    DECLARE cID INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cID FROM incidencia WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM personal_incidencia WHERE incidenciaid = P_ID) THEN
        SET @MSJ2 = 'No puede eliminar la incidencia seleccionada porque existen otros registros que dependen de este'; 
    ELSEIF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta eliminar no existe';
    ELSE
        DELETE FROM incidencia WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente la incidencia';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_TERMINOS_CONDICIONES
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_TERMINOS_CONDICIONES(
    IN P_NOMBRE VARCHAR(255),
    IN P_ARCHIVO VARCHAR(255),
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM terminos_condiciones WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre de términos y condiciones ya existe';
    ELSE
        INSERT INTO terminos_condiciones (
            nombre, archivo, estado, usuario
        ) VALUES (
            P_NOMBRE, P_ARCHIVO, 0, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el término y condición';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_TERMINOS_CONDICIONES
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_TERMINOS_CONDICIONES(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_ARCHIVO VARCHAR(255),
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cTermino INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTermino 
    FROM terminos_condiciones 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM terminos_condiciones 
    WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cTermino <= 0 THEN
        SET @MSJ2 = 'El término y condición que intenta editar no existe';
    ELSEIF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe en otro término y condición';
    ELSE
        UPDATE terminos_condiciones 
        SET nombre = P_NOMBRE, 
            archivo = P_ARCHIVO,
            usuario = P_USUARIO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente el término y condición';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TERMINOS_CONDICIONES
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_TERMINOS_CONDICIONES(
    IN P_ID INT
)
BEGIN
    DECLARE cTermino INT;
    DECLARE flagTermino BOOLEAN;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTermino 
    FROM terminos_condiciones 
    WHERE id = P_ID;

    SELECT estado INTO flagTermino 
    FROM terminos_condiciones 
    WHERE id = P_ID;

    IF cTermino <= 0 THEN
        SET @MSJ2 = 'El término y condición que intenta eliminar no existe';
    ELSEIF flagTermino = 1 THEN
        SET @MSJ2 = 'El término y condición activo no puede ser eliminado';
    ELSE
        DELETE FROM terminos_condiciones 
        WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente el término y condición';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ACTIVAR_TERMINOS_CONDICIONES
DELIMITER $$

CREATE PROCEDURE SP_ACTIVAR_TERMINOS_CONDICIONES(
    IN P_ID INT
)
BEGIN
    DECLARE cTermino INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTermino 
    FROM terminos_condiciones 
    WHERE id = P_ID;

    IF cTermino <= 0 THEN
        SET @MSJ2 = 'El término y condición que intenta activar no existe';
    ELSE
        UPDATE terminos_condiciones SET estado = 0;
        UPDATE terminos_condiciones SET estado = 1 WHERE id = P_ID;

        SET @MSJ = 'Se activó correctamente el término y condición';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_USUARIO(
    IN P_NOMBRE VARCHAR(255),
    IN P_EMAIL VARCHAR(255),
    IN P_PASS VARCHAR(255),
    IN P_IMAGEN VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_IDTIPOUSUARIO INT,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cEmail INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cEmail 
    FROM usuarios 
    WHERE EMAIL = P_EMAIL;

    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSE
        INSERT INTO usuarios (
            NOMBRE, EMAIL, PASSWORD, IMAGEN, ESTADO, ID_TIPOUSUARIO, USUARIO
        ) VALUES (
            P_NOMBRE, P_EMAIL, P_PASS, P_IMAGEN, P_ESTADO, P_IDTIPOUSUARIO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente al usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_USUARIO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_EMAIL VARCHAR(255),
    IN P_IMAGEN VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cUsuario INT;
    DECLARE cEmail INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM usuarios 
    WHERE ID = P_ID;

    SELECT COUNT(*) INTO cEmail 
    FROM usuarios 
    WHERE EMAIL = P_EMAIL AND ID != P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta editar no existe';
    ELSEIF cEmail != 0 THEN
        SET @MSJ2 = 'El correo ingresado ya existe';
    ELSE
        UPDATE usuarios 
        SET NOMBRE = P_NOMBRE, 
            EMAIL = P_EMAIL,
            IMAGEN = P_IMAGEN,
            ESTADO = P_ESTADO,
            ID_TIPOUSUARIO = P_IDTIPOUSUARIO
        WHERE ID = P_ID;

        SET @MSJ = 'Se modificó correctamente al usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_CAMBIAR_CLAVE
DELIMITER $$

CREATE PROCEDURE SP_CAMBIAR_CLAVE(
    IN P_EMAIL VARCHAR(255),
    IN P_PASSWORD VARCHAR(255),
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE cEmail INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET MSJ = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SELECT COUNT(*) INTO cEmail 
    FROM usuarios 
    WHERE EMAIL = P_EMAIL AND ESTADO = 1;

    IF cEmail = 0 THEN
        SET MSJ2 = 'El correo no existe o el usuario no está activo';
    ELSE
        UPDATE usuarios 
        SET PASSWORD = P_PASSWORD
        WHERE EMAIL = P_EMAIL AND ESTADO = 1;

        SET MSJ = 'Contraseña modificada correctamente';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_USUARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM usuarios 
    WHERE ID = P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta dar de baja no existe';
    ELSE
        UPDATE usuarios 
        SET ESTADO = 0 
        WHERE ID = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_USUARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM usuarios 
    WHERE ID = P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta eliminar no existe';
    ELSE
        DELETE FROM usuarios 
        WHERE ID = P_ID;

        SET @MSJ = 'Se eliminó correctamente al usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_CLIENTE
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_CLIENTE(
    IN P_ID_PAIS INT,
    IN P_ID_TIPO_DOC INT,
    IN P_ID_TIPO_CLIENTE INT,
    IN P_NUMERO_DOCUMENTO VARCHAR(11),
    IN P_NOMBRE VARCHAR(255),
    IN P_APE_PATERNO VARCHAR(50),
    IN P_APE_MATERNO VARCHAR(50),
    IN P_SEXO BOOLEAN,
    IN P_F_NACIMIENTO DATE,
    IN P_DIRECCION VARCHAR(255),
    IN P_TELEFONO VARCHAR(13),
    IN P_EMAIL VARCHAR(100),
    IN P_PASSWORD VARCHAR(256),
    IN P_ESTADO TINYINT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cEmail INT;
    DECLARE cNumeroDoc INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

        SET @MSJ = NULL;
        SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cEmail FROM CLIENTE WHERE EMAIL = P_EMAIL;
    SELECT COUNT(*) INTO cNumeroDoc FROM CLIENTE WHERE numero_documento = P_NUMERO_DOCUMENTO;
    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSEIF cNumeroDoc > 0 THEN
        SET @MSJ2 = 'El numero de documento que intenta registrar ya está registrado';
    ELSE
        INSERT INTO CLIENTE (id_pais,id_tipo_doc,id_tipo_cliente,numero_documento,nombre, ape_paterno, ape_materno, sexo, f_nacimiento, direccion, telefono, email, password,estado,usuario) 
        VALUES (P_ID_PAIS, P_ID_TIPO_DOC, 3, P_NUMERO_DOCUMENTO, P_NOMBRE, P_APE_PATERNO, P_APE_MATERNO, P_SEXO, P_F_NACIMIENTO, P_DIRECCION, P_TELEFONO, P_EMAIL, P_PASSWORD,P_ESTADO,P_USUARIO);
        SET @MSJ = 'Se registró correctamente al cliente';
    END IF;
END $$
DELIMITER ;

-- Procedimiento unificado para editar cliente (natural o jurídico) según tipo de documento
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_CLIENTE(
    IN P_ID INT,
    IN P_ID_PAIS INT,
    IN P_ID_TIPO_DOC INT,
    IN P_ID_TIPO_CLIENTE INT,
    IN P_NUMERO_DOCUMENTO VARCHAR(20),
    IN P_NOMBRES VARCHAR(90),
    IN P_APE_PATERNO VARCHAR(50),
    IN P_APE_MATERNO VARCHAR(50),
    IN P_SEXO TINYINT,
    IN P_F_NACIMIENTO DATE,
    IN P_DIRECCION VARCHAR(255),
    IN P_TELEFONO VARCHAR(13),
    IN P_EMAIL VARCHAR(100),
    IN P_PASSWORD VARCHAR(256),
    IN P_ESTADO TINYINT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cCliente INT;
    DECLARE cEmail INT;
    DECLARE cNumeroDoc INT;
    DECLARE v_tipo_doc VARCHAR(10);

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

        SET @MSJ = NULL;
        SET @MSJ2 = NULL;

    -- Obtener la abreviatura del tipo de documento
    SELECT abreviatura INTO v_tipo_doc FROM tipo_documento WHERE id = P_ID_TIPO_DOC;

    SELECT COUNT(*) INTO cCliente FROM cliente WHERE id = P_ID;
    SELECT COUNT(*) INTO cEmail FROM cliente WHERE email = P_EMAIL AND id != P_ID;
    SELECT COUNT(*) INTO cNumeroDoc FROM cliente WHERE numero_documento = P_NUMERO_DOCUMENTO AND id != P_ID;

    IF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta editar no existe';
    ELSEIF cEmail != 0 THEN
        SET @MSJ2 = 'El correo ingresado ya existe';
    ELSEIF cNumeroDoc != 0 THEN
        SET @MSJ2 = 'El número de documento ingresado ya existe';
    ELSE
        IF v_tipo_doc = 'DNI' THEN
            UPDATE cliente
            SET id_pais = P_ID_PAIS,
                id_tipo_doc = P_ID_TIPO_DOC,
                id_tipo_cliente = 3,
                numero_documento = P_NUMERO_DOCUMENTO,
                nombre = P_NOMBRES,
                ape_paterno = P_APE_PATERNO,
                ape_materno = P_APE_MATERNO,
                sexo = P_SEXO,
                f_nacimiento = P_F_NACIMIENTO,
                direccion = P_DIRECCION,
                telefono = P_TELEFONO,
                email = P_EMAIL,
                password = P_PASSWORD,
                estado = P_ESTADO,
                usuario = P_USUARIO
            -- Actualizar el cliente natural
            WHERE id = P_ID;
            SET @MSJ = 'Se modificó correctamente al cliente natural';
        ELSEIF v_tipo_doc = 'RUC' THEN
            UPDATE cliente
            SET id_pais = P_ID_PAIS,
                id_tipo_doc = P_ID_TIPO_DOC,
                id_tipo_cliente = 4,
                numero_documento = P_NUMERO_DOCUMENTO,
                nombre = P_NOMBRES,
                ape_paterno = NULL,
                ape_materno = NULL,
                sexo = NULL,
                f_nacimiento = NULL,
                direccion = P_DIRECCION,
                telefono = P_TELEFONO,
                email = P_EMAIL,
                password = P_PASSWORD,
                estado = P_ESTADO,
                usuario = P_USUARIO
            -- Actualizar el cliente jurídico
            WHERE id = P_ID;
            SET @MSJ = 'Se modificó correctamente al cliente jurídico';
        ELSE
            -- Para otros tipos de documento, se puede ajustar la lógica según necesidad
            UPDATE cliente
            SET id_pais = P_ID_PAIS,
                id_tipo_doc = P_ID_TIPO_DOC,
                id_tipo_cliente = 3,
                numero_documento = P_NUMERO_DOCUMENTO,
                nombre = P_NOMBRES,
                ape_paterno = P_APE_PATERNO,
                ape_materno = P_APE_MATERNO,
                sexo = P_SEXO,
                f_nacimiento = P_F_NACIMIENTO,
                direccion = P_DIRECCION,
                telefono = P_TELEFONO,
                email = P_EMAIL,
                password = P_PASSWORD,
                estado = P_ESTADO,
                usuario = P_USUARIO
            -- Actualizar el cliente con otro tipo de documento
            WHERE id = P_ID;
            SET @MSJ = 'Se modificó correctamente al cliente';
        END IF;
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_CLIENTE
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_CLIENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cCliente INT;
    DECLARE cDeBaja INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cCliente FROM cliente WHERE ID = P_ID;
    SELECT COUNT(*) INTO cDeBaja FROM cliente WHERE ID = P_ID AND estado = 0;

    IF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta dar de baja no existe';
    ELSEIF cDeBaja > 0 THEN
        SET @MSJ2 = 'El cliente ya se encuentra dado de baja';
    ELSE
        UPDATE cliente SET ESTADO = 0 WHERE ID = P_ID;
        SET @MSJ = 'Se dio de baja correctamente al cliente';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_CLIENTE
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_CLIENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cCliente INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cCliente FROM cliente WHERE ID = P_ID;

    IF (SELECT 1 FROM venta WHERE idCliente = P_ID) THEN
        SET @MSJ2 = 'El cliente no se puede eliminar porque otros registros depende de este';
    ELSEIF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta eliminar no existe';
    ELSE
        DELETE FROM cliente WHERE ID = P_ID;
        SET @MSJ = 'Se eliminó correctamente al cliente';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_VERIFICAR_CORREO_CLIENTE
DELIMITER $$

CREATE PROCEDURE SP_VERIFICAR_CORREO_CLIENTE(
    IN p_email VARCHAR(100),
    OUT p_resultado INT
)
BEGIN
    DECLARE v_total INT;

    SELECT COUNT(*) INTO v_total
    FROM cliente
    WHERE email = p_email AND estado = 1;

    IF v_total > 0 THEN
        SET p_resultado = 1;
    ELSE
        SET p_resultado = -1;
    END IF;
END $$

DELIMITER ;

-- aaaaaaaaaaaaaaa

-- Crear procedimiento SP_REGISTRAR_ABREVIATURA_CIUDAD
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_ABREVIATURA_CIUDAD(
    IN P_NOMBRE VARCHAR(50),
    IN P_ABREVIATURA CHAR(3)
)
BEGIN
    DECLARE cAbreviatura INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cAbreviatura
    FROM ciudad 
    WHERE nombre = P_NOMBRE AND abreviatura = P_ABREVIATURA;

    IF cAbreviatura > 0 THEN
        SET @MSJ2 = 'La abreviatura que intenta registrar ya está registrada';
    ELSE
        INSERT INTO ciudad (nombre, abreviatura) 
        VALUES (P_NOMBRE, P_ABREVIATURA);

        SET @MSJ = 'Se registró correctamente la abreviatura de la ciudad';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_SUCURSAL
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_SUCURSAL(
    IN P_CIUDAD VARCHAR(50),
    IN P_NOMBRE VARCHAR(50),
    IN P_DIRECCION VARCHAR(255),
    IN P_LATITUD DECIMAL(8,6),
    IN P_LONGITUD DECIMAL(9,6),
    IN P_ESTADO TINYINT,
    IN P_ABREVIATURA CHAR(3),
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cSucursal INT;
    DECLARE cAUX CHAR(6);
    DECLARE cCorrelativo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cSucursal
    FROM sucursal 
    WHERE nombre = P_NOMBRE AND abreviatura = P_ABREVIATURA;

    SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(cod_sucursal, '-', -1) AS UNSIGNED)), 0) + 1 
    INTO cCorrelativo 
    FROM sucursal 
    WHERE abreviatura = P_ABREVIATURA;

    SET cAUX = CONCAT(P_ABREVIATURA, '-', LPAD(cCorrelativo, 2, '0'));

    IF cSucursal > 0 THEN
        SET @MSJ2 = 'La sucursal que intenta registrar ya está registrada';
    ELSE
        INSERT INTO sucursal (
            cod_sucursal, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario
        ) VALUES (
            cAUX, P_CIUDAD, P_NOMBRE, P_DIRECCION, P_LATITUD, P_LONGITUD, P_ESTADO, P_ABREVIATURA, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente la sucursal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_SUCURSAL
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_SUCURSAL(
    IN P_ID INT,
    IN P_DEPARTAMENTO VARCHAR(50),
    IN P_NOMBRE VARCHAR(50),
    IN P_DIRECCION VARCHAR(255),
    IN P_LATITUD DECIMAL(8,6),
    IN P_LONGITUD DECIMAL(9,6),
    IN P_ESTADO INT,
    IN P_ABREVIATURA CHAR(3),
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cSucursal INT;
    DECLARE cNombre INT;
    DECLARE cAUX CHAR(6);
    DECLARE cCorrelativo INT;
    DECLARE abreviatura_cambiada BOOLEAN DEFAULT FALSE;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cSucursal 
    FROM sucursal 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM sucursal 
    WHERE nombre = P_NOMBRE AND id != P_ID;

    SELECT CASE WHEN abreviatura != P_ABREVIATURA THEN TRUE ELSE FALSE END 
    INTO abreviatura_cambiada
    FROM sucursal 
    WHERE id = P_ID LIMIT 1;

    IF abreviatura_cambiada THEN
        SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(cod_sucursal, '-', -1) AS UNSIGNED)), 0) + 1 
        INTO cCorrelativo
        FROM sucursal 
        WHERE abreviatura = P_ABREVIATURA AND id != P_ID;

        SET cAUX = CONCAT(P_ABREVIATURA, '-', LPAD(cCorrelativo, 2, '0'));
    ELSE
        SELECT cod_sucursal INTO cAUX FROM sucursal WHERE id = P_ID;
    END IF;

    IF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta editar no existe';
    ELSEIF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre de la sucursal ya está en uso';
    ELSE
        UPDATE sucursal 
        SET ciudad = P_DEPARTAMENTO,
            nombre = P_NOMBRE,
            cod_sucursal = cAUX,
            direccion = P_DIRECCION,
            latitud = P_LATITUD,
            longitud = P_LONGITUD,
            estado = P_ESTADO,
            abreviatura = P_ABREVIATURA,
            usuario = P_USUARIO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente la sucursal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_SUCURSAL
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_SUCURSAL(
    IN P_ID INT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cSucursal INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cSucursal 
    FROM sucursal 
    WHERE id = P_ID;

    IF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta dar de baja no existe';
    ELSE
        UPDATE sucursal 
        SET estado = 0, usuario = P_USUARIO
        WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente la sucursal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_SUCURSAL
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_SUCURSAL(
    IN P_ID INT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cSucursal INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cSucursal 
    FROM sucursal 
    WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM escala WHERE idSucursal = P_ID) THEN
        SET @MSJ2 = 'Esta sucursal no se puede eliminar porque otros registros dependen de este';
    ELSEIF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta eliminar no existe';
    ELSE
        DELETE FROM sucursal WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente la sucursal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_ASIENTO
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_ASIENTO(
    IN P_NRO_ASIENTO SMALLINT,
    IN P_ID_NIVEL TINYINT,
    IN P_TIPO_ASIENTO VARCHAR(30),
    IN P_ESTADO TINYINT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    IF P_ESTADO NOT IN (0, 1, 2, 3, 4) THEN
        SET @MSJ2 = 'El estado seleccionado no está disponible';
    ELSE
        INSERT INTO asiento (
            nro_asiento, id_nivel, tipo_asiento, estado, usuario
        ) VALUES (
            P_NRO_ASIENTO, P_ID_NIVEL, P_TIPO_ASIENTO, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el asiento';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_ASIENTO
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_ASIENTO(
    IN P_ID INT,
    IN P_NRO_ASIENTO SMALLINT,
    IN P_ID_NIVEL TINYINT,
    IN P_TIPO_ASIENTO VARCHAR(30),
    IN P_ESTADO TINYINT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cAsiento INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cAsiento FROM asiento WHERE id = P_ID;

    IF cAsiento = 0 THEN
        SET @MSJ2 = 'El asiento que intenta editar no existe';
    ELSEIF P_ESTADO NOT IN (0, 1, 2, 3, 4) THEN
        SET @MSJ2 = 'El estado seleccionado no está disponible';
    ELSE
        UPDATE asiento
        SET nro_asiento = P_NRO_ASIENTO,
            id_nivel = P_ID_NIVEL,
            tipo_asiento = P_TIPO_ASIENTO,
            estado = P_ESTADO,
            usuario = P_USUARIO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente el asiento';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_ASIENTO
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_ASIENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cAsiento INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cAsiento FROM asiento WHERE id = P_ID;

    IF cAsiento = 0 THEN
        SET @MSJ2 = 'El asiento que intenta dar de baja no existe';
    ELSE
        UPDATE asiento
        SET estado = 0
        WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente el asiento';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_ASIENTO
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_ASIENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cAsiento INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cAsiento FROM asiento WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM viaje WHERE idVehiculo = (SELECT id_vehiculo FROM asiento WHERE id = P_ID)) THEN
        SET @MSJ2 = 'Este asiento no se puede eliminar porque otros registros dependen de este';
    ELSEIF cAsiento = 0 THEN
        SET @MSJ2 = 'El asiento que intenta eliminar no existe';
    ELSE
        DELETE FROM asiento WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente el asiento';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_TIPO_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_TIPO_USUARIO(
    IN P_NOMBRE VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM tipo_usuario WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta registrar ya está registrado';
    ELSE
        INSERT INTO tipo_usuario (nombre, estado, usuario) 
        VALUES (P_NOMBRE, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_TIPO_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_TIPO_USUARIO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cTipoUsuario INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM tipo_usuario WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_usuario 
        SET nombre = P_NOMBRE, 
            estado = P_ESTADO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente al tipo de usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_TIPO_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_TIPO_USUARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE id = P_ID;

    IF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_usuario SET estado = 0 WHERE id = P_ID;
        SET @MSJ = 'Se dio de baja correctamente al tipo de usuario';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_USUARIO
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_TIPO_USUARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM usuarios WHERE id_tipousuario = P_ID) THEN
        SET @MSJ2 = 'El tipo de usuario no se puede eliminar porque otros registros dependen de este';
    ELSEIF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta eliminar no existe';
    ELSE
        DELETE FROM conf_dclaims WHERE idTipoUsuario = P_ID;
        DELETE FROM conf_dmenus WHERE idTipoUsuario = P_ID;
        DELETE FROM tipo_usuario WHERE id = P_ID;
        SET @MSJ = 'El tipo de usuario se eliminó correctamente';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_TIPO_PERSONAL
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_TIPO_PERSONAL(
    IN P_NOMBRE VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM tipo_personal WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta registrar ya está registrado';
    ELSE
        INSERT INTO tipo_personal (nombre, estado, usuario) 
        VALUES (P_NOMBRE, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_TIPO_PERSONAL
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_TIPO_PERSONAL(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cTipoPersonal INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM tipo_personal WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_personal 
        SET nombre = P_NOMBRE, 
            estado = P_ESTADO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente al tipo de personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_DARBAJA_TIPO_PERSONAL
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_TIPO_PERSONAL(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoPersonal INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID;

    IF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_personal SET estado = 0 WHERE id = P_ID;
        SET @MSJ = 'Se dio de baja correctamente al tipo de personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_PERSONAL
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_TIPO_PERSONAL(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoPersonal INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM personal WHERE id_tipopersonal = P_ID) THEN
        SET @MSJ2 = 'El tipo de personal no se puede eliminar porque otros registros dependen de este';
    ELSEIF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_personal WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente al tipo de personal';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ASIGNAR_DMENU
DELIMITER $$

CREATE PROCEDURE SP_ASIGNAR_DMENU(
    IN P_IDMENU INT,
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cMenus INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMenus 
    FROM conf_dmenus 
    WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cMenus > 0 THEN
        SET @MSJ2 = 'El permiso que intenta asignar, ya existe';
    ELSE
        INSERT INTO conf_dmenus (idMenu, idTipoUsuario) 
        VALUES (P_IDMENU, P_IDTIPOUSUARIO);

        SET @MSJ = 'Se asignó correctamente el permiso';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_DMENU
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_DMENU(
    IN P_IDMENU INT,
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cMenus INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMenus 
    FROM conf_dmenus 
    WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cMenus <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM conf_dmenus 
        WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO;

        SET @MSJ = 'Se eliminó correctamente el permiso';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ASIGNAR_DCLAIM
DELIMITER $$

CREATE PROCEDURE SP_ASIGNAR_DCLAIM(
    IN P_IDCLAIM INT,
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cClaims INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cClaims 
    FROM conf_dclaims 
    WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cClaims > 0 THEN
        SET @MSJ2 = 'El permiso que intenta asignar, ya existe';
    ELSE
        INSERT INTO conf_dclaims (idClaim, idTipoUsuario) 
        VALUES (P_IDCLAIM, P_IDTIPOUSUARIO);

        SET @MSJ = 'Se asignó correctamente el permiso';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_DCLAIM
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_DCLAIM(
    IN P_IDCLAIM INT,
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cClaims INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cClaims 
    FROM conf_dclaims 
    WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cClaims <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM conf_dclaims 
        WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO;

        SET @MSJ = 'Se eliminó correctamente el permiso';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_PLANTILLA
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_PLANTILLA(
    IN P_NOMBRE VARCHAR(255),
    IN P_COLORH VARCHAR(255),
    IN P_COLORF VARCHAR(255),
    IN P_LOGO VARCHAR(255),
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre 
    FROM conf_plantillas 
    WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre que intenta registrar ya está registrado';
    ELSE
        INSERT INTO conf_plantillas (
            nombre, color_header, color_footer, logo, estado, usuario
        ) VALUES (
            P_NOMBRE, P_COLORH, P_COLORF, P_LOGO, 0, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente la plantilla';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_PLANTILLA
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_PLANTILLA(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_COLORH VARCHAR(255),
    IN P_COLORF VARCHAR(255),
    IN P_LOGO VARCHAR(255)
)
BEGIN
    DECLARE cPlantilla INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM conf_plantillas WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE conf_plantillas 
        SET nombre = P_NOMBRE, 
            color_header = P_COLORH,
            color_footer = P_COLORF,
            logo = P_LOGO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente la plantilla';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_PLANTILLA
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_PLANTILLA(
    IN P_ID INT
)
BEGIN
    DECLARE cPlantilla INT;
    DECLARE flagPlantilla BOOLEAN;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE id = P_ID;
    SELECT estado INTO flagPlantilla FROM conf_plantillas WHERE id = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta eliminar no existe';
    ELSEIF flagPlantilla = 1 THEN
        SET @MSJ2 = 'La plantilla que está activa no puede ser eliminada';
    ELSE
        DELETE FROM conf_plantillas WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente la plantilla';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_ACTIVAR_PLANTILLA
DELIMITER $$

CREATE PROCEDURE SP_ACTIVAR_PLANTILLA(
    IN P_ID INT
)
BEGIN
    DECLARE cPlantilla INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE id = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta activar no existe';
    ELSE
        UPDATE conf_plantillas SET estado = 0;
        UPDATE conf_plantillas SET estado = 1 WHERE id = P_ID;

        SET @MSJ = 'Se activó correctamente la plantilla';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_INSERTAR_TIPOVEHICULO
DELIMITER $$

CREATE PROCEDURE SP_INSERTAR_TIPOVEHICULO(
    IN p_nombre VARCHAR(50),
    IN p_idMarca INT,
    IN p_cantidad INT,
    IN P_ESTADO BOOLEAN,
    IN P_SERVICIO INT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE v_existeMarca INT DEFAULT 0;
    DECLARE v_nuevoTipo INT DEFAULT 0;
    DECLARE v_i INT DEFAULT 1;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET @MSJ2 = 'Error al ejecutar el procedimiento';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO v_existeMarca
    FROM marca
    WHERE id = p_idMarca;

    IF v_existeMarca = 0 THEN
        SET @MSJ2 = 'La marca ingresada no existe';
    ELSE
        INSERT INTO tipo_vehiculo (
            nombre, id_marca, id_servicio, estado, cantidad, usuario
        ) VALUES (
            p_nombre, p_idMarca, P_SERVICIO, P_ESTADO, p_cantidad, P_USUARIO
        );

        SET v_nuevoTipo = LAST_INSERT_ID();

        WHILE v_i <= p_cantidad DO
            INSERT INTO vehiculo (
                placa, anio, color, estado, id_tipo_vehiculo, usuario
            ) VALUES (
                NULL, NULL, NULL, 1, v_nuevoTipo, P_USUARIO
            );
            SET v_i = v_i + 1;
        END WHILE;

        SET @MSJ = CONCAT('Tipo de vehículo insertado y ', p_cantidad, ' vehículos creados');
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SP_ACTUALIZAR_TIPOVEHICULO(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    IN p_idMarca INT,
    IN p_estado TINYINT,
    IN p_cantidad INT,
    IN P_SERVICIO INT,
    IN P_USUARIO VARCHAR(100),
    OUT p_MSJ VARCHAR(255),
    OUT p_MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_existeMarca INT DEFAULT 0;
    DECLARE v_total INT DEFAULT 0;
    DECLARE v_sinplaca INT DEFAULT 0;
    DECLARE v_diff INT DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_MSJ2 = 'Error al ejecutar el procedimiento';
    END;

    SET p_MSJ = '';
    SET p_MSJ2 = '';

    SELECT COUNT(*) INTO v_existeMarca
    FROM marca
    WHERE id = p_idMarca;

    IF v_existeMarca = 0 THEN
        SET p_MSJ2 = 'La marca indicada no existe';
    END IF;

    IF p_MSJ2 = '' THEN
        SELECT 
            COUNT(*) AS total,
            SUM(CASE WHEN placa IS NULL THEN 1 ELSE 0 END) AS sinplaca
        INTO v_total, v_sinplaca
        FROM vehiculo
        WHERE id_tipo_vehiculo = p_id;

        START TRANSACTION;

        IF p_cantidad < v_total THEN
            SET v_diff = v_total - p_cantidad;

            IF v_sinplaca = 0 THEN
                SET p_MSJ2 = 'No se puede reducir: todos los vehículos ya tienen placa';

            ELSEIF v_diff > v_sinplaca THEN
                SET p_MSJ2 = CONCAT(
                    'Sólo hay ', v_sinplaca,
                    ' vehículos sin placa; no se pueden eliminar ',
                    v_diff
                );

            ELSE
                DELETE FROM vehiculo
                WHERE id_tipo_vehiculo = p_id AND placa IS NULL
                ORDER BY id
                LIMIT v_diff;
            END IF;

        ELSEIF p_cantidad > v_total THEN
            SET v_diff = p_cantidad - v_total;

            WHILE v_diff > 0 DO
                INSERT INTO vehiculo (
                    placa, anio, color, estado, id_tipo_vehiculo, usuario
                ) VALUES (
                    NULL, NULL, NULL, 1, p_id, P_USUARIO
                );
                SET v_diff = v_diff - 1;
            END WHILE;
        END IF;

        IF p_MSJ2 = '' THEN
            UPDATE tipo_vehiculo
            SET nombre = p_nombre,
                id_marca = p_idMarca,
                id_servicio = P_SERVICIO,
                estado = p_estado,
                cantidad = p_cantidad
            WHERE id = p_id;

            COMMIT;
            SET p_MSJ = 'Tipo de vehículo y su flota actualizada correctamente';
        ELSE
            ROLLBACK;
        END IF;
    END IF;
END $$

DELIMITER ;

-- Procedimiento para dar de baja (baja lógica)
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_TIPOVEHICULO(
    IN p_id INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET MSJ2 = 'Error inesperado al dar de baja el tipo de vehículo';
    END;

    SET MSJ = NULL;
    SET MSJ2 = NULL;

    SELECT COUNT(*) INTO v_existe
    FROM tipo_vehiculo
    WHERE id = p_id;

    IF v_existe = 0 THEN
        SET MSJ2 = 'El tipo de vehículo no existe';
    ELSE
        START TRANSACTION;
        UPDATE tipo_vehiculo
        SET estado = 0
        WHERE id = p_id;
        COMMIT;

        SET MSJ = 'Tipo de vehículo dado de baja correctamente';
    END IF;
END $$

-- Procedimiento para eliminar físicamente
CREATE PROCEDURE SP_ELIMINAR_TIPOVEHICULO(
    IN p_id INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET MSJ2 = 'Error inesperado al eliminar físicamente el tipo de vehículo';
    END;

    SET MSJ = NULL;
    SET MSJ2 = NULL;

    SELECT COUNT(*) INTO v_existe
    FROM tipo_vehiculo
    WHERE id = p_id;

    IF EXISTS (SELECT 1 FROM vehiculo WHERE id_tipo_vehiculo = P_ID) THEN
        SET MSJ2 = 'No se puede eliminar el tipo de vehículo porque otros registros dependen de este';
    ELSEIF v_existe = 0 THEN
        SET MSJ2 = 'El tipo de vehículo no existe';
    ELSE
        START TRANSACTION;
        DELETE FROM tipo_vehiculo
        WHERE id = p_id;
        COMMIT;

        SET MSJ = 'Tipo de vehículo eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SP_INSERTAR_NIVEL(
    IN p_vehiculo INT,
    IN p_cantidad INT
)
BEGIN
    DECLARE nuevo_nroPiso INT;
    DECLARE nuevo_idNivel INT;
    DECLARE contador INT DEFAULT 1;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al insertar nivel';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    IF p_cantidad > 0 THEN
        SELECT COUNT(*) + 1 INTO nuevo_nroPiso
        FROM nivel
        WHERE id_vehiculo = p_vehiculo;

        INSERT INTO nivel (
            nroPiso, id_vehiculo, cantidad, estado
        ) VALUES (
            nuevo_nroPiso, p_vehiculo, p_cantidad, 1
        );

        SET nuevo_idNivel = LAST_INSERT_ID();

        WHILE contador <= p_cantidad DO
            INSERT INTO asiento (
                nro_asiento, id_nivel, tipo_asiento, estado, fecha_registro
            ) VALUES (
                contador, nuevo_idNivel, 'Económico', 1, NOW()
            );
            SET contador = contador + 1;
        END WHILE;

        SET @MSJ = CONCAT(
            'Nivel insertado correctamente con nroPiso ',
            nuevo_nroPiso,
            ' y se crearon ',
            p_cantidad,
            ' asientos.'
        );
    ELSE
        SET @MSJ2 = 'La cantidad debe ser mayor a 0';
    END IF;
END $$

DELIMITER ;

-- CREATE PROCEDURE SP_INSERTAR_NIVEL( 
-- IN p_vehiculo INT, 
-- IN p_cantidad INT 
-- ) 
-- BEGIN 
--     DECLARE nuevo_nroPiso INT; 
--     DECLARE EXIT HANDLER FOR SQLEXCEPTION 
--     BEGIN 
--     SET @MSJ2 = 'Error inesperado al insertar nivel'; 
--     SET @MSJ = NULL; 
--     END; 
--     SET @MSJ = NULL; 
--     SET @MSJ2 = NULL; 
--     IF p_cantidad > 0 THEN 
--     SELECT COUNT(*) + 1 
--     INTO nuevo_nroPiso 
--     FROM nivel 
--     WHERE id_vehiculo = p_vehiculo; 
--     INSERT INTO nivel (nroPiso, id_vehiculo, cantidad, estado) 
--     VALUES (nuevo_nroPiso, p_vehiculo, p_cantidad, 1); 
--     SET @MSJ = CONCAT( 
--     'Nivel insertado correctamente con nroPiso ', 
--     nuevo_nroPiso 
--     ); 
--     ELSE 
--     SET @MSJ2 = 'La cantidad debe ser mayor a 0'; 
--     END IF; 
-- END$$

DELIMITER $$

-- Actualizar nivel
CREATE PROCEDURE SP_ACTUALIZAR_NIVEL(
    IN p_idNivel INT,
    IN p_nroPiso INT,
    IN p_vehiculo INT,
    IN p_cantidad INT,
    IN p_estado TINYINT
)
BEGIN
    DECLARE max_piso INT DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al actualizar nivel';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    IF p_cantidad <= 0 THEN
        SET @MSJ2 = 'La cantidad debe ser mayor a 0';
    ELSEIF p_nroPiso <= 0 THEN
        SET @MSJ2 = 'El número de piso debe ser mayor a 0';
    ELSE
        SELECT COALESCE(MAX(nroPiso), 0) INTO max_piso
        FROM nivel
        WHERE id_vehiculo = p_vehiculo;

        IF p_nroPiso > max_piso + 1 THEN
            SET @MSJ2 = 'No puede actualizar a un piso mayor que el siguiente consecutivo';
        ELSE
            UPDATE nivel
            SET nroPiso = p_nroPiso,
                id_vehiculo = p_vehiculo,
                cantidad = p_cantidad,
                estado = p_estado
            WHERE id = p_idNivel;

            IF ROW_COUNT() = 0 THEN
                SET @MSJ2 = 'No se encontró el nivel especificado';
            ELSE
                SET @MSJ = 'Nivel actualizado correctamente';
            END IF;
        END IF;
    END IF;
END $$

-- Dar de baja nivel
CREATE PROCEDURE SP_DARBAJA_PISO(
    IN p_idNivel INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al dar de baja el piso';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    UPDATE nivel
    SET estado = 0
    WHERE id = p_idNivel;

    SET @MSJ = 'Piso dado de baja correctamente';
END $$

-- Eliminar nivel físicamente
CREATE PROCEDURE SP_ELIMINAR_NIVEL(
    IN p_idNivel INT
)
BEGIN
    DECLARE piso_actual INT;
    DECLARE vehiculo_act INT;
    DECLARE max_piso INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al eliminar nivel';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO piso_actual
    FROM nivel
    WHERE id = p_idNivel;

    DELETE FROM nivel_herramienta
    WHERE id_nivel = p_idNivel;

    IF piso_actual <= 0 THEN
        SET @MSJ2 = 'Intenta eliminar un nivel que no existe';
    ELSE
        DELETE FROM nivel
        WHERE id = p_idNivel;

        SET @MSJ = 'Nivel eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

-- Insertar un nuevo vehículo
DELIMITER $$

CREATE PROCEDURE SP_INSERTAR_VEHICULO(
    IN p_placa VARCHAR(10),
    IN p_anio INT,
    IN p_color VARCHAR(30),
    IN p_idTipoVehiculo INT,
    IN p_estado BOOLEAN,
    IN p_usuario VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al insertar vehículo';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    INSERT INTO vehiculo (
        placa, anio, color, estado, id_tipo_vehiculo, usuario
    ) VALUES (
        p_placa, p_anio, p_color, p_estado, p_idTipoVehiculo, p_usuario
    );

    SET @MSJ = 'Vehículo insertado correctamente';
END $$

-- Actualizar vehículo existente
CREATE PROCEDURE SP_ACTUALIZAR_VEHICULO(
    IN p_idVehiculo INT,
    IN p_placa VARCHAR(10),
    IN p_anio INT,
    IN p_color VARCHAR(30),
    IN p_idTipoVehiculo INT,
    IN p_estado BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al actualizar vehículo';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    UPDATE vehiculo
    SET placa = p_placa,
        anio = p_anio,
        color = p_color,
        id_tipo_vehiculo = p_idTipoVehiculo,
        estado = p_estado
    WHERE id = p_idVehiculo;

    IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el vehículo especificado';
    ELSE
        SET @MSJ = 'Vehículo actualizado correctamente';
    END IF;
END $$

-- Dar de baja vehículo (estado = 0)
CREATE PROCEDURE SP_BAJA_VEHICULO(
    IN p_idVehiculo INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al dar de baja vehículo';
        SET @MSJ = NULL;
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    UPDATE vehiculo
    SET estado = 0
    WHERE id = p_idVehiculo;

    IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el vehículo para dar de baja';
    ELSE
        SET @MSJ = 'Vehículo dado de baja correctamente';
    END IF;
END $$

DELIMITER ;

-- Eliminar vehículo de la tabla
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_VEHICULO(
    IN p_idVehiculo INT
)
BEGIN
    DECLARE v_idTipoVehiculo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al eliminar vehículo';
        SET @MSJ = NULL;
        ROLLBACK;
    END;

    START TRANSACTION;

    SELECT id_tipo_vehiculo INTO v_idTipoVehiculo
    FROM vehiculo
    WHERE id = p_idVehiculo;

    IF EXISTS (SELECT 1 FROM viaje WHERE idVehiculo = p_idVehiculo) THEN
        SET @MSJ2 = 'No se puede eliminar el vehículo porque otros registros dependen de este';
        ROLLBACK;
    ELSE
        DELETE FROM asiento WHERE id_vehiculo = p_idVehiculo;
        DELETE FROM vehiculo WHERE id = p_idVehiculo;
        SET @MSJ = 'Vehículo eliminado correctamente';
        COMMIT;
    END IF;

    -- IF ROW_COUNT() = 0 THEN
    --     SET @MSJ2 = 'No se encontró el vehículo para eliminar';
    --     ROLLBACK;
    -- ELSE
    --     UPDATE tipo_vehiculo
    --     SET cantidad = cantidad - 1
    --     WHERE id = v_idTipoVehiculo;

    --     SET @MSJ = 'Vehículo eliminado correctamente';
    --     COMMIT;
    -- END IF;
END $$

-- Registrar horario
CREATE PROCEDURE SP_REGISTRAR_HORARIO(
    IN P_HORARIO_ENTRADA TIME,
    IN P_HORARIO_SALIDA TIME,
    IN P_ESTADO VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    IF P_HORARIO_ENTRADA >= P_HORARIO_SALIDA THEN
        SET @MSJ2 = 'El horario de entrada es mayor que el de salida';
    ELSE
        INSERT INTO horario (
            horario_entrada, horario_salida, estado
        ) VALUES (
            P_HORARIO_ENTRADA, P_HORARIO_SALIDA, P_ESTADO
        );
        SET @MSJ = 'Se registró correctamente el horario';
    END IF;
END $$

-- Editar horario
CREATE PROCEDURE SP_EDITAR_HORARIO(
    IN P_ID INT,
    IN P_HORARIO_ENTRADA TIME,
    IN P_HORARIO_SALIDA TIME,
    IN P_ESTADO VARCHAR(255)
)
BEGIN
    DECLARE cHorarios INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios FROM horario WHERE id = P_ID;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta editar no existe';
    ELSEIF P_HORARIO_ENTRADA >= P_HORARIO_SALIDA THEN
        SET @MSJ2 = 'El horario de entrada es mayor que el de la salida';
    ELSE
        UPDATE horario
        SET horario_entrada = P_HORARIO_ENTRADA,
            horario_salida = P_HORARIO_SALIDA,
            estado = P_ESTADO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente al horario';
    END IF;
END $$

DELIMITER ;

-- Dar de baja horario
DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_HORARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cHorarios INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios 
    FROM horario 
    WHERE id = P_ID;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta dar de baja no existe';
    ELSE
        UPDATE horario 
        SET estado = 'I' 
        WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente el horario';
    END IF;
END $$

-- Eliminar horario
CREATE PROCEDURE SP_ELIMINAR_HORARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cHorarios INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios 
    FROM horario 
    WHERE id = P_ID;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta eliminar no existe';
    ELSE
        DELETE FROM horario 
        WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente el horario';
    END IF;
END $$

-- Registrar pregunta frecuente
CREATE PROCEDURE SP_REGISTRAR_PREGUNTA_FRECUENTE(
    IN P_PREGUNTA VARCHAR(255),
    IN P_RESPUESTA TEXT,
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cPregunta INT;
    DECLARE cRespuesta INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPregunta 
    FROM preguntas_frecuentes 
    WHERE pregunta = P_PREGUNTA;

    SELECT COUNT(*) INTO cRespuesta 
    FROM preguntas_frecuentes 
    WHERE respuesta = P_RESPUESTA;

    IF cPregunta > 0 THEN
        SET @MSJ2 = 'La pregunta frecuente que intenta registrar ya existe';
    ELSEIF cRespuesta > 0 THEN
        SET @MSJ2 = 'La respuesta que intenta registrar ya existe';
    ELSE
        INSERT INTO preguntas_frecuentes (
            pregunta, respuesta, estado, usuario
        ) VALUES (
            P_PREGUNTA, P_RESPUESTA, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente la pregunta frecuente';
    END IF;
END $$

DELIMITER ;

-- Editar pregunta frecuente
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_PREGUNTA_FRECUENTE(
    IN P_ID INT,
    IN P_PREGUNTA VARCHAR(255),
    IN P_RESPUESTA TEXT,
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cPregunta INT;
    DECLARE cRespuesta INT;
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM preguntas_frecuentes 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cPregunta 
    FROM preguntas_frecuentes 
    WHERE pregunta = P_PREGUNTA AND id != P_ID;

    SELECT COUNT(*) INTO cRespuesta 
    FROM preguntas_frecuentes 
    WHERE respuesta = P_RESPUESTA AND id != P_ID;

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La pregunta frecuente que intenta editar no existe';
    ELSEIF cPregunta > 0 THEN
        SET @MSJ2 = 'La pregunta ingresada ya existe';
    ELSEIF cRespuesta > 0 THEN
        SET @MSJ2 = 'La respuesta ingresada ya existe';
    ELSE
        UPDATE preguntas_frecuentes 
        SET pregunta = P_PREGUNTA, 
            respuesta = P_RESPUESTA, 
            estado = P_ESTADO,
            usuario = P_USUARIO 
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente la pregunta frecuente';
    END IF;
END $$

-- Eliminar pregunta frecuente
CREATE PROCEDURE SP_ELIMINAR_PREGUNTA_FRECUENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cPregunta INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPregunta 
    FROM preguntas_frecuentes 
    WHERE id = P_ID;

    IF cPregunta <= 0 THEN
        SET @MSJ2 = 'La pregunta frecuente que intenta eliminar no existe';
    ELSE
        DELETE FROM preguntas_frecuentes 
        WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente la pregunta frecuente';
    END IF;
END $$

-- Dar de baja pregunta frecuente
CREATE PROCEDURE SP_DAR_BAJA_PREGUNTA_FRECUENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cPregunta INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPregunta 
    FROM preguntas_frecuentes 
    WHERE id = P_ID AND estado = 1;

    IF cPregunta <= 0 THEN
        SET @MSJ2 = 'La pregunta frecuente que intenta dar de baja no existe';
    ELSE
        UPDATE preguntas_frecuentes 
        SET estado = 0 
        WHERE id = P_ID AND estado = 1;

        SET @MSJ = 'Se dio de baja correctamente la pregunta frecuente';
    END IF;
END $$

-- Registrar tipo de documento
CREATE PROCEDURE SP_REGISTRAR_TIPO_DOCUMENTO(
    IN P_NOMBRE VARCHAR(50),
    IN P_ABREVIATURA VARCHAR(10),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;
    DECLARE cAbreviatura INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre 
    FROM tipo_documento 
    WHERE nombre = P_NOMBRE;

    SELECT COUNT(*) INTO cAbreviatura 
    FROM tipo_documento 
    WHERE abreviatura = P_ABREVIATURA;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta registrar ya está registrado';
    ELSEIF cAbreviatura > 0 THEN
        SET @MSJ2 = 'La abreviatura que intenta registrar ya está registrada';
    ELSE
        INSERT INTO tipo_documento (
            nombre, abreviatura, estado, usuario
        ) VALUES (
            P_NOMBRE, P_ABREVIATURA, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el tipo de documento';
    END IF;
END $$

DELIMITER ;

-- Editar tipo de documento
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_TIPO_DOCUMENTO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ABREVIATURA VARCHAR(10),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cExiste INT;
    DECLARE cNombre INT;
    DECLARE cAbreviatura INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste FROM tipo_documento WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM tipo_documento WHERE nombre = P_NOMBRE AND id != P_ID;
    SELECT COUNT(*) INTO cAbreviatura FROM tipo_documento WHERE abreviatura = P_ABREVIATURA AND id != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta actualizar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSEIF cAbreviatura != 0 THEN
        SET @MSJ2 = 'La abreviatura ingresada ya existe';
    ELSE
        UPDATE tipo_documento 
        SET nombre = P_NOMBRE, 
            abreviatura = P_ABREVIATURA, 
            estado = P_ESTADO
        WHERE id = P_ID;

        SET @MSJ = 'Se actualizó correctamente el tipo de documento';
    END IF;
END $$

-- Eliminar tipo de documento
CREATE PROCEDURE SP_ELIMINAR_TIPO_DOCUMENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoDocumento INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoDocumento FROM tipo_documento WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM pasajero WHERE idTipoDocumento = P_ID) THEN
        SET @MSJ2 = 'El tipo de documento no se puede eliminar porque otros registros dependen de este';
    ELSEIF cTipoDocumento <= 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_documento WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente el tipo de documento';
    END IF;
END $$

-- Dar de baja tipo de documento
CREATE PROCEDURE SP_DARBAJA_TIPO_DOCUMENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoDocumento INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoDocumento FROM tipo_documento WHERE id = P_ID;

    IF cTipoDocumento = 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_documento SET estado = 0 WHERE id = P_ID;
        SET @MSJ = 'Se dio de baja correctamente el tipo de documento';
    END IF;
END $$

-- Insertar tipo de cliente
CREATE PROCEDURE SP_INSERTAR_TIPO_CLIENTE(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE nombre = P_NOMBRE;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de cliente con ese nombre';
    ELSE
        INSERT INTO tipo_cliente (
            nombre, estado, usuario
        ) VALUES (
            P_NOMBRE, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el tipo de cliente';
    END IF;
END $$

DELIMITER ;

-- Actualizar tipo de cliente
DELIMITER $$

CREATE PROCEDURE SP_ACTUALIZAR_TIPO_CLIENTE(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cExiste INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE idTipoCliente = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM tipo_cliente 
    WHERE nombre = P_NOMBRE AND idTipoCliente != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de cliente que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_cliente 
        SET nombre = P_NOMBRE, estado = P_ESTADO
        WHERE idTipoCliente = P_ID;

        SET @MSJ = 'Se actualizó correctamente el tipo de cliente';
    END IF;
END $$

-- Dar de baja tipo de cliente
CREATE PROCEDURE SP_DAR_BAJA_TIPO_CLIENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar SP_DAR_BAJA_TIPO_CLIENTE';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE idTipoCliente = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de cliente que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_cliente 
        SET estado = 0
        WHERE idTipoCliente = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al tipo de cliente';
    END IF;
END $$

-- Eliminar tipo de cliente
CREATE PROCEDURE SP_ELIMINAR_TIPO_CLIENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM tipo_cliente 
    WHERE idTipoCliente = P_ID;

    IF EXISTS (SELECT 1 FROM cliente WHERE id_tipo_cliente = P_ID) THEN
        SET @MSJ2 = 'El tipo de cliente no se puede eliminar porque otros registros dependen de este';
    ELSEIF cUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de cliente que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_cliente 
        WHERE idTipoCliente = P_ID;

        SET @MSJ = 'Se eliminó correctamente al tipo de cliente';
    END IF;
END $$

DELIMITER ;

-- Procedimiento para actualizar cliente
DELIMITER $$

CREATE PROCEDURE SP_ACTUALIZAR_CLIENTE (
    IN p_id INT,
    IN p_id_pais INT,
    IN p_id_tipo_cliente INT,
    IN p_id_tipo_doc INT,
    IN p_numero_documento VARCHAR(20),
    IN p_nombres VARCHAR(90),
    IN p_ape_paterno VARCHAR(50),
    IN p_ape_materno VARCHAR(50),
    IN p_sexo TINYINT,
    IN p_f_nacimiento DATE,
    IN p_razon_social VARCHAR(90),
    IN p_direccion VARCHAR(70),
    IN p_telefono VARCHAR(13),
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(256),
    IN p_usuario VARCHAR(100),
    OUT MSJ VARCHAR(100),
    OUT MSJ2 VARCHAR(100)
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SET MSJ = NULL;
        SET MSJ2 = 'Error al actualizar cliente';
    END;

    UPDATE cliente
    SET id_pais = p_id_pais,
        id_tipo_cliente = p_id_tipo_cliente,
        id_tipo_doc = p_id_tipo_doc,
        numero_documento = p_numero_documento,
        nombres = p_nombres,
        ape_paterno = p_ape_paterno,
        ape_materno = p_ape_materno,
        sexo = p_sexo,
        f_nacimiento = p_f_nacimiento,
        razon_social = p_razon_social,
        direccion = p_direccion,
        telefono = p_telefono,
        email = p_email,
        usuario = p_usuario
    WHERE id = p_id;

    IF p_password IS NOT NULL AND LENGTH(p_password) > 0 THEN
        UPDATE cliente
        SET password = p_password
        WHERE id = p_id;
    END IF;

    SET MSJ = 'Cliente actualizado correctamente';
    SET MSJ2 = NULL;
END $$

-- Procedimiento para insertar tipo de comprobante
CREATE PROCEDURE SP_INSERTAR_TIPO_COMPROBANTE(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_comprobante
    WHERE nombre = P_NOMBRE;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de comprobante con ese nombre';
    ELSE
        INSERT INTO tipo_comprobante (
            nombre, estado, usuario
        ) VALUES (
            P_NOMBRE, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el tipo de comprobante';
    END IF;
END $$

DELIMITER ;

-- Actualizar tipo de comprobante
DELIMITER $$

CREATE PROCEDURE SP_ACTUALIZAR_TIPO_COMPROBANTE(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cExiste INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_comprobante 
    WHERE idTipoComprobante = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM tipo_comprobante 
    WHERE nombre = P_NOMBRE AND idTipoComprobante != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de comprobante que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_comprobante 
        SET nombre = P_NOMBRE, estado = P_ESTADO
        WHERE idTipoComprobante = P_ID;

        SET @MSJ = 'Se actualizó correctamente el tipo de comprobante';
    END IF;
END $$

-- Dar de baja tipo de comprobante
CREATE PROCEDURE SP_DAR_BAJA_TIPO_COMPROBANTE(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_comprobante 
    WHERE idTipoComprobante = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de comprobante que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_comprobante 
        SET estado = 0
        WHERE idTipoComprobante = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al tipo de comprobante';
    END IF;
END $$

-- Eliminar tipo de comprobante
CREATE PROCEDURE SP_ELIMINAR_TIPO_COMPROBANTE(
    IN P_ID INT
)
BEGIN
    DECLARE cUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM tipo_comprobante 
    WHERE idTipoComprobante = P_ID;

    IF EXISTS (SELECT 1 FROM venta WHERE idTipoComprobante = P_ID) THEN
        SET @MSJ2 = 'El tipo de comprobante no se puede eliminar porque otros registros dependen de este';
    ELSEIF cUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de comprobante que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_comprobante 
        WHERE idTipoComprobante = P_ID;

        SET @MSJ = 'Se eliminó correctamente el tipo de comprobante';
    END IF;
END $$

DELIMITER ;

-- Insertar microservicio
DELIMITER $$

CREATE PROCEDURE SP_INSERTAR_MICROSERVICIO(
    IN P_NOMBRE VARCHAR(50),
    IN P_DESP VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM microservicio
    WHERE nombre = P_NOMBRE;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un microservicio con ese nombre';
    ELSE
        INSERT INTO microservicio (
            nombre, descripcion, estado, usuario
        ) VALUES (
            P_NOMBRE, P_DESP, P_ESTADO, P_USUARIO
        );

        SET @MSJ = 'Se registró correctamente el microservicio';
    END IF;
END $$

-- Actualizar microservicio
CREATE PROCEDURE SP_ACTUALIZAR_MICROSERVICIO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_DESP VARCHAR(255),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cExiste INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM microservicio 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM microservicio 
    WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el microservicio que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre del microservicio ingresado ya existe';
    ELSE
        UPDATE microservicio 
        SET nombre = P_NOMBRE, descripcion = P_DESP, estado = P_ESTADO 
        WHERE id = P_ID;

        SET @MSJ = 'Se actualizó correctamente el microservicio';
    END IF;
END $$

-- Dar de baja microservicio
CREATE PROCEDURE SP_DAR_BAJA_MICROSERVICIO(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM microservicio 
    WHERE id = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El microservicio que intenta dar de baja no existe';
    ELSE
        UPDATE microservicio 
        SET estado = 0 
        WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al microservicio';
    END IF;
END $$

DELIMITER ;

-- Eliminar microservicio
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_MICROSERVICIO(
    IN P_ID INT
)
BEGIN 
    DECLARE cUsuario INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario 
    FROM microservicio 
    WHERE id = P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El microservicio que intenta eliminar no existe';
    ELSE
        DELETE FROM servicio_microservicio WHERE idMicroservicio = P_ID;
        DELETE FROM microservicio WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente el microservicio';
    END IF;
END $$

-- Insertar servicio
CREATE PROCEDURE SP_INSERTAR_SERVICIO(
    IN P_NOMBRE VARCHAR(50),
    IN P_DESCRIPCION VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100),
    IN P_IMAGEN TEXT
)
BEGIN
    DECLARE existe_nombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO existe_nombre 
    FROM servicio 
    WHERE nombre = P_NOMBRE;

    IF existe_nombre = 0 THEN
        INSERT INTO servicio (
            nombre, descripcion, estado, usuario, imagen
        ) VALUES (
            P_NOMBRE, P_DESCRIPCION, P_ESTADO, P_USUARIO, P_IMAGEN
        );

        SET @MSJ = 'Se registró correctamente el servicio';
    ELSE
        SET @MSJ2 = 'Ya existe un servicio con ese nombre registrado';
    END IF;
END $$

-- Actualizar servicio
CREATE PROCEDURE SP_ACTUALIZAR_SERVICIO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_DESCRIPCION VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_IMAGEN TEXT
)
BEGIN
    DECLARE existe_nombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO existe_nombre 
    FROM servicio 
    WHERE nombre = P_NOMBRE AND id != P_ID;

    IF existe_nombre = 0 THEN
        UPDATE servicio 
        SET nombre = P_NOMBRE,
            descripcion = P_DESCRIPCION,
            estado = P_ESTADO,
            imagen = P_IMAGEN
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente el servicio';
    ELSE
        SET @MSJ2 = 'Ya existe un servicio con ese nombre registrado';
    END IF;
END $$

-- Dar de baja servicio
CREATE PROCEDURE SP_BAJA_SERVICIO(
    IN P_ID INT
)
BEGIN
    DECLARE existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO existe 
    FROM servicio 
    WHERE id = P_ID;

    IF existe <= 0 THEN
        SET @MSJ2 = 'El servicio al que intenta dar de baja no existe';
    ELSE
        UPDATE servicio 
        SET estado = 0 
        WHERE id = P_ID;

        SET @MSJ = 'Servicio dado de baja correctamente';
    END IF;
END $$

-- Eliminar servicio (físicamente)
CREATE PROCEDURE SP_DELETE_SERVICIO(
    IN P_ID INT
)
BEGIN
    DECLARE existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO existe 
    FROM servicio 
    WHERE id = P_ID;

    IF existe <= 0 THEN
        SET @MSJ2 = 'El servicio al que intenta eliminar no existe';
    ELSE
        DELETE FROM servicio_microservicio WHERE idServicio = P_ID;
        DELETE FROM servicio WHERE id = P_ID;

        SET @MSJ = 'Servicio eliminado correctamente';
    END IF;
END $$

DELIMITER ;

-- Registrar método de pago
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_METODO_PAGO(
    IN P_NOMBRE VARCHAR(100),
    IN P_LOGO VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100),
    IN P_TIPO_METODO_PAGO INT,
    IN P_QR VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre 
    FROM metodo_pago 
    WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El método de pago que intenta registrar ya está registrado';
    ELSE
        INSERT INTO metodo_pago (
            nombre, logo, estado, fecha_registro, usuario, qr, id_tipo_metodoPago
        ) VALUES (
            P_NOMBRE, P_LOGO, P_ESTADO, CURRENT_TIMESTAMP, P_USUARIO, P_QR, P_TIPO_METODO_PAGO
        );

        SET @MSJ = 'Se registró correctamente el método de pago';
    END IF;
END $$

-- Editar método de pago
CREATE PROCEDURE SP_EDITAR_METODO_PAGO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(100),
    IN P_LOGO VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_TIPO_METODO_PAGO INT,
    IN P_QR VARCHAR(255)
)
BEGIN
    DECLARE cMetodoPago INT;
    DECLARE cNombre INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMetodoPago 
    FROM metodo_pago 
    WHERE id = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM metodo_pago 
    WHERE nombre = P_NOMBRE AND id != P_ID;

    IF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre del método de pago ingresado ya existe';
    ELSE
        UPDATE metodo_pago 
        SET nombre = P_NOMBRE, 
            logo = P_LOGO,
            estado = P_ESTADO,
            qr = P_QR,
            id_tipo_metodoPago = P_TIPO_METODO_PAGO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente el método de pago';
    END IF;
END $$

-- Dar de baja método de pago
CREATE PROCEDURE SP_DARBAJA_METODO_PAGO(
    IN P_ID INT
)
BEGIN
    DECLARE cMetodoPago INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMetodoPago 
    FROM metodo_pago 
    WHERE id = P_ID;

    IF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta dar de baja no existe';
    ELSE
        UPDATE metodo_pago 
        SET estado = 0 
        WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente el método de pago';
    END IF;
END $$

-- Eliminar método de pago
CREATE PROCEDURE SP_ELIMINAR_METODO_PAGO(
    IN P_ID INT
)
BEGIN
    DECLARE cMetodoPago INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMetodoPago 
    FROM metodo_pago 
    WHERE id = P_ID;

    IF EXISTS (SELECT 1 FROM venta WHERE idMetodoPago = P_ID) THEN
        SET @MSJ2 = 'El método de no se puede eliminar porque otros registros dependen de este';
    ELSEIF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta eliminar no existe';
    ELSE
        DELETE FROM metodo_pago 
        WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente el método de pago';
    END IF;
END $$

DELIMITER ;

    

-- Crear procedimiento SP_REGISTRAR_RUTA
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_RUTA(
    IN P_NOMBRE VARCHAR(255),
    IN P_DISTANCIA DECIMAL(9,2),
    IN P_TIEMPO DECIMAL(9,2),
    IN P_ESTADO BOOLEAN,
    IN P_TIPO VARCHAR(255),
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cNombre INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM ruta WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre de ruta que intenta registrar ya está registrado';
    ELSE
        INSERT INTO ruta (NOMBRE, DISTANCIA_ESTIMADA, TIEMPO_ESTIMADO, TIPO, ESTADO, USUARIO) 
        VALUES (P_NOMBRE, P_DISTANCIA, P_TIEMPO, P_TIPO, P_ESTADO, P_USUARIO);
        SET @MSJ = 'Se registró correctamente la ruta';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_EDITAR_RUTA
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_RUTA(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_DISTANCIA DECIMAL(9,2),
    IN P_TIEMPO DECIMAL(9,2),
    IN P_TIPO VARCHAR(255),
    IN P_ESTADO BOOLEAN
)
BEGIN
    DECLARE cNombre INT;
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;
    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID;
    SELECT COUNT(*) INTO cNombre FROM ruta WHERE NOMBRE = P_NOMBRE AND ID != P_ID;
    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE ruta 
        SET NOMBRE = P_NOMBRE,
            DISTANCIA_ESTIMADA = P_DISTANCIA,
            TIEMPO_ESTIMADO = P_TIEMPO,
            TIPO = P_TIPO,
            ESTADO = P_ESTADO
        WHERE ID = P_ID;
        SET @MSJ = 'Se modificó correctamente la ruta';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_RUTA
DELIMITER $$
CREATE PROCEDURE SP_DARBAJA_RUTA(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID;

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta dar de baja no existe';
    ELSE
        UPDATE ruta SET ESTADO = 0 WHERE ID = P_ID;
        SET @MSJ = 'Se dio de baja correctamente a la ruta';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_RUTA
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_RUTA(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID;

    IF EXISTS (SELECT 1 FROM viaje WHERE idRuta = P_ID) THEN
        SET @MSJ2 = 'La ruta seleccionada no se puede eliminar porque otros registros dependen de este';
    ELSEIF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta eliminar no existe';
    ELSE
        DELETE FROM escala WHERE idRuta = P_ID;
        DELETE FROM ruta WHERE id = P_ID;
        SET @MSJ = 'Se eliminó correctamente a la ruta';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_PERSONAL
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_PERSONAL(
    IN P_NOMBRE VARCHAR(255),
    IN P_IMAGEN VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_IDTIPOPERSONAL INT,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

        INSERT INTO personal (NOMBRE, IMAGEN, ESTADO, ID_TIPOPERSONAL, USUARIO) 
        VALUES (P_NOMBRE, P_IMAGEN, P_ESTADO, P_IDTIPOPERSONAL, P_USUARIO);
        SET @MSJ = 'Se registró correctamente al personal';
END $$
DELIMITER ;

-- Crear procedimiento SP_EDITAR_PERSONAL
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_PERSONAL(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
    IN P_IMAGEN VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_IDTIPOPERSONAL INT
)
BEGIN
    DECLARE cPersonal INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID;

    IF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta editar no existe';
    ELSE
        UPDATE personal 
        SET NOMBRE = P_NOMBRE,
            IMAGEN = P_IMAGEN,
            ESTADO = P_ESTADO,
            ID_TIPOPERSONAL = P_IDTIPOPERSONAL
        WHERE ID = P_ID;
        SET @MSJ = 'Se modificó correctamente al personal';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_PERSONAL
DELIMITER $$
CREATE PROCEDURE SP_DARBAJA_PERSONAL(
    IN P_ID INT
)
BEGIN
    DECLARE cPersonal INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID;
    IF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta dar de baja no existe';
    ELSE
        UPDATE personal SET ESTADO = 0 WHERE ID = P_ID;
        SET @MSJ = 'Se dio de baja correctamente al personal';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_PERSONAL
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_PERSONAL(
    IN P_ID INT
)
BEGIN
    DECLARE cPersonal INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID;
    
    IF EXISTS (SELECT 1 FROM detalle_personal WHERE idPersonal = P_ID) THEN
        SET @MSJ2 = 'El personal seleccionado no se puede eliminar porque otros registros dependen de este';
    ELSEIF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta eliminar no existe';
    ELSE
        DELETE FROM personal WHERE ID = P_ID;
        SET @MSJ = 'Se eliminó correctamente al personal';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_INSERTAR_TIPO_METODOPAGO
DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_TIPO_METODOPAGO(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_metodoPago
    WHERE nombre = P_NOMBRE AND estado = 1;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de método de pago con ese nombre';
    ELSE
        INSERT INTO tipo_metodoPago (nombre, estado, usuario)
        VALUES (P_NOMBRE, P_ESTADO, P_USUARIO);
        SET @MSJ = 'Se registró correctamente el tipo de método de pago';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_TIPO_METODOPAGO
DELIMITER $$
CREATE PROCEDURE SP_ACTUALIZAR_TIPO_METODOPAGO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE cNombre INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_metodoPago 
    WHERE idTipoMetodoPago = P_ID;

    SELECT COUNT(*) INTO cNombre 
    FROM tipo_metodoPago 
    WHERE nombre = P_NOMBRE AND idTipoMetodoPago != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de método de pago que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_metodoPago 
        SET nombre = P_NOMBRE,
            estado = P_ESTADO,
            usuario = P_USUARIO
        WHERE idTipoMetodoPago = P_ID;
        SET @MSJ = 'Se actualizó correctamente el tipo de método de pago';
    END IF;
END $$
DELIMITER ;
-- Crear procedimiento SP_DAR_BAJA_TIPO_METODOPAGO
DELIMITER $$
CREATE PROCEDURE SP_DAR_BAJA_TIPO_METODOPAGO(
    IN P_ID INT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_metodoPago 
    WHERE idTipoMetodoPago = P_ID AND estado = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de método de pago no existe o ya fue dado de baja';
    ELSE
        UPDATE tipo_metodoPago 
        SET estado = 0,
            usuario = P_USUARIO
        WHERE idTipoMetodoPago = P_ID;
        SET @MSJ = 'Se dio de baja correctamente el tipo de método de pago';
    END IF;
END $$
DELIMITER ;
-- Crear Procedimiento SP_ELIMINAR_TIPO_METODOPAGO
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_TIPO_METODOPAGO(
    IN P_ID INT
)
BEGIN 
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar el procedimiento almacenado';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_metodoPago 
    WHERE idTipoMetodoPago = P_ID;

    IF EXISTS (SELECT 1 FROM metodo_pago WHERE id_tipo_metodoPago = P_ID) THEN
        SET @MSJ2 = 'El tipo de método de pago seleccionado no se puede eliminar porque otros registros dependen de este';
    ELSEIF cExiste <= 0 THEN
        SET @MSJ2 = 'El tipo de método de pago que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_metodoPago 
        WHERE idTipoMetodoPago = P_ID;
        SET @MSJ = 'Se eliminó correctamente el tipo de método de pago';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_INSERTAR_PASAJE
DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_PASAJE(
    IN P_idDetalleViajeAsiento INT,
    IN P_numeroComprobante CHAR(13),
    IN P_esPasajeNormal TINYINT,
    IN P_esPasajeLibre TINYINT,
    IN P_esTransferencia TINYINT,
    IN P_esReserva TINYINT,
    IN P_esCambioRuta TINYINT,
    IN P_idVenta INT,
    IN P_codigo CHAR(8),
    IN P_idPasaje INT
)
BEGIN
    DECLARE cExist INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al registrar el pasaje';
    END;
    SET @MSJ = NULL; SET @MSJ2 = NULL;

    -- Verificar duplicado por detalle+comprobante
    SELECT COUNT(*) INTO cExist
      FROM pasaje
     WHERE idDetalleViajeAsiento = P_idDetalleViajeAsiento
       AND numeroComprobante     = P_numeroComprobante;

    IF cExist > 0 THEN
        SET @MSJ2 = 'El pasaje ya existe';
    ELSE
        INSERT INTO pasaje (
            idDetalleViajeAsiento,
            numeroComprobante,
            esPasajeNormal,
            esPasajeLibre,
            esTransferencia,
            esReserva,
            esCambioRuta,
            idVenta,
            codigo,
            idPasaje
        ) VALUES (
            P_idDetalleViajeAsiento,
            P_numeroComprobante,
            P_esPasajeNormal,
            P_esPasajeLibre,
            P_esTransferencia,
            P_esReserva,
            P_esCambioRuta,
            P_idVenta,
            P_codigo,
            P_idPasaje
        );
        SET @MSJ = 'Pasaje registrado correctamente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_MODIFICAR_PASAJE
DELIMITER $$
CREATE PROCEDURE SP_MODIFICAR_PASAJE(
    IN P_id INT,
    IN P_idDetalleViajeAsiento INT,
    IN P_numeroComprobante CHAR(13),
    IN P_esPasajeNormal TINYINT,
    IN P_esPasajeLibre TINYINT,
    IN P_esTransferencia TINYINT,
    IN P_esReserva TINYINT,
    IN P_esCambioRuta TINYINT,
    IN P_idVenta INT,
    IN P_codigo CHAR(8),
    IN P_idPasaje INT
)
BEGIN
    DECLARE cExist INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al modificar el pasaje';
    END;
    SET @MSJ = NULL; SET @MSJ2 = NULL;

    -- Verificar existencia
    SELECT COUNT(*) INTO cExist FROM pasaje WHERE id = P_id;
    IF cExist = 0 THEN
        SET @MSJ2 = 'El pasaje que intenta modificar no existe';
    ELSE
        UPDATE pasaje
           SET idDetalleViajeAsiento = P_idDetalleViajeAsiento,
               numeroComprobante     = P_numeroComprobante,
               esPasajeNormal        = P_esPasajeNormal,
               esPasajeLibre         = P_esPasajeLibre,
               esTransferencia       = P_esTransferencia,
               esReserva             = P_esReserva,
               esCambioRuta          = P_esCambioRuta,
               idVenta               = P_idVenta,
               codigo                = P_codigo,
               idPasaje              = P_idPasaje
         WHERE id = P_id;
        SET @MSJ = 'Pasaje modificado correctamente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_PASAJE
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_PASAJE(
    IN P_id INT
)
BEGIN
    DECLARE cExist INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al eliminar el pasaje';
    END;
    SET @MSJ = NULL; SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExist FROM pasaje WHERE id = P_id;
    IF cExist = 0 THEN
        SET @MSJ2 = 'El pasaje que intenta eliminar no existe';
    ELSE
        DELETE FROM pasaje WHERE id = P_id;
        SET @MSJ = 'Pasaje eliminado correctamente';
    END IF;
END $$
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SP_CAMBIAR_ESTADO_PASAJE(
    IN  p_idPasaje INT,
    OUT p_MSJ    VARCHAR(255),
    OUT p_MSJ2   VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre cualquier error, devolvemos mensaje de error
        SET p_MSJ  = '';
        SET p_MSJ2 = 'Error al cambiar el estado del pasaje';
    END;

    -- Actualizamos los flags: ponemos PasajeNormal=1 y el resto a 0
    UPDATE pasaje
    SET 
        esPasajeNormal  = 1,
        esPasajeLibre   = 0,
        esTransferencia = 0,
        esReserva       = 0,
        esCambioRuta    = 0
    WHERE id = p_idPasaje;

    -- Comprobamos si realmente se actualizó alguna fila
    IF ROW_COUNT() = 0 THEN
        SET p_MSJ  = '';
        SET p_MSJ2 = CONCAT('No se encontró pasaje con id=', p_idPasaje);
    ELSE
        SET p_MSJ  = 'El pasaje se marcó como Normal correctamente.';
        SET p_MSJ2 = '';
    END IF;
END$$

DELIMITER ;


-- Procedimientos almacenados para reclamo y tipo reclamo
DELIMITER $$

CREATE PROCEDURE SP_INSERTAR_TIPO_RECLAMO(
    IN p_nombre VARCHAR(100),
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    SELECT COUNT(*) INTO v_count
    FROM tipo_reclamo
    WHERE nombre = p_nombre;

    IF v_count > 0 THEN
        SET MSJ2 = 'Ya existe un tipo_reclamo con ese nombre';
    ELSE
        INSERT INTO tipo_reclamo (nombre,estado)
        VALUES (p_nombre,1);
        SET MSJ = 'Tipo_reclamo insertado correctamente';
    END IF;
END$$

CREATE PROCEDURE SP_MODIFICAR_TIPO_RECLAMO(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_estado TINYINT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

        SET MSJ  = NULL;
        SET MSJ2 = NULL;

        SELECT COUNT(*) INTO v_count
        FROM tipo_reclamo
        WHERE nombre = p_nombre
        AND id <> p_id;

    IF v_count > 0 THEN
        SET MSJ2 = 'Ya existe un tipo_reclamo con ese nombre';
    ELSE
        UPDATE tipo_reclamo
           SET nombre = p_nombre, estado = p_estado
         WHERE id = p_id;
        SET MSJ = 'Tipo_reclamo modificado correctamente';
    END IF;
END$$

CREATE PROCEDURE SP_ELIMINAR_TIPO_RECLAMO(
    IN p_id INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    IF EXISTS (SELECT 1 FROM reclamo WHERE id_tipo_reclamo = p_id) THEN
        SET MSJ2 = 'El tipo reclamo no se puede eliminar porque otros registros dependen de este';
    ELSE
        DELETE FROM tipo_reclamo
        WHERE id = p_id;
        SET MSJ = 'Tipo reclamo eliminado correctamente';
    END IF;
END$$

CREATE PROCEDURE SP_DARBAJA_TIPO_RECLAMO (
    IN p_id INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    UPDATE tipo_reclamo SET estado=0 WHERE id = p_id;
    SET MSJ = 'Tipo de reclamo dado de baja correctamente';
END$$

CREATE PROCEDURE SP_INSERTAR_RECLAMO(
    IN p_tipo_reclamo INT,
    IN p_detalle TEXT,
    IN p_monto DECIMAL(9,2),
    IN p_idPasaje INT,
    IN p_motivo TEXT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    INSERT INTO reclamo (id_tipo_reclamo, detalle, monto, idPasaje, motivo,estado)
    VALUES (p_tipo_reclamo, p_detalle, p_monto, p_idPasaje, p_motivo,1);
    SET MSJ = 'Reclamo insertado correctamente';
END$$

CREATE PROCEDURE SP_MODIFICAR_RECLAMO(
    IN p_id INT,
    IN p_tipo_reclamo INT,
    IN p_detalle TEXT,
    IN p_monto DECIMAL(9,2),
    IN p_idPasaje INT,
    IN p_motivo TEXT,
    IN p_estado TINYINT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    UPDATE reclamo
    SET id_tipo_reclamo = p_tipo_reclamo,
        detalle       = p_detalle,
        monto         = p_monto,
        idPasaje      = p_idPasaje,
        motivo        = p_motivo,
        estado        = p_estado
    WHERE id = p_id;
        SET MSJ = 'Reclamo modificado correctamente';
END$$

CREATE PROCEDURE SP_ELIMINAR_RECLAMO(
    IN p_id INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    DELETE FROM reclamo
    WHERE id = p_id;
    SET MSJ = 'Reclamo eliminado correctamente';
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SP_DARBAJA_RECLAMO(
    IN  p_id   INT,
    OUT MSJ    VARCHAR(255),
    OUT MSJ2   VARCHAR(255)
)
BEGIN
    DECLARE v_existe INT;

    -- Captura cualquier error inesperado
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            MSJ2 = MESSAGE_TEXT;
        SET MSJ = NULL;
    END;

    -- Inicializar mensajes
    SET MSJ  = NULL;
    SET MSJ2 = NULL;

    -- Verificar si el reclamo existe
    SELECT COUNT(*) INTO v_existe
    FROM reclamo
    WHERE id = p_id;

    IF v_existe <= 0 THEN
        SET MSJ2 = 'El reclamo que intenta dar de baja no existe';
    ELSE
        -- Dar de baja (baja lógica)
        UPDATE reclamo
        SET estado = 0
        WHERE id = p_id;

        SET MSJ = 'Se dio de baja correctamente el reclamo';
    END IF;
END$$

DELIMITER ;

-- SP para registrar una promoción
DELIMITER $$

CREATE PROCEDURE SP_REGISTRAR_PROMOCION (
    IN p_nombre VARCHAR(100),
    IN p_estado TINYINT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_codigo CHAR(8),
    IN p_monto_promo DECIMAL(9,2)
)
BEGIN
    IF EXISTS (SELECT 1 FROM promocion WHERE codigo = p_codigo) THEN
        SET @MSJ2 = 'Ya existe una promoción con ese código';
        
    ELSEIF p_fecha_fin < p_fecha_inicio THEN
        SET @MSJ2 = 'La fecha de fin no puede ser anterior a la fecha de inicio';
        
    ELSE
        INSERT INTO promocion (nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo)
        VALUES (p_nombre, p_estado, p_fecha_inicio, p_fecha_fin, p_codigo, p_monto_promo);

        SET @MSJ = 'Promoción registrada correctamente';
    END IF;
END$$

DELIMITER ;

-- SP para editar una promoción
DELIMITER $$

CREATE PROCEDURE SP_EDITAR_PROMOCION (
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_estado TINYINT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_codigo CHAR(8),
    IN p_monto_promo DECIMAL(9,2)
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM promocion WHERE codigo = p_codigo AND id != p_id
    ) THEN
        SET @MSJ2 = 'El código ya está registrado en otra promoción';
    ELSEIF p_fecha_fin < p_fecha_inicio THEN
        SET @MSJ2 = 'La fecha de fin no puede ser anterior a la fecha de inicio';
    ELSE
        UPDATE promocion
        SET nombre = p_nombre,
            estado = p_estado,
            fecha_inicio = p_fecha_inicio,
            fecha_fin = p_fecha_fin,
            codigo = p_codigo,
            monto_promo = p_monto_promo
        WHERE id = p_id;

        SET @MSJ = 'Promoción actualizada correctamente';
    END IF;
END$$

DELIMITER ;

-- SP para dar de baja una promoción
DELIMITER $$

CREATE PROCEDURE SP_DAR_BAJA_PROMOCION (
    IN p_id INT
)
BEGIN
    UPDATE promocion SET estado = 0 WHERE id = p_id;

    SET @MSJ = 'Promoción dada de baja correctamente';
END$$

DELIMITER ;

-- SP para eliminar una promoción
DELIMITER $$

CREATE PROCEDURE SP_ELIMINAR_PROMOCION (
    IN p_id INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM venta WHERE idPromocion = p_id) THEN
        SET @MSJ2 = 'La promoción no se puede eliminar porque otros registros dependen de este';
    ELSE
        DELETE FROM promocion WHERE id = p_id;
        SET @MSJ = 'Promoción eliminada correctamente';
    END IF;
END$$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_MARCA
DELIMITER $$ 
CREATE PROCEDURE SP_REGISTRAR_MARCA(
    IN P_NOMBRE VARCHAR(100),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100),
    IN P_LOGO VARCHAR(255) -- Parámetro para el logo
)
BEGIN
    DECLARE cNombre INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;
    
    SET @MSJ = NULL;
    SET @MSJ2 = NULL;
    
    SELECT COUNT(*) INTO cNombre FROM marca WHERE NOMBRE = P_NOMBRE;
    IF cNombre > 0 THEN
        SET @MSJ2 = 'La marca ya está registrada';
    ELSE
        INSERT INTO marca (NOMBRE, ESTADO, FECHA_REGISTRO, USUARIO, LOGO) 
        VALUES (P_NOMBRE, P_ESTADO, CURRENT_TIMESTAMP, P_USUARIO, P_LOGO); -- Incluir logo
        SET @MSJ = 'Marca registrada correctamente';
    END IF;
END $$ 

-- Crear procedimiento SP_EDITAR_MARCA
DELIMITER $$ 
CREATE PROCEDURE SP_EDITAR_MARCA(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(100),
    IN P_ESTADO BOOLEAN,
    IN P_LOGO VARCHAR(255) -- Parámetro para el logo
)
BEGIN
    DECLARE cMarca INT;
    DECLARE cNombre INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION

    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID;
    SELECT COUNT(*) INTO cNombre FROM marca WHERE NOMBRE = P_NOMBRE AND ID != P_ID;

    IF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre de la marca ya existe';
    ELSE
        UPDATE marca 
        SET NOMBRE = P_NOMBRE, 
            ESTADO = P_ESTADO,
            LOGO = P_LOGO -- Actualizar logo
        WHERE ID = P_ID;
        SET @MSJ = 'Marca modificada correctamente';
    END IF;
END $$ 

-- Crear procedimiento SP_DARBAJA_MARCA
DELIMITER $$ 
CREATE PROCEDURE SP_DARBAJA_MARCA(
    IN P_ID INT
)
BEGIN
    DECLARE cMarca INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 

    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID;

    IF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSE
        UPDATE marca 
        SET ESTADO = 0
        WHERE ID = P_ID;
        SET @MSJ = 'Marca dada de baja correctamente';
    END IF;
END $$ 

-- Crear procedimiento SP_ELIMINAR_MARCA
DELIMITER $$ 
CREATE PROCEDURE SP_ELIMINAR_MARCA(
    IN P_ID INT
)
BEGIN
    DECLARE cMarca INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID;

    IF EXISTS (SELECT 1 FROM tipo_vehiculo WHERE id_marca = P_ID) THEN
        SET @MSJ2 = 'No se puede eliminar la marca porque otros registros dependen de este';
    ELSEIF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSE
        DELETE FROM marca WHERE ID = P_ID;
        SET @MSJ = 'Marca eliminada correctamente';
    END IF;
END $$ 
