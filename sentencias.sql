-- Primero eliminamos los procedimientos por si existen
DROP PROCEDURE IF EXISTS SP_ASIGNAR_DMENU;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_DMENU;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_EDITAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ACTIVAR_PLANTILLA;
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

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPOVEHICULO;

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_COMPROBANTE;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_COMPROBANTE;

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_SERVICIO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_SERVICIO;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_SERVICIO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_SERVICIO;

-- Luego eliminamos las tablas, primero la que depende de la otra
DROP TABLE IF EXISTS conf_plantillas;
DROP TABLE IF EXISTS conf_dmenus;
DROP TABLE IF EXISTS conf_menus;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS tipo_usuario;
DROP TABLE IF EXISTS tipo_vehiculo;
DROP TABLE IF EXISTS sucursal;
DROP TABLE IF EXISTS horario;
DROP TABLE IF EXISTS tipo_cliente;
DROP TABLE IF EXISTS ubigeo;
DROP TABLE IF EXISTS metodo_pago;
DROP TABLE IF EXISTS tipo_personal;
DROP TABLE IF EXISTS tipo_servicio;
DROP TABLE IF EXISTS tipo_comprobante;
DROP TABLE IF EXISTS tipo_documento;

-- Crear tabla tipo_servicio
CREATE TABLE tipo_servicio (
    idTipoServicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    estado BOOLEAN NOT NULL,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100) not null
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
    ubigeo CHAR(6) NOT NULL REFERENCES ubigeo(ubigeo),
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    latitud DECIMAL(8,6) NOT NULL,
    longitud DECIMAL(9,6) NOT NULL,
    estado TINYINT NOT NULL DEFAULT 1,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT NOT NULL DEFAULT 1,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
    idMenu INT REFERENCES conf_menus (id),
    idUsuario INT REFERENCES usuarios (id),
    PRIMARY KEY (idMenu, idUsuario)
);

-- Crear tabla conf_plantillas
CREATE TABLE conf_plantillas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    color_header VARCHAR(255) NOT NULL,
    color_footer VARCHAR(255) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    usuario VARCHAR(100) NOT NULL
);

CREATE TABLE tipo_vehiculo(
	idTipoVehiculo int AUTO_INCREMENT primary key,
    nombre varchar(50) not null,
    capacidad int not null,
    estado TINYINT not null
);

-- Crear tabla metodo_pago
CREATE TABLE metodo_pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
    usuario VARCHAR(100) not null
);

-- INSERTS DE UBIGEO
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010101','Amazonas','Chachapoyas','Chachapoyas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010102','Amazonas','Chachapoyas','Asuncion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010103','Amazonas','Chachapoyas','Balsas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010104','Amazonas','Chachapoyas','Cheto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010105','Amazonas','Chachapoyas','Chiliquin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010106','Amazonas','Chachapoyas','Chuquibamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010107','Amazonas','Chachapoyas','Granada');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010108','Amazonas','Chachapoyas','Huancas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010109','Amazonas','Chachapoyas','La Jalca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010110','Amazonas','Chachapoyas','Leimebamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010111','Amazonas','Chachapoyas','Levanto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010112','Amazonas','Chachapoyas','Magdalena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010113','Amazonas','Chachapoyas','Mariscal Castilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010114','Amazonas','Chachapoyas','Molinopampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010115','Amazonas','Chachapoyas','Montevideo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010116','Amazonas','Chachapoyas','Olleros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010117','Amazonas','Chachapoyas','Quinjalca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010118','Amazonas','Chachapoyas','San Francisco de Daguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010119','Amazonas','Chachapoyas','San Isidro de Maino');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010120','Amazonas','Chachapoyas','Soloco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010121','Amazonas','Chachapoyas','Sonche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010201','Amazonas','Bagua','Bagua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010202','Amazonas','Bagua','Aramango');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010203','Amazonas','Bagua','Copallin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010204','Amazonas','Bagua','El Parco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010205','Amazonas','Bagua','Imaza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010206','Amazonas','Bagua','La Peca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010301','Amazonas','Bongara','Jumbilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010302','Amazonas','Bongara','Chisquilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010303','Amazonas','Bongara','Churuja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010304','Amazonas','Bongara','Corosha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010305','Amazonas','Bongara','Cuispes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010306','Amazonas','Bongara','Florida');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010307','Amazonas','Bongara','Jazan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010308','Amazonas','Bongara','Recta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010309','Amazonas','Bongara','San Carlos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010310','Amazonas','Bongara','Shipasbamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010311','Amazonas','Bongara','Valera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010312','Amazonas','Bongara','Yambrasbamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010401','Amazonas','Condorcanqui','Nieva');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010402','Amazonas','Condorcanqui','El Cenepa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010403','Amazonas','Condorcanqui','Rio Santiago');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010501','Amazonas','Luya','Lamud');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010502','Amazonas','Luya','Camporredondo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010503','Amazonas','Luya','Cocabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010504','Amazonas','Luya','Colcamar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010505','Amazonas','Luya','Conila');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010506','Amazonas','Luya','Inguilpata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010507','Amazonas','Luya','Longuita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010508','Amazonas','Luya','Lonya Chico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010509','Amazonas','Luya','Luya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010510','Amazonas','Luya','Luya Viejo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010511','Amazonas','Luya','Maria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010512','Amazonas','Luya','Ocalli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010513','Amazonas','Luya','Ocumal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010514','Amazonas','Luya','Pisuquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010515','Amazonas','Luya','Providencia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010516','Amazonas','Luya','San Cristobal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010517','Amazonas','Luya','San Francisco del Yeso');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010518','Amazonas','Luya','San Jeronimo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010519','Amazonas','Luya','San Juan de Lopecancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010520','Amazonas','Luya','Santa Catalina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010521','Amazonas','Luya','Santo Tomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010522','Amazonas','Luya','Tingo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010523','Amazonas','Luya','Trita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010601','Amazonas','Rodriguez de Mendoza','San Nicolas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010602','Amazonas','Rodriguez de Mendoza','Chirimoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010603','Amazonas','Rodriguez de Mendoza','Cochamal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010604','Amazonas','Rodriguez de Mendoza','Huambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010605','Amazonas','Rodriguez de Mendoza','Limabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010606','Amazonas','Rodriguez de Mendoza','Longar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010607','Amazonas','Rodriguez de Mendoza','Mariscal Benavides');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010608','Amazonas','Rodriguez de Mendoza','Milpuc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010609','Amazonas','Rodriguez de Mendoza','Omia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010610','Amazonas','Rodriguez de Mendoza','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010611','Amazonas','Rodriguez de Mendoza','Totora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010612','Amazonas','Rodriguez de Mendoza','Vista Alegre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010701','Amazonas','Utcubamba','Bagua Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010702','Amazonas','Utcubamba','Cajaruro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010703','Amazonas','Utcubamba','Cumba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010704','Amazonas','Utcubamba','El Milagro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010705','Amazonas','Utcubamba','Jamalca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010706','Amazonas','Utcubamba','Lonya Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('010707','Amazonas','Utcubamba','Yamon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020101','Ancash','Huaraz','Huaraz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020102','Ancash','Huaraz','Cochabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020103','Ancash','Huaraz','Colcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020104','Ancash','Huaraz','Huanchay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020105','Ancash','Huaraz','Independencia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020106','Ancash','Huaraz','Jangas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020107','Ancash','Huaraz','La Libertad');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020108','Ancash','Huaraz','Olleros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020109','Ancash','Huaraz','Pampas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020110','Ancash','Huaraz','Pariacoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020111','Ancash','Huaraz','Pira');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020112','Ancash','Huaraz','Tarica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020201','Ancash','Aija','Aija');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020202','Ancash','Aija','Coris');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020203','Ancash','Aija','Huacllan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020204','Ancash','Aija','La Merced');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020205','Ancash','Aija','Succha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020301','Ancash','Antonio Raymondi','Llamellin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020302','Ancash','Antonio Raymondi','Aczo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020303','Ancash','Antonio Raymondi','Chaccho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020304','Ancash','Antonio Raymondi','Chingas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020305','Ancash','Antonio Raymondi','Mirgas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020306','Ancash','Antonio Raymondi','San Juan de Rontoy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020401','Ancash','Asuncion','Chacas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020402','Ancash','Asuncion','Acochaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020501','Ancash','Bolognesi','Chiquian');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020502','Ancash','Bolognesi','Abelardo Pardo Lezameta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020503','Ancash','Bolognesi','Antonio Raymondi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020504','Ancash','Bolognesi','Aquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020505','Ancash','Bolognesi','Cajacay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020506','Ancash','Bolognesi','Canis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020507','Ancash','Bolognesi','Colquioc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020508','Ancash','Bolognesi','Huallanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020509','Ancash','Bolognesi','Huasta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020510','Ancash','Bolognesi','Huayllacayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020511','Ancash','Bolognesi','La Primavera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020512','Ancash','Bolognesi','Mangas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020513','Ancash','Bolognesi','Pacllon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020514','Ancash','Bolognesi','San Miguel de Corpanqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020515','Ancash','Bolognesi','Ticllos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020601','Ancash','Carhuaz','Carhuaz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020602','Ancash','Carhuaz','Acopampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020603','Ancash','Carhuaz','Amashca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020604','Ancash','Carhuaz','Anta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020605','Ancash','Carhuaz','Ataquero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020606','Ancash','Carhuaz','Marcara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020607','Ancash','Carhuaz','Pariahuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020608','Ancash','Carhuaz','San Miguel de Aco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020609','Ancash','Carhuaz','Shilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020610','Ancash','Carhuaz','Tinco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020611','Ancash','Carhuaz','Yungar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020701','Ancash','Carlos Fermin Fitzca','San Luis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020702','Ancash','Carlos Fermin Fitzca','San Nicolas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020703','Ancash','Carlos Fermin Fitzca','Yauya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020801','Ancash','Casma','Casma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020802','Ancash','Casma','Buena Vista Alta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020803','Ancash','Casma','Comandante Noel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020804','Ancash','Casma','Yautan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020901','Ancash','Corongo','Corongo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020902','Ancash','Corongo','Aco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020903','Ancash','Corongo','Bambas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020904','Ancash','Corongo','Cusca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020905','Ancash','Corongo','La Pampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020906','Ancash','Corongo','Yanac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('020907','Ancash','Corongo','Yupan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021001','Ancash','Huari','Huari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021002','Ancash','Huari','Anra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021003','Ancash','Huari','Cajay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021004','Ancash','Huari','Chavin de Huantar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021005','Ancash','Huari','Huacachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021006','Ancash','Huari','Huacchis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021007','Ancash','Huari','Huachis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021008','Ancash','Huari','Huantar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021009','Ancash','Huari','Masin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021010','Ancash','Huari','Paucas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021011','Ancash','Huari','Ponto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021012','Ancash','Huari','Rahuapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021013','Ancash','Huari','Rapayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021014','Ancash','Huari','San Marcos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021015','Ancash','Huari','San Pedro de Chana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021016','Ancash','Huari','Uco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021101','Ancash','Huarmey','Huarmey');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021102','Ancash','Huarmey','Cochapeti');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021103','Ancash','Huarmey','Culebras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021104','Ancash','Huarmey','Huayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021105','Ancash','Huarmey','Malvas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021201','Ancash','Huaylas','Caraz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021202','Ancash','Huaylas','Huallanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021203','Ancash','Huaylas','Huata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021204','Ancash','Huaylas','Huaylas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021205','Ancash','Huaylas','Mato');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021206','Ancash','Huaylas','Pamparomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021207','Ancash','Huaylas','Pueblo Libre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021208','Ancash','Huaylas','Santa Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021209','Ancash','Huaylas','Santo Toribio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021210','Ancash','Huaylas','Yuracmarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021301','Ancash','Mariscal Luzuriaga','Piscobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021302','Ancash','Mariscal Luzuriaga','Casca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021303','Ancash','Mariscal Luzuriaga','Eleazar Guzman Barron');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021304','Ancash','Mariscal Luzuriaga','Fidel Olivas Escudero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021305','Ancash','Mariscal Luzuriaga','Llama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021306','Ancash','Mariscal Luzuriaga','Llumpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021307','Ancash','Mariscal Luzuriaga','Lucma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021308','Ancash','Mariscal Luzuriaga','Musga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021401','Ancash','Ocros','Ocros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021402','Ancash','Ocros','Acas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021403','Ancash','Ocros','Cajamarquilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021404','Ancash','Ocros','Carhuapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021405','Ancash','Ocros','Cochas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021406','Ancash','Ocros','Congas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021407','Ancash','Ocros','Llipa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021408','Ancash','Ocros','San Cristobal de Rajan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021409','Ancash','Ocros','San Pedro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021410','Ancash','Ocros','Santiago de Chilcas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021501','Ancash','Pallasca','Cabana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021502','Ancash','Pallasca','Bolognesi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021503','Ancash','Pallasca','Conchucos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021504','Ancash','Pallasca','Huacaschuque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021505','Ancash','Pallasca','Huandoval');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021506','Ancash','Pallasca','Lacabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021507','Ancash','Pallasca','Llapo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021508','Ancash','Pallasca','Pallasca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021509','Ancash','Pallasca','Pampas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021510','Ancash','Pallasca','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021511','Ancash','Pallasca','Tauca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021601','Ancash','Pomabamba','Pomabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021602','Ancash','Pomabamba','Huayllan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021603','Ancash','Pomabamba','Parobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021604','Ancash','Pomabamba','Quinuabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021701','Ancash','Recuay','Recuay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021702','Ancash','Recuay','Catac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021703','Ancash','Recuay','Cotaparaco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021704','Ancash','Recuay','Huayllapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021705','Ancash','Recuay','Llacllin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021706','Ancash','Recuay','Marca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021707','Ancash','Recuay','Pampas Chico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021708','Ancash','Recuay','Pararin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021709','Ancash','Recuay','Tapacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021710','Ancash','Recuay','Ticapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021801','Ancash','Santa','Chimbote');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021802','Ancash','Santa','Caceres del Peru');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021803','Ancash','Santa','Coishco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021804','Ancash','Santa','Macate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021805','Ancash','Santa','Moro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021806','Ancash','Santa','Nepeña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021807','Ancash','Santa','Samanco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021808','Ancash','Santa','Santa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021809','Ancash','Santa','Nuevo Chimbote');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021901','Ancash','Sihuas','Sihuas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021902','Ancash','Sihuas','Acobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021903','Ancash','Sihuas','Alfonso Ugarte');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021904','Ancash','Sihuas','Cashapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021905','Ancash','Sihuas','Chingalpo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021906','Ancash','Sihuas','Huayllabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021907','Ancash','Sihuas','Quiches');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021908','Ancash','Sihuas','Ragash');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021909','Ancash','Sihuas','San Juan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('021910','Ancash','Sihuas','Sicsibamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022001','Ancash','Yungay','Yungay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022002','Ancash','Yungay','Cascapara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022003','Ancash','Yungay','Mancos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022004','Ancash','Yungay','Matacoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022005','Ancash','Yungay','Quillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022006','Ancash','Yungay','Ranrahirca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022007','Ancash','Yungay','Shupluy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('022008','Ancash','Yungay','Yanama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030101','Apurimac','Abancay','Abancay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030102','Apurimac','Abancay','Chacoche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030103','Apurimac','Abancay','Circa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030104','Apurimac','Abancay','Curahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030105','Apurimac','Abancay','Huanipaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030106','Apurimac','Abancay','Lambrama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030107','Apurimac','Abancay','Pichirhua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030108','Apurimac','Abancay','San Pedro de Cachora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030109','Apurimac','Abancay','Tamburco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030201','Apurimac','Andahuaylas','Andahuaylas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030202','Apurimac','Andahuaylas','Andarapa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030203','Apurimac','Andahuaylas','Chiara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030204','Apurimac','Andahuaylas','Huancarama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030205','Apurimac','Andahuaylas','Huancaray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030206','Apurimac','Andahuaylas','Huayana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030207','Apurimac','Andahuaylas','Kishuara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030208','Apurimac','Andahuaylas','Pacobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030209','Apurimac','Andahuaylas','Pacucha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030210','Apurimac','Andahuaylas','Pampachiri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030211','Apurimac','Andahuaylas','Pomacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030212','Apurimac','Andahuaylas','San Antonio de Cachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030213','Apurimac','Andahuaylas','San Jeronimo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030214','Apurimac','Andahuaylas','San Miguel de Chaccrampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030215','Apurimac','Andahuaylas','Santa Maria de Chicmo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030216','Apurimac','Andahuaylas','Talavera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030217','Apurimac','Andahuaylas','Tumay Huaraca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030218','Apurimac','Andahuaylas','Turpo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030219','Apurimac','Andahuaylas','Kaquiabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030220','Apurimac','Andahuaylas','José María Arguedas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030301','Apurimac','Antabamba','Antabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030302','Apurimac','Antabamba','El Oro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030303','Apurimac','Antabamba','Huaquirca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030304','Apurimac','Antabamba','Juan Espinoza Medrano');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030305','Apurimac','Antabamba','Oropesa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030306','Apurimac','Antabamba','Pachaconas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030307','Apurimac','Antabamba','Sabaino');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030401','Apurimac','Aymaraes','Chalhuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030402','Apurimac','Aymaraes','Capaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030403','Apurimac','Aymaraes','Caraybamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030404','Apurimac','Aymaraes','Chapimarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030405','Apurimac','Aymaraes','Colcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030406','Apurimac','Aymaraes','Cotaruse');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030407','Apurimac','Aymaraes','Huayllo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030408','Apurimac','Aymaraes','Justo Apu Sahuaraura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030409','Apurimac','Aymaraes','Lucre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030410','Apurimac','Aymaraes','Pocohuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030411','Apurimac','Aymaraes','San Juan de Chacña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030412','Apurimac','Aymaraes','Sañayca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030413','Apurimac','Aymaraes','Soraya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030414','Apurimac','Aymaraes','Tapairihua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030415','Apurimac','Aymaraes','Tintay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030416','Apurimac','Aymaraes','Toraya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030417','Apurimac','Aymaraes','Yanaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030501','Apurimac','Cotabambas','Tambobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030502','Apurimac','Cotabambas','Cotabambas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030503','Apurimac','Cotabambas','Coyllurqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030504','Apurimac','Cotabambas','Haquira');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030505','Apurimac','Cotabambas','Mara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030506','Apurimac','Cotabambas','Challhuahuacho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030601','Apurimac','Chincheros','Chincheros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030602','Apurimac','Chincheros','Anco_Huallo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030603','Apurimac','Chincheros','Cocharcas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030604','Apurimac','Chincheros','Huaccana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030605','Apurimac','Chincheros','Ocobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030606','Apurimac','Chincheros','Ongoy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030607','Apurimac','Chincheros','Uranmarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030608','Apurimac','Chincheros','Ranracancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030609','Apurimac','Chincheros','Rocchacc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030610','Apurimac','Chincheros','El Porvenir');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030611','Apurimac','Chincheros','Los Chankas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030701','Apurimac','Grau','Chuquibambilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030702','Apurimac','Grau','Curpahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030703','Apurimac','Grau','Gamarra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030704','Apurimac','Grau','Huayllati');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030705','Apurimac','Grau','Mamara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030706','Apurimac','Grau','Micaela Bastidas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030707','Apurimac','Grau','Pataypampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030708','Apurimac','Grau','Progreso');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030709','Apurimac','Grau','San Antonio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030710','Apurimac','Grau','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030711','Apurimac','Grau','Turpay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030712','Apurimac','Grau','Vilcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030713','Apurimac','Grau','Virundo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('030714','Apurimac','Grau','Curasco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040101','Arequipa','Arequipa','Arequipa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040102','Arequipa','Arequipa','Alto Selva Alegre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040103','Arequipa','Arequipa','Cayma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040104','Arequipa','Arequipa','Cerro Colorado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040105','Arequipa','Arequipa','Characato');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040106','Arequipa','Arequipa','Chiguata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040107','Arequipa','Arequipa','Jacobo Hunter');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040108','Arequipa','Arequipa','La Joya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040109','Arequipa','Arequipa','Mariano Melgar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040110','Arequipa','Arequipa','Miraflores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040111','Arequipa','Arequipa','Mollebaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040112','Arequipa','Arequipa','Paucarpata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040113','Arequipa','Arequipa','Pocsi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040114','Arequipa','Arequipa','Polobaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040115','Arequipa','Arequipa','Quequeña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040116','Arequipa','Arequipa','Sabandia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040117','Arequipa','Arequipa','Sachaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040118','Arequipa','Arequipa','San Juan de Siguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040119','Arequipa','Arequipa','San Juan de Tarucani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040120','Arequipa','Arequipa','Santa Isabel de Siguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040121','Arequipa','Arequipa','Santa Rita de Siguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040122','Arequipa','Arequipa','Socabaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040123','Arequipa','Arequipa','Tiabaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040124','Arequipa','Arequipa','Uchumayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040125','Arequipa','Arequipa','Vitor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040126','Arequipa','Arequipa','Yanahuara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040127','Arequipa','Arequipa','Yarabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040128','Arequipa','Arequipa','Yura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040129','Arequipa','Arequipa','Jose Luis Bustamante y Rivero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040201','Arequipa','Camana','Camana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040202','Arequipa','Camana','Jose Maria Quimper');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040203','Arequipa','Camana','Mariano Nicolas Valcarcel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040204','Arequipa','Camana','Mariscal Caceres');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040205','Arequipa','Camana','Nicolas de Pierola');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040206','Arequipa','Camana','Ocoña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040207','Arequipa','Camana','Quilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040208','Arequipa','Camana','Samuel Pastor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040301','Arequipa','Caraveli','Caraveli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040302','Arequipa','Caraveli','Acari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040303','Arequipa','Caraveli','Atico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040304','Arequipa','Caraveli','Atiquipa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040305','Arequipa','Caraveli','Bella Union');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040306','Arequipa','Caraveli','Cahuacho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040307','Arequipa','Caraveli','Chala');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040308','Arequipa','Caraveli','Chaparra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040309','Arequipa','Caraveli','Huanuhuanu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040310','Arequipa','Caraveli','Jaqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040311','Arequipa','Caraveli','Lomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040312','Arequipa','Caraveli','Quicacha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040313','Arequipa','Caraveli','Yauca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040401','Arequipa','Castilla','Aplao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040402','Arequipa','Castilla','Andagua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040403','Arequipa','Castilla','Ayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040404','Arequipa','Castilla','Chachas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040405','Arequipa','Castilla','Chilcaymarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040406','Arequipa','Castilla','Choco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040407','Arequipa','Castilla','Huancarqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040408','Arequipa','Castilla','Machaguay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040409','Arequipa','Castilla','Orcopampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040410','Arequipa','Castilla','Pampacolca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040411','Arequipa','Castilla','Tipan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040412','Arequipa','Castilla','Uñon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040413','Arequipa','Castilla','Uraca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040414','Arequipa','Castilla','Viraco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040501','Arequipa','Caylloma','Chivay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040502','Arequipa','Caylloma','Achoma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040503','Arequipa','Caylloma','Cabanaconde');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040504','Arequipa','Caylloma','Callalli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040505','Arequipa','Caylloma','Caylloma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040506','Arequipa','Caylloma','Coporaque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040507','Arequipa','Caylloma','Huambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040508','Arequipa','Caylloma','Huanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040509','Arequipa','Caylloma','Ichupampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040510','Arequipa','Caylloma','Lari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040511','Arequipa','Caylloma','Lluta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040512','Arequipa','Caylloma','Maca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040513','Arequipa','Caylloma','Madrigal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040514','Arequipa','Caylloma','San Antonio de Chuca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040515','Arequipa','Caylloma','Sibayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040516','Arequipa','Caylloma','Tapay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040517','Arequipa','Caylloma','Tisco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040518','Arequipa','Caylloma','Tuti');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040519','Arequipa','Caylloma','Yanque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040520','Arequipa','Caylloma','Majes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040601','Arequipa','Condesuyos','Chuquibamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040602','Arequipa','Condesuyos','Andaray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040603','Arequipa','Condesuyos','Cayarani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040604','Arequipa','Condesuyos','Chichas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040605','Arequipa','Condesuyos','Iray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040606','Arequipa','Condesuyos','Rio Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040607','Arequipa','Condesuyos','Salamanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040608','Arequipa','Condesuyos','Yanaquihua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040701','Arequipa','Islay','Mollendo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040702','Arequipa','Islay','Cocachacra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040703','Arequipa','Islay','Dean Valdivia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040704','Arequipa','Islay','Islay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040705','Arequipa','Islay','Mejia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040706','Arequipa','Islay','Punta de Bombon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040801','Arequipa','La Union','Cotahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040802','Arequipa','La Union','Alca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040803','Arequipa','La Union','Charcana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040804','Arequipa','La Union','Huaynacotas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040805','Arequipa','La Union','Pampamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040806','Arequipa','La Union','Puyca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040807','Arequipa','La Union','Quechualla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040808','Arequipa','La Union','Sayla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040809','Arequipa','La Union','Tauria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040810','Arequipa','La Union','Tomepampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('040811','Arequipa','La Union','Toro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050101','Ayacucho','Huamanga','Ayacucho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050102','Ayacucho','Huamanga','Acocro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050103','Ayacucho','Huamanga','Acos Vinchos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050104','Ayacucho','Huamanga','Carmen Alto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050105','Ayacucho','Huamanga','Chiara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050106','Ayacucho','Huamanga','Ocros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050107','Ayacucho','Huamanga','Pacaycasa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050108','Ayacucho','Huamanga','Quinua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050109','Ayacucho','Huamanga','San Jose de Ticllas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050110','Ayacucho','Huamanga','San Juan Bautista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050111','Ayacucho','Huamanga','Santiago de Pischa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050112','Ayacucho','Huamanga','Socos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050113','Ayacucho','Huamanga','Tambillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050114','Ayacucho','Huamanga','Vinchos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050115','Ayacucho','Huamanga','Jesus Nazareno');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050116','Ayacucho','Huamanga','Andrés Avelino Cáceres Dorregaray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050201','Ayacucho','Cangallo','Cangallo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050202','Ayacucho','Cangallo','Chuschi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050203','Ayacucho','Cangallo','Los Morochucos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050204','Ayacucho','Cangallo','Maria Parado de Bellido');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050205','Ayacucho','Cangallo','Paras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050206','Ayacucho','Cangallo','Totos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050301','Ayacucho','Huanca Sancos','Sancos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050302','Ayacucho','Huanca Sancos','Carapo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050303','Ayacucho','Huanca Sancos','Sacsamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050304','Ayacucho','Huanca Sancos','Santiago de Lucanamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050401','Ayacucho','Huanta','Huanta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050402','Ayacucho','Huanta','Ayahuanco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050403','Ayacucho','Huanta','Huamanguilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050404','Ayacucho','Huanta','Iguain');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050405','Ayacucho','Huanta','Luricocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050406','Ayacucho','Huanta','Santillana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050407','Ayacucho','Huanta','Sivia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050408','Ayacucho','Huanta','Llochegua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050409','Ayacucho','Huanta','Canayre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050410','Ayacucho','Huanta','Uchuraccay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050411','Ayacucho','Huanta','Pucacolpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050412','Ayacucho','Huanta','Chaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050501','Ayacucho','La Mar','San Miguel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050502','Ayacucho','La Mar','Anco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050503','Ayacucho','La Mar','Ayna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050504','Ayacucho','La Mar','Chilcas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050505','Ayacucho','La Mar','Chungui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050506','Ayacucho','La Mar','Luis Carranza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050507','Ayacucho','La Mar','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050508','Ayacucho','La Mar','Tambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050509','Ayacucho','La Mar','Samugari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050510','Ayacucho','La Mar','Anchihuay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050511','Ayacucho','La Mar','Oronccoy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050601','Ayacucho','Lucanas','Puquio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050602','Ayacucho','Lucanas','Aucara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050603','Ayacucho','Lucanas','Cabana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050604','Ayacucho','Lucanas','Carmen Salcedo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050605','Ayacucho','Lucanas','Chaviña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050606','Ayacucho','Lucanas','Chipao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050607','Ayacucho','Lucanas','Huac-Huas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050608','Ayacucho','Lucanas','Laramate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050609','Ayacucho','Lucanas','Leoncio Prado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050610','Ayacucho','Lucanas','Llauta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050611','Ayacucho','Lucanas','Lucanas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050612','Ayacucho','Lucanas','Ocaña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050613','Ayacucho','Lucanas','Otoca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050614','Ayacucho','Lucanas','Saisa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050615','Ayacucho','Lucanas','San Cristobal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050616','Ayacucho','Lucanas','San Juan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050617','Ayacucho','Lucanas','San Pedro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050618','Ayacucho','Lucanas','San Pedro de Palco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050619','Ayacucho','Lucanas','Sancos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050620','Ayacucho','Lucanas','Santa Ana de Huaycahuacho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050621','Ayacucho','Lucanas','Santa Lucia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050701','Ayacucho','Parinacochas','Coracora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050702','Ayacucho','Parinacochas','Chumpi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050703','Ayacucho','Parinacochas','Coronel Castañeda');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050704','Ayacucho','Parinacochas','Pacapausa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050705','Ayacucho','Parinacochas','Pullo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050706','Ayacucho','Parinacochas','Puyusca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050707','Ayacucho','Parinacochas','San Francisco de Ravacayco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050708','Ayacucho','Parinacochas','Upahuacho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050801','Ayacucho','Paucar del Sara Sara','Pausa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050802','Ayacucho','Paucar del Sara Sara','Colta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050803','Ayacucho','Paucar del Sara Sara','Corculla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050804','Ayacucho','Paucar del Sara Sara','Lampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050805','Ayacucho','Paucar del Sara Sara','Marcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050806','Ayacucho','Paucar del Sara Sara','Oyolo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050807','Ayacucho','Paucar del Sara Sara','Pararca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050808','Ayacucho','Paucar del Sara Sara','San Javier de Alpabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050809','Ayacucho','Paucar del Sara Sara','San Jose de Ushua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050810','Ayacucho','Paucar del Sara Sara','Sara Sara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050901','Ayacucho','Sucre','Querobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050902','Ayacucho','Sucre','Belen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050903','Ayacucho','Sucre','Chalcos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050904','Ayacucho','Sucre','Chilcayoc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050905','Ayacucho','Sucre','Huacaña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050906','Ayacucho','Sucre','Morcolla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050907','Ayacucho','Sucre','Paico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050908','Ayacucho','Sucre','San Pedro de Larcay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050909','Ayacucho','Sucre','San Salvador de Quije');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050910','Ayacucho','Sucre','Santiago de Paucaray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('050911','Ayacucho','Sucre','Soras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051001','Ayacucho','Victor Fajardo','Huancapi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051002','Ayacucho','Victor Fajardo','Alcamenca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051003','Ayacucho','Victor Fajardo','Apongo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051004','Ayacucho','Victor Fajardo','Asquipata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051005','Ayacucho','Victor Fajardo','Canaria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051006','Ayacucho','Victor Fajardo','Cayara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051007','Ayacucho','Victor Fajardo','Colca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051008','Ayacucho','Victor Fajardo','Huamanquiquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051009','Ayacucho','Victor Fajardo','Huancaraylla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051010','Ayacucho','Victor Fajardo','Huaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051011','Ayacucho','Victor Fajardo','Sarhua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051012','Ayacucho','Victor Fajardo','Vilcanchos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051101','Ayacucho','Vilcas Huaman','Vilcas Huaman');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051102','Ayacucho','Vilcas Huaman','Accomarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051103','Ayacucho','Vilcas Huaman','Carhuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051104','Ayacucho','Vilcas Huaman','Concepcion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051105','Ayacucho','Vilcas Huaman','Huambalpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051106','Ayacucho','Vilcas Huaman','Independencia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051107','Ayacucho','Vilcas Huaman','Saurama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('051108','Ayacucho','Vilcas Huaman','Vischongo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060101','Cajamarca','Cajamarca','Cajamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060102','Cajamarca','Cajamarca','Asuncion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060103','Cajamarca','Cajamarca','Chetilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060104','Cajamarca','Cajamarca','Cospan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060105','Cajamarca','Cajamarca','Encañada');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060106','Cajamarca','Cajamarca','Jesus');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060107','Cajamarca','Cajamarca','Llacanora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060108','Cajamarca','Cajamarca','Los Baños del Inca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060109','Cajamarca','Cajamarca','Magdalena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060110','Cajamarca','Cajamarca','Matara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060111','Cajamarca','Cajamarca','Namora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060112','Cajamarca','Cajamarca','San Juan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060201','Cajamarca','Cajabamba','Cajabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060202','Cajamarca','Cajabamba','Cachachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060203','Cajamarca','Cajabamba','Condebamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060204','Cajamarca','Cajabamba','Sitacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060301','Cajamarca','Celendin','Celendin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060302','Cajamarca','Celendin','Chumuch');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060303','Cajamarca','Celendin','Cortegana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060304','Cajamarca','Celendin','Huasmin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060305','Cajamarca','Celendin','Jorge Chavez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060306','Cajamarca','Celendin','Jose Galvez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060307','Cajamarca','Celendin','Miguel Iglesias');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060308','Cajamarca','Celendin','Oxamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060309','Cajamarca','Celendin','Sorochuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060310','Cajamarca','Celendin','Sucre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060311','Cajamarca','Celendin','Utco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060312','Cajamarca','Celendin','La Libertad de Pallan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060401','Cajamarca','Chota','Chota');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060402','Cajamarca','Chota','Anguia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060403','Cajamarca','Chota','Chadin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060404','Cajamarca','Chota','Chiguirip');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060405','Cajamarca','Chota','Chimban');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060406','Cajamarca','Chota','Choropampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060407','Cajamarca','Chota','Cochabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060408','Cajamarca','Chota','Conchan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060409','Cajamarca','Chota','Huambos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060410','Cajamarca','Chota','Lajas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060411','Cajamarca','Chota','Llama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060412','Cajamarca','Chota','Miracosta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060413','Cajamarca','Chota','Paccha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060414','Cajamarca','Chota','Pion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060415','Cajamarca','Chota','Querocoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060416','Cajamarca','Chota','San Juan de Licupis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060417','Cajamarca','Chota','Tacabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060418','Cajamarca','Chota','Tocmoche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060419','Cajamarca','Chota','Chalamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060501','Cajamarca','Contumaza','Contumaza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060502','Cajamarca','Contumaza','Chilete');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060503','Cajamarca','Contumaza','Cupisnique');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060504','Cajamarca','Contumaza','Guzmango');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060505','Cajamarca','Contumaza','San Benito');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060506','Cajamarca','Contumaza','Santa Cruz de Toled');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060507','Cajamarca','Contumaza','Tantarica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060508','Cajamarca','Contumaza','Yonan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060601','Cajamarca','Cutervo','Cutervo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060602','Cajamarca','Cutervo','Callayuc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060603','Cajamarca','Cutervo','Choros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060604','Cajamarca','Cutervo','Cujillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060605','Cajamarca','Cutervo','La Ramada');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060606','Cajamarca','Cutervo','Pimpingos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060607','Cajamarca','Cutervo','Querocotillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060608','Cajamarca','Cutervo','San Andres de Cutervo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060609','Cajamarca','Cutervo','San Juan de Cutervo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060610','Cajamarca','Cutervo','San Luis de Lucma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060611','Cajamarca','Cutervo','Santa Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060612','Cajamarca','Cutervo','Santo Domingo de La Capilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060613','Cajamarca','Cutervo','Santo Tomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060614','Cajamarca','Cutervo','Socota');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060615','Cajamarca','Cutervo','Toribio Casanova');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060701','Cajamarca','Hualgayoc','Bambamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060702','Cajamarca','Hualgayoc','Chugur');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060703','Cajamarca','Hualgayoc','Hualgayoc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060801','Cajamarca','Jaen','Jaen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060802','Cajamarca','Jaen','Bellavista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060803','Cajamarca','Jaen','Chontali');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060804','Cajamarca','Jaen','Colasay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060805','Cajamarca','Jaen','Huabal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060806','Cajamarca','Jaen','Las Pirias');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060807','Cajamarca','Jaen','Pomahuaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060808','Cajamarca','Jaen','Pucara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060809','Cajamarca','Jaen','Sallique');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060810','Cajamarca','Jaen','San Felipe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060811','Cajamarca','Jaen','San Jose del Alto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060812','Cajamarca','Jaen','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060901','Cajamarca','San Ignacio','San Ignacio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060902','Cajamarca','San Ignacio','Chirinos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060903','Cajamarca','San Ignacio','Huarango');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060904','Cajamarca','San Ignacio','La Coipa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060905','Cajamarca','San Ignacio','Namballe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060906','Cajamarca','San Ignacio','San Jose de Lourdes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('060907','Cajamarca','San Ignacio','Tabaconas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061001','Cajamarca','San Marcos','Pedro Galvez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061002','Cajamarca','San Marcos','Chancay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061003','Cajamarca','San Marcos','Eduardo Villanueva');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061004','Cajamarca','San Marcos','Gregorio Pita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061005','Cajamarca','San Marcos','Ichocan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061006','Cajamarca','San Marcos','Jose Manuel Quiroz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061007','Cajamarca','San Marcos','Jose Sabogal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061101','Cajamarca','San Miguel','San Miguel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061102','Cajamarca','San Miguel','Bolivar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061103','Cajamarca','San Miguel','Calquis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061104','Cajamarca','San Miguel','Catilluc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061105','Cajamarca','San Miguel','El Prado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061106','Cajamarca','San Miguel','La Florida');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061107','Cajamarca','San Miguel','Llapa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061108','Cajamarca','San Miguel','Nanchoc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061109','Cajamarca','San Miguel','Niepos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061110','Cajamarca','San Miguel','San Gregorio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061111','Cajamarca','San Miguel','San Silvestre de Cochan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061112','Cajamarca','San Miguel','Tongod');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061113','Cajamarca','San Miguel','Union Agua Blanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061201','Cajamarca','San Pablo','San Pablo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061202','Cajamarca','San Pablo','San Bernardino');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061203','Cajamarca','San Pablo','San Luis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061204','Cajamarca','San Pablo','Tumbaden');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061301','Cajamarca','Santa Cruz','Santa Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061302','Cajamarca','Santa Cruz','Andabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061303','Cajamarca','Santa Cruz','Catache');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061304','Cajamarca','Santa Cruz','Chancaybaños');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061305','Cajamarca','Santa Cruz','La Esperanza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061306','Cajamarca','Santa Cruz','Ninabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061307','Cajamarca','Santa Cruz','Pulan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061308','Cajamarca','Santa Cruz','Saucepampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061309','Cajamarca','Santa Cruz','Sexi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061310','Cajamarca','Santa Cruz','Uticyacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('061311','Cajamarca','Santa Cruz','Yauyucan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070101','Callao','Callao','Callao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070102','Callao','Callao','Bellavista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070103','Callao','Callao','Carmen de La Legua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070104','Callao','Callao','La Perla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070105','Callao','Callao','La Punta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070106','Callao','Callao','Ventanilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('070107','Callao','Callao','Mi Peru');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080101','Cusco','Cusco','Cusco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080102','Cusco','Cusco','Ccorca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080103','Cusco','Cusco','Poroy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080104','Cusco','Cusco','San Jeronimo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080105','Cusco','Cusco','San Sebastian');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080106','Cusco','Cusco','Santiago');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080107','Cusco','Cusco','Saylla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080108','Cusco','Cusco','Wanchaq');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080201','Cusco','Acomayo','Acomayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080202','Cusco','Acomayo','Acopia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080203','Cusco','Acomayo','Acos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080204','Cusco','Acomayo','Mosoc Llacta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080205','Cusco','Acomayo','Pomacanchi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080206','Cusco','Acomayo','Rondocan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080207','Cusco','Acomayo','Sangarara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080301','Cusco','Anta','Anta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080302','Cusco','Anta','Ancahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080303','Cusco','Anta','Cachimayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080304','Cusco','Anta','Chinchaypujio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080305','Cusco','Anta','Huarocondo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080306','Cusco','Anta','Limatambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080307','Cusco','Anta','Mollepata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080308','Cusco','Anta','Pucyura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080309','Cusco','Anta','Zurite');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080401','Cusco','Calca','Calca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080402','Cusco','Calca','Coya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080403','Cusco','Calca','Lamay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080404','Cusco','Calca','Lares');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080405','Cusco','Calca','Pisac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080406','Cusco','Calca','San Salvador');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080407','Cusco','Calca','Taray');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080408','Cusco','Calca','Yanatile');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080501','Cusco','Canas','Yanaoca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080502','Cusco','Canas','Checca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080503','Cusco','Canas','Kunturkanki');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080504','Cusco','Canas','Langui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080505','Cusco','Canas','Layo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080506','Cusco','Canas','Pampamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080507','Cusco','Canas','Quehue');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080508','Cusco','Canas','Tupac Amaru');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080601','Cusco','Canchis','Sicuani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080602','Cusco','Canchis','Checacupe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080603','Cusco','Canchis','Combapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080604','Cusco','Canchis','Marangani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080605','Cusco','Canchis','Pitumarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080606','Cusco','Canchis','San Pablo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080607','Cusco','Canchis','San Pedro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080608','Cusco','Canchis','Tinta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080701','Cusco','Chumbivilcas','Santo Tomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080702','Cusco','Chumbivilcas','Capacmarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080703','Cusco','Chumbivilcas','Chamaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080704','Cusco','Chumbivilcas','Colquemarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080705','Cusco','Chumbivilcas','Livitaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080706','Cusco','Chumbivilcas','Llusco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080707','Cusco','Chumbivilcas','Quiñota');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080708','Cusco','Chumbivilcas','Velille');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080801','Cusco','Espinar','Espinar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080802','Cusco','Espinar','Condoroma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080803','Cusco','Espinar','Coporaque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080804','Cusco','Espinar','Ocoruro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080805','Cusco','Espinar','Pallpata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080806','Cusco','Espinar','Pichigua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080807','Cusco','Espinar','Suyckutambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080808','Cusco','Espinar','Alto Pichigua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080901','Cusco','La Convencion','Santa Ana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080902','Cusco','La Convencion','Echarate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080903','Cusco','La Convencion','Huayopata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080904','Cusco','La Convencion','Maranura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080905','Cusco','La Convencion','Ocobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080906','Cusco','La Convencion','Quellouno');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080907','Cusco','La Convencion','Kimbiri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080908','Cusco','La Convencion','Santa Teresa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080909','Cusco','La Convencion','Vilcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080910','Cusco','La Convencion','Pichari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080911','Cusco','La Convencion','Inkawasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080912','Cusco','La Convencion','Villa Virgen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080913','Cusco','La Convencion','Villa Kintiarina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('080914','Cusco','La Convencion','Megantoni');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081001','Cusco','Paruro','Paruro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081002','Cusco','Paruro','Accha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081003','Cusco','Paruro','Ccapi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081004','Cusco','Paruro','Colcha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081005','Cusco','Paruro','Huanoquite');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081006','Cusco','Paruro','Omacha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081007','Cusco','Paruro','Paccaritambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081008','Cusco','Paruro','Pillpinto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081009','Cusco','Paruro','Yaurisque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081101','Cusco','Paucartambo','Paucartambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081102','Cusco','Paucartambo','Caicay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081103','Cusco','Paucartambo','Challabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081104','Cusco','Paucartambo','Colquepata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081105','Cusco','Paucartambo','Huancarani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081106','Cusco','Paucartambo','Kosñipata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081201','Cusco','Quispicanchi','Urcos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081202','Cusco','Quispicanchi','Andahuaylillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081203','Cusco','Quispicanchi','Camanti');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081204','Cusco','Quispicanchi','Ccarhuayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081205','Cusco','Quispicanchi','Ccatca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081206','Cusco','Quispicanchi','Cusipata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081207','Cusco','Quispicanchi','Huaro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081208','Cusco','Quispicanchi','Lucre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081209','Cusco','Quispicanchi','Marcapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081210','Cusco','Quispicanchi','Ocongate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081211','Cusco','Quispicanchi','Oropesa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081212','Cusco','Quispicanchi','Quiquijana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081301','Cusco','Urubamba','Urubamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081302','Cusco','Urubamba','Chinchero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081303','Cusco','Urubamba','Huayllabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081304','Cusco','Urubamba','Machupicchu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081305','Cusco','Urubamba','Maras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081306','Cusco','Urubamba','Ollantaytambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('081307','Cusco','Urubamba','Yucay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090101','Huancavelica','Huancavelica','Huancavelica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090102','Huancavelica','Huancavelica','Acobambilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090103','Huancavelica','Huancavelica','Acoria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090104','Huancavelica','Huancavelica','Conayca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090105','Huancavelica','Huancavelica','Cuenca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090106','Huancavelica','Huancavelica','Huachocolpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090107','Huancavelica','Huancavelica','Huayllahuara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090108','Huancavelica','Huancavelica','Izcuchaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090109','Huancavelica','Huancavelica','Laria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090110','Huancavelica','Huancavelica','Manta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090111','Huancavelica','Huancavelica','Mariscal Caceres');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090112','Huancavelica','Huancavelica','Moya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090113','Huancavelica','Huancavelica','Nuevo Occoro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090114','Huancavelica','Huancavelica','Palca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090115','Huancavelica','Huancavelica','Pilchaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090116','Huancavelica','Huancavelica','Vilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090117','Huancavelica','Huancavelica','Yauli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090118','Huancavelica','Huancavelica','Ascension');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090119','Huancavelica','Huancavelica','Huando');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090201','Huancavelica','Acobamba','Acobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090202','Huancavelica','Acobamba','Andabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090203','Huancavelica','Acobamba','Anta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090204','Huancavelica','Acobamba','Caja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090205','Huancavelica','Acobamba','Marcas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090206','Huancavelica','Acobamba','Paucara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090207','Huancavelica','Acobamba','Pomacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090208','Huancavelica','Acobamba','Rosario');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090301','Huancavelica','Angaraes','Lircay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090302','Huancavelica','Angaraes','Anchonga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090303','Huancavelica','Angaraes','Callanmarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090304','Huancavelica','Angaraes','Ccochaccasa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090305','Huancavelica','Angaraes','Chincho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090306','Huancavelica','Angaraes','Congalla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090307','Huancavelica','Angaraes','Huanca-Huanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090308','Huancavelica','Angaraes','Huayllay Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090309','Huancavelica','Angaraes','Julcamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090310','Huancavelica','Angaraes','San Antonio de Antaparco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090311','Huancavelica','Angaraes','Santo Tomas de Pata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090312','Huancavelica','Angaraes','Secclla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090401','Huancavelica','Castrovirreyna','Castrovirreyna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090402','Huancavelica','Castrovirreyna','Arma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090403','Huancavelica','Castrovirreyna','Aurahua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090404','Huancavelica','Castrovirreyna','Capillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090405','Huancavelica','Castrovirreyna','Chupamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090406','Huancavelica','Castrovirreyna','Cocas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090407','Huancavelica','Castrovirreyna','Huachos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090408','Huancavelica','Castrovirreyna','Huamatambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090409','Huancavelica','Castrovirreyna','Mollepampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090410','Huancavelica','Castrovirreyna','San Juan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090411','Huancavelica','Castrovirreyna','Santa Ana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090412','Huancavelica','Castrovirreyna','Tantara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090413','Huancavelica','Castrovirreyna','Ticrapo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090501','Huancavelica','Churcampa','Churcampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090502','Huancavelica','Churcampa','Anco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090503','Huancavelica','Churcampa','Chinchihuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090504','Huancavelica','Churcampa','El Carmen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090505','Huancavelica','Churcampa','La Merced');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090506','Huancavelica','Churcampa','Locroja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090507','Huancavelica','Churcampa','Paucarbamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090508','Huancavelica','Churcampa','San Miguel de Mayocc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090509','Huancavelica','Churcampa','San Pedro de Coris');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090510','Huancavelica','Churcampa','Pachamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090511','Huancavelica','Churcampa','Cosme');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090601','Huancavelica','Huaytara','Huaytara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090602','Huancavelica','Huaytara','Ayavi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090603','Huancavelica','Huaytara','Cordova');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090604','Huancavelica','Huaytara','Huayacundo Arma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090605','Huancavelica','Huaytara','Laramarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090606','Huancavelica','Huaytara','Ocoyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090607','Huancavelica','Huaytara','Pilpichaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090608','Huancavelica','Huaytara','Querco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090609','Huancavelica','Huaytara','Quito-Arma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090610','Huancavelica','Huaytara','San Antonio de Cusicancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090611','Huancavelica','Huaytara','San Francisco de Sangayaico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090612','Huancavelica','Huaytara','San Isidro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090613','Huancavelica','Huaytara','Santiago de Chocorvos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090614','Huancavelica','Huaytara','Santiago de Quirahuara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090615','Huancavelica','Huaytara','Santo Domingo de Capillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090616','Huancavelica','Huaytara','Tambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090701','Huancavelica','Tayacaja','Pampas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090702','Huancavelica','Tayacaja','Acostambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090703','Huancavelica','Tayacaja','Acraquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090704','Huancavelica','Tayacaja','Ahuaycha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090705','Huancavelica','Tayacaja','Colcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090706','Huancavelica','Tayacaja','Daniel Hernandez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090707','Huancavelica','Tayacaja','Huachocolpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090709','Huancavelica','Tayacaja','Huaribamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090710','Huancavelica','Tayacaja','Ñahuimpuquio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090711','Huancavelica','Tayacaja','Pazos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090713','Huancavelica','Tayacaja','Quishuar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090714','Huancavelica','Tayacaja','Salcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090715','Huancavelica','Tayacaja','Salcahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090716','Huancavelica','Tayacaja','San Marcos de Rocchac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090717','Huancavelica','Tayacaja','Surcubamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090718','Huancavelica','Tayacaja','Tintay Puncu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090719','Huancavelica','Tayacaja','Quichuas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090720','Huancavelica','Tayacaja','Andaymarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090721','Huancavelica','Tayacaja','Roble');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090722','Huancavelica','Tayacaja','Pichos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('090723','Huancavelica','Tayacaja','Santiago de Túcuma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100101','Huanuco','Huanuco','Huanuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100102','Huanuco','Huanuco','Amarilis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100103','Huanuco','Huanuco','Chinchao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100104','Huanuco','Huanuco','Churubamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100105','Huanuco','Huanuco','Margos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100106','Huanuco','Huanuco','Quisqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100107','Huanuco','Huanuco','San Francisco de Cayran');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100108','Huanuco','Huanuco','San Pedro de Chaulan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100109','Huanuco','Huanuco','Santa Maria del Valle');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100110','Huanuco','Huanuco','Yarumayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100111','Huanuco','Huanuco','Pillco Marca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100112','Huanuco','Huanuco','Yacus');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100113','Huanuco','Huanuco','San Pablo de Pillao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100201','Huanuco','Ambo','Ambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100202','Huanuco','Ambo','Cayna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100203','Huanuco','Ambo','Colpas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100204','Huanuco','Ambo','Conchamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100205','Huanuco','Ambo','Huacar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100206','Huanuco','Ambo','San Francisco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100207','Huanuco','Ambo','San Rafael');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100208','Huanuco','Ambo','Tomay Kichwa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100301','Huanuco','Dos de Mayo','La Union');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100307','Huanuco','Dos de Mayo','Chuquis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100311','Huanuco','Dos de Mayo','Marias');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100313','Huanuco','Dos de Mayo','Pachas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100316','Huanuco','Dos de Mayo','Quivilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100317','Huanuco','Dos de Mayo','Ripan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100321','Huanuco','Dos de Mayo','Shunqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100322','Huanuco','Dos de Mayo','Sillapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100323','Huanuco','Dos de Mayo','Yanas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100401','Huanuco','Huacaybamba','Huacaybamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100402','Huanuco','Huacaybamba','Canchabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100403','Huanuco','Huacaybamba','Cochabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100404','Huanuco','Huacaybamba','Pinra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100501','Huanuco','Huamalies','Llata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100502','Huanuco','Huamalies','Arancay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100503','Huanuco','Huamalies','Chavin de Pariarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100504','Huanuco','Huamalies','Jacas Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100505','Huanuco','Huamalies','Jircan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100506','Huanuco','Huamalies','Miraflores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100507','Huanuco','Huamalies','Monzon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100508','Huanuco','Huamalies','Punchao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100509','Huanuco','Huamalies','Puños');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100510','Huanuco','Huamalies','Singa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100511','Huanuco','Huamalies','Tantamayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100601','Huanuco','Leoncio Prado','Rupa-Rupa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100602','Huanuco','Leoncio Prado','Daniel Alomias Robles');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100603','Huanuco','Leoncio Prado','Hermilio Valdizan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100604','Huanuco','Leoncio Prado','Jose Crespo y Castillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100605','Huanuco','Leoncio Prado','Luyando');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100606','Huanuco','Leoncio Prado','Mariano Damaso Beraun');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100607','Huanuco','Leoncio Prado','Pucayacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100608','Huanuco','Leoncio Prado','Castillo Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100609','Huanuco','Leoncio Prado','Pueblo Nuevo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100610','Huanuco','Leoncio Prado','Santo Domingo de Anda');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100701','Huanuco','Marañon','Huacrachuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100702','Huanuco','Marañon','Cholon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100703','Huanuco','Marañon','San Buenaventura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100704','Huanuco','Marañon','La Morada');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100705','Huanuco','Marañon','Santa Rosa de Alto Yanajanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100801','Huanuco','Pachitea','Panao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100802','Huanuco','Pachitea','Chaglla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100803','Huanuco','Pachitea','Molino');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100804','Huanuco','Pachitea','Umari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100901','Huanuco','Puerto Inca','Puerto Inca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100902','Huanuco','Puerto Inca','Codo del Pozuzo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100903','Huanuco','Puerto Inca','Honoria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100904','Huanuco','Puerto Inca','Tournavista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('100905','Huanuco','Puerto Inca','Yuyapichis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101001','Huanuco','Lauricocha','Jesus');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101002','Huanuco','Lauricocha','Baños');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101003','Huanuco','Lauricocha','Jivia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101004','Huanuco','Lauricocha','Queropalca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101005','Huanuco','Lauricocha','Rondos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101006','Huanuco','Lauricocha','San Francisco de Asis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101007','Huanuco','Lauricocha','San Miguel de Cauri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101101','Huanuco','Yarowilca','Chavinillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101102','Huanuco','Yarowilca','Cahuac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101103','Huanuco','Yarowilca','Chacabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101104','Huanuco','Yarowilca','Aparicio Pomares');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101105','Huanuco','Yarowilca','Jacas Chico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101106','Huanuco','Yarowilca','Obas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101107','Huanuco','Yarowilca','Pampamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('101108','Huanuco','Yarowilca','Choras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110101','Ica','Ica','Ica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110102','Ica','Ica','La Tinguiña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110103','Ica','Ica','Los Aquijes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110104','Ica','Ica','Ocucaje');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110105','Ica','Ica','Pachacutec');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110106','Ica','Ica','Parcona');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110107','Ica','Ica','Pueblo Nuevo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110108','Ica','Ica','Salas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110109','Ica','Ica','San Jose de los Molinos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110110','Ica','Ica','San Juan Bautista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110111','Ica','Ica','Santiago');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110112','Ica','Ica','Subtanjalla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110113','Ica','Ica','Tate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110114','Ica','Ica','Yauca del Rosario');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110201','Ica','Chincha','Chincha Alta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110202','Ica','Chincha','Alto Laran');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110203','Ica','Chincha','Chavin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110204','Ica','Chincha','Chincha Baja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110205','Ica','Chincha','El Carmen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110206','Ica','Chincha','Grocio Prado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110207','Ica','Chincha','Pueblo Nuevo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110208','Ica','Chincha','San Juan de Yanac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110209','Ica','Chincha','San Pedro de Huacarpana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110210','Ica','Chincha','Sunampe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110211','Ica','Chincha','Tambo de Mora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110301','Ica','Nazca','Nazca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110302','Ica','Nazca','Changuillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110303','Ica','Nazca','El Ingenio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110304','Ica','Nazca','Marcona');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110305','Ica','Nazca','Vista Alegre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110401','Ica','Palpa','Palpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110402','Ica','Palpa','Llipata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110403','Ica','Palpa','Rio Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110404','Ica','Palpa','Santa Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110405','Ica','Palpa','Tibillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110501','Ica','Pisco','Pisco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110502','Ica','Pisco','Huancano');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110503','Ica','Pisco','Humay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110504','Ica','Pisco','Independencia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110505','Ica','Pisco','Paracas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110506','Ica','Pisco','San Andres');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110507','Ica','Pisco','San Clemente');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('110508','Ica','Pisco','Tupac Amaru Inca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120101','Junin','Huancayo','Huancayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120104','Junin','Huancayo','Carhuacallanga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120105','Junin','Huancayo','Chacapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120106','Junin','Huancayo','Chicche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120107','Junin','Huancayo','Chilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120108','Junin','Huancayo','Chongos Alto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120111','Junin','Huancayo','Chupuro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120112','Junin','Huancayo','Colca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120113','Junin','Huancayo','Cullhuas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120114','Junin','Huancayo','El Tambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120116','Junin','Huancayo','Huacrapuquio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120117','Junin','Huancayo','Hualhuas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120119','Junin','Huancayo','Huancan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120120','Junin','Huancayo','Huasicancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120121','Junin','Huancayo','Huayucachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120122','Junin','Huancayo','Ingenio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120124','Junin','Huancayo','Pariahuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120125','Junin','Huancayo','Pilcomayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120126','Junin','Huancayo','Pucara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120127','Junin','Huancayo','Quichuay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120128','Junin','Huancayo','Quilcas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120129','Junin','Huancayo','San Agustin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120130','Junin','Huancayo','San Jeronimo de Tunan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120132','Junin','Huancayo','Saño');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120133','Junin','Huancayo','Sapallanga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120134','Junin','Huancayo','Sicaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120135','Junin','Huancayo','Santo Domingo de Acobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120136','Junin','Huancayo','Viques');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120201','Junin','Concepcion','Concepcion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120202','Junin','Concepcion','Aco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120203','Junin','Concepcion','Andamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120204','Junin','Concepcion','Chambara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120205','Junin','Concepcion','Cochas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120206','Junin','Concepcion','Comas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120207','Junin','Concepcion','Heroinas Toledo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120208','Junin','Concepcion','Manzanares');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120209','Junin','Concepcion','Mariscal Castilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120210','Junin','Concepcion','Matahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120211','Junin','Concepcion','Mito');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120212','Junin','Concepcion','Nueve de Julio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120213','Junin','Concepcion','Orcotuna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120214','Junin','Concepcion','San Jose de Quero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120215','Junin','Concepcion','Santa Rosa de Ocopa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120301','Junin','Chanchamayo','Chanchamayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120302','Junin','Chanchamayo','Perene');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120303','Junin','Chanchamayo','Pichanaqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120304','Junin','Chanchamayo','San Luis de Shuaro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120305','Junin','Chanchamayo','San Ramon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120306','Junin','Chanchamayo','Vitoc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120401','Junin','Jauja','Jauja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120402','Junin','Jauja','Acolla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120403','Junin','Jauja','Apata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120404','Junin','Jauja','Ataura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120405','Junin','Jauja','Canchayllo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120406','Junin','Jauja','Curicaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120407','Junin','Jauja','El Mantaro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120408','Junin','Jauja','Huamali');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120409','Junin','Jauja','Huaripampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120410','Junin','Jauja','Huertas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120411','Junin','Jauja','Janjaillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120412','Junin','Jauja','Julcan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120413','Junin','Jauja','Leonor Ordoñez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120414','Junin','Jauja','Llocllapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120415','Junin','Jauja','Marco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120416','Junin','Jauja','Masma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120417','Junin','Jauja','Masma Chicche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120418','Junin','Jauja','Molinos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120419','Junin','Jauja','Monobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120420','Junin','Jauja','Muqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120421','Junin','Jauja','Muquiyauyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120422','Junin','Jauja','Paca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120423','Junin','Jauja','Paccha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120424','Junin','Jauja','Pancan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120425','Junin','Jauja','Parco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120426','Junin','Jauja','Pomacancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120427','Junin','Jauja','Ricran');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120428','Junin','Jauja','San Lorenzo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120429','Junin','Jauja','San Pedro de Chunan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120430','Junin','Jauja','Sausa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120431','Junin','Jauja','Sincos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120432','Junin','Jauja','Tunan Marca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120433','Junin','Jauja','Yauli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120434','Junin','Jauja','Yauyos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120501','Junin','Junin','Junin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120502','Junin','Junin','Carhuamayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120503','Junin','Junin','Ondores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120504','Junin','Junin','Ulcumayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120601','Junin','Satipo','Satipo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120602','Junin','Satipo','Coviriali');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120603','Junin','Satipo','Llaylla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120604','Junin','Satipo','Mazamari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120605','Junin','Satipo','Pampa Hermosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120606','Junin','Satipo','Pangoa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120607','Junin','Satipo','Rio Negro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120608','Junin','Satipo','Rio Tambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120609','Junin','Satipo','Vizcatán del Ene');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120701','Junin','Tarma','Tarma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120702','Junin','Tarma','Acobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120703','Junin','Tarma','Huaricolca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120704','Junin','Tarma','Huasahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120705','Junin','Tarma','La Union');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120706','Junin','Tarma','Palca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120707','Junin','Tarma','Palcamayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120708','Junin','Tarma','San Pedro de Cajas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120709','Junin','Tarma','Tapo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120801','Junin','Yauli','La Oroya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120802','Junin','Yauli','Chacapalpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120803','Junin','Yauli','Huay-Huay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120804','Junin','Yauli','Marcapomacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120805','Junin','Yauli','Morococha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120806','Junin','Yauli','Paccha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120807','Junin','Yauli','Santa Barbara de Carhuacayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120808','Junin','Yauli','Santa Rosa de Sacco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120809','Junin','Yauli','Suitucancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120810','Junin','Yauli','Yauli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120901','Junin','Chupaca','Chupaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120902','Junin','Chupaca','Ahuac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120903','Junin','Chupaca','Chongos Bajo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120904','Junin','Chupaca','Huachac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120905','Junin','Chupaca','Huamancaca Chico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120906','Junin','Chupaca','San Juan de Yscos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120907','Junin','Chupaca','San Juan de Jarpa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120908','Junin','Chupaca','Tres de Diciembre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('120909','Junin','Chupaca','Yanacancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130101','La Libertad','Trujillo','Trujillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130102','La Libertad','Trujillo','El Porvenir');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130103','La Libertad','Trujillo','Florencia de Mora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130104','La Libertad','Trujillo','Huanchaco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130105','La Libertad','Trujillo','La Esperanza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130106','La Libertad','Trujillo','Laredo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130107','La Libertad','Trujillo','Moche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130108','La Libertad','Trujillo','Poroto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130109','La Libertad','Trujillo','Salaverry');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130110','La Libertad','Trujillo','Simbal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130111','La Libertad','Trujillo','Victor Larco Herrera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130201','La Libertad','Ascope','Ascope');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130202','La Libertad','Ascope','Chicama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130203','La Libertad','Ascope','Chocope');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130204','La Libertad','Ascope','Magdalena de Cao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130205','La Libertad','Ascope','Paijan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130206','La Libertad','Ascope','Razuri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130207','La Libertad','Ascope','Santiago de Cao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130208','La Libertad','Ascope','Casa Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130301','La Libertad','Bolivar','Bolivar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130302','La Libertad','Bolivar','Bambamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130303','La Libertad','Bolivar','Condormarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130304','La Libertad','Bolivar','Longotea');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130305','La Libertad','Bolivar','Uchumarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130306','La Libertad','Bolivar','Ucuncha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130401','La Libertad','Chepen','Chepen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130402','La Libertad','Chepen','Pacanga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130403','La Libertad','Chepen','Pueblo Nuevo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130501','La Libertad','Julcan','Julcan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130502','La Libertad','Julcan','Calamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130503','La Libertad','Julcan','Carabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130504','La Libertad','Julcan','Huaso');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130601','La Libertad','Otuzco','Otuzco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130602','La Libertad','Otuzco','Agallpampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130604','La Libertad','Otuzco','Charat');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130605','La Libertad','Otuzco','Huaranchal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130606','La Libertad','Otuzco','La Cuesta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130608','La Libertad','Otuzco','Mache');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130610','La Libertad','Otuzco','Paranday');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130611','La Libertad','Otuzco','Salpo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130613','La Libertad','Otuzco','Sinsicap');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130614','La Libertad','Otuzco','Usquil');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130701','La Libertad','Pacasmayo','San Pedro de Lloc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130702','La Libertad','Pacasmayo','Guadalupe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130703','La Libertad','Pacasmayo','Jequetepeque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130704','La Libertad','Pacasmayo','Pacasmayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130705','La Libertad','Pacasmayo','San Jose');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130801','La Libertad','Pataz','Tayabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130802','La Libertad','Pataz','Buldibuyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130803','La Libertad','Pataz','Chillia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130804','La Libertad','Pataz','Huancaspata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130805','La Libertad','Pataz','Huaylillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130806','La Libertad','Pataz','Huayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130807','La Libertad','Pataz','Ongon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130808','La Libertad','Pataz','Parcoy');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130809','La Libertad','Pataz','Pataz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130810','La Libertad','Pataz','Pias');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130811','La Libertad','Pataz','Santiago de Challas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130812','La Libertad','Pataz','Taurija');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130813','La Libertad','Pataz','Urpay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130901','La Libertad','Sanchez Carrion','Huamachuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130902','La Libertad','Sanchez Carrion','Chugay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130903','La Libertad','Sanchez Carrion','Cochorco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130904','La Libertad','Sanchez Carrion','Curgos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130905','La Libertad','Sanchez Carrion','Marcabal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130906','La Libertad','Sanchez Carrion','Sanagoran');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130907','La Libertad','Sanchez Carrion','Sarin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('130908','La Libertad','Sanchez Carrion','Sartimbamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131001','La Libertad','Santiago de Chuco','Santiago de Chuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131002','La Libertad','Santiago de Chuco','Angasmarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131003','La Libertad','Santiago de Chuco','Cachicadan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131004','La Libertad','Santiago de Chuco','Mollebamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131005','La Libertad','Santiago de Chuco','Mollepata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131006','La Libertad','Santiago de Chuco','Quiruvilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131007','La Libertad','Santiago de Chuco','Santa Cruz de Chuca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131008','La Libertad','Santiago de Chuco','Sitabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131101','La Libertad','Gran Chimu','Cascas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131102','La Libertad','Gran Chimu','Lucma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131103','La Libertad','Gran Chimu','Compin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131104','La Libertad','Gran Chimu','Sayapullo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131201','La Libertad','Viru','Viru');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131202','La Libertad','Viru','Chao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('131203','La Libertad','Viru','Guadalupito');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140101','Lambayeque','Chiclayo','Chiclayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140102','Lambayeque','Chiclayo','Chongoyape');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140103','Lambayeque','Chiclayo','Eten');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140104','Lambayeque','Chiclayo','Eten Puerto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140105','Lambayeque','Chiclayo','Jose Leonardo Ortiz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140106','Lambayeque','Chiclayo','La Victoria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140107','Lambayeque','Chiclayo','Lagunas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140108','Lambayeque','Chiclayo','Monsefu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140109','Lambayeque','Chiclayo','Nueva Arica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140110','Lambayeque','Chiclayo','Oyotun');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140111','Lambayeque','Chiclayo','Picsi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140112','Lambayeque','Chiclayo','Pimentel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140113','Lambayeque','Chiclayo','Reque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140114','Lambayeque','Chiclayo','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140115','Lambayeque','Chiclayo','Saña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140116','Lambayeque','Chiclayo','Cayalti');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140117','Lambayeque','Chiclayo','Patapo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140118','Lambayeque','Chiclayo','Pomalca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140119','Lambayeque','Chiclayo','Pucala');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140120','Lambayeque','Chiclayo','Tuman');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140201','Lambayeque','Ferreñafe','Ferreñafe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140202','Lambayeque','Ferreñafe','Cañaris');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140203','Lambayeque','Ferreñafe','Incahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140204','Lambayeque','Ferreñafe','Manuel Antonio Mesones Muro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140205','Lambayeque','Ferreñafe','Pitipo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140206','Lambayeque','Ferreñafe','Pueblo Nuevo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140301','Lambayeque','Lambayeque','Lambayeque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140302','Lambayeque','Lambayeque','Chochope');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140303','Lambayeque','Lambayeque','Illimo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140304','Lambayeque','Lambayeque','Jayanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140305','Lambayeque','Lambayeque','Mochumi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140306','Lambayeque','Lambayeque','Morrope');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140307','Lambayeque','Lambayeque','Motupe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140308','Lambayeque','Lambayeque','Olmos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140309','Lambayeque','Lambayeque','Pacora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140310','Lambayeque','Lambayeque','Salas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140311','Lambayeque','Lambayeque','San Jose');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('140312','Lambayeque','Lambayeque','Tucume');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150101','Lima','Lima','Lima');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150102','Lima','Lima','Ancon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150103','Lima','Lima','Ate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150104','Lima','Lima','Barranco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150105','Lima','Lima','Breña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150106','Lima','Lima','Carabayllo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150107','Lima','Lima','Chaclacayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150108','Lima','Lima','Chorrillos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150109','Lima','Lima','Cieneguilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150110','Lima','Lima','Comas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150111','Lima','Lima','El Agustino');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150112','Lima','Lima','Independencia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150113','Lima','Lima','Jesus Maria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150114','Lima','Lima','La Molina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150115','Lima','Lima','La Victoria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150116','Lima','Lima','Lince');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150117','Lima','Lima','Los Olivos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150118','Lima','Lima','Lurigancho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150119','Lima','Lima','Lurin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150120','Lima','Lima','Magdalena del Mar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150121','Lima','Lima','Pueblo Libre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150122','Lima','Lima','Miraflores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150123','Lima','Lima','Pachacamac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150124','Lima','Lima','Pucusana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150125','Lima','Lima','Puente Piedra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150126','Lima','Lima','Punta Hermosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150127','Lima','Lima','Punta Negra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150128','Lima','Lima','Rimac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150129','Lima','Lima','San Bartolo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150130','Lima','Lima','San Borja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150131','Lima','Lima','San Isidro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150132','Lima','Lima','San Juan de Lurigancho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150133','Lima','Lima','San Juan de Miraflores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150134','Lima','Lima','San Luis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150135','Lima','Lima','San Martin de Porres');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150136','Lima','Lima','San Miguel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150137','Lima','Lima','Santa Anita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150138','Lima','Lima','Santa Maria del Mar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150139','Lima','Lima','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150140','Lima','Lima','Santiago de Surco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150141','Lima','Lima','Surquillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150142','Lima','Lima','Villa El Salvador');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150143','Lima','Lima','Villa Maria del Triunfo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150201','Lima','Barranca','Barranca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150202','Lima','Barranca','Paramonga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150203','Lima','Barranca','Pativilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150204','Lima','Barranca','Supe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150205','Lima','Barranca','Supe Puerto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150301','Lima','Cajatambo','Cajatambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150302','Lima','Cajatambo','Copa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150303','Lima','Cajatambo','Gorgor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150304','Lima','Cajatambo','Huancapon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150305','Lima','Cajatambo','Manas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150401','Lima','Canta','Canta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150402','Lima','Canta','Arahuay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150403','Lima','Canta','Huamantanga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150404','Lima','Canta','Huaros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150405','Lima','Canta','Lachaqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150406','Lima','Canta','San Buenaventura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150407','Lima','Canta','Santa Rosa de Quives');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150501','Lima','Cañete','San Vicente de Cañete');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150502','Lima','Cañete','Asia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150503','Lima','Cañete','Calango');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150504','Lima','Cañete','Cerro Azul');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150505','Lima','Cañete','Chilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150506','Lima','Cañete','Coayllo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150507','Lima','Cañete','Imperial');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150508','Lima','Cañete','Lunahuana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150509','Lima','Cañete','Mala');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150510','Lima','Cañete','Nuevo Imperial');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150511','Lima','Cañete','Pacaran');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150512','Lima','Cañete','Quilmana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150513','Lima','Cañete','San Antonio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150514','Lima','Cañete','San Luis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150515','Lima','Cañete','Santa Cruz de Flores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150516','Lima','Cañete','Zuñiga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150601','Lima','Huaral','Huaral');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150602','Lima','Huaral','Atavillos Alto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150603','Lima','Huaral','Atavillos Bajo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150604','Lima','Huaral','Aucallama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150605','Lima','Huaral','Chancay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150606','Lima','Huaral','Ihuari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150607','Lima','Huaral','Lampian');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150608','Lima','Huaral','Pacaraos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150609','Lima','Huaral','San Miguel de Acos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150610','Lima','Huaral','Santa Cruz de Andamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150611','Lima','Huaral','Sumbilca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150612','Lima','Huaral','Veintisiete de Noviembre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150701','Lima','Huarochiri','Matucana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150702','Lima','Huarochiri','Antioquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150703','Lima','Huarochiri','Callahuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150704','Lima','Huarochiri','Carampoma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150705','Lima','Huarochiri','Chicla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150706','Lima','Huarochiri','Cuenca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150707','Lima','Huarochiri','Huachupampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150708','Lima','Huarochiri','Huanza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150709','Lima','Huarochiri','Huarochiri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150710','Lima','Huarochiri','Lahuaytambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150711','Lima','Huarochiri','Langa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150712','Lima','Huarochiri','Laraos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150713','Lima','Huarochiri','Mariatana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150714','Lima','Huarochiri','Ricardo Palma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150715','Lima','Huarochiri','San Andres de Tupicocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150716','Lima','Huarochiri','San Antonio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150717','Lima','Huarochiri','San Bartolome');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150718','Lima','Huarochiri','San Damian');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150719','Lima','Huarochiri','San Juan de Iris');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150720','Lima','Huarochiri','San Juan de Tantaranche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150721','Lima','Huarochiri','San Lorenzo de Quinti');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150722','Lima','Huarochiri','San Mateo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150723','Lima','Huarochiri','San Mateo de Otao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150724','Lima','Huarochiri','San Pedro de Casta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150725','Lima','Huarochiri','San Pedro de Huancayre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150726','Lima','Huarochiri','Sangallaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150727','Lima','Huarochiri','Santa Cruz de Cocachacra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150728','Lima','Huarochiri','Santa Eulalia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150729','Lima','Huarochiri','Santiago de Anchucaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150730','Lima','Huarochiri','Santiago de Tuna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150731','Lima','Huarochiri','Santo Domingo de los Olleros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150732','Lima','Huarochiri','Surco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150801','Lima','Huaura','Huacho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150802','Lima','Huaura','Ambar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150803','Lima','Huaura','Caleta de Carquin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150804','Lima','Huaura','Checras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150805','Lima','Huaura','Hualmay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150806','Lima','Huaura','Huaura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150807','Lima','Huaura','Leoncio Prado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150808','Lima','Huaura','Paccho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150809','Lima','Huaura','Santa Leonor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150810','Lima','Huaura','Santa Maria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150811','Lima','Huaura','Sayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150812','Lima','Huaura','Vegueta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150901','Lima','Oyon','Oyon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150902','Lima','Oyon','Andajes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150903','Lima','Oyon','Caujul');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150904','Lima','Oyon','Cochamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150905','Lima','Oyon','Navan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('150906','Lima','Oyon','Pachangara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151001','Lima','Yauyos','Yauyos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151002','Lima','Yauyos','Alis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151003','Lima','Yauyos','Ayauca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151004','Lima','Yauyos','Ayaviri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151005','Lima','Yauyos','Azangaro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151006','Lima','Yauyos','Cacra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151007','Lima','Yauyos','Carania');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151008','Lima','Yauyos','Catahuasi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151009','Lima','Yauyos','Chocos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151010','Lima','Yauyos','Cochas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151011','Lima','Yauyos','Colonia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151012','Lima','Yauyos','Hongos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151013','Lima','Yauyos','Huampara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151014','Lima','Yauyos','Huancaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151015','Lima','Yauyos','Huangascar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151016','Lima','Yauyos','Huantan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151017','Lima','Yauyos','Huañec');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151018','Lima','Yauyos','Laraos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151019','Lima','Yauyos','Lincha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151020','Lima','Yauyos','Madean');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151021','Lima','Yauyos','Miraflores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151022','Lima','Yauyos','Omas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151023','Lima','Yauyos','Putinza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151024','Lima','Yauyos','Quinches');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151025','Lima','Yauyos','Quinocay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151026','Lima','Yauyos','San Joaquin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151027','Lima','Yauyos','San Pedro de Pilas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151028','Lima','Yauyos','Tanta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151029','Lima','Yauyos','Tauripampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151030','Lima','Yauyos','Tomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151031','Lima','Yauyos','Tupe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151032','Lima','Yauyos','Viñac');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('151033','Lima','Yauyos','Vitis');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160101','Loreto','Maynas','Iquitos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160102','Loreto','Maynas','Alto Nanay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160103','Loreto','Maynas','Fernando Lores');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160104','Loreto','Maynas','Indiana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160105','Loreto','Maynas','Las Amazonas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160106','Loreto','Maynas','Mazan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160107','Loreto','Maynas','Napo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160108','Loreto','Maynas','Punchana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160110','Loreto','Maynas','Torres Causana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160112','Loreto','Maynas','Belen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160113','Loreto','Maynas','San Juan Bautista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160201','Loreto','Alto Amazonas','Yurimaguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160202','Loreto','Alto Amazonas','Balsapuerto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160205','Loreto','Alto Amazonas','Jeberos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160206','Loreto','Alto Amazonas','Lagunas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160210','Loreto','Alto Amazonas','Santa Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160211','Loreto','Alto Amazonas','Teniente Cesar Lopez Rojas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160301','Loreto','Loreto','Nauta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160302','Loreto','Loreto','Parinari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160303','Loreto','Loreto','Tigre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160304','Loreto','Loreto','Trompeteros');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160305','Loreto','Loreto','Urarinas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160401','Loreto','Mariscal Ramon Castilla','Ramon Castilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160402','Loreto','Mariscal Ramon Castilla','Pebas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160403','Loreto','Mariscal Ramon Castilla','Yavari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160404','Loreto','Mariscal Ramon Castilla','San Pablo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160501','Loreto','Requena','Requena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160502','Loreto','Requena','Alto Tapiche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160503','Loreto','Requena','Capelo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160504','Loreto','Requena','Emilio San Martin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160505','Loreto','Requena','Maquia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160506','Loreto','Requena','Puinahua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160507','Loreto','Requena','Saquena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160508','Loreto','Requena','Soplin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160509','Loreto','Requena','Tapiche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160510','Loreto','Requena','Jenaro Herrera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160511','Loreto','Requena','Yaquerana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160601','Loreto','Ucayali','Contamana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160602','Loreto','Ucayali','Inahuaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160603','Loreto','Ucayali','Padre Marquez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160604','Loreto','Ucayali','Pampa Hermosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160605','Loreto','Ucayali','Sarayacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160606','Loreto','Ucayali','Vargas Guerra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160701','Loreto','Datem del Marañon','Barranca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160702','Loreto','Datem del Marañon','Cahuapanas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160703','Loreto','Datem del Marañon','Manseriche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160704','Loreto','Datem del Marañon','Morona');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160705','Loreto','Datem del Marañon','Pastaza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160706','Loreto','Datem del Marañon','Andoas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160801','Loreto','Maynas','Putumayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160802','Loreto','Maynas','Rosa Panduro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160803','Loreto','Maynas','Teniente Manuel Clavero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('160804','Loreto','Maynas','Yaguas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170101','Madre de Dios','Tambopata','Tambopata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170102','Madre de Dios','Tambopata','Inambari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170103','Madre de Dios','Tambopata','Las Piedras');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170104','Madre de Dios','Tambopata','Laberinto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170201','Madre de Dios','Manu','Manu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170202','Madre de Dios','Manu','Fitzcarrald');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170203','Madre de Dios','Manu','Madre de Dios');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170204','Madre de Dios','Manu','Huepetuhe');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170301','Madre de Dios','Tahuamanu','Iñapari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170302','Madre de Dios','Tahuamanu','Iberia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('170303','Madre de Dios','Tahuamanu','Tahuamanu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180101','Moquegua','Mariscal Nieto','Moquegua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180102','Moquegua','Mariscal Nieto','Carumas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180103','Moquegua','Mariscal Nieto','Cuchumbaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180104','Moquegua','Mariscal Nieto','Samegua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180105','Moquegua','Mariscal Nieto','San Cristobal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180106','Moquegua','Mariscal Nieto','Torata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180201','Moquegua','General Sanchez Cerr','Omate');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180202','Moquegua','General Sanchez Cerr','Chojata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180203','Moquegua','General Sanchez Cerr','Coalaque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180204','Moquegua','General Sanchez Cerr','Ichuña');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180205','Moquegua','General Sanchez Cerr','La Capilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180206','Moquegua','General Sanchez Cerr','Lloque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180207','Moquegua','General Sanchez Cerr','Matalaque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180208','Moquegua','General Sanchez Cerr','Puquina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180209','Moquegua','General Sanchez Cerr','Quinistaquillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180210','Moquegua','General Sanchez Cerr','Ubinas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180211','Moquegua','General Sanchez Cerr','Yunga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180301','Moquegua','Ilo','Ilo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180302','Moquegua','Ilo','El Algarrobal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('180303','Moquegua','Ilo','Pacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190101','Pasco','Pasco','Chaupimarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190102','Pasco','Pasco','Huachon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190103','Pasco','Pasco','Huariaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190104','Pasco','Pasco','Huayllay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190105','Pasco','Pasco','Ninacaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190106','Pasco','Pasco','Pallanchacra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190107','Pasco','Pasco','Paucartambo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190108','Pasco','Pasco','San Francisco de Asis de Yarusyacan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190109','Pasco','Pasco','Simon Bolivar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190110','Pasco','Pasco','Ticlacayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190111','Pasco','Pasco','Tinyahuarco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190112','Pasco','Pasco','Vicco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190113','Pasco','Pasco','Yanacancha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190201','Pasco','Daniel Alcides Carri','Yanahuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190202','Pasco','Daniel Alcides Carri','Chacayan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190203','Pasco','Daniel Alcides Carri','Goyllarisquizga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190204','Pasco','Daniel Alcides Carri','Paucar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190205','Pasco','Daniel Alcides Carri','San Pedro de Pillao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190206','Pasco','Daniel Alcides Carri','Santa Ana de Tusi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190207','Pasco','Daniel Alcides Carri','Tapuc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190208','Pasco','Daniel Alcides Carri','Vilcabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190301','Pasco','Oxapampa','Oxapampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190302','Pasco','Oxapampa','Chontabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190303','Pasco','Oxapampa','Huancabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190304','Pasco','Oxapampa','Palcazu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190305','Pasco','Oxapampa','Pozuzo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190306','Pasco','Oxapampa','Puerto Bermudez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190307','Pasco','Oxapampa','Villa Rica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('190308','Pasco','Oxapampa','Constitución');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200101','Piura','Piura','Piura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200104','Piura','Piura','Castilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200105','Piura','Piura','Catacaos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200107','Piura','Piura','Cura Mori');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200108','Piura','Piura','El Tallan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200109','Piura','Piura','La Arena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200110','Piura','Piura','La Union');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200111','Piura','Piura','Las Lomas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200114','Piura','Piura','Tambo Grande');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200115','Piura','Piura','26 de Octubre');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200201','Piura','Ayabaca','Ayabaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200202','Piura','Ayabaca','Frias');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200203','Piura','Ayabaca','Jilili');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200204','Piura','Ayabaca','Lagunas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200205','Piura','Ayabaca','Montero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200206','Piura','Ayabaca','Pacaipampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200207','Piura','Ayabaca','Paimas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200208','Piura','Ayabaca','Sapillica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200209','Piura','Ayabaca','Sicchez');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200210','Piura','Ayabaca','Suyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200301','Piura','Huancabamba','Huancabamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200302','Piura','Huancabamba','Canchaque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200303','Piura','Huancabamba','El Carmen de La Frontera');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200304','Piura','Huancabamba','Huarmaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200305','Piura','Huancabamba','Lalaquiz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200306','Piura','Huancabamba','San Miguel de El Faique');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200307','Piura','Huancabamba','Sondor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200308','Piura','Huancabamba','Sondorillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200401','Piura','Morropon','Chulucanas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200402','Piura','Morropon','Buenos Aires');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200403','Piura','Morropon','Chalaco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200404','Piura','Morropon','La Matanza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200405','Piura','Morropon','Morropon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200406','Piura','Morropon','Salitral');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200407','Piura','Morropon','San Juan de Bigote');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200408','Piura','Morropon','Santa Catalina de Mossa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200409','Piura','Morropon','Santo Domingo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200410','Piura','Morropon','Yamango');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200501','Piura','Paita','Paita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200502','Piura','Paita','Amotape');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200503','Piura','Paita','Arenal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200504','Piura','Paita','Colan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200505','Piura','Paita','La Huaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200506','Piura','Paita','Tamarindo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200507','Piura','Paita','Vichayal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200601','Piura','Sullana','Sullana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200602','Piura','Sullana','Bellavista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200603','Piura','Sullana','Ignacio Escudero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200604','Piura','Sullana','Lancones');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200605','Piura','Sullana','Marcavelica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200606','Piura','Sullana','Miguel Checa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200607','Piura','Sullana','Querecotillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200608','Piura','Sullana','Salitral');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200701','Piura','Talara','Pariñas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200702','Piura','Talara','El Alto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200703','Piura','Talara','La Brea');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200704','Piura','Talara','Lobitos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200705','Piura','Talara','Los Organos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200706','Piura','Talara','Mancora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200801','Piura','Sechura','Sechura');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200802','Piura','Sechura','Bellavista de La Union');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200803','Piura','Sechura','Bernal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200804','Piura','Sechura','Cristo Nos Valga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200805','Piura','Sechura','Vice');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('200806','Piura','Sechura','Rinconada Llicuar');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210101','Puno','Puno','Puno');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210102','Puno','Puno','Acora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210103','Puno','Puno','Amantani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210104','Puno','Puno','Atuncolla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210105','Puno','Puno','Capachica');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210106','Puno','Puno','Chucuito');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210107','Puno','Puno','Coata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210108','Puno','Puno','Huata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210109','Puno','Puno','Mañazo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210110','Puno','Puno','Paucarcolla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210111','Puno','Puno','Pichacani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210112','Puno','Puno','Plateria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210113','Puno','Puno','San Antonio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210114','Puno','Puno','Tiquillaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210115','Puno','Puno','Vilque');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210201','Puno','Azangaro','Azangaro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210202','Puno','Azangaro','Achaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210203','Puno','Azangaro','Arapa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210204','Puno','Azangaro','Asillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210205','Puno','Azangaro','Caminaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210206','Puno','Azangaro','Chupa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210207','Puno','Azangaro','Jose Domingo Choquehuanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210208','Puno','Azangaro','Muñani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210209','Puno','Azangaro','Potoni');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210210','Puno','Azangaro','Saman');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210211','Puno','Azangaro','San Anton');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210212','Puno','Azangaro','San Jose');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210213','Puno','Azangaro','San Juan de Salinas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210214','Puno','Azangaro','Santiago de Pupuja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210215','Puno','Azangaro','Tirapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210301','Puno','Carabaya','Macusani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210302','Puno','Carabaya','Ajoyani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210303','Puno','Carabaya','Ayapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210304','Puno','Carabaya','Coasa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210305','Puno','Carabaya','Corani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210306','Puno','Carabaya','Crucero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210307','Puno','Carabaya','Ituata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210308','Puno','Carabaya','Ollachea');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210309','Puno','Carabaya','San Gaban');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210310','Puno','Carabaya','Usicayos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210401','Puno','Chucuito','Juli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210402','Puno','Chucuito','Desaguadero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210403','Puno','Chucuito','Huacullani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210404','Puno','Chucuito','Kelluyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210405','Puno','Chucuito','Pisacoma');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210406','Puno','Chucuito','Pomata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210407','Puno','Chucuito','Zepita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210501','Puno','El Collao','Ilave');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210502','Puno','El Collao','Capazo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210503','Puno','El Collao','Pilcuyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210504','Puno','El Collao','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210505','Puno','El Collao','Conduriri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210601','Puno','Huancane','Huancane');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210602','Puno','Huancane','Cojata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210603','Puno','Huancane','Huatasani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210604','Puno','Huancane','Inchupalla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210605','Puno','Huancane','Pusi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210606','Puno','Huancane','Rosaspata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210607','Puno','Huancane','Taraco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210608','Puno','Huancane','Vilque Chico');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210701','Puno','Lampa','Lampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210702','Puno','Lampa','Cabanilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210703','Puno','Lampa','Calapuja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210704','Puno','Lampa','Nicasio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210705','Puno','Lampa','Ocuviri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210706','Puno','Lampa','Palca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210707','Puno','Lampa','Paratia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210708','Puno','Lampa','Pucara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210709','Puno','Lampa','Santa Lucia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210710','Puno','Lampa','Vilavila');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210801','Puno','Melgar','Ayaviri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210802','Puno','Melgar','Antauta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210803','Puno','Melgar','Cupi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210804','Puno','Melgar','Llalli');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210805','Puno','Melgar','Macari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210806','Puno','Melgar','Nuñoa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210807','Puno','Melgar','Orurillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210808','Puno','Melgar','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210809','Puno','Melgar','Umachiri');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210901','Puno','Moho','Moho');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210902','Puno','Moho','Conima');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210903','Puno','Moho','Huayrapata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('210904','Puno','Moho','Tilali');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211001','Puno','San Antonio de Putin','Putina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211002','Puno','San Antonio de Putin','Ananea');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211003','Puno','San Antonio de Putin','Pedro Vilca Apaza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211004','Puno','San Antonio de Putin','Quilcapuncu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211005','Puno','San Antonio de Putin','Sina');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211101','Puno','San Roman','Juliaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211102','Puno','San Roman','Cabana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211103','Puno','San Roman','Cabanillas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211104','Puno','San Roman','Caracoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211105','Puno','San Roman','San Miguel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211201','Puno','Sandia','Sandia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211202','Puno','Sandia','Cuyocuyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211203','Puno','Sandia','Limbani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211204','Puno','Sandia','Patambuco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211205','Puno','Sandia','Phara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211206','Puno','Sandia','Quiaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211207','Puno','Sandia','San Juan del Oro');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211208','Puno','Sandia','Yanahuaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211209','Puno','Sandia','Alto Inambari');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211210','Puno','Sandia','San Pedro de Putina Punco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211301','Puno','Yunguyo','Yunguyo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211302','Puno','Yunguyo','Anapia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211303','Puno','Yunguyo','Copani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211304','Puno','Yunguyo','Cuturapi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211305','Puno','Yunguyo','Ollaraya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211306','Puno','Yunguyo','Tinicachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('211307','Puno','Yunguyo','Unicachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220101','San Martin','Moyobamba','Moyobamba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220102','San Martin','Moyobamba','Calzada');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220103','San Martin','Moyobamba','Habana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220104','San Martin','Moyobamba','Jepelacio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220105','San Martin','Moyobamba','Soritor');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220106','San Martin','Moyobamba','Yantalo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220201','San Martin','Bellavista','Bellavista');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220202','San Martin','Bellavista','Alto Biavo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220203','San Martin','Bellavista','Bajo Biavo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220204','San Martin','Bellavista','Huallaga');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220205','San Martin','Bellavista','San Pablo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220206','San Martin','Bellavista','San Rafael');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220301','San Martin','El Dorado','San Jose de Sisa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220302','San Martin','El Dorado','Agua Blanca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220303','San Martin','El Dorado','San Martin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220304','San Martin','El Dorado','Santa Rosa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220305','San Martin','El Dorado','Shatoja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220401','San Martin','Huallaga','Saposoa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220402','San Martin','Huallaga','Alto Saposoa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220403','San Martin','Huallaga','El Eslabon');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220404','San Martin','Huallaga','Piscoyacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220405','San Martin','Huallaga','Sacanche');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220406','San Martin','Huallaga','Tingo de Saposoa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220501','San Martin','Lamas','Lamas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220502','San Martin','Lamas','Alonso de Alvarado');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220503','San Martin','Lamas','Barranquita');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220504','San Martin','Lamas','Caynarachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220505','San Martin','Lamas','Cuñumbuqui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220506','San Martin','Lamas','Pinto Recodo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220507','San Martin','Lamas','Rumisapa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220508','San Martin','Lamas','San Roque de Cumbaza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220509','San Martin','Lamas','Shanao');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220510','San Martin','Lamas','Tabalosos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220511','San Martin','Lamas','Zapatero');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220601','San Martin','Mariscal Caceres','Juanjui');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220602','San Martin','Mariscal Caceres','Campanilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220603','San Martin','Mariscal Caceres','Huicungo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220604','San Martin','Mariscal Caceres','Pachiza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220605','San Martin','Mariscal Caceres','Pajarillo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220701','San Martin','Picota','Picota');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220702','San Martin','Picota','Buenos Aires');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220703','San Martin','Picota','Caspisapa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220704','San Martin','Picota','Pilluana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220705','San Martin','Picota','Pucacaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220706','San Martin','Picota','San Cristobal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220707','San Martin','Picota','San Hilarion');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220708','San Martin','Picota','Shamboyacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220709','San Martin','Picota','Tingo de Ponasa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220710','San Martin','Picota','Tres Unidos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220801','San Martin','Rioja','Rioja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220802','San Martin','Rioja','Awajun');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220803','San Martin','Rioja','Elias Soplin Vargas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220804','San Martin','Rioja','Nueva Cajamarca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220805','San Martin','Rioja','Pardo Miguel');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220806','San Martin','Rioja','Posic');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220807','San Martin','Rioja','San Fernando');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220808','San Martin','Rioja','Yorongos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220809','San Martin','Rioja','Yuracyacu');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220901','San Martin','San Martin','Tarapoto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220902','San Martin','San Martin','Alberto Leveau');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220903','San Martin','San Martin','Cacatachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220904','San Martin','San Martin','Chazuta');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220905','San Martin','San Martin','Chipurana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220906','San Martin','San Martin','El Porvenir');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220907','San Martin','San Martin','Huimbayoc');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220908','San Martin','San Martin','Juan Guerra');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220909','San Martin','San Martin','La Banda de Shilcayo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220910','San Martin','San Martin','Morales');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220911','San Martin','San Martin','Papaplaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220912','San Martin','San Martin','San Antonio');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220913','San Martin','San Martin','Sauce');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('220914','San Martin','San Martin','Shapaja');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('221001','San Martin','Tocache','Tocache');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('221002','San Martin','Tocache','Nuevo Progreso');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('221003','San Martin','Tocache','Polvora');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('221004','San Martin','Tocache','Shunte');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('221005','San Martin','Tocache','Uchiza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230101','Tacna','Tacna','Tacna');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230102','Tacna','Tacna','Alto de La Alianza');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230103','Tacna','Tacna','Calana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230104','Tacna','Tacna','Ciudad Nueva');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230105','Tacna','Tacna','Inclan');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230106','Tacna','Tacna','Pachia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230107','Tacna','Tacna','Palca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230108','Tacna','Tacna','Pocollay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230109','Tacna','Tacna','Sama');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230110','Tacna','Tacna','Coronel Gregorio Albarracin Lanchipa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230111','Tacna','Tacna','La Yarada-Los Palos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230201','Tacna','Candarave','Candarave');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230202','Tacna','Candarave','Cairani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230203','Tacna','Candarave','Camilaca');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230204','Tacna','Candarave','Curibaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230205','Tacna','Candarave','Huanuara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230206','Tacna','Candarave','Quilahuani');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230301','Tacna','Jorge Basadre','Locumba');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230302','Tacna','Jorge Basadre','Ilabaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230303','Tacna','Jorge Basadre','Ite');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230401','Tacna','Tarata','Tarata');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230402','Tacna','Tarata','Heroes Albarracin');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230403','Tacna','Tarata','Estique');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230404','Tacna','Tarata','Estique-Pampa');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230405','Tacna','Tarata','Sitajara');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230406','Tacna','Tarata','Susapaya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230407','Tacna','Tarata','Tarucachi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('230408','Tacna','Tarata','Ticaco');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240101','Tumbes','Tumbes','Tumbes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240102','Tumbes','Tumbes','Corrales');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240103','Tumbes','Tumbes','La Cruz');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240104','Tumbes','Tumbes','Pampas de Hospital');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240105','Tumbes','Tumbes','San Jacinto');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240106','Tumbes','Tumbes','San Juan de La Virgen');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240201','Tumbes','Contralmirante Villa','Zorritos');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240202','Tumbes','Contralmirante Villa','Casitas');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240203','Tumbes','Contralmirante Villa','Canoas de Punta Sal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240301','Tumbes','Zarumilla','Zarumilla');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240302','Tumbes','Zarumilla','Aguas Verdes');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240303','Tumbes','Zarumilla','Matapalo');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('240304','Tumbes','Zarumilla','Papayal');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250101','Ucayali','Coronel Portillo','Calleria');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250102','Ucayali','Coronel Portillo','Campoverde');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250103','Ucayali','Coronel Portillo','Iparia');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250104','Ucayali','Coronel Portillo','Masisea');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250105','Ucayali','Coronel Portillo','Yarinacocha');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250106','Ucayali','Coronel Portillo','Nueva Requena');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250107','Ucayali','Coronel Portillo','Manantay');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250201','Ucayali','Atalaya','Raymondi');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250202','Ucayali','Atalaya','Sepahua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250203','Ucayali','Atalaya','Tahuania');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250204','Ucayali','Atalaya','Yurua');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250301','Ucayali','Padre Abad','Padre Abad');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250302','Ucayali','Padre Abad','Irazola');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250303','Ucayali','Padre Abad','Curimana');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250304','Ucayali','Padre Abad','Neshuya');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250305','Ucayali','Padre Abad','Alexander von Humboldt');
insert into ubigeo (ubigeo, departamento, provincia, distrito) values ('250401','Ucayali','Purus','Purus');

INSERT INTO tipo_vehiculo (nombre,capacidad, estado) 
VALUES ('MetroRapid X12', 120, 1);  -- Bus articulado eléctrico

-- Vehículos especializados
INSERT INTO tipo_vehiculo (nombre, capacidad, estado) 
VALUES ('CargoMaster Pro',  40, 1);  -- Camión de carga mediana

INSERT INTO tipo_vehiculo (nombre, capacidad, estado) 
VALUES ('EcoGlider Prime', 54, 1);

-- Tabla Tipo Usuario
INSERT INTO tipo_usuario (id,nombre, estado, estado_proceso,estado_registro,fecha_registro, usuario) VALUES (1,'ADMINISTRADOR', 1, 'REGISTRADO',1,'2025-03-06 20:02:56','SYSTEM');

-- Tabla Usuario
INSERT INTO usuarios (id, nombre, email, password, imagen, estado, id_tipousuario,estado_proceso,estado_registro,fecha_registro,usuario) VALUES (1,'Alexis','alexis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', '/Static/img/trabajadores/alexis.jpeg', 1, 1,'MODIFICADO',1,'2025-03-06 20:06:14','SYSTEM');

-- Tabla menus
INSERT INTO conf_menus (id, nombre, estado) VALUES (1, 'M_USUARIOS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (2, 'M_CONFIGURACION', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (3, 'M_VENTAS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (4, 'M_VIAJES', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (5, 'M_PERSONAL', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (6, 'M_ATENCION', 1);
-- Submenús de USUARIOS
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (10, 'Gestionar usuarios', 1, 1);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (11, 'Gestionar tipos de usuarios', 1, 1);
-- Submenús de CONFIGURACIÓN
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (20, 'Gestionar permisos', 1, 2);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (21, 'Gestionar plantillas', 1, 2);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (22, 'Gestionar métodos de pago', 1, 2);
-- Submenús de VENTAS
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (30, 'Gestionar tipo comprobante', 1, 3);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (31, 'Gestionar tipo cliente', 1, 3);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (32, 'Gestionar tipo servicio', 1, 3);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (33, 'Gestionar tipo documento', 1, 3);
-- Submenús de VIAJES
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (40, 'Gestionar horarios', 1, 4);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (41, 'Gestionar tipo vehículo', 1, 4);
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (42, 'Gestionar sucursales', 1, 4);
-- Submenús de PERSONAL
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (50, 'Gestionar tipo personal', 1, 5);
-- Submenús de ATENCIÓN AL CLIENTE
INSERT INTO conf_menus (id, nombre, estado, idPadre) VALUES (60, 'Ejemplo', 1, 6);

-- Tabla dmenus
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (1, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (2, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (3, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (4, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (5, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (6, 1);
-- Submenús de "USUARIOS"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (10, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (11, 1);
-- Submenús de "CONFIGURACIÓN"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (20, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (21, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (22, 1);
-- Submenús de "VENTAS"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (30, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (31, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (32, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (33, 1);
-- Submenús de "VIAJES"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (40, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (41, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (42, 1);
-- Submenús de "PERSONAL"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (50, 1);
-- Submenús de "ATENCIÓN AL CLIENTE"
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (60, 1);

-- Tabla apariencia
INSERT INTO conf_plantillas (id, nombre, color_header, color_footer, logo, estado, usuario) VALUES (1, 'YATRAX', '#0c336e', '#000000', '/Static/img/plantillas/logo_yatusa.png', 1, 'SYSTEM');

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

DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_SUCURSAL(
    IN P_UBIGEO CHAR(6),
    IN P_NOMBRE VARCHAR(50),
    IN P_DIRECCION VARCHAR(255),
    IN P_LATITUD DECIMAL(8,6),
    IN P_LONGITUD DECIMAL(9,6),
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
    WHERE nombre = P_NOMBRE AND estado_registro = 1;

    IF cSucursal > 0 THEN
        SET @MSJ2 = 'Ya existe una sucursal con ese nombre';
    ELSE
        INSERT INTO sucursal (ubigeo, nombre, direccion, latitud, longitud, usuario) 
        VALUES (P_UBIGEO, P_NOMBRE, P_DIRECCION, P_LATITUD, P_LONGITUD, P_USUARIO);

        SET @MSJ = 'Se registró correctamente la sucursal';
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_EDITAR_SUCURSAL(
    IN P_ID INT,
    IN P_UBIGEO CHAR(6),
    IN P_NOMBRE VARCHAR(50),
    IN P_DIRECCION VARCHAR(255),
    IN P_LATITUD DECIMAL(8,6),
    IN P_LONGITUD DECIMAL(9,6),
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cSucursal INT;
    DECLARE cNombre INT;
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

    IF cSucursal <= 0 THEN
        SET @MSJ2 = 'La sucursal que intenta editar no existe';
    ELSEIF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre de la sucursal ya está en uso';
    ELSE
        UPDATE sucursal 
        SET ubigeo = P_UBIGEO,
            nombre = P_NOMBRE,
            direccion = P_DIRECCION,
            latitud = P_LATITUD,
            longitud = P_LONGITUD,
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
    IN P_IDUSUARIO INT
)
BEGIN
    DECLARE cMenus INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMenus FROM conf_dmenus WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO;

    IF cMenus > 0 THEN
        SET @MSJ2 = 'El permiso que intenta asignar, ya existe';
    ELSE
        INSERT INTO conf_dmenus (idMenu, idUsuario) 
        VALUES (P_IDMENU, P_IDUSUARIO);

        SET @MSJ = 'Se asignó correctamente el permiso';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_DMENU
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_DMENU(
    IN P_IDMENU INT,
    IN P_IDUSUARIO INT
)
BEGIN
    DECLARE cMenus INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cMenus FROM conf_dmenus WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO;

    IF cMenus <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM conf_dmenus WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO; 
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

-- Eliminar procedimientos existentes (si los hay)

DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_VEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_VEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPO_VEHICULO;

-- Cambiar delimitador para creación de procedimientos
DELIMITER $$

-- Procedimiento para insertar tipo de vehículo
CREATE PROCEDURE SP_INSERTAR_TIPOVEHICULO(
    IN p_nombre VARCHAR(50),
    IN p_capacidad INT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET MSJ2 = 'Error inesperado al insertar el tipo de vehículo';
    END;

    SET MSJ = NULL;
    SET MSJ2 = NULL;

    -- Validaciones
    IF p_nombre IS NULL OR p_nombre = '' THEN
        SET MSJ2 = 'El nombre es obligatorio';
    ELSEIF p_capacidad <= 0 THEN
        SET MSJ2 = 'La capacidad debe ser mayor a 0';
    ELSE
        SELECT COUNT(*) INTO v_existe FROM tipo_vehiculo WHERE nombre = p_nombre;

        IF v_existe > 0 THEN
            SET MSJ2 = 'Ya existe un tipo de vehículo con ese nombre';
        ELSE
            INSERT INTO tipo_vehiculo (nombre, capacidad, estado)
            VALUES (p_nombre, p_capacidad, 1);

            SET MSJ = 'Se registró correctamente el tipo de vehículo';
        END IF;
    END IF;
END$$

-- Procedimiento para actualizar tipo de vehículo
CREATE PROCEDURE SP_ACTUALIZAR_TIPOVEHICULO(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    IN p_capacidad INT,
    IN p_estado TINYINT,
    OUT MSJ VARCHAR(255),
    OUT MSJ2 VARCHAR(255)
)
BEGIN
    DECLARE v_existe INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET MSJ2 = 'Error inesperado al actualizar el tipo de vehículo';
    END;

    SET MSJ = NULL;
    SET MSJ2 = NULL;

    -- Validaciones
    IF p_nombre IS NULL OR p_nombre = '' THEN
        SET MSJ2 = 'El nombre es obligatorio';
    ELSEIF p_capacidad <= 0 THEN
        SET MSJ2 = 'La capacidad debe ser mayor a 0';
    ELSEIF p_estado NOT IN (0, 1) THEN
        SET MSJ2 = 'El estado debe ser 0 o 1';
    ELSE
        SELECT COUNT(*) INTO v_existe FROM tipo_vehiculo WHERE idTipoVehiculo = p_id;

        IF v_existe = 0 THEN
            SET MSJ2 = 'El tipo de vehículo no existe';
        ELSE
            UPDATE tipo_vehiculo
            SET nombre = p_nombre,
                capacidad = p_capacidad,
                estado = p_estado
            WHERE idTipoVehiculo = p_id;

            SET MSJ = 'Se actualizó correctamente el tipo de vehículo';
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
    WHERE idTipoVehiculo = p_id;

    IF v_existe = 0 THEN
        SET MSJ2 = 'El tipo de vehículo no existe';
    ELSE
        START TRANSACTION;
        UPDATE tipo_vehiculo
        SET estado = 0
        WHERE idTipoVehiculo = p_id;
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
    WHERE idTipoVehiculo = p_id;

    IF v_existe = 0 THEN
        SET MSJ2 = 'El tipo de vehículo no existe';
    ELSE
        START TRANSACTION;
        DELETE FROM tipo_vehiculo
        WHERE idTipoVehiculo = p_id;
        COMMIT;

        SET MSJ = 'Tipo de vehículo eliminado correctamente';
    END IF;
END$$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_HORARIO
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `SP_REGISTRAR_HORARIO`(
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

-- Crear procedimiento SP_INSERTAR_TIPO_SERVICIO

DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_TIPO_SERVICIO(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_DESP VARCHAR (255),
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
    FROM tipo_servicio
    WHERE nombre = P_NOMBRE AND ESTADO_REGISTRO = 1;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de servicio con ese nombre';
    ELSE
        INSERT INTO tipo_servicio (nombre, descripcion, estado, usuario)
        VALUES (P_NOMBRE, P_DESP, P_ESTADO, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de servicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_TIPO_SERVICIO

DELIMITER $$
CREATE PROCEDURE SP_ACTUALIZAR_TIPO_SERVICIO(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BOOLEAN,
    IN P_DESP VARCHAR(255)
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

    SELECT COUNT(*) INTO cExiste FROM tipo_servicio WHERE idTipoServicio = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cNombre FROM tipo_servicio WHERE NOMBRE = P_NOMBRE AND idTipoServicio != P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de servicio que desea actualizar';
    ELSEIF cNombre != 0 THEN
        SET @MS2J = 'El tipo de servicio ingresado ya existe';
    ELSE
        UPDATE tipo_servicio 
        SET nombre = P_NOMBRE, descripcion = P_DESP, estado = P_ESTADO, estado_proceso = 'MODIFICADO'
        WHERE idTipoServicio = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se actualizó correctamente el tipo de servicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_DAR_BAJA_SERVICIO

DELIMITER $$
CREATE PROCEDURE SP_DAR_BAJA_TIPO_SERVICIO(
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

    SELECT COUNT(*) INTO cExiste FROM tipo_servicio WHERE idTipoServicio = P_ID AND ESTADO_REGISTRO = 1;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'El tipo de servicio que intenta dar de baja no existe';
    ELSE
        UPDATE tipo_servicio 
        SET estado = 0, ESTADO_PROCESO = 'MODIFICADO'
        WHERE idTipoServicio = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se dio de baja correctamente al tipo de servicio';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ELIMINAR_TIPO_SERVICIO
DELIMITER $$
CREATE PROCEDURE SP_ELIMINAR_TIPO_SERVICIO(
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

    SELECT COUNT(*) INTO cUsuario FROM tipo_servicio where idTipoServicio = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MS2J = 'El tipo de servicio que intenta eliminar no existe';
    ELSE
        UPDATE tipo_servicio SET ESTADO_REGISTRO =2, ESTADO_PROCESO = 'ELIMINADO' WHERE idTipoServicio = P_ID  AND ESTADO_REGISTRO = 1;
        SET @MSJ = 'Se eliminó correctamente el tipo de servicio|';
    END IF;
END $$

DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_METODO_PAGO
DELIMITER $$ 
CREATE PROCEDURE SP_REGISTRAR_METODO_PAGO(
    IN P_NOMBRE VARCHAR(100),
    IN P_LOGO VARCHAR(255),
    IN P_ESTADO BOOLEAN,
    IN P_USUARIO VARCHAR(100)
)
BEGIN
    DECLARE cNombre INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado al ejecutar el procedimiento almacenado');
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cNombre FROM metodo_pago WHERE NOMBRE = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El método de pago que intenta registrar ya está registrado';
    ELSE
        INSERT INTO metodo_pago (NOMBRE, LOGO, ESTADO, ESTADO_PROCESO, ESTADO_REGISTRO, FECHA_REGISTRO, USUARIO) 
        VALUES (P_NOMBRE, P_LOGO, P_ESTADO, DEFAULT, DEFAULT, CURRENT_TIMESTAMP, P_USUARIO);

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
    IN P_ESTADO BOOLEAN
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
    SELECT COUNT(*) INTO cNombre FROM metodo_pago WHERE NOMBRE = P_NOMBRE AND ID != P_ID;

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
            ESTADO_REGISTRO = 1 -- El estado de registro permanece en 1
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
