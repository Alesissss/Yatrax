import hashlib
import bd

class Cliente:
    def __init__(self, id = None, numero_documento = None, nombre = None, ape_paterno = None, ape_materno = None, sexo = None, f_nacimiento = None, razon_social = None, direccion = None, telefono = None, email = None, password = None, estado = None ,id_pais=None, id_tipo_doc=None, id_tipo_cliente=None, fechaRegistro = None, usuario = None):
        self.id = id
        self.numero_documento = numero_documento
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.sexo = sexo
        self.f_nacimiento = f_nacimiento
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.password = password
        self.estado = estado
        self.id_pais=id_pais
        self.id_tipo_cliente=id_tipo_cliente
        self.id_tipo_doc=id_tipo_doc
        # Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario
    @classmethod    
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            clientes = conexion.obtener("""select cl.id as ID, ps.nombre as nombre_pais, tp.abreviatura, cl.numero_documento, cl.nombre, CONCAT(cl.ape_paterno, ' ', cl.ape_materno) AS apellidos, cl.sexo, cl.f_nacimiento, cl.direccion, cl.telefono, cl.email, cl.estado
                                            from cliente cl inner join pais ps on cl.id_pais = ps.id
                                            inner join tipo_documento tp on cl.id_tipo_doc = tp.id;""")
            return clientes
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, cliente_id):
        conexion = bd.Conexion()
        try:
            cliente = conexion.obtener("""select cl.id as ID, ps.nombre as nombre_pais, tp.abreviatura, cl.numero_documento, cl.nombre, CONCAT(cl.ape_paterno, ' ', cl.ape_materno) AS apellidos, cl.sexo, cl.f_nacimiento, cl.direccion, cl.telefono, cl.email, cl.estado, cl.password
                                            from cliente cl inner join pais ps on cl.id_pais = ps.id
                                            inner join tipo_documento tp on cl.id_tipo_doc = tp.id WHERE cl.id  = %s""", (cliente_id,))
            return cliente[0] if cliente else None
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_por_numero_documento(cls, numero_documento):
        conexion = bd.Conexion()
        try:
            query = """
                select cli.nombres, cli.ape_paterno, cli.ape_materno, cli.razon_social, cli.email, cli.numero_documento, cli.telefono, 
                cli.f_nacimiento, cli.sexo from cliente cli inner join tipo_cliente tc on cli.id_tipo_cliente = tc.idTipoCliente 
                where cli.numero_documento = %s
            """
            usuario = conexion.obtener(query, (numero_documento,))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    @classmethod
    def logear_cliente(cls, email,contrasena):
        conexion = bd.Conexion()
        try:
            contrasena_hasheada = hashlib.sha256(contrasena.encode()).hexdigest()
            usuario = conexion.obtener("SELECT * FROM cliente WHERE email=%s AND password=%s",(email,contrasena_hasheada))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    @classmethod
    def actualizar_cliente(cls, id_cliente, id_pais, id_tipo_cliente, id_tipo_doc, numero_documento, nombre, ape_paterno, ape_materno, sexo, f_nacimiento, direccion, telefono, email, password, estado, usuario):
        conexion = bd.Conexion()
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest() if password else None
            conexion.ejecutar(
                "CALL SP_EDITAR_CLIENTE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    id_cliente, id_pais, id_tipo_cliente, id_tipo_doc, numero_documento,
                    nombre, ape_paterno, ape_materno, sexo, f_nacimiento,
                    direccion, telefono, email, password_hash, estado, usuario
                )
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        except Exception as e:
            return {'@MSJ': '', '@MSJ2': f'Error: {str(e)}'}
        finally:
            conexion.cerrar()

    @classmethod
    def verificar_correo_cliente(cls,correo):
        conexion = bd.Conexion()
        status = -1
        try:
            conn = conexion.obtener_conexion()
            cursor = conn.cursor()

            # Declarar variable de salida
            cursor.callproc('SP_VERIFICAR_CORREO_CLIENTE', (correo, 0))

            # Obtener el valor de la variable OUT
            resultado = -1
            for res in cursor.stored_results():
                row = res.fetchone()
                if row:
                    resultado = row[0]

            status = 1 if resultado == 1 else 0
            return status

        except Exception as e:
            return status
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, id_pais, id_tipo_doc, id_tipo_cliente, numero_documento, nombre,
                  ape_paterno, ape_materno, sexo, f_nacimiento, direccion,
                  telefono, email, password, estado, usuario):
        conexion = bd.Conexion()
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            # Llamar al procedimiento almacenado SP_REGISTRAR_CLIENTE
            conexion.ejecutar(
                "CALL SP_REGISTRAR_CLIENTE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    id_pais, id_tipo_doc, id_tipo_cliente, numero_documento, nombre,
                    ape_paterno, ape_materno, sexo, f_nacimiento, direccion,
                    telefono, email, password_hash, estado, usuario
                )
            )
            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    
    
   # @classmethod
    #def registrarForm(cls, id_pais, id_tipo_cliente, id_tipo_doc, numero_documento, nombres,
     #           ape_paterno, ape_materno, sexo, f_nacimiento, razon_social,
      #          direccion, telefono, email, password, usuario):
       # conexion = bd.Conexion()
        #try:
         #   password_hash = hashlib.sha256(password.encode()).hexdigest()
          #  query = """
           # INSERT INTO cliente (
            #    id_pais, id_tipo_cliente, id_tipo_doc, numero_documento, 
             #   nombres, ape_paterno, ape_materno, sexo, f_nacimiento, 
              #  razon_social, direccion, telefono, email, password, usuario
            #) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            #"""

            #conexion.ejecutar(query, (
             #   id_pais, id_tipo_cliente, id_tipo_doc, numero_documento,
              #  nombres, ape_paterno, ape_materno, sexo, f_nacimiento,
               # razon_social, direccion, telefono, email, password_hash, usuario
            #))

            # Simular respuesta exitosa como los otros métodos
            #return {'@MSJ': 'Cliente registrado con éxito', '@MSJ2': ''}
        #except Exception as e:
         #   print("ERROR en Cliente.registrar:", e)
          #  return {'@MSJ': '', '@MSJ2': f'Error: {str(e)}'}
        #finally:
         #   conexion.cerrar()

    
    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_CLIENTE(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #DAR DE BAJA
    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_DARBAJA_CLIENTE(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
