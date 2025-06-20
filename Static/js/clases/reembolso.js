export class Reembolso {
  constructor(numeroComprobante, monto, fecha, idPasaje, idCliente, idTipoComprobante, idMetodoPago) {
    this.numeroComprobante = numeroComprobante;
    this.monto = monto;
    this.fecha = fecha; // puede ser una fecha actual o asignada por el backend
    this.idPasaje = idPasaje;
    this.idCliente = idCliente;
    this.idTipoComprobante = idTipoComprobante;
    this.idMetodoPago = idMetodoPago;
  }
}
