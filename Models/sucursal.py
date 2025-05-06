import bd

class Sucursal:
    def __init__(self, id=None, departamento=None, nombre=None, direccion=None, latitud=None, longitud=None, estado=1, estado_proceso='REGISTRADO', estado_registro=1, fecha_registro=None, usuario=None):
        self.id = id
        self.departamento = departamento
        self.nombre = nombre
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.estado = estado
        #Auditoría
        self.estado_proceso = estado_proceso
        self.estado_registro = estado_registro
        self.fecha_registro = fecha_registro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, departamento, nombre, direccion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal WHERE estado_registro = 1
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, departamento, nombre, direccion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal WHERE id = %s and estado_registro = 1
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, departamento, nombre, direccion, latitud, longitud, usuario_actual):
        try:
            conexion = bd.Conexion()
            cursor = conexion.conexion.cursor()
            
            # Llamar al procedimiento almacenado actualizado
            cursor.callproc('SP_REGISTRAR_SUCURSAL', [
                departamento, 
                nombre, 
                direccion, 
                latitud, 
                longitud, 
                usuario_actual
            ])
            
            # Obtener los resultados
            for resultado in cursor.stored_results():
                fila = resultado.fetchone()
                if fila:
                    msj, msj2, error_code, error_msg = fila
                    
                    if error_code == 0:
                        return {'Status': 'success', 'Msj': msj, 'Msj2': msj2}
                    else:
                        return {'Status': 'error', 'Msj': msj2, 'ErrorCode': error_code}
            
            return {'Status': 'error', 'Msj': 'No se recibió respuesta del procedimiento'}
            
        except Exception as e:
            return {'Status': 'error', 'Msj': f'Error al registrar sucursal: {str(e)}'}
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexion.cerrar()

    @classmethod
    def editar(cls, id, departamento, direccion, nombre, latitud, longitud, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_SUCURSAL(%s, %s, %s, %s, %s, %s, %s);",
                (id, departamento, nombre, direccion, latitud, longitud, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_SUCURSAL(%s, %s);", (id, usuario,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_SUCURSAL(%s);", (id, usuario,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
