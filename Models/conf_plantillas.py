import bd

class Conf_Plantillas:
    def __init__(self, id=None, color_header=None, color_footer=None, logo=None, estado=None):
        self.id = id
        self.color_header = color_header
        self.color_footer = color_footer
        self.logo = logo
        self.estado = estado
    
    @classmethod
    def obtener_Plantillas(cls):
        conexion = bd.Conexion()
        try:
            conf_plantillas = conexion.obtener("SELECT id, nombre, color_header, color_footer, logo, estado FROM conf_plantillas")
            return conf_plantillas
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_PlantillaActiva(cls):
        conexion = bd.Conexion()
        try:
            conf_plantillas = conexion.obtener("SELECT id, nombre, color_header, color_footer, logo, estado FROM conf_plantillas WHERE estado = 1")
            return conf_plantillas[0] if conf_plantillas else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_PlantillaPorId(cls, id):
        conexion = bd.Conexion()
        try:
            conf_plantillas = conexion.obtener("SELECT id, nombre, color_header, color_footer, logo, estado FROM conf_plantillas WHERE id = %s", (id,))
            return conf_plantillas[0] if conf_plantillas else None
        finally:
            conexion.cerrar()
    
    #REGISTRAR
    @classmethod
    def registrar(cls, nombre, color_header, color_footer, logo, usuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_PLANTILLA(%s, %s, %s, %s, %s);", (nombre, color_header, color_footer, logo, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, color_header, color_footer, logo):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_PLANTILLA(%s, %s, %s, %s, %s);", (id, nombre, color_header, color_footer, logo))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    
    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_PLANTILLA(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()