import hashlib
import bd

class Tipo_Reclamo:
    def __init__(self,id,nombre,estado):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("SELECT * FROM tipo_reclamo")
            return resultados if resultados else ""
        finally:
            conexion.cerrar()
        
    @classmethod
    def obtener_por_id(cls,id):
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("SELECT * FROM tipo_reclamo WHERE id=%s",(id,))
            return resultados[0] if resultados else ""
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls,nombre):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_INSERTAR_TIPO_RECLAMO(%s,@MSJ,@MSJ2);",(nombre,))
            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else ""
        except Exception as e:
            return {"Status":0,"Mensaje":"Error: "+repr(e)}
        finally:
            if conexion != None:
                conexion.cerrar()
    
    @classmethod
    def editar(cls,id,nombre,estado):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_MODIFICAR_TIPO_RECLAMO(%s,%s,%s,@MSJ,@MSJ2)",(id,nombre,estado,))
            resultado = conexion.obtener("SELECT @MSJ AS msj,@MSJ2 AS msj2;")
            return resultado[0] if resultado else ""
        except Exception as e:
            return {"Status":0,"Mensaje":"Error: "+repr(e)}
        finally:
            if conexion != None:
                conexion.cerrar()

    @classmethod
    def eliminar(cls,id):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_RECLAMO(%s,@MSJ,@MSJ2)",(id,))
            resultado = conexion.obtener("SELECT @MSJ AS msj,@MSJ2 AS msj2;")
            return resultado[0] if resultado else ""
        except Exception as e:
            return {"Status":0,"Mensaje":"Error: "+repr(e)}
        finally:
            if conexion != None:
                conexion.cerrar()
