-- Primero eliminamos los procedimientos por si existen
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
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE_NATURAL;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_CLIENTE_JURIDICO;

DROP PROCEDURE IF EXISTS SP_EDITAR_CLIENTE_NATURAL;
DROP PROCEDURE IF EXISTS SP_EDITAR_CLIENTE_JURIDICO;

DROP PROCEDURE IF EXISTS SP_DARBAJA_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_CLIENTE;

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


DROP PROCEDURE IF EXISTS SP_CAMBIAR_CLAVE;
-- Luego eliminamos las tablas, primero la que depende de la otra
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
DROP TABLE IF EXISTS tipo_cliente;
DROP TABLE IF EXISTS ubigeo;
DROP TABLE IF EXISTS metodo_pago;
DROP TABLE IF EXISTS personal;
DROP TABLE IF EXISTS tipo_personal;
DROP TABLE IF EXISTS tipo_comprobante;
DROP TABLE IF EXISTS tipo_documento;
DROP TABLE IF EXISTS nivel_herramienta;
DROP TABLE IF EXISTS nivel;
DROP TABLE IF EXISTS vehiculo;
DROP TABLE IF EXISTS tipo_vehiculo;
DROP TABLE IF EXISTS servicio;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS ruta;
DROP TABLE IF EXISTS ciudad;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS pais;
DROP TABLE IF EXISTS herramienta;
DROP TABLE IF EXISTS tipo_herramienta;
DROP TABLE IF EXISTS tipo_metodoPago;


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
    estado BIT NOT NULL,
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

CREATE TABLE tipo_documento(
    id int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    abreviatura varchar(10) NOT NULL,
    estado BOOLEAN NOT NULL,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla tipo_cliente
CREATE TABLE tipo_cliente (
    idTipoCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
);

-- Crear tabla tipo_usuario
CREATE TABLE tipo_usuario (
    id int AUTO_INCREMENT PRIMARY key,
    nombre varchar(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
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
    id_tipousuario INT not null REFERENCES tipo_usuario (id),
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
    usuario VARCHAR(100) not null
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
    estado_proceso varchar(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro int(11) NOT NULL,
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

-- Crear tabla ruta
CREATE TABLE ruta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT 1,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

-- Crear tabla escala
CREATE TABLE escala (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nro_orden INT NOT NULL,
    idSucursal INT NOT NULL,
    idRuta INT NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (idSucursal) REFERENCES sucursal (id),
    FOREIGN KEY (idRuta) REFERENCES ruta (id)
);

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    id_pais INT NOT NULL,
    id_tipo_cliente INT NOT NULL,
    id_tipo_doc INT NOT NULL,
    
    numero_documento VARCHAR(20) NOT NULL, -- UNIQUE,
    
    nombres VARCHAR(90),
    ape_paterno VARCHAR(50),
    ape_materno VARCHAR(50),
        
    sexo TINYINT DEFAULT 0, -- 'O' para otros/no especificado
    f_nacimiento DATE,
    
    razon_social VARCHAR(90),
    direccion VARCHAR(70),
    
    telefono VARCHAR(13), -- Ej: +51912345678
    email VARCHAR(100) NOT NULL,
    password VARCHAR(256) NOT NULL, -- SHA-256 hash
    estado TINYINT DEFAULT 1,
    
    fechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

CREATE TABLE asiento (
    id INT AUTO_INCREMENT PRIMARY KEY,

    nro_asiento SMALLINT  NOT NULL,  -- Hasta 9999
    id_nivel TINYINT NOT NULL,

    tipo_asiento VARCHAR(30) NOT NULL,

    estado TINYINT NOT NULL CHECK (estado IN (0, 1, 2, 3)),

    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) NOT NULL
);

CREATE TABLE tipo_vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    id_marca INT NULL,
    id_servicio INT NOT NULL,
    estado BOOLEAN NOT NULL,
    cantidad INT NOT NULL,
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
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
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
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
    estado BIT NOT NULL,
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
    id_tipo INT REFERENCES tipo_herramienta(id)
);

CREATE TABLE nivel_herramienta(
    id int AUTO_INCREMENT PRIMARY KEY,
    id_herramienta int REFERENCES herramienta(id),
    id_nivel int REFERENCES nivel(id),
    x_dimension int not null,
    y_dimension int not null
 
);

-- INSERT TIPO CLIENTE
INSERT INTO tipo_cliente (nombre, estado, usuario)
VALUES 
('Bebé', TRUE, 'admin'),
('Niño', TRUE, 'admin'),
('Adulto', TRUE, 'admin');

-- INSERT TIPO DOCUMENTO
INSERT INTO tipo_documento (nombre, abreviatura, estado, usuario)
VALUES ('DOCUMENTO NACIONAL DE IDENTIFICACION', 'DNI', TRUE, 'admin');
INSERT INTO tipo_documento (nombre, abreviatura, estado, usuario)
VALUES ('REGISTRO UNICO DE CONTRIBUYENTE', 'RUC', TRUE, 'admin');


-- INSERT SERVICIO
insert into servicio values (1,'Premium','Los autobuses más modernos y lujosos del mercado. Asientos cama, entretenimiento a bordo, snacks incluidos, aire acondicionado y cargadores USB. Ideal para viajes de largo trayecto.',1,'2025-05-25 19:30:00','Alexis','Static/img/servicios/busPremium.png');
insert into servicio values (2,'Económico','Autobuses cómodos y seguros a precios accesibles. Pensado para usuarios que priorizan economía sin perder calidad.',1,'2025-05-25 19:32:00','Alexis','Static/img/servicios/busEconomico.png');
insert into servicio values (3,'Exprés','Servicios rápidos con pocas paradas. Unidades modernas y seguras para viajeros que buscan llegar en el menor tiempo posible.',1,'2025-05-25 19:40:00','Alexis','Static/img/servicios/busExpress.png');

-- INSERT MARCA

INSERT INTO `marca` (`id`,`nombre`, `logo`, `estado`, `estado_proceso`, `estado_registro`, `fecha_registro`, `usuario`) 
VALUES (1,'Mercedes-Benz', '/Static/img/marca/MercedesBenz.png', '1', 'REGISTRADO', '1', '2025-05-26 11:40:29', 'edgar@gmail.com'), 
(2,'Dodge', '/Static/img/marca/Dodge.png', '1', 'REGISTRADO', '1', '2025-05-26 11:40:50', 'edgar@gmail.com'), 
(3,'Volkswagen','/Static/img/marca/Volkswagen.png', '1', 'REGISTRADO', '1', '2025-05-26 11:41:09', 'edgar@gmail.com'), 
(4,'Hyundai','/Static/img/marca/Hyundai.png', '1', 'REGISTRADO', '1', '2025-05-26 11:41:28', 'edgar@gmail.com');

-- INSERT TIPO_VEHICULO
INSERT INTO `tipo_vehiculo` (`id`, `nombre`, `id_marca`, `id_servicio`, `estado`, `cantidad`, `fecha_registro`, `usuario`) 
VALUES (1, 'Solati H350', '4', '1', '1', '0', '2025-05-26 11:57:29', 'edgar@gmail.com'),
(2, 'County bus', '4', '1', '1', '0', '2025-05-26 11:58:51', 'edgar@gmail.com'),
(3, 'Volksbus', '3', '2', '1', '0', '2025-05-26 12:01:43', 'edgar@gmail.com'),
(4, 'eCitaro fuel cell', '1', '1', '1', '0', '2025-05-26 12:04:08', 'edgar@gmail.com'),
(5, 'eCitaro', '1', '2', '1', '0', '2025-05-26 12:04:42', 'edgar@gmail.com'),
(6, 'Citaro', '1', '2', '1', '0', '2025-05-26 12:05:05', 'edgar@gmail.com'),
(7, 'Citaro U', '1', '3', '1', '0', '2025-05-26 12:05:38', 'edgar@gmail.com'),
(8, 'Intouro', '1', '3', '1', '0', '2025-05-26 12:05:50', 'edgar@gmail.com'),
(9, 'Tourismo', '1', '3', '1', '0', '2025-05-26 12:08:52', 'edgar@gmail.com');

-- INSERT TIPO_HERRAMIENTA  

INSERT INTO tipo_herramienta (nombre) VALUES ('Asientos');
INSERT INTO tipo_herramienta (nombre) VALUES ('Acceso');
INSERT INTO tipo_herramienta (nombre) VALUES ('Seguridad');
INSERT INTO tipo_herramienta (nombre) VALUES ('Multimedia');

-- INSERT HERRAMIENTA

INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Asiento a 140°','fas fa-chair',1);
INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Asiento a 160°','fas fa-chair',1);
INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Asiento cama','fas fa-chair',1);


INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Televisor','fas fa-desktop',4);


INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Baño','fas fa-restroom',3);
INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Extintor','fas fa-fire-extinguisher',3);


INSERT INTO herramienta (nombre, icono,id_tipo) VALUES ('Puerta','fas fa-door-closed',2	);



-- INSERTS PAIS
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (1,'Afganistán','Afghanistan','AF','AFG','93','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (2,'Albania','Albania','AL','ALB','355','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (3,'Alemania','Germany','DE','DEU','49','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (4,'Algeria','Algeria','DZ','DZA','213','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (5,'Andorra','Andorra','AD','AND','376','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (6,'Angola','Angola','AO','AGO','244','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (7,'Anguila','Anguilla','AI','AIA','1 264','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (8,'Antártida','Antarctica','AQ','ATA','672','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (9,'Antigua y Barbuda','Antigua and Barbuda','AG','ATG','1 268','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (10,'Antillas Neerlandesas','Netherlands Antilles','AN','ANT','599','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (11,'Arabia Saudita','Saudi Arabia','SA','SAU','966','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (12,'Argentina','Argentina','AR','ARG','54','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (13,'Armenia','Armenia','AM','ARM','374','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (14,'Aruba','Aruba','AW','ABW','297','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (15,'Australia','Australia','AU','AUS','61','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (16,'Austria','Austria','AT','AUT','43','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (17,'Azerbayán','Azerbaijan','AZ','AZE','994','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (18,'Bélgica','Belgium','BE','BEL','32','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (19,'Bahamas','Bahamas','BS','BHS','1 242','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (20,'Bahrein','Bahrain','BH','BHR','973','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (21,'Bangladesh','Bangladesh','BD','BGD','880','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (22,'Barbados','Barbados','BB','BRB','1 246','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (23,'Belice','Belize','BZ','BLZ','501','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (24,'Benín','Benin','BJ','BEN','229','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (25,'Bhután','Bhutan','BT','BTN','975','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (26,'Bielorrusia','Belarus','BY','BLR','375','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (27,'Birmania','Myanmar','MM','MMR','95','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (28,'Bolivia','Bolivia','BO','BOL','591','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (29,'Bosnia y Herzegovina','Bosnia and Herzegovina','BA','BIH','387','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (30,'Botsuana','Botswana','BW','BWA','267','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (31,'Brasil','Brazil','BR','BRA','55','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (32,'Brunéi','Brunei','BN','BRN','673','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (33,'Bulgaria','Bulgaria','BG','BGR','359','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (34,'Burkina Faso','Burkina Faso','BF','BFA','226','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (35,'Burundi','Burundi','BI','BDI','257','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (36,'Cabo Verde','Cape Verde','CV','CPV','238','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (37,'Camboya','Cambodia','KH','KHM','855','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (38,'Camerún','Cameroon','CM','CMR','237','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (39,'Canadá','Canada','CA','CAN','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (40,'Chad','Chad','TD','TCD','235','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (41,'Chile','Chile','CL','CHL','56','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (42,'China','China','CN','CHN','86','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (43,'Chipre','Cyprus','CY','CYP','357','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (44,'Ciudad del Vaticano','Vatican City State','VA','VAT','39','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (45,'Colombia','Colombia','CO','COL','57','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (46,'Comoras','Comoros','KM','COM','269','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (47,'Congo','Congo','CG','COG','242','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (48,'Congo','Congo','CD','COD','243','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (49,'Corea del Norte','North Korea','KP','PRK','850','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (50,'Corea del Sur','South Korea','KR','KOR','82','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (51,'Costa de Marfil','Ivory Coast','CI','CIV','225','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (52,'Costa Rica','Costa Rica','CR','CRI','506','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (53,'Croacia','Croatia','HR','HRV','385','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (54,'Cuba','Cuba','CU','CUB','53','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (55,'Dinamarca','Denmark','DK','DNK','45','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (56,'Dominica','Dominica','DM','DMA','1 767','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (57,'Ecuador','Ecuador','EC','ECU','593','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (58,'Egipto','Egypt','EG','EGY','20','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (59,'El Salvador','El Salvador','SV','SLV','503','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (60,'Emiratos Árabes Unidos','United Arab Emirates','AE','ARE','971','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (61,'Eritrea','Eritrea','ER','ERI','291','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (62,'Eslovaquia','Slovakia','SK','SVK','421','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (63,'Eslovenia','Slovenia','SI','SVN','386','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (64,'España','Spain','ES','ESP','34','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (65,'Estados Unidos de América','United States of America','US','USA','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (66,'Estonia','Estonia','EE','EST','372','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (67,'Etiopía','Ethiopia','ET','ETH','251','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (68,'Filipinas','Philippines','PH','PHL','63','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (69,'Finlandia','Finland','FI','FIN','358','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (70,'Fiyi','Fiji','FJ','FJI','679','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (71,'Francia','France','FR','FRA','33','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (72,'Gabón','Gabon','GA','GAB','241','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (73,'Gambia','Gambia','GM','GMB','220','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (74,'Georgia','Georgia','GE','GEO','995','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (75,'Ghana','Ghana','GH','GHA','233','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (76,'Gibraltar','Gibraltar','GI','GIB','350','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (77,'Granada','Grenada','GD','GRD','1 473','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (78,'Grecia','Greece','GR','GRC','30','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (79,'Groenlandia','Greenland','GL','GRL','299','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (80,'Guadalupe','Guadeloupe','GP','GLP','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (81,'Guam','Guam','GU','GUM','1 671','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (82,'Guatemala','Guatemala','GT','GTM','502','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (83,'Guayana Francesa','French Guiana','GF','GUF','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (84,'Guernsey','Guernsey','GG','GGY','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (85,'Guinea','Guinea','GN','GIN','224','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (86,'Guinea Ecuatorial','Equatorial Guinea','GQ','GNQ','240','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (87,'Guinea-Bissau','Guinea-Bissau','GW','GNB','245','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (88,'Guyana','Guyana','GY','GUY','592','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (89,'Haití','Haiti','HT','HTI','509','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (90,'Honduras','Honduras','HN','HND','504','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (91,'Hong kong','Hong Kong','HK','HKG','852','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (92,'Hungría','Hungary','HU','HUN','36','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (93,'India','India','IN','IND','91','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (94,'Indonesia','Indonesia','ID','IDN','62','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (95,'Irán','Iran','IR','IRN','98','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (96,'Irak','Iraq','IQ','IRQ','964','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (97,'Irlanda','Ireland','IE','IRL','353','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (98,'Isla Bouvet','Bouvet Island','BV','BVT','','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (99,'Isla de Man','Isle of Man','IM','IMN','44','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (100,'Isla de Navidad','Christmas Island','CX','CXR','61','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (101,'Isla Norfolk','Norfolk Island','NF','NFK','','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (102,'Islandia','Iceland','IS','ISL','354','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (103,'Islas Bermudas','Bermuda Islands','BM','BMU','1 441','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (104,'Islas Caimán','Cayman Islands','KY','CYM','1 345','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (105,'Islas Cocos (Keeling)','Cocos (Keeling) Islands','CC','CCK','61','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (106,'Islas Cook','Cook Islands','CK','COK','682','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (107,'Islas de Åland','Åland Islands','AX','ALA','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (108,'Islas Feroe','Faroe Islands','FO','FRO','298','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (109,'Islas Georgias del Sur y Sandwich del Sur','South Georgia and the South Sandwich Islands','GS','SGS','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (110,'Islas Heard y McDonald','Heard Island and McDonald Islands','HM','HMD','','Antártida');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (111,'Islas Maldivas','Maldives','MV','MDV','960','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (112,'Islas Malvinas','Falkland Islands (Malvinas)','FK','FLK','500','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (113,'Islas Marianas del Norte','Northern Mariana Islands','MP','MNP','1 670','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (114,'Islas Marshall','Marshall Islands','MH','MHL','692','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (115,'Islas Pitcairn','Pitcairn Islands','PN','PCN','870','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (116,'Islas Salomón','Solomon Islands','SB','SLB','677','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (117,'Islas Turcas y Caicos','Turks and Caicos Islands','TC','TCA','1 649','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (118,'Islas Ultramarinas Menores de Estados Unidos','United States Minor Outlying Islands','UM','UMI','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (119,'Islas Vírgenes Británicas','Virgin Islands','VG','VG','1 284','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (120,'Islas Vírgenes de los Estados Unidos','United States Virgin Islands','VI','VIR','1 340','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (121,'Israel','Israel','IL','ISR','972','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (122,'Italia','Italy','IT','ITA','39','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (123,'Jamaica','Jamaica','JM','JAM','1 876','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (124,'Japón','Japan','JP','JPN','81','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (125,'Jersey','Jersey','JE','JEY','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (126,'Jordania','Jordan','JO','JOR','962','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (127,'Kazajistán','Kazakhstan','KZ','KAZ','7','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (128,'Kenia','Kenya','KE','KEN','254','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (129,'Kirgizstán','Kyrgyzstan','KG','KGZ','996','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (130,'Kiribati','Kiribati','KI','KIR','686','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (131,'Kuwait','Kuwait','KW','KWT','965','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (132,'Líbano','Lebanon','LB','LBN','961','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (133,'Laos','Laos','LA','LAO','856','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (134,'Lesoto','Lesotho','LS','LSO','266','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (135,'Letonia','Latvia','LV','LVA','371','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (136,'Liberia','Liberia','LR','LBR','231','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (137,'Libia','Libya','LY','LBY','218','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (138,'Liechtenstein','Liechtenstein','LI','LIE','423','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (139,'Lituania','Lithuania','LT','LTU','370','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (140,'Luxemburgo','Luxembourg','LU','LUX','352','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (141,'México','Mexico','MX','MEX','52','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (142,'Mónaco','Monaco','MC','MCO','377','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (143,'Macao','Macao','MO','MAC','853','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (144,'Macedônia','Macedonia','MK','MKD','389','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (145,'Madagascar','Madagascar','MG','MDG','261','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (146,'Malasia','Malaysia','MY','MYS','60','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (147,'Malawi','Malawi','MW','MWI','265','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (148,'Mali','Mali','ML','MLI','223','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (149,'Malta','Malta','MT','MLT','356','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (150,'Marruecos','Morocco','MA','MAR','212','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (151,'Martinica','Martinique','MQ','MTQ','','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (152,'Mauricio','Mauritius','MU','MUS','230','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (153,'Mauritania','Mauritania','MR','MRT','222','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (154,'Mayotte','Mayotte','YT','MYT','262','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (155,'Micronesia','Estados Federados de','FM','FSM','691','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (156,'Moldavia','Moldova','MD','MDA','373','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (157,'Mongolia','Mongolia','MN','MNG','976','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (158,'Montenegro','Montenegro','ME','MNE','382','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (159,'Montserrat','Montserrat','MS','MSR','1 664','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (160,'Mozambique','Mozambique','MZ','MOZ','258','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (161,'Namibia','Namibia','NA','NAM','264','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (162,'Nauru','Nauru','NR','NRU','674','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (163,'Nepal','Nepal','NP','NPL','977','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (164,'Nicaragua','Nicaragua','NI','NIC','505','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (165,'Niger','Niger','NE','NER','227','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (166,'Nigeria','Nigeria','NG','NGA','234','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (167,'Niue','Niue','NU','NIU','683','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (168,'Noruega','Norway','NO','NOR','47','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (169,'Nueva Caledonia','New Caledonia','NC','NCL','687','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (170,'Nueva Zelanda','New Zealand','NZ','NZL','64','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (171,'Omán','Oman','OM','OMN','968','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (172,'Países Bajos','Netherlands','NL','NLD','31','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (173,'Pakistán','Pakistan','PK','PAK','92','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (174,'Palau','Palau','PW','PLW','680','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (175,'Palestina','Palestine','PS','PSE','','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (176,'Panamá','Panama','PA','PAN','507','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (177,'Papúa Nueva Guinea','Papua New Guinea','PG','PNG','675','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (178,'Paraguay','Paraguay','PY','PRY','595','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (179,'Perú','Peru','PE','PER','51','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (180,'Polinesia Francesa','French Polynesia','PF','PYF','689','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (181,'Polonia','Poland','PL','POL','48','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (182,'Portugal','Portugal','PT','PRT','351','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (183,'Puerto Rico','Puerto Rico','PR','PRI','1','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (184,'Qatar','Qatar','QA','QAT','974','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (185,'Reino Unido','United Kingdom','GB','GBR','44','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (186,'República Centroafricana','Central African Republic','CF','CAF','236','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (187,'República Checa','Czech Republic','CZ','CZE','420','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (188,'República Dominicana','Dominican Republic','DO','DOM','1 809','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (189,'Reunión','Réunion','RE','REU','','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (190,'Ruanda','Rwanda','RW','RWA','250','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (191,'Rumanía','Romania','RO','ROU','40','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (192,'Rusia','Russia','RU','RUS','7','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (193,'Sahara Occidental','Western Sahara','EH','ESH','','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (194,'Samoa','Samoa','WS','WSM','685','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (195,'Samoa Americana','American Samoa','AS','ASM','1 684','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (196,'San Bartolomé','Saint Barthélemy','BL','BLM','590','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (197,'San Cristóbal y Nieves','Saint Kitts and Nevis','KN','KNA','1 869','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (198,'San Marino','San Marino','SM','SMR','378','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (199,'San Martín (Francia)','Saint Martin (French part)','MF','MAF','1 599','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (200,'San Pedro y Miquelón','Saint Pierre and Miquelon','PM','SPM','508','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (201,'San Vicente y las Granadinas','Saint Vincent and the Grenadines','VC','VCT','1 784','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (202,'Santa Elena','Ascensión y Tristán de Acuña','SH','SHN','290','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (203,'Santa Lucía','Saint Lucia','LC','LCA','1 758','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (204,'Santo Tomé y Príncipe','Sao Tome and Principe','ST','STP','239','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (205,'Senegal','Senegal','SN','SEN','221','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (206,'Serbia','Serbia','RS','SRB','381','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (207,'Seychelles','Seychelles','SC','SYC','248','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (208,'Sierra Leona','Sierra Leone','SL','SLE','232','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (209,'Singapur','Singapore','SG','SGP','65','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (210,'Siria','Syria','SY','SYR','963','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (211,'Somalia','Somalia','SO','SOM','252','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (212,'Sri lanka','Sri Lanka','LK','LKA','94','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (213,'Sudáfrica','South Africa','ZA','ZAF','27','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (214,'Sudán','Sudan','SD','SDN','249','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (215,'Suecia','Sweden','SE','SWE','46','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (216,'Suiza','Switzerland','CH','CHE','41','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (217,'Surinám','Suriname','SR','SUR','597','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (218,'Svalbard y Jan Mayen','Svalbard and Jan Mayen','SJ','SJM','','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (219,'Swazilandia','Swaziland','SZ','SWZ','268','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (220,'Tadjikistán','Tajikistan','TJ','TJK','992','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (221,'Tailandia','Thailand','TH','THA','66','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (222,'Taiwán','Taiwan','TW','TWN','886','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (223,'Tanzania','Tanzania','TZ','TZA','255','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (224,'Territorio Británico del Océano Índico','British Indian Ocean Territory','IO','IOT','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (225,'Territorios Australes y Antárticas Franceses','French Southern Territories','TF','ATF','','');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (226,'Timor Oriental','East Timor','TL','TLS','670','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (227,'Togo','Togo','TG','TGO','228','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (228,'Tokelau','Tokelau','TK','TKL','690','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (229,'Tonga','Tonga','TO','TON','676','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (230,'Trinidad y Tobago','Trinidad and Tobago','TT','TTO','1 868','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (231,'Tunez','Tunisia','TN','TUN','216','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (232,'Turkmenistán','Turkmenistan','TM','TKM','993','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (233,'Turquía','Turkey','TR','TUR','90','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (234,'Tuvalu','Tuvalu','TV','TUV','688','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (235,'Ucrania','Ukraine','UA','UKR','380','Europa');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (236,'Uganda','Uganda','UG','UGA','256','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (237,'Uruguay','Uruguay','UY','URY','598','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (238,'Uzbekistán','Uzbekistan','UZ','UZB','998','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (239,'Vanuatu','Vanuatu','VU','VUT','678','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (240,'Venezuela','Venezuela','VE','VEN','58','América');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (241,'Vietnam','Vietnam','VN','VNM','84','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (242,'Wallis y Futuna','Wallis and Futuna','WF','WLF','681','Australia y Oceanía');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (243,'Yemen','Yemen','YE','YEM','967','Asia');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (244,'Yibuti','Djibouti','DJ','DJI','253','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (245,'Zambia','Zambia','ZM','ZMB','260','África');
INSERT INTO pais (id, nombre, name, iso2, iso3, phone_code, continente) VALUES (246,'Zimbabue','Zimbabwe','ZW','ZWE','263','África');

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
INSERT INTO tipo_usuario (id,nombre, estado, estado_proceso,estado_registro,fecha_registro, usuario) VALUES (1,'ADMINISTRADOR', 1, 'REGISTRADO',1,'2025-03-06 20:02:56','SYSTEM');

-- Tabla Usuario
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,estado_proceso,estado_registro,fecha_registro,usuario) VALUES (1,'Alexis','alexis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', '/Static/img/trabajadores/alexis.jpeg', 1, 1,'MODIFICADO',1,'2025-03-06 20:06:14','SYSTEM');
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,estado_proceso,estado_registro,fecha_registro,usuario) VALUES (2,'Edgar','edgar@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', '/Static/img/trabajadores/edgar.png', 1, 1,'MODIFICADO',1,'2025-03-06 20:06:14','SYSTEM');

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
INSERT INTO conf_plantillas (id, nombre, color_header, color_footer, logo, estado, fecha_registro, usuario) VALUES (1, 'YATRAX', '#0c336e', '#000000', '/Static/img/plantillas/logo_yatusa.png', 1, '2025-03-06 20:06:14', 'SYSTEM');


-- Crear procedimiento SP_REGISTRAR_INCIDENCIA
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_INCIDENCIA(
    IN P_NOMBRE VARCHAR(255),
    IN P_DESCRIPCION VARCHAR(255),
    IN P_DURACION_SANCION INT,
    IN P_ESTADO BIT,
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

    SELECT COUNT(*) INTO cNombre FROM incidencia where nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'La incidencia que intenga registrar ya está registrada';
    ELSE
        INSERT INTO incidencia (nombre, descripcion, duracion_sancion, estado, usuario)
        VALUES (P_NOMBRE, P_DESCRIPCION, P_DURACION_SANCION, P_ESTADO, P_USUARIO);

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
    IN P_ESTADO BIT
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

    SELECT COUNT(*) INTO cID FROM incidencia WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM incidencia where nombre = P_NOMBRE;

    IF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta editar no existe';
    ELSEIF cNombre !=0 THEN
        SET @MSJ2 = 'El nombre de incidencia ya existe';
    ELSE
        UPDATE incidencia SET nombre = P_NOMBRE, descripcion = P_DESCRIPCION, duracion_sancion = P_DURACION_SANCION, estado = P_ESTADO WHERE id =P_ID;
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
        SET @MSJ2 = CONCAT
        ('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cID FROM incidencia WHERE id = P_ID;

    IF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta dar de baja no existe';
    ELSE
        UPDATE incidencia SET estado = 0 where id = P_ID;
        SET @MSJ = 'Se dio de baja correctamente la incidencia';
    END IF;

END $$

DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_INCIDENCIA

DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_INCIDENCIA(
    P_ID INT
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

    IF cID <= 0 THEN
        SET @MSJ2 = 'La incidencia que intenta eliminar no existe';
    ELSE
        DELETE FROM incidencia where id = P_ID;
        SET @MSJ = 'Se eliminó correctamente la incidencia';
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

    SELECT COUNT(*) INTO cEmail FROM usuarios WHERE EMAIL = P_EMAIL AND ESTADO_REGISTRO = 1;

    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSE
        INSERT INTO usuarios (NOMBRE, EMAIL, PASSWORD, IMAGEN, ESTADO, ID_TIPOUSUARIO, USUARIO) 
        VALUES (P_NOMBRE, P_EMAIL, P_PASS, P_IMAGEN, P_ESTADO, P_IDTIPOUSUARIO, P_USUARIO);

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

    SELECT COUNT(*) INTO cUsuario FROM usuarios WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cEmail FROM usuarios WHERE EMAIL = P_EMAIL AND ID != P_ID AND ESTADO_REGISTRO = 1;

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
            ID_TIPOUSUARIO = P_IDTIPOUSUARIO, 
            estado_proceso = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se modificó correctamente al usuario';
    END IF;
END $$
DELIMITER ;

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

    -- Verificar si existe el correo con ESTADO_REGISTRO = 1 y ESTADO = 1
    SELECT COUNT(*) INTO cEmail 
    FROM usuarios 
    WHERE EMAIL = P_EMAIL 
      AND ESTADO_REGISTRO = 1 
      AND ESTADO = 1;

    IF cEmail = 0 THEN
        SET MSJ2 = 'El correo no existe o el usuario no está activo';
    ELSE
        -- Actualizar la contraseña
        UPDATE usuarios 
        SET PASSWORD = P_PASSWORD
        WHERE EMAIL = P_EMAIL 
          AND ESTADO_REGISTRO = 1 
          AND ESTADO = 1;

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

    SELECT COUNT(*) INTO cUsuario FROM usuarios WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta dar de baja no existe';
    ELSE
        UPDATE usuarios SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cUsuario FROM usuarios WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta eliminar no existe';
    ELSE
        UPDATE usuarios SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se eliminó correctamente al usuario';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_CLIENTE
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_CLIENTE_NATURAL(
    IN P_ID_PAIS INT,
    IN P_ID_TIPO_DOC INT,
    IN P_ID_TIPO_CLIENTE INT,
    IN P_NUMERO_DOCUMENTO VARCHAR(20),
    IN P_NOMBRES VARCHAR(90),
    IN P_APE_PATERNO VARCHAR(50),
    IN P_APE_MATERNO VARCHAR(50),
    IN P_SEXO TINYINT,
    IN P_F_NACIMIENTO DATE,
    IN P_DIRECCION VARCHAR(70),
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
        INSERT INTO CLIENTE (id_pais,id_tipo_doc,id_tipo_cliente,numero_documento,nombres, ape_paterno, ape_materno, sexo, f_nacimiento, direccion, telefono, email, password,estado,usuario) 
        VALUES (P_ID_PAIS, P_ID_TIPO_DOC, P_ID_TIPO_CLIENTE, P_NUMERO_DOCUMENTO, P_NOMBRES, P_APE_PATERNO, P_APE_MATERNO, P_SEXO, P_F_NACIMIENTO, P_DIRECCION, P_TELEFONO, P_EMAIL, P_PASSWORD,P_ESTADO,P_USUARIO);
        SET @MSJ = 'Se registró correctamente al cliente';
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_CLIENTE_JURIDICO(
    IN P_ID_PAIS INT,
    IN P_ID_TIPO_DOC INT,
    IN P_NUMERO_DOCUMENTO VARCHAR(20),
    IN P_RAZON_SOCIAL VARCHAR(90),
    IN P_DIRECCION VARCHAR(70),
    IN P_TELEFONO VARCHAR(13),
    IN P_EMAIL VARCHAR(100),
    IN P_PASSWORD VARCHAR(256),
    IN P_ESTADO TINYINT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cEmail INT;
    DECLARE cRazonSocial INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cEmail FROM cliente WHERE EMAIL = P_EMAIL;
    SELECT COUNT(*) INTO cRazonSocial FROM cliente WHERE RAZON_SOCIAL = P_RAZON_SOCIAL;

    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSEIF cRazonSocial > 0 THEN
    	SET @MSJ2 = 'La razón social que intenta registrar ya está registrado';
    ELSE  
        INSERT INTO CLIENTE (id_pais,id_tipo_doc,numero_documento, razon_social, direccion, telefono, email, password,estado,usuario) 
        VALUES (P_ID_PAIS, P_ID_TIPO_DOC, P_NUMERO_DOCUMENTO, P_RAZON_SOCIAL, P_DIRECCION, P_TELEFONO, P_EMAIL, P_PASSWORD, P_ESTADO,P_USUARIO);
        SET @MSJ = 'Se registró correctamente al cliente';
    END IF;
END $$
DELIMITER ;


-- Crear procedimiento SP_EDITAR_CLIENTE_NATURAL
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_CLIENTE_NATURAL(
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
    IN P_DIRECCION VARCHAR(70),
    IN P_TELEFONO VARCHAR(13),
    IN P_EMAIL VARCHAR(100),
    IN P_PASSWORD VARCHAR(256),
    IN P_ESTADO TINYINT
)
BEGIN
    DECLARE cCliente INT;
    DECLARE cEmail INT;
    DECLARE cNumeroDoc INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cCliente FROM CLIENTE WHERE id = P_ID;
    SELECT COUNT(*) INTO cEmail FROM CLIENTE WHERE EMAIL = P_EMAIL AND id != P_ID;
    SELECT COUNT(*) INTO cNumeroDoc FROM CLIENTE WHERE numero_documento = P_NUMERO_DOCUMENTO AND id != P_ID;

    IF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta editar no existe';
    ELSEIF cEmail != 0 THEN
        SET @MSJ2 = 'El correo ingresado ya existe';
    ELSEIF cNumeroDoc != 0 THEN
        SET @MSJ2 = 'El numero de documento ingresado ya existe';
    ELSE
        UPDATE CLIENTE
        SET id_pais = P_ID_PAIS,
        id_tipo_doc = P_ID_TIPO_DOC,
        id_tipo_cliente = P_ID_TIPO_CLIENTE,
        numero_documento = P_NUMERO_DOCUMENTO,
        nombres = P_NOMBRES,
        ape_paterno = P_APE_PATERNO,
        ape_materno = P_APE_MATERNO,
        sexo = P_SEXO,
        f_nacimiento = P_F_NACIMIENTO,
        direccion = P_DIRECCION,
        telefono = P_TELEFONO,
        email = P_EMAIL,
        password = P_PASSWORD,
        estado = P_ESTADO
        WHERE id = P_ID;
        
        SET @MSJ = 'Se modificó correctamente al usuario';
    END IF;
END $$
DELIMITER ;
-- Crear procedimiento SP_EDITAR_CLIENTE_JURIDICO
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_CLIENTE_JURIDICO(
    IN P_ID INT,
    IN P_ID_PAIS INT,
    IN P_ID_TIPO_DOC INT,
    IN P_NUMERO_DOCUMENTO VARCHAR(20),
    IN P_RAZON_SOCIAL VARCHAR(90),
    IN P_DIRECCION VARCHAR(70),
    IN P_TELEFONO VARCHAR(13),
    IN P_EMAIL VARCHAR(100),
    IN P_PASSWORD VARCHAR(256),
    IN P_ESTADO TINYINT
)
BEGIN
    DECLARE cCliente INT;
    DECLARE cEmail INT;
    DECLARE cNumeroDoc INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cCliente FROM CLIENTE WHERE id = P_ID;
    SELECT COUNT(*) INTO cEmail FROM CLIENTE WHERE EMAIL = P_EMAIL AND id != P_ID;
    SELECT COUNT(*) INTO cNumeroDoc FROM CLIENTE WHERE numero_documento = P_NUMERO_DOCUMENTO AND id != P_ID;

    IF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta editar no existe';
    ELSEIF cEmail != 0 THEN
        SET @MSJ2 = 'El correo ingresado ya existe';
    ELSEIF cNumeroDoc != 0 THEN
        SET @MSJ2 = 'El número de documento ingresado ya existe';
    ELSE
        UPDATE CLIENTE
        SET id_pais = P_ID_PAIS,
            id_tipo_doc = P_ID_TIPO_DOC,
            numero_documento = P_NUMERO_DOCUMENTO,
            razon_social = P_RAZON_SOCIAL,
            direccion = P_DIRECCION,
            telefono = P_TELEFONO,
            email = P_EMAIL,
            password = P_PASSWORD,
            estado = P_ESTADO
        WHERE id = P_ID;

        SET @MSJ = 'Se modificó correctamente al cliente';
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
    SELECT COUNT(*) INTO cDeBaja FROM cliente where ID = P_ID AND estado = 0;

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

    IF cCliente <= 0 THEN
        SET @MSJ2 = 'El cliente que intenta eliminar no existe';
    ELSE
        DELETE FROM CLIENTE WHERE ID = P_ID;
        SET @MSJ = 'Se eliminó correctamente al usuario';
    END IF;
END $$
DELIMITER ;
-- aaaaaaaaaaaaaaa




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
    FROM CIUDAD 
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
    WHERE nombre = P_NOMBRE AND estado_registro = 1 AND abreviatura = P_ABREVIATURA;

    SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(cod_sucursal, '-', -1) AS UNSIGNED)), 0) + 1 INTO cCorrelativo FROM sucursal WHERE abreviatura = P_ABREVIATURA AND estado_registro = 1;

    SET cAUX = CONCAT(P_ABREVIATURA, '-', LPAD(cCorrelativo, 2, '0'));

    IF cSucursal > 0 THEN
        SET @MSJ2 = 'La sucursal que intenta registrar ya está registrada';
    ELSE
        INSERT INTO sucursal (cod_sucursal, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario) 
        VALUES (cAUX,P_CIUDAD, P_NOMBRE, P_DIRECCION, P_LATITUD, P_LONGITUD,P_ESTADO, P_ABREVIATURA, P_USUARIO);
        
        SET @MSJ = 'Se registró correctamente la sucursal';
    END IF;
END $$
DELIMITER ;


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
    WHERE id = P_ID AND estado_registro = 1;

    SELECT COUNT(*) INTO cNombre 
    FROM sucursal 
    WHERE nombre = P_NOMBRE AND id != P_ID AND estado_registro = 1;

    SELECT CASE WHEN abreviatura != P_ABREVIATURA THEN TRUE ELSE FALSE END INTO abreviatura_cambiada
    FROM sucursal WHERE id = P_ID LIMIT 1;

    IF abreviatura_cambiada THEN
        SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(cod_sucursal, '-', -1) AS UNSIGNED)), 0) + 1
        INTO cCorrelativo
        FROM sucursal 
        WHERE abreviatura = P_ABREVIATURA AND estado_registro = 1 AND id != P_ID;

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
            usuario = P_USUARIO,
            estado_proceso = 'MODIFICADO'
        WHERE id = P_ID AND estado_registro = 1;

        SET @MSJ = 'Se modificó correctamente la sucursal';
    END IF;
END $$
DELIMITER ;

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
    WHERE id = P_ID AND estado_registro = 1;

    IF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta dar de baja no existe';
    ELSE
        UPDATE sucursal 
        SET estado = 0, usuario = P_USUARIO,
            estado_proceso = 'MODIFICADO'
        WHERE id = P_ID AND estado_registro = 1;

        SET @MSJ = 'Se dio de baja correctamente la sucursal';
    END IF;
END $$
DELIMITER ;

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

    IF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta eliminar no existe';
    ELSE
        UPDATE sucursal 
        SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO', usuario = P_USUARIO
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se eliminó correctamente la sucursal';
    END IF;
END $$
DELIMITER ;

-- REGISTRAR ASIENTO
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
        INSERT INTO asiento (nro_asiento, id_nivel, tipo_asiento, estado, usuario)
        VALUES (P_NRO_ASIENTO, P_ID_NIVEL, P_TIPO_ASIENTO, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el asiento';
    END IF;
END $$
DELIMITER ;


-- EDITAR ASIENTO
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


-- DAR DE BAJA EL ASIENTO
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


-- ELIMINAR ASIENTO
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

    IF cAsiento = 0 THEN
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM tipo_usuario WHERE nombre = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta registrar ya está registrado';
    ELSE
        INSERT INTO tipo_usuario (NOMBRE, ESTADO, USUARIO) 
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_usuario WHERE NOMBRE = P_NOMBRE AND ID != P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_usuario 
        SET NOMBRE = P_NOMBRE, 
            ESTADO = P_ESTADO, 
            estado_proceso = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_usuario SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cTipoUsuario FROM tipo_usuario WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoUsuario <= 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta eliminar no existe';
    ELSE
        UPDATE tipo_usuario SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se eliminó correctamente al tipo de usuario';
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

    SELECT COUNT(*) INTO cNombre FROM tipo_personal WHERE NOMBRE = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta registrar ya está registrado';
    ELSE
        INSERT INTO tipo_personal (NOMBRE, ESTADO, USUARIO) 
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

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_personal WHERE NOMBRE = P_NOMBRE AND id != P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_personal 
        SET NOMBRE = P_NOMBRE, 
            ESTADO = P_ESTADO, 
            ESTADO_PROCESO = 'MODIFICADO' 
        WHERE id = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_personal SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE id = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cTipoPersonal FROM tipo_personal WHERE id = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoPersonal <= 0 THEN
        SET @MSJ2 = 'El tipo de personal que intenta eliminar no existe';
    ELSE
        UPDATE tipo_personal SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE id = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cMenus FROM conf_dmenus WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO;

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

    SELECT COUNT(*) INTO cMenus FROM conf_dmenus WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cMenus <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM conf_dmenus WHERE idMenu = P_IDMENU AND idTipoUsuario = P_IDTIPOUSUARIO; 
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

    SELECT COUNT(*) INTO cClaims FROM conf_dclaims WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO;

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

    SELECT COUNT(*) INTO cClaims FROM conf_dclaims WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO;

    IF cClaims <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM conf_dclaims WHERE idClaim = P_IDCLAIM AND idTipoUsuario = P_IDTIPOUSUARIO; 
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

    SELECT COUNT(*) INTO cNombre FROM conf_plantillas WHERE NOMBRE = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre que intenta registrar ya está registrado';
    ELSE
        INSERT INTO conf_plantillas (NOMBRE, COLOR_HEADER, COLOR_FOOTER, LOGO, ESTADO, USUARIO) 
        VALUES (P_NOMBRE, P_COLORH, P_COLORF, P_LOGO, 0, P_USUARIO);

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

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE ID = P_ID;
    SELECT COUNT(*) INTO cNombre FROM conf_plantillas WHERE NOMBRE = P_NOMBRE AND ID != P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE conf_plantillas 
        SET NOMBRE = P_NOMBRE, 
            COLOR_HEADER = P_COLORH,
            COLOR_FOOTER = P_COLORF,
            LOGO = P_LOGO
        WHERE ID = P_ID;

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

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE ID = P_ID;
    SELECT ESTADO INTO flagPlantilla FROM conf_plantillas WHERE ID = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta eliminar no existe';
    ELSEIF flagPlantilla = 1 THEN
        SET @MSJ2 = 'La plantilla que está activa no puede ser eliminada';
    ELSE
        DELETE FROM conf_plantillas WHERE ID = P_ID;

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

    SELECT COUNT(*) INTO cPlantilla FROM conf_plantillas WHERE ID = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta activar no existe';
    ELSE
        UPDATE conf_plantillas SET ESTADO = 0;
        UPDATE conf_plantillas SET ESTADO = 1 WHERE ID = P_ID;

        SET @MSJ = 'Se activó correctamente la plantilla';
    END IF;
END $$
DELIMITER ;

--  tipo vehiculo

-- Cambiar delimitador para creación de procedimientos
DELIMITER $$

-- Procedimiento para insertar tipo de vehículo

CREATE PROCEDURE SP_INSERTAR_TIPOVEHICULO(
    IN  p_nombre     VARCHAR(50),
    IN  p_idMarca    INT,
    IN  p_cantidad   INT,
    IN P_ESTADO BOOLEAN,
    IN P_SERVICIO INT,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    -- 1) Declaración de variables LO PRIMERO
    DECLARE v_existeMarca INT DEFAULT 0;
    DECLARE v_nuevoTipo   INT DEFAULT 0;
    DECLARE v_i           INT DEFAULT 1;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET @MSJ2 = 'Error al ejecutar el procedimiento';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    -- 2) Verificar si la marca existe
    SELECT COUNT(*) INTO v_existeMarca
      FROM marca
     WHERE id = p_idMarca;

    IF v_existeMarca = 0 THEN
        SET @MSJ2 = 'La marca ingresada no existe';
    ELSE
        -- 3) Inserto el nuevo tipo de vehículo
        INSERT INTO tipo_vehiculo (nombre, id_marca, id_servicio, estado, cantidad, usuario)
        VALUES (p_nombre, p_idMarca, P_SERVICIO, P_ESTADO, p_cantidad, P_USUARIO);

        -- 4) Capturo el ID recién generado
        SET v_nuevoTipo = LAST_INSERT_ID();

        -- 5) Bucle para crear p_cantidad vehículos con placa NULL
        WHILE v_i <= p_cantidad DO
            INSERT INTO vehiculo (
                placa,
                anio,
                color,
                estado,
                id_tipo_vehiculo,
                usuario
            ) VALUES (
                NULL,       -- placa como NULL
                NULL,       -- año
                NULL,       -- color
                1,          -- estado activo
                v_nuevoTipo,
                P_USUARIO
            );
            SET v_i = v_i + 1;
        END WHILE;

        SET @MSJ = CONCAT('Tipo de vehículo insertado y ', p_cantidad, ' vehículos creados');
    END IF;
END$$

CREATE PROCEDURE SP_ACTUALIZAR_TIPOVEHICULO(
    IN  p_id        INT,
    IN  p_nombre    VARCHAR(50),
    IN  p_idMarca   INT,
    IN  p_estado    TINYINT,
    IN  p_cantidad  INT,
    IN P_SERVICIO INT,
    IN P_USUARIO VARCHAR(100),
    OUT p_MSJ       VARCHAR(255),
    OUT p_MSJ2      VARCHAR(255)
)
BEGIN
    -- 1) Declaraciones
    DECLARE v_existeMarca INT DEFAULT 0;
    DECLARE v_total       INT DEFAULT 0;
    DECLARE v_sinplaca    INT DEFAULT 0;
    DECLARE v_diff        INT DEFAULT 0;

    -- 2) Handler de error: marca p_MSJ2 y hace ROLLBACK
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_MSJ2 = 'Error al ejecutar el procedimiento';
    END;

    -- 3) Inicializar mensajes
    SET p_MSJ  = '';
    SET p_MSJ2 = '';

    -- 4) Verificar marca
    SELECT COUNT(*) INTO v_existeMarca
      FROM marca
     WHERE id = p_idMarca;

    IF v_existeMarca = 0 THEN
        SET p_MSJ2 = 'La marca indicada no existe';
    END IF;

    -- 5) Si la marca existe, continuo con la lógica
    IF p_MSJ2 = '' THEN

        -- Obtener totales y sin placa
        SELECT 
          COUNT(*) AS total,
          SUM(CASE WHEN placa IS NULL THEN 1 ELSE 0 END) AS sinplaca
        INTO v_total, v_sinplaca
        FROM vehiculo
        WHERE id_tipo_vehiculo = p_id;

        START TRANSACTION;

        -- 6) Reducir flota si p_cantidad < total
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
                 WHERE id_tipo_vehiculo = p_id
                   AND placa IS NULL
                 ORDER BY id
                 LIMIT v_diff;
            END IF;

        -- 7) Aumentar flota si p_cantidad > total
        ELSEIF p_cantidad > v_total THEN
            SET v_diff = p_cantidad - v_total;
            WHILE v_diff > 0 DO
                INSERT INTO vehiculo(
                    placa, anio, color, estado, id_tipo_vehiculo, usuario
                ) VALUES (
                    NULL, NULL, NULL, 1, p_id, P_USUARIO
                );
                SET v_diff = v_diff - 1;
            END WHILE;
        END IF;

        -- 8) Si en ningún paso se puso p_MSJ2, actualizar y commitear
        IF p_MSJ2 = '' THEN
            UPDATE tipo_vehiculo
               SET nombre   = p_nombre,
                   id_marca = p_idMarca,
                   id_servicio = P_SERVICIO,
                   estado   = p_estado,
                   cantidad = p_cantidad
             WHERE id = p_id;
            COMMIT;
            SET p_MSJ = 'Tipo de vehículo y su flota actualizada correctamente';
        ELSE
            ROLLBACK;
        END IF;

    END IF;

END$$

-- Procedimiento para dar de baja (baja lógica)
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
END$$

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

    IF v_existe = 0 THEN
        SET MSJ2 = 'El tipo de vehículo no existe';
    ELSE
        START TRANSACTION;
        DELETE FROM tipo_vehiculo
        WHERE id = p_id;
        COMMIT;

        SET MSJ = 'Tipo de vehículo eliminado correctamente';
    END IF;
END$$

-- Restaurar delimitador
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

    -- Declarar variables de mensaje si no están declaradas globalmente
    -- Puedes omitir esto si @MSJ y @MSJ2 ya están definidas como variables de sesión
    -- DECLARE @MSJ TEXT;
    -- DECLARE @MSJ2 TEXT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al insertar nivel';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    IF p_cantidad > 0 THEN
        -- Obtener el nuevo nroPiso
        SELECT COUNT(*) + 1
        INTO nuevo_nroPiso
        FROM nivel
        WHERE id_vehiculo = p_vehiculo;

        -- Insertar nuevo nivel
        INSERT INTO nivel (nroPiso, id_vehiculo, cantidad, estado)
        VALUES (nuevo_nroPiso, p_vehiculo, p_cantidad, 1);

        -- Obtener el id generado del nivel insertado
        SET nuevo_idNivel = LAST_INSERT_ID();

        -- Insertar los asientos correspondientes
        WHILE contador <= p_cantidad DO
            INSERT INTO asiento (
                nro_asiento,
                id_nivel,
                tipo_asiento,
                estado,
                fecha_registro
            ) VALUES (
                contador,
                nuevo_idNivel,
                'Económico',
                1,
                NOW()
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
END$$

-- CREATE PROCEDURE SP_INSERTAR_NIVEL(
--     IN p_vehiculo INT,
--     IN p_cantidad INT
-- )
-- BEGIN
--     DECLARE nuevo_nroPiso INT;

--     DECLARE EXIT HANDLER FOR SQLEXCEPTION
--     BEGIN
--         SET @MSJ2 = 'Error inesperado al insertar nivel';
--         SET @MSJ  = NULL;
--     END;

--     SET @MSJ  = NULL;
--     SET @MSJ2 = NULL;

--     IF p_cantidad > 0 THEN
--         SELECT COUNT(*) + 1
--           INTO nuevo_nroPiso
--         FROM nivel
--         WHERE id_vehiculo = p_vehiculo;

--         INSERT INTO nivel (nroPiso, id_vehiculo, cantidad, estado)
--         VALUES (nuevo_nroPiso, p_vehiculo, p_cantidad, 1);

--         SET @MSJ = CONCAT(
--             'Nivel insertado correctamente con nroPiso ',
--             nuevo_nroPiso
--         );
--     ELSE
--         SET @MSJ2 = 'La cantidad debe ser mayor a 0';
--     END IF;
-- END$$

CREATE PROCEDURE SP_ACTUALIZAR_NIVEL(
  IN p_idNivel        INT,
  IN p_nroPiso        INT,
  IN p_vehiculo       INT,
  IN p_cantidad       INT,
  IN p_estado         TINYINT
)
BEGIN
  DECLARE max_piso INT DEFAULT 0;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    SET @MSJ2 = 'Error inesperado al actualizar nivel';
    SET @MSJ  = NULL;
  END;
  SET @MSJ  = NULL; SET @MSJ2 = NULL;
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
        SET nroPiso         = p_nroPiso,
            id_vehiculo = p_vehiculo,
            cantidad        = p_cantidad,
            estado          = p_estado
      WHERE id = p_idNivel;
      IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el nivel especificado';
      ELSE
        SET @MSJ = 'Nivel actualizado correctamente';
      END IF;
    END IF;
  END IF;
END$$

CREATE PROCEDURE SP_DARBAJA_PISO(
    IN p_idNivel INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al dar de baja el piso';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    UPDATE nivel
    SET estado = 0
    WHERE id = p_idNivel;

    SET @MSJ = 'Piso dado de baja correctamente';
END$$


CREATE PROCEDURE SP_ELIMINAR_NIVEL(
    IN p_idNivel INT
)
BEGIN
    DECLARE piso_actual         INT;
    DECLARE vehiculo_act   INT;
    DECLARE max_piso            INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al eliminar nivel';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO piso_actual
    FROM nivel
    WHERE id = p_idNivel;

    DELETE FROM nivel_herramienta WHERE id_nivel = p_idNivel;

    IF piso_actual <= 0 THEN
        SET @MSJ2 = 'Intenta eliminar un nivel que no existe';
    ELSE
        DELETE FROM nivel
        WHERE id = p_idNivel;
        SET @MSJ = 'Nivel eliminado correctamente';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

-- 1) Insertar un nuevo vehículo (estado = 1)
CREATE PROCEDURE SP_INSERTAR_VEHICULO(
    IN p_placa VARCHAR(10),
    IN p_anio INT,
    IN p_color VARCHAR(30),
    IN p_idTipoVehiculo INT,
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    -- Variables de salida en user variables
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al insertar vehículo';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    INSERT INTO vehiculo (placa, anio, color, estado, id_tipo_vehiculo, usuario)
    VALUES (p_placa, p_anio, p_color, P_ESTADO, p_idTipoVehiculo, P_USUARIO);

    SET @MSJ  = 'Vehículo insertado correctamente';
END$$

-- 2) Actualizar datos de un vehículo existente
CREATE PROCEDURE SP_ACTUALIZAR_VEHICULO(
    IN p_idVehiculo      INT,
    IN p_placa           VARCHAR(10),
    IN p_anio            INT,
    IN p_color           VARCHAR(30),
    IN p_idTipoVehiculo  INT,
    IN p_estado          BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al actualizar vehículo';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    UPDATE vehiculo
    SET
        placa          = p_placa,
        anio           = p_anio,
        color          = p_color,
        id_tipo_vehiculo = p_idTipoVehiculo,
        estado         = p_estado
    WHERE id = p_idVehiculo;

    IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el vehículo especificado';
    ELSE
        SET @MSJ = 'Vehículo actualizado correctamente';
    END IF;
END$$

-- 3) Dar de baja (poner estado = 0)
CREATE PROCEDURE SP_BAJA_VEHICULO(
    IN p_idVehiculo INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al dar de baja vehículo';
        SET @MSJ  = NULL;
    END;

    SET @MSJ  = NULL;
    SET @MSJ2 = NULL;

    UPDATE vehiculo
    SET estado = 0
    WHERE id = p_idVehiculo;

    IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el vehículo para dar de baja';
    ELSE
        SET @MSJ = 'Vehículo dado de baja correctamente';
    END IF;
END$$

-- 4) Eliminar un vehículo de la tabla
CREATE PROCEDURE SP_ELIMINAR_VEHICULO(
    IN p_idVehiculo INT
)
BEGIN
    DECLARE v_idTipoVehiculo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = 'Error inesperado al eliminar vehículo';
        SET @MSJ  = NULL;
        ROLLBACK;
    END;

    START TRANSACTION;

    -- Obtener el tipo de vehículo antes de eliminar
    SELECT id_tipo_vehiculo INTO v_idTipoVehiculo
    FROM vehiculo
    WHERE id = p_idVehiculo;

    -- Eliminar el vehículo
    DELETE FROM vehiculo
    WHERE id = p_idVehiculo;

    IF ROW_COUNT() = 0 THEN
        SET @MSJ2 = 'No se encontró el vehículo para eliminar';
        ROLLBACK;
    ELSE
        -- Actualizar la cantidad del tipo de vehículo
        UPDATE tipo_vehiculo
        SET cantidad = cantidad - 1
        WHERE id = v_idTipoVehiculo;

        SET @MSJ = 'Vehículo eliminado correctamente';
        COMMIT;
    END IF;
END$$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_HORARIO
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_HORARIO(
    IN P_HORARIO_ENTRADA TIME,
    IN P_HORARIO_SALIDA TIME,
    IN P_ESTADO VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    IF P_HORARIO_ENTRADA >= P_HORARIO_SALIDA THEN
        SET @MSJ2 = 'El horario de entrada es mayor que el de salida';
    ELSE
        INSERT INTO horario (horario_entrada, horario_salida, estado, estado_registro) 
        VALUES (P_HORARIO_ENTRADA, P_HORARIO_SALIDA, P_ESTADO, 1);
        SET @MSJ = 'Se registró correctamente el horario';
    END IF;
END$$

DELIMITER ;

-- Crear procedimiento SP_EDITAR_HORARIO
DELIMITER $$
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios FROM horario WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta editar no existe';
    ELSEIF P_HORARIO_ENTRADA >= P_HORARIO_SALIDA THEN
        SET @MSJ2 = 'El horario de entrada es mayor que el de la salida';
    ELSE
        UPDATE horario
        SET horario_entrada = P_HORARIO_ENTRADA, 
            horario_salida = P_HORARIO_SALIDA,
            estado = P_ESTADO,
            estado_proceso = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se modificó correctamente al horario';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_USUARIO
DELIMITER $$
CREATE PROCEDURE SP_DARBAJA_HORARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cHorarios INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios FROM horario WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta dar de baja no existe';
    ELSE
        UPDATE horario SET ESTADO = 'I' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se dio de baja correctamente el horario';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_HORARIO
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_HORARIO(
    IN P_ID INT
)
BEGIN
    DECLARE cHorarios INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cHorarios FROM horario WHERE ID = P_ID;

    IF cHorarios <= 0 THEN
        SET @MSJ2 = 'El horario que intenta eliminar no existe';
    ELSE
        DELETE FROM horario WHERE ID = P_ID;

        SET @MSJ = 'Se eliminó correctamente el horario';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_TIPO_DOCUMENTO
DELIMITER $$
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM tipo_documento WHERE NOMBRE = P_NOMBRE AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cAbreviatura FROM tipo_documento WHERE ABREVIATURA = P_ABREVIATURA AND ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta registrar ya está registrado';
    ELSEIF cAbreviatura > 0 THEN
        SET @MSJ2 = 'La abreviatura que intenta registrar ya está registrada';
    ELSE
        INSERT INTO tipo_documento (NOMBRE, ABREVIATURA, ESTADO, USUARIO) 
        VALUES (P_NOMBRE, P_ABREVIATURA, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de documento';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_EDITAR_TIPO_DOCUMENTO
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste FROM tipo_documento WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_documento WHERE NOMBRE = P_NOMBRE AND ID != P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cAbreviatura FROM tipo_documento WHERE ABREVIATURA = P_ABREVIATURA AND ID != P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta actualizar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSEIF cAbreviatura != 0 THEN
        SET @MSJ2 = 'La abreviatura ingresada ya existe';
    ELSE
        UPDATE tipo_documento 
        SET NOMBRE = P_NOMBRE, 
            ABREVIATURA = P_ABREVIATURA, 
            ESTADO = P_ESTADO, 
            ESTADO_PROCESO = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se actualizó correctamente el tipo de documento';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_DOCUMENTO
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_TIPO_DOCUMENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoDocumento INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoDocumento FROM tipo_documento WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoDocumento <= 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta eliminar no existe';
    ELSE
        UPDATE tipo_documento SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se eliminó correctamente el tipo de documento';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_TIPO_DOCUMENTO
DELIMITER $$
CREATE PROCEDURE SP_DARBAJA_TIPO_DOCUMENTO(
    IN P_ID INT
)
BEGIN
    DECLARE cTipoDocumento INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cTipoDocumento FROM tipo_documento WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cTipoDocumento = 0 THEN
        SET @MSJ2 = 'El tipo de documento que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_documento SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se dio de baja correctamente el tipo de documento';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_INSERTAR_TIPO_CLIENTE
DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_TIPO_CLIENTE(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE nombre = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de cliente con ese nombre';
    ELSE
        INSERT INTO tipo_cliente (nombre, estado, usuario)
        VALUES (P_NOMBRE, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de cliente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_TIPO_CLIENTE

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

    SELECT COUNT(*) INTO cExiste FROM tipo_cliente WHERE idTipoCliente = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_cliente WHERE NOMBRE = P_NOMBRE AND idTipoCliente != P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de cliente que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_cliente 
        SET nombre = P_NOMBRE, estado = P_ESTADO, estado_proceso = 'MODIFICADO'
        WHERE idTipoCliente = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se actualizó correctamente el tipo de cliente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DAR_BAJA_CLIENTE

DELIMITER $$
CREATE PROCEDURE SP_DAR_BAJA_TIPO_CLIENTE(
    IN P_ID INT
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar SP_DAR_BAJA_TIPO_CLIENTE');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste FROM tipo_cliente WHERE idTipoCliente = P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de cliente que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_cliente 
        SET estado = 0, ESTADO_PROCESO = 'MODIFICADO'
        WHERE idTipoCliente = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se dio de baja correctamente al tipo de cliente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_CLIENTE
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_TIPO_CLIENTE(
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

    SELECT COUNT(*) INTO cUsuario FROM tipo_cliente where idTipoCliente = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MS2J = 'El tipo de cliente que intenta eliminar no existe';
    ELSE
        UPDATE tipo_cliente SET ESTADO_REGISTRO =2, ESTADO_PROCESO = 'ELIMINADO' WHERE idTipoCliente = P_ID  AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se eliminó correctamente al usuario';
    END IF;
END $$

DELIMITER ;


-- Crear procedimiento SP_INSERTAR_TIPO_COMPROBANTE

DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_TIPO_COMPROBANTE(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_comprobante
    WHERE nombre = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de comprobante con ese nombre';
    ELSE
        INSERT INTO tipo_comprobante (nombre, estado, usuario)
        VALUES (P_NOMBRE, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de comprobante';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_TIPO_COMPROBANTE

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

    SELECT COUNT(*) INTO cExiste FROM tipo_comprobante WHERE idTipoComprobante = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_comprobante WHERE NOMBRE = P_NOMBRE AND idTipoComprobante != P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de comprobante que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MS2J = 'El nombre ingresado ya existe';
    ELSE
        UPDATE tipo_comprobante 
        SET nombre = P_NOMBRE, estado = P_ESTADO, estado_proceso = 'MODIFICADO'
        WHERE idTipoComprobante = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se actualizó correctamente el tipo de comprobante';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DAR_BAJA_COMPROBANTE

DELIMITER $$
CREATE PROCEDURE SP_DAR_BAJA_TIPO_COMPROBANTE(
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

    SELECT COUNT(*) INTO cExiste FROM tipo_comprobante WHERE idTipoComprobante = P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de comprobante que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_comprobante 
        SET estado = 0, ESTADO_PROCESO = 'MODIFICADO'
        WHERE idTipoComprobante = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se dio de baja correctamente al tipo de comprobante';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_COMPROBANTE
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_TIPO_COMPROBANTE(
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

    SELECT COUNT(*) INTO cUsuario FROM tipo_comprobante where idTipoComprobante = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MS2J = 'El tipo de comprobante que intenta eliminar no existe';
    ELSE
        UPDATE tipo_comprobante SET ESTADO_REGISTRO =2, ESTADO_PROCESO = 'ELIMINADO' WHERE idTipoComprobante = P_ID  AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se eliminó correctamente el tipo de comprobante';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_INSERTAR_MICROSERVICIO

DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_MICROSERVICIO(
    IN P_NOMBRE VARCHAR(50),
    IN P_DESP VARCHAR (255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM microservicio
    WHERE nombre = P_NOMBRE;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un microservicio con ese nombre';
    ELSE
        INSERT INTO microservicio (nombre, descripcion, estado, usuario)
        VALUES (P_NOMBRE, P_DESP, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el microservicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_MICROSERVICIO

DELIMITER $$
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

    SELECT COUNT(*) INTO cExiste FROM microservicio WHERE id = P_ID;
    SELECT COUNT(*) INTO cNombre FROM microservicio WHERE NOMBRE = P_NOMBRE AND id != P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el microservicio que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MS2J = 'El nombre del microservicio ingresado ya existe';
    ELSE
        UPDATE microservicio 
        SET nombre = P_NOMBRE, descripcion = P_DESP, estado = P_ESTADO WHERE id = P_ID;

        SET @MSJ = 'Se actualizó correctamente el microservicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DAR_BAJA_MICROSERVICIO

DELIMITER $$
CREATE PROCEDURE SP_DAR_BAJA_MICROSERVICIO(
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

    SELECT COUNT(*) INTO cExiste FROM microservicio WHERE id = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El microservicio que intenta dar de baja no existe';
    ELSE
        UPDATE microservicio 
        SET estado = 0 WHERE id = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al microservicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_MICROSERVICIO
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_MICROSERVICIO(
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

    SELECT COUNT(*) INTO cUsuario FROM microservicio where id = P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El microservicio que intenta eliminar no existe';
    ELSE
        DELETE FROM servicio_microservicio WHERE idMicroservicio = P_ID;
        DELETE FROM microservicio WHERE id = P_ID;

        SET @MSJ = 'Se eliminó correctamente el microservicio';
    END IF;
END $$
DELIMITER ;


-- Procedimientos almacenados de servicios
DELIMITER $$

-- SP: Insertar Servicio
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

    SELECT COUNT(*) INTO existe_nombre FROM servicio WHERE nombre = P_NOMBRE;

    IF existe_nombre = 0 THEN
        INSERT INTO servicio (nombre, descripcion, estado, usuario, imagen)
        VALUES (P_NOMBRE, P_DESCRIPCION, P_ESTADO, P_USUARIO, P_IMAGEN);
        SET @MSJ = 'Se registró correctamente el servicio';
    ELSE
        SET @MSJ2 = 'Ya existe un servicio con ese nombre registrado';
    END IF;
END$$


-- SP: Actualizar Servicio
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

    SELECT COUNT(*) INTO existe_nombre FROM servicio WHERE nombre = P_NOMBRE AND id != P_ID;

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
END$$


-- SP: Dar de Baja Servicio (actualiza estado a 0)
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

    SELECT COUNT(*) INTO existe FROM servicio WHERE ID = P_ID;

    IF existe <= 0 THEN
        SET @MSJ2 = 'El servicio al que intenta dar de baja no existe';
    ELSE
        UPDATE servicio 
        SET estado = 0 
        WHERE id = P_ID;

        SET @MSJ = 'Servicio dado de baja correctamente';
    END IF;
END$$


-- SP: Eliminar Servicio (delete físico + relación)
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

    SELECT COUNT(*) INTO existe FROM servicio WHERE ID = P_ID;

    IF existe <= 0 THEN
        SET @MSJ2 = 'El servicio al que intenta eliminar no existe';
    ELSE
        DELETE FROM servicio_microservicio WHERE idServicio = P_ID;
        DELETE FROM servicio WHERE ID = P_ID;

        SET @MSJ = 'Servicio eliminado correctamente';
    END IF;
END$$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_METODO_PAGO
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM metodo_pago WHERE NOMBRE = P_NOMBRE and ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El método de pago que intenta registrar ya está registrado';
    ELSE
        INSERT INTO metodo_pago (NOMBRE, LOGO, ESTADO, ESTADO_PROCESO, ESTADO_REGISTRO, FECHA_REGISTRO, USUARIO, qr, id_tipo_metodoPago) 
        VALUES (P_NOMBRE, P_LOGO, P_ESTADO, DEFAULT, DEFAULT, CURRENT_TIMESTAMP, P_USUARIO, P_QR, P_TIPO_METODO_PAGO);

        SET @MSJ = 'Se registró correctamente el método de pago';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_EDITAR_METODO_PAGO
DELIMITER $$ 
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
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    -- Verificar si el método de pago existe
    SELECT COUNT(*) INTO cMetodoPago FROM metodo_pago WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    
    -- Verificar si el nombre del método de pago ya está registrado (excluyendo el registro actual)
    SELECT COUNT(*) INTO cNombre FROM metodo_pago WHERE NOMBRE = P_NOMBRE AND ID != P_ID and ESTADO_REGISTRO = 1;

    IF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre del método de pago ingresado ya existe';
    ELSE
        -- Actualizar los datos del método de pago, con el estado de registro siempre igual a 1 y el estado de proceso modificado
        UPDATE metodo_pago 
        SET NOMBRE = P_NOMBRE, 
            LOGO = P_LOGO,
            ESTADO = P_ESTADO,
            ESTADO_PROCESO = 'MODIFICADO',
            ESTADO_REGISTRO = 1, -- El estado de registro permanece en 1
            QR= P_QR,
            id_tipo_metodoPago = P_TIPO_METODO_PAGO
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se modificó correctamente el método de pago';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DARBAJA_METODO_PAGO

DELIMITER $$ 
CREATE PROCEDURE SP_DARBAJA_METODO_PAGO(
    IN P_ID INT
)
BEGIN
    DECLARE cMetodoPago INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMetodoPago FROM metodo_pago WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta dar de baja no existe';
    ELSE
        UPDATE metodo_pago 
        SET ESTADO = 0, 
            ESTADO_PROCESO = 'DADO DE BAJA' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se dio de baja correctamente el método de pago';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_METODO_PAGO
DELIMITER $$ 
CREATE PROCEDURE SP_ELIMINAR_METODO_PAGO(
    IN P_ID INT
)
BEGIN
    DECLARE cMetodoPago INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMetodoPago FROM metodo_pago WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cMetodoPago <= 0 THEN
        SET @MSJ2 = 'El método de pago que intenta eliminar no existe';
    ELSE
        UPDATE metodo_pago 
        SET ESTADO_REGISTRO = 2, 
            ESTADO_PROCESO = 'ELIMINADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se eliminó correctamente el método de pago';
    END IF;
END $$

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

    SELECT COUNT(*) INTO cNombre FROM marca WHERE NOMBRE = P_NOMBRE and ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'La marca ya está registrada';
    ELSE
        INSERT INTO marca (NOMBRE, ESTADO, ESTADO_PROCESO, ESTADO_REGISTRO, FECHA_REGISTRO, USUARIO, LOGO) 
        VALUES (P_NOMBRE, P_ESTADO, DEFAULT, DEFAULT, CURRENT_TIMESTAMP, P_USUARIO, P_LOGO); -- Incluir logo

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

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM marca WHERE NOMBRE = P_NOMBRE AND ID != P_ID and ESTADO_REGISTRO = 1;

    IF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre de la marca ya existe';
    ELSE
        UPDATE marca 
        SET NOMBRE = P_NOMBRE, 
            ESTADO = P_ESTADO,
            LOGO = P_LOGO, -- Actualizar logo
            ESTADO_PROCESO = 'MODIFICADO',
            ESTADO_REGISTRO = 1 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSE
        UPDATE marca 
        SET ESTADO = 0, 
            ESTADO_PROCESO = 'DADO DE BAJA' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cMarca FROM marca WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cMarca <= 0 THEN
        SET @MSJ2 = 'Marca no encontrada';
    ELSE
        UPDATE marca 
        SET ESTADO_REGISTRO = 2, 
            ESTADO_PROCESO = 'ELIMINADA' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Marca eliminada correctamente';
    END IF;
END $$ 

-- Crear procedimiento SP_REGISTRAR_RUTA
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_RUTA(
    IN P_NOMBRE VARCHAR(255),
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

    SELECT COUNT(*) INTO cNombre FROM ruta WHERE nombre = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre de ruta que intenta registrar ya está registrado';
    ELSE
        INSERT INTO ruta (NOMBRE, TIPO, ESTADO, USUARIO) 
        VALUES (P_NOMBRE, P_TIPO, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente la ruta';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_EDITAR_RUTA
DELIMITER $$
CREATE PROCEDURE SP_EDITAR_RUTA(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(255),
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

    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM ruta WHERE NOMBRE = P_NOMBRE AND ID != P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE ruta 
        SET NOMBRE = P_NOMBRE,
            TIPO = P_TIPO,
            ESTADO = P_ESTADO, 
            estado_proceso = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta dar de baja no existe';
    ELSE
        UPDATE ruta SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cExiste FROM ruta WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'La ruta que intenta eliminar no existe';
    ELSE
        -- UPDATE ruta SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        DELETE FROM escala WHERE idRuta = P_ID;
        DELETE FROM ruta WHERE id = ID;

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

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta editar no existe';
    ELSE
        UPDATE personal 
        SET NOMBRE = P_NOMBRE,
            IMAGEN = P_IMAGEN,
            ESTADO = P_ESTADO,
            ID_TIPOPERSONAL = P_IDTIPOPERSONAL, 
            ESTADO_PROCESO = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
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

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta dar de baja no existe';
    ELSE
        UPDATE personal SET ESTADO = 0, ESTADO_PROCESO = 'MODIFICADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cPersonal FROM personal WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cPersonal <= 0 THEN
        SET @MSJ2 = 'El personal que intenta eliminar no existe';
    ELSE
        UPDATE personal SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    IF cExiste <= 0 THEN
        SET @MSJ2 = 'El tipo de método de pago que intenta eliminar no existe';
    ELSE
        DELETE FROM tipo_metodoPago 
        WHERE idTipoMetodoPago = P_ID;

        SET @MSJ = 'Se eliminó correctamente el tipo de método de pago';
    END IF;
END $$

