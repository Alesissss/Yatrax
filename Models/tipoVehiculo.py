import bd
import hashlib

class TipoVehiculo:
    def __init__(self,idTipoVehiculo=None,largo=None,ancho=None,capacidad=None,combustible=None,consumo=None,estado=None):
        self.idTipoVehiculo=idTipoVehiculo
        self.largo=largo
        self.ancho=ancho
        self.capacidad=capacidad
        self.combustible=combustible
        self.consumo=consumo
