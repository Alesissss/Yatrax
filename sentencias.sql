-- Primero eliminamos los procedimientos por si existen
DROP PROCEDURE IF EXISTS SP_ASIGNAR_DMENU;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_DMENU;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_DARBAJA_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_EDITAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_ACTIVAR_PLANTILLA;
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_ELIMINAR_TIPOVEHICULO;
DROP PROCEDURE IF EXISTS SP_INSERTAR_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_ACTUALIZAR_TIPO_CLIENTE;
DROP PROCEDURE IF EXISTS SP_DAR_BAJA_TIPO_CLIENTE;
-- Luego eliminamos las tablas, primero la que depende de la otra
DROP TABLE IF EXISTS conf_plantillas;
DROP TABLE IF EXISTS conf_dmenus;
DROP TABLE IF EXISTS conf_menus;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS tipo_usuario;
DROP TABLE IF EXISTS tipo_vehiculo;
DROP TABLE IF EXISTS metodo_pago;
DROP TABLE IF EXISTS tipo_cliente;

-- Crear tabla metodo_pago
CREATE TABLE metodo_pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    logo VARCHAR(255) NOT NULL,
    estado VARCHAR(50) NOT NULL
);

-- Crear tabla tipo_usuario
CREATE TABLE tipo_usuario (
    id int AUTO_INCREMENT PRIMARY key,
    nombre varchar(100) NOT NULL UNIQUE,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
    usuario VARCHAR(100) not null
);

-- Crear tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    id_tipousuario INT not null REFERENCES tipo_usuario (id),
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
    usuario VARCHAR(100) not null
);

-- Crear tabla menus
CREATE TABLE conf_menus (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    nombre VARCHAR(100) UNIQUE NOT NULL,
    estado BOOLEAN NOT NULL
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
    estado tinyint not null
);

-- Crear tabla tipo_cliente
CREATE TABLE tipo_cliente (
    idTipoCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    estado BIT NOT NULL
);

INSERT INTO tipo_vehiculo (nombre, capacidad, estado) 
VALUES ('MetroRapid X12', 120, 1);

INSERT INTO tipo_vehiculo (nombre, capacidad, estado) 
VALUES ('CargoMaster Pro', 30, 1);

INSERT INTO tipo_vehiculo (nombre, capacidad, estado) 
VALUES ('EcoGlider Prime', 54, 1);

-- Tabla Tipo Usuario
INSERT INTO tipo_usuario (id,nombre,estado_proceso,estado_registro,fecha_registro, usuario) VALUES (1,'ADMINISTRADOR','REGISTRADO',1,'2025-03-06 20:02:56','SYSTEM');

-- Tabla Usuario
INSERT INTO usuarios (id,nombre,email,password, imagen, id_tipousuario,estado_proceso,estado_registro,fecha_registro,usuario) VALUES (1,'Alexis','alexis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', '/Static/img/trabajadores/alexis.jpeg',1,'MODIFICADO',1,'2025-03-06 20:06:14','SYSTEM');

-- Tabla menus
INSERT INTO conf_menus (id, nombre, estado) VALUES (1, 'M_USUARIOS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (2, 'M_CONFIGURACION', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (3, 'M_VENTAS', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (4, 'M_VIAJES', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (5, 'M_PERSONAL', 1);
INSERT INTO conf_menus (id, nombre, estado) VALUES (6, 'M_ATENCION', 1);

-- Tabla dmenus
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (1, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (2, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (3, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (4, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (5, 1);
INSERT INTO conf_dmenus (idMenu, idUsuario) VALUES (6, 1);

-- Tabla apariencia
INSERT INTO conf_plantillas (id, nombre, color_header, color_footer, logo, estado, usuario) VALUES (1, 'YATRAX', '#0c336e', '#000000', '/Static/img/plantillas/logo_yatusa.png', 1, 'SYSTEM');

-- Crear procedimiento SP_REGISTRAR_USUARIO
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_USUARIO(
    IN P_NOMBRE VARCHAR(255),
    IN P_EMAIL VARCHAR(255),
    IN P_PASS VARCHAR(255),
    IN P_IMAGEN VARCHAR(255),
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

    SELECT COUNT(*) INTO cEmail FROM USUARIOS WHERE EMAIL = P_EMAIL;

    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSE
        INSERT INTO USUARIOS (NOMBRE, EMAIL, PASSWORD, IMAGEN, ID_TIPOUSUARIO, USUARIO) 
        VALUES (P_NOMBRE, P_EMAIL, P_PASS, P_IMAGEN, P_IDTIPOUSUARIO, P_USUARIO);

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

    SELECT COUNT(*) INTO cUsuario FROM USUARIOS WHERE ID = P_ID AND ESTADO_REGISTRO = 1;
    SELECT COUNT(*) INTO cEmail FROM USUARIOS WHERE EMAIL = P_EMAIL AND ID != P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta editar no existe';
    ELSEIF cEmail != 0 THEN
        SET @MSJ2 = 'El correo ingresado ya existe';
    ELSE
        UPDATE USUARIOS 
        SET NOMBRE = P_NOMBRE, 
            EMAIL = P_EMAIL,
            IMAGEN = P_IMAGEN,
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

    SELECT COUNT(*) INTO cUsuario FROM USUARIOS WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta dar de baja no existe';
    ELSE
        UPDATE USUARIOS SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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

    SELECT COUNT(*) INTO cUsuario FROM USUARIOS WHERE ID = P_ID;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta eliminar no existe';
    ELSE
        DELETE FROM USUARIOS WHERE ID = P_ID;

        SET @MSJ = 'Se eliminó correctamente al usuario';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_REGISTRAR_TIPO_USUARIO
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_TIPO_USUARIO(
    IN P_NOMBRE VARCHAR(255),
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

    SELECT COUNT(*) INTO cNombre FROM TIPO_USUARIO WHERE nombre = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El tipo de usuario que intenta registrar ya está registrado';
    ELSE
        INSERT INTO TIPO_USUARIO (NOMBRE, USUARIO) 
        VALUES (P_NOMBRE, P_USUARIO);

        SET @MSJ = 'Se registró correctamente el tipo de usuario';
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

    SELECT COUNT(*) INTO cMenus FROM CONF_DMENUS WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO;

    IF cMenus > 0 THEN
        SET @MSJ2 = 'El permiso que intenta asignar, ya existe';
    ELSE
        INSERT INTO CONF_DMENUS (idMenu, idUsuario) 
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

    SELECT COUNT(*) INTO cMenus FROM CONF_DMENUS WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO;

    IF cMenus <= 0 THEN
        SET @MSJ2 = 'El permiso que intenta eliminar, no existe';
    ELSE
        DELETE FROM CONF_DMENUS WHERE idMenu = P_IDMENU AND idUsuario = P_IDUSUARIO; 
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

    SELECT COUNT(*) INTO cNombre FROM CONF_PLANTILLAS WHERE NOMBRE = P_NOMBRE;

    IF cNombre > 0 THEN
        SET @MSJ2 = 'El nombre que intenta registrar ya está registrado';
    ELSE
        INSERT INTO CONF_PLANTILLAS (NOMBRE, COLOR_HEADER, COLOR_FOOTER, LOGO, ESTADO, USUARIO) 
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

    SELECT COUNT(*) INTO cPlantilla FROM CONF_PLANTILLAS WHERE ID = P_ID;
    SELECT COUNT(*) INTO cNombre FROM CONF_PLANTILLAS WHERE NOMBRE = P_NOMBRE AND ID != P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta editar no existe';
    ELSEIF cNombre != 0 THEN
        SET @MSJ2 = 'El nombre ingresado ya existe';
    ELSE
        UPDATE CONF_PLANTILLAS 
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

    SELECT COUNT(*) INTO cPlantilla FROM CONF_PLANTILLAS WHERE ID = P_ID;
    SELECT ESTADO INTO flagPlantilla FROM CONF_PLANTILLAS WHERE ID = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta eliminar no existe';
    ELSEIF flagPlantilla = 1 THEN
        SET @MSJ2 = 'La plantilla que está activa no puede ser eliminada';
    ELSE
        DELETE FROM CONF_PLANTILLAS WHERE ID = P_ID;

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

    SELECT COUNT(*) INTO cPlantilla FROM CONF_PLANTILLAS WHERE ID = P_ID;

    IF cPlantilla <= 0 THEN
        SET @MSJ2 = 'La plantilla que intenta activar no existe';
    ELSE
        UPDATE CONF_PLANTILLAS SET ESTADO = 0;
        UPDATE CONF_PLANTILLAS SET ESTADO = 1 WHERE ID = P_ID;

        SET @MSJ = 'Se activó correctamente la plantilla';
    END IF;
END $$
DELIMITER ;

DELIMITER $$

-- Procedimiento INSERTAR con transacciones y manejo de errores
CREATE PROCEDURE SP_INSERTAR_TIPOVEHICULO(
    IN p_nombre VARCHAR(50),
    IN p_capacidad INT,
    IN p_estado TINYINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    INSERT INTO tipo_vehiculo (nombre, capacidad, estado)
    VALUES (p_nombre, p_capacidad, p_estado);
    COMMIT;
END$$

-- Procedimiento ACTUALIZAR con validación de existencia
CREATE PROCEDURE SP_ACTUALIZAR_TIPOVEHICULO(
    IN p_idTipoVehiculo INT,
    IN p_nombre VARCHAR(50),
    IN p_capacidad INT,
    IN p_estado TINYINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Validación de existencia del registro
    IF NOT EXISTS (SELECT 1 FROM tipo_vehiculo WHERE idTipoVehiculo = p_idTipoVehiculo) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El tipo de vehículo no existe';
    END IF;
    
    UPDATE tipo_vehiculo
    SET 
        nombre = p_nombre,
        capacidad = p_capacidad,
        estado = p_estado
    WHERE idTipoVehiculo = p_idTipoVehiculo;
    
    COMMIT;
END$$

-- Procedimiento ELIMINAR con validación de existencia
CREATE PROCEDURE SP_ELIMINAR_TIPOVEHICULO(
    IN p_idTipoVehiculo INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Validación de existencia del registro
    IF NOT EXISTS (SELECT 1 FROM tipo_vehiculo WHERE idTipoVehiculo = p_idTipoVehiculo) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El tipo de vehículo no existe';
    END IF;
    
    DELETE FROM tipo_vehiculo
    WHERE idTipoVehiculo = p_idTipoVehiculo;
    
    COMMIT;
END$$

DELIMITER ;

-- Crear procedimiento SP_INSERTAR_TIPO_CLIENTE

DELIMITER $$
CREATE PROCEDURE SP_INSERTAR_TIPO_CLIENTE(
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BIT
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar SP_INSERTAR_TIPO_CLIENTE';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE nombre = P_NOMBRE;

    IF cExiste > 0 THEN
        SET @MSJ2 = 'Ya existe un tipo de cliente con ese nombre';
    ELSE
        INSERT INTO tipo_cliente (nombre, estado)
        VALUES (P_NOMBRE, P_ESTADO);

        SET @MSJ = 'Se registró correctamente el tipo de cliente';
    END IF;
END $$
DELIMITER ;

-- Crear procedimiento SP_ACTUALIZAR_TIPO_CLIENTE

DELIMITER $$
CREATE PROCEDURE SP_ACTUALIZAR_TIPO_CLIENTE(
    IN P_ID INT,
    IN P_NOMBRE VARCHAR(50),
    IN P_ESTADO BIT
)
BEGIN
    DECLARE cExiste INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = 'Error inesperado al ejecutar SP_ACTUALIZAR_TIPO_CLIENTE';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE idTipoCliente = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de cliente que desea actualizar';
    ELSE
        UPDATE tipo_cliente 
        SET nombre = P_NOMBRE, estado = P_ESTADO
        WHERE idTipoCliente = P_ID;

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
        SET @MSJ2 = 'Error inesperado al ejecutar SP_DAR_BAJA_TIPO_CLIENTE';
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cExiste 
    FROM tipo_cliente 
    WHERE idTipoCliente = P_ID;

    IF cExiste = 0 THEN
        SET @MSJ2 = 'No se encontró el tipo de cliente para dar de baja';
    ELSE
        UPDATE tipo_cliente 
        SET estado = 0
        WHERE idTipoCliente = P_ID;

        SET @MSJ = 'Se dio de baja correctamente al tipo de cliente';
    END IF;
END $$
DELIMITER ;

DELIMITER ;