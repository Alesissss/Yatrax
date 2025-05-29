import bd
import re

class Ciudad:
    def __init__(self, id=None, nombre=None, abreviatura=None):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, nombre, abreviatura FROM ciudad")
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_abreviatura(cls, nombre):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("SELECT abreviatura FROM ciudad WHERE nombre = %s", (nombre,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()
            
    @classmethod
    def _exists_abreviatura(cls, abbr):
        conexion = bd.Conexion()
        try:
            filas = conexion.obtener(
                "SELECT 1 FROM ciudad WHERE abreviatura = %s",
                (abbr,)
            )
            return bool(filas)
        finally:
            conexion.cerrar()

    @classmethod
    def _generar_abreviatura_recursivo(cls, nombre, index=0):
        """
        Toma 3 letras consecutivas (en mayúsculas) del nombre limpio.
        Si choca, avanza un carácter y vuelve a intentar.
        """
        # 1) Limpiar y pasar a mayúsculas
        clean = re.sub(r'[^A-Za-zÁÉÍÓÚÜÑ]', '', nombre).upper()

        # 2) Extraer tramo de 3 caracteres a partir de index
        tramo = clean[index:index+3]

        # 3) Si queda corto (<3), rellenar con 'X' hasta 3
        if len(tramo) < 3:
            tramo = (tramo + "XXX")[:3]

        # 4) Si ya existe, avanzar un carácter
        if cls._exists_abreviatura(tramo):
            return cls._generar_abreviatura_recursivo(nombre, index+1)

        # 5) Devolver exactamente 3 caracteres en mayúsculas
        return tramo

    @classmethod
    def registrar_abreviatura(cls, nombre, abreviatura):
        conexion = bd.Conexion()
        try:
            # Garantizar que abreviatura llega en MAYÚSCULAS y 3 chars
            abbr3 = abreviatura.upper()[:3]
            conexion.ejecutar(
                "CALL SP_REGISTRAR_ABREVIATURA_CIUDAD(%s, %s);",
                (nombre, abbr3)
            )
            # Opcional: leer mensajes del SP
            res = conexion.obtener("SELECT @MSJ AS mensaje1, @MSJ2 AS mensaje2;")
            return res[0] if res else None
        finally:
            conexion.cerrar()