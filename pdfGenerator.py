from fpdf import FPDF
import os
from generadorQR import generar_codigo_qr

class TicketTransporteSimple:
    def __init__(self):
        self.ancho_total = 80
        self.margen = 5
        self.ancho_util = self.ancho_total - 2 * self.margen
        self.pdf = FPDF("P", "mm", (self.ancho_total, 250))
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=10)
        self.pdf.set_margins(self.margen, self.margen, self.margen)

    def generar_ticket(self, datos_ticket, nombre_archivo="ticket_transporte.pdf"):
        try:
            empresa = datos_ticket['empresa']
            comprobante = datos_ticket['comprobante']
            cliente = datos_ticket['cliente']
            viaje = datos_ticket.get('viaje', {})
            servicio = datos_ticket['servicio']
            totales = datos_ticket['totales']

            # Datos de empresa
            self.pdf.set_font('Helvetica', 'B', 10)
            self.pdf.multi_cell(self.ancho_util, 5, empresa['nombre'], align='C')

            self.pdf.ln(3)
            self.pdf.set_font('Helvetica', '', 8)
            self.pdf.multi_cell(self.ancho_util, 4, f"R.U.C. {empresa['ruc']}", align='C')

            direccion_lineas = empresa['direccion'].split('\n')
            for linea in direccion_lineas:
                self.pdf.ln(3)
                self.pdf.multi_cell(self.ancho_util, 4, linea.strip(), align='C')

            telefono = empresa.get('telefono', '').strip().rstrip('/')
            if telefono:
                self.pdf.ln(3)
                self.pdf.multi_cell(self.ancho_util, 4, telefono, align='C')

            self.pdf.ln(1)
            self.pdf.set_font('Helvetica', 'B', 9)
            self.pdf.cell(self.ancho_util, 5, empresa.get('tipo_comprobante', ''), ln=True, align='C')
            self.pdf.cell(self.ancho_util, 5, empresa['numero_comprobante'], ln=True, align='C')
            self.pdf.ln(2)

            self.pdf.set_font('Helvetica', '', 8)
            self._etiqueta_valor("Fecha de emisión", comprobante.get('fecha', ''))
            self._etiqueta_valor("Hora", comprobante.get('hora', ''))
            self._etiqueta_valor("Tipo de moneda", comprobante.get('moneda', 'PEN'))
            self._etiqueta_valor("Cajero", comprobante.get('cajero', ''))
            self._etiqueta_valor("Doc. Identidad", cliente['documento'])
            self._etiqueta_valor("Cliente", cliente['nombre'])
            self._etiqueta_valor("EMBARQUE", viaje.get('embarque', ''))
            self._etiqueta_valor("DESEMBARQUE", viaje.get('desembarque', ''))
            self.pdf.ln(2)

            y1 = self.pdf.get_y()
            self.pdf.line(self.margen, y1, self.ancho_total - self.margen, y1)
            self.pdf.ln(2)

            self.pdf.set_font('Helvetica', 'B', 8)
            self.pdf.cell(self.ancho_util * 0.7, 5, "DESCRIPCION", ln=False)
            self.pdf.cell(self.ancho_util * 0.3, 5, "TOTAL", ln=True, align='R')
            y2 = self.pdf.get_y()
            self.pdf.line(self.margen, y2, self.ancho_total - self.margen, y2)
            self.pdf.ln(1)

            self.pdf.set_font('Helvetica', '', 7.5)
            descripcion = f"POR EL SERVICIO DE TRANSPORTE DE LA RUTA {servicio['ruta']}"
            if 'tipo_servicio' in servicio:
                descripcion += f"/ SERVICIO: {servicio['tipo_servicio']}"
            if 'asiento' in servicio:
                descripcion += f"/ NRO ASIENTO:{servicio['asiento']}"
            if 'pasajero' in servicio:
                descripcion += f"/ PASAJERO: {servicio['pasajero']}"
            if 'documento_pasajero' in servicio:
                descripcion += f" / DNI: {servicio['documento_pasajero']}"
            if 'fecha_viaje' in servicio:
                descripcion += f" / FECHA VIAJE: {servicio['fecha_viaje']}"
            if 'hora_viaje' in servicio:
                descripcion += f" / HORA VIAJE: {servicio['hora_viaje']}"
            descripcion += f" /{servicio['cantidad']}/{servicio['precio_unitario']:.2f}"

            x_actual = self.pdf.get_x()
            y_desc = self.pdf.get_y()
            self.pdf.multi_cell(self.ancho_util * 0.7, 4, descripcion.strip(), align='L')
            y_fin = self.pdf.get_y()
            self.pdf.set_xy(self.margen + self.ancho_util * 0.7, y_desc)
            self.pdf.multi_cell(self.ancho_util * 0.3, 4, f"{servicio['total']:.2f}", align='R')
            self.pdf.set_y(max(y_fin, self.pdf.get_y()) + 1)
            self.pdf.line(self.margen, self.pdf.get_y(), self.ancho_total - self.margen, self.pdf.get_y())
            self.pdf.ln(2)

            self._fila_monto_con_simbolo("Op. Gravada", totales.get('op_gravada', 0.00))
            self._fila_monto_con_simbolo("Op. Exonerada", totales.get('op_exonerada', 0.00))
            self._fila_monto_con_simbolo("I.G.V. (18%)", totales.get('igv', 0.00))
            self._fila_monto_con_simbolo("Total Dscto.", totales.get('descuento', 0.00))
            self._fila_total_monto("Importe Total", totales['total'])

            self.pdf.ln(1)
            if 'total_letras' in datos_ticket:
                self.pdf.set_font('Helvetica', '', 8)
                self.pdf.multi_cell(self.ancho_util, 4, f"SON: {datos_ticket['total_letras']}", align='L')

            self.pdf.ln(1)
            self._etiqueta_valor("COND. PAGO", datos_ticket.get('condicion_pago', 'CONTADO'))

            self.pdf.ln(3)
            self.pdf.set_font('Helvetica', '', 7)
            self.pdf.multi_cell(self.ancho_util, 4, "Representación impresa de la BOLETA DE VENTA ELECTRÓNICA", align='C')

            qr_path = datos_ticket.get('qr')
            if qr_path and os.path.exists(qr_path):
                self.pdf.ln(2)
                self.pdf.image(qr_path, x=(self.ancho_total - 30) / 2, w=30)

            url_path = datos_ticket.get('url')
            self.pdf.ln(3)
            self.pdf.set_font('Helvetica', '', 7)
            self.pdf.multi_cell(self.ancho_util, 4, f"Consulte documento en {url_path}", align='C')

            self.pdf.ln(3)
            self.pdf.set_font('Helvetica', '', 7)
            self.pdf.multi_cell(self.ancho_util, 4, "Cubierto por POLIZA DE SEGURO LA POSITIVA 05-60004991 - 1 15/01/2024-15/01/2025", align='C')

            self.pdf.output(nombre_archivo)
            return os.path.abspath(nombre_archivo) if os.path.exists(nombre_archivo) else None

        except Exception as e:
            print(f"\u274c Error al generar ticket: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def _etiqueta_valor(self, etiqueta, valor):
        self.pdf.set_font('Helvetica', '', 8)
        col1 = self.ancho_util * 0.38
        col2 = self.ancho_util * 0.06
        col3 = self.ancho_util - col1 - col2
        y_ini = self.pdf.get_y()
        self.pdf.set_xy(self.margen + col1 + col2, y_ini)
        self.pdf.multi_cell(col3, 4, str(valor), align='R')
        y_fin = self.pdf.get_y()
        self.pdf.set_y(y_ini)
        self.pdf.cell(col1, 4, etiqueta, ln=False)
        self.pdf.cell(col2, 4, ":", ln=False, align='C')
        self.pdf.set_y(max(y_fin, self.pdf.get_y()))

    def _fila_total_monto(self, etiqueta, monto):
        self.pdf.set_font('Helvetica', 'B', 9)
        col1 = self.ancho_util * 0.4
        col2 = self.ancho_util * 0.2
        col3 = self.ancho_util * 0.4
        self.pdf.cell(col1, 5, etiqueta, ln=False)
        self.pdf.cell(col2, 5, "S/", ln=False, align='C')
        self.pdf.cell(col3, 5, f"{monto:.2f}", ln=True, align='R')

    def _fila_monto_con_simbolo(self, etiqueta, monto):
        self.pdf.set_font('Helvetica', '', 8)
        col1 = self.ancho_util * 0.4
        col2 = self.ancho_util * 0.2
        col3 = self.ancho_util * 0.4
        self.pdf.cell(col1, 4, etiqueta, ln=False)
        self.pdf.cell(col2, 4, "S/", ln=False, align='C')
        self.pdf.cell(col3, 4, f"{monto:.2f}", ln=True, align='R')


def ejemplo_ticket():
    print("\U0001f68c Generando ticket de transporte...")

    url = 'http://see.transporteschiclayo.pe/'
    ruta_qr = generar_codigo_qr(url)

    datos_ticket = {
        'empresa': {
            'nombre': 'EMPRESA DE TRANSPORTES CHICLAYO S.A.',
            'ruc': '20103626448',
            'direccion': 'AV PASEO DE LA REPÚBLICA 857 INT 1 LA VICTORIA, LIMA, LIMA',
            'telefono': 'CHICLAYO-CHICLAYO-957578490/',
            'tipo_comprobante': 'BOLETA DE VENTA ELECTRÓNICA',
            'numero_comprobante': 'B995-00507106'
        },
        'comprobante': {
            'fecha': '16/08/2024',
            'hora': '11:30:49',
            'moneda': 'PEN',
            'cajero': 'Web'
        },
        'cliente': {
            'documento': '77057132',
            'nombre': 'FRIDA YAMILET, CABREJOS, ESCURRA'
        },
        'viaje': {
            'embarque': 'AV. VIA DE AVITAMIENTO SUR N° 2339',
            'desembarque': 'AV. JOSE LEONARDO ORTIZ 010'
        },
        'servicio': {
            'ruta': 'CAJAMARCA-CHICLAYO',
            'tipo_servicio': 'BUSCAMA',
            'asiento': '44',
            'pasajero': 'FRIDA YAMILET, CABREJOS, ESCURRA',
            'documento_pasajero': '77057132',
            'fecha_viaje': '29/08/2024',
            'hora_viaje': '10:40PM',
            'cantidad': 1,
            'precio_unitario': 40.00,
            'total': 40.00
        },
        'totales': {
            'op_gravada': 0.00,
            'op_exonerada': 40.00,
            'igv': 0.00,
            'descuento': 0.00,
            'total': 40.00
        },
        'total_letras': 'CUARENTA Y 00/100 SOLES',
        'condicion_pago': 'CONTADO',
        'info_legal': {
            'url_consulta': url,
            'poliza_seguro': 'Cubierto por POLIZA DE SEGURO LA POSITIVA 05-60004991 - 1 15/01/2024-15/01/2025'
        },
        'qr': ruta_qr,
        'url': url
    }

    ticket = TicketTransporteSimple()
    ruta = ticket.generar_ticket(datos_ticket, "mi_ticket_transporte.pdf")

    if ruta:
        print(f"\U0001f3ab ¡Éxito! Tu ticket está listo en: {ruta}")
    else:
        print("❌ Falló la generación")


ejemplo_ticket()