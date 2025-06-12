import bd

class Pasajero:
    def __init__(self, id=None, nombre=None, ape_paterno=None, ape_materno=None, idTipoDocumento=None, numero_documento=None, sexo=None, f_nacimiento=None, telefono=None, email=None):
        self.id = id
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.idTipoDocumento = idTipoDocumento
        self.numero_documento = numero_documento
        self.sexo = sexo
        self.f_nacimiento = f_nacimiento
        self.telefono = telefono
        self.email = email
    
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            pasajeros = conexion.obtener("""SELECT p.id, p.nombre, p.ape_paterno, p.ape_materno, td.abreviatura AS tipo_documento, 
                                            p.numero_documento, p.sexo, p.f_nacimiento, p.telefono, p.email
                                            FROM pasajero p
                                            INNER JOIN tipo_documento td ON p.idTipoDocumento = td.id""")
            return pasajeros
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_por_numero_documento(cls, numero_documento):
        conexion = bd.Conexion()
        try:
            pasajero = conexion.obtener("""SELECT p.id, p.nombre, p.ape_paterno, p.ape_materno, td.abreviatura AS tipo_documento, 
                                            p.numero_documento, p.sexo, p.f_nacimiento, p.telefono, p.email
                                            FROM pasajero p
                                            INNER JOIN tipo_documento td ON p.idTipoDocumento = td.id
                                            WHERE p.numero_documento = %s""", (numero_documento,))
            return pasajero[0] if pasajero else None
        finally:
            conexion.cerrar()