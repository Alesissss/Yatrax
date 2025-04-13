-- Primero eliminamos los procedimientos por si existen
DROP PROCEDURE IF EXISTS SP_ELIMINAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_EDITAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_USUARIO;
DROP PROCEDURE IF EXISTS SP_REGISTRAR_TIPO_USUARIO;

-- Luego eliminamos las tablas, primero la que depende de la otra
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS tipo_usuario;

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
    id_tipousuario INT not null,
    estado_proceso VARCHAR(100) NOT NULL DEFAULT 'REGISTRADO',
    estado_registro INT not null DEFAULT 1,
    fecha_registro DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
    usuario VARCHAR(100) not null
);

-- Tabla Tipo Usuario
INSERT INTO tipo_usuario (id,nombre,estado_proceso,estado_registro,fecha_registro, usuario) VALUES (1,'ADMINISTRADOR','REGISTRADO',1,'2025-03-06 20:02:56','SYSTEM');

-- Tabla Usuario
INSERT INTO usuarios (id,nombre,email,password,id_tipousuario,estado_proceso,estado_registro,fecha_registro,usuario) VALUES (1,'Alexis','alexis@gmail.com','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',1,'MODIFICADO',1,'2025-03-06 20:06:14','SYSTEM');

-- Crear procedimiento SP_REGISTRAR_USUARIO
DELIMITER $$
CREATE PROCEDURE SP_REGISTRAR_USUARIO(
    IN P_NOMBRE VARCHAR(255),
    IN P_EMAIL VARCHAR(255),
    IN P_PASS VARCHAR(255),
    IN P_IDTIPOUSUARIO INT,
    IN P_USUARIO VARCHAR(255)
)
BEGIN
    DECLARE cEmail INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado: ', (SELECT MESSAGE_TEXT FROM INFORMATION_SCHEMA.INNODB_TRX LIMIT 1));
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cEmail FROM USUARIOS WHERE EMAIL = P_EMAIL;

    IF cEmail > 0 THEN
        SET @MSJ2 = 'El correo que intenta registrar ya está registrado';
    ELSE
        INSERT INTO USUARIOS (NOMBRE, EMAIL, PASSWORD, ID_TIPOUSUARIO, USUARIO) 
        VALUES (P_NOMBRE, P_EMAIL, P_PASS, P_IDTIPOUSUARIO, P_USUARIO);

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
    IN P_IDTIPOUSUARIO INT
)
BEGIN
    DECLARE cUsuario INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET @MSJ2 = CONCAT('Error inesperado: ', (SELECT MESSAGE_TEXT FROM INFORMATION_SCHEMA.INNODB_TRX LIMIT 1));
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario FROM USUARIOS WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta editar no existe';
    ELSE
        UPDATE USUARIOS 
        SET NOMBRE = P_NOMBRE, EMAIL = P_EMAIL, ID_TIPOUSUARIO = P_IDTIPOUSUARIO, estado_proceso = 'MODIFICADO' 
        WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

        SET @MSJ = 'Se modificó correctamente al usuario';
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
        SET @MSJ2 = CONCAT('Error inesperado: ', (SELECT MESSAGE_TEXT FROM INFORMATION_SCHEMA.INNODB_TRX LIMIT 1));
    END;

    SET @MSJ = NULL;
    SET @MSJ2 = NULL;

    SELECT COUNT(*) INTO cUsuario FROM USUARIOS WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

    IF cUsuario <= 0 THEN
        SET @MSJ2 = 'El usuario que intenta eliminar no existe';
    ELSE
        UPDATE USUARIOS SET ESTADO_REGISTRO = 2, ESTADO_PROCESO = 'ELIMINADO' WHERE ID = P_ID AND ESTADO_REGISTRO = 1;

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
        SET @MSJ2 = CONCAT('Error inesperado: ', (SELECT MESSAGE_TEXT FROM INFORMATION_SCHEMA.INNODB_TRX LIMIT 1));
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