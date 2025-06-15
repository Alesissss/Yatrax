export class Venta {
  constructor(numDoc, nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, telefono, recuperarSeleccion, sexo, correo, brazos, esMenor) {
    this.numDoc = numDoc;
    this.nombres = nombres;
    this.apellidoPaterno = apellidoPaterno;
    this.apellidoMaterno = apellidoMaterno;
    this.fechaNacimiento = fechaNacimiento;
    this.telefono = telefono;
    this.recuperarSeleccion = recuperarSeleccion;
    this.sexo = sexo;
    this.correo = correo;
    this.brazos = brazos;
    this.esMenor = esMenor;
  }
}