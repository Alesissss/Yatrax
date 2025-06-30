import hashlib
import os
import re
import random
from weakref import ref
#extra agregado para la transaccion
import bd
from correo import enviar_correo
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort,current_app
from Models.pasaje import Pasaje
from flask_mail import Mail
import datetime

from Models.conf_plantillas import Conf_Plantillas
from Models.api_net import ApiNetPe
from Models.servicio import Servicio
from Models.cliente import Cliente
from Models.tipo_herramienta import TipoHerramienta
from Models.microservicio import MicroServicio
from Models.tipoDocumento import TipoDocumento
from Models.tipoCliente import TipoCliente
from Models.tipoVehiculo import TipoVehiculo
from Models.pais import Pais
from Models.terminos_condiciones import TerminosCondiciones
from Models.viaje import Viaje
from Models.pasaje import Pasaje
from Models.reembolso import Reembolso
from Models.tipoComprobante import TipoComprobante
from Models.metodo_pago import MetodoPago
from Models.herramienta import Herramienta
from Models.preguntas_frecuentes import PreguntasFrecuentes
from Models.pasajero import Pasajero
from Models.ruta import Ruta
from Models.tipoMetodoPago import TipoMetodoPago
from Models.asiento import Asiento
from Models.venta import Venta
from Models.reserva import Reserva
from Models.conf_general import ConfGeneral
from Models.promocion import Promocion


homeClientes_bp = Blueprint('homeClientes', __name__, url_prefix='/ecommerce/home')

# FUNCIONES AUXILIARES
# REGION RESERVA

@homeClientes_bp.route("/obtenerMetodoPagoxID/<int:idMetodo>")
def obtenerMetodoPagoxID(idMetodo):
    try:
        resultado = MetodoPago.obtener_por_id(idMetodo)
        return resultado["nombre"].lower()
    except Exception as e:
        return jsonify({"Status": "error", "Msj": "Error inesperado:"+repr(e)})
    
@homeClientes_bp.route("/obtenerTipoMetodoxID/<int:idTipoMetodo>")
def obtenerTipoMetodoPagoxID(idTipoMetodo):
    try:
        resultado = TipoMetodoPago.obtener_por_id(idTipoMetodo)
        return resultado["nombre"].lower()
    except Exception as e:
        return jsonify({"Status": "error", "Msj": "Error inesperado:"+repr(e)})

@homeClientes_bp.route("/procesar_reserva", methods=["POST"])
def procesar_reserva():
    try:
        data = request.get_json()

        contacto = data.get("contacto", {})
        pago = data.get("pago", {})
        ventas = data.get("ventas", {})
        codigoReserva = Pasaje.generar_codigo_reserva(),
        fecha = datetime.datetime.now()

        resultado = Reserva.registrar_operacion(contacto, pago, ventas,codigoReserva,fecha)

        if resultado["status"] == 1:
            email = contacto.get("email", None)
            print(email)

            datosEnvio = {
                'asunto':'Envio codigo de reservacion Yatrax',
                'remitente': 'yatraxyatusa@gmail.com',
                'destinatario': email,
                'mensaje': 'Estimado(a), recordarle que el lapso de tiempo para efectuar el pago de su reserva es de 2h máximo. A continuacion, se le hace entrega del codigo de reserva que debera presentar en agencia: '+str(codigoReserva)
            }

            enviar_correo(current_app.extensions['mail'],datosEnvio)
            return jsonify({"Status": "success", "codigo_confirmacion": f"VENTA-{resultado['id_venta']}"})
        else:
            return jsonify({"Status": "error", "Msj": resultado["msg"]})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

# END REGION

def renderizarCompra():
    herramientas = Herramienta.obtener_todos()
    return render_template('/Ecommerce/home/partials/ventaPasajes.html', herramientas = herramientas)


@homeClientes_bp.route('/renderizar_itinerario', methods=['POST'])
def renderizar_itinerario():
    data = request.get_json()
    itinerarios = data.get('itinerarios', [])
    sufijo = data.get('sufijo')
    # Renderiza el HTML del itinerario con Jinja
    html_renderizado = render_template('Ecommerce/home/partials/itinerario.html', itinerarios=itinerarios, sufijo = sufijo )
    return jsonify({'html': html_renderizado})


# VIEWS
@homeClientes_bp.route('/inicio')
def index():
    
    datos_recibidos = {
        "servicios":Servicio.obtener_todos(),
        "contenido_venta": renderizarCompra(),
        "promociones": Promocion.obtener_todos_activos()
    }
    return render_template('Ecommerce/home/home.html', active_page="home",datos=datos_recibidos)

@homeClientes_bp.route('/cambioRuta')
def cambioRuta():

    return render_template('Ecommerce/home/cambioRuta.html')

@homeClientes_bp.route("/obtenerDatosPasajero", methods=["POST"])
def obtenerDatosPasajero():
    payload = request.get_json(force=True) or {}
    numero_doc = payload.get("numero_documento")
    if not numero_doc:
        return jsonify(status="error", msg="Falta número de documento"), 400

    # Suponemos que Pasajero.obtener_por_numero_documento devuelve un dict o un objeto serializable
    datos_pasajero = Pasajero.obtener_por_numero_documento(numero_doc)
    if not datos_pasajero:
        return jsonify(status="error", msg="Pasajero no encontrado"), 404
    
    # Convertir fecha si es string
    if isinstance(datos_pasajero["f_nacimiento"], str):
        try:
            datos_pasajero["f_nacimiento"] = datetime.strptime(datos_pasajero["f_nacimiento"], "%Y-%m-%d")
        except ValueError:
            return jsonify(status="error", msg="Formato de fecha inválido"), 500

    return jsonify(status="success", datos=datos_pasajero), 200


@homeClientes_bp.route("/sobreNosotros")
def sobreNosotros():
    return render_template('Ecommerce/home/sobreNosotros.html')

@homeClientes_bp.route('/error')
def error():
    return render_template('Ecommerce/error.html')

@homeClientes_bp.route('/login',methods=["GET","POST"])
def login_cliente():
    
    if request.method == "GET":
        if 'cliente' in session:
            return redirect("/ecommerce/home/inicio")
        else:
            return render_template('Ecommerce/home/modalLoginNewVer.html')
    else:
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]
        cliente = Cliente.logear_cliente(correo,contrasena)

        if cliente != None:
            session["cliente"] = cliente
            return redirect("/ecommerce/home/inicio")
        else:
            return jsonify({"msj": "Ingreso de credenciales incorrecto. Vuelva a intentarlo"})

@homeClientes_bp.route("/logout")
def logoutCliente():
    if 'cliente' in session:
        session.pop('cliente',None)
        return redirect("/ecommerce/home/inicio")
    else:
        return redirect("/ecommerce/home/inicio")

#REGION POR TERMINAR    
@homeClientes_bp.route("/miPerfil",methods=["GET","POST"])
def perfilCliente():
    if request.method == "GET":
        paises = Pais.obtener_todos()
        tipoCliente = TipoCliente.obtener_todos()
        tipoDocumentos = TipoDocumento.obtener_todos()
        return render_template("Ecommerce/home/miPerfil.html",paises=paises,tiposCliente=tipoCliente,tipoDocumentos=tipoDocumentos)
    else:
        try:
            data = request.get_json()  # Recupera el JSON enviado
            # Accede a cada campo del JSON
            id_cliente = data.get("id_cliente")
            usuario = data.get("usuario")
            id_pais = data.get("id_pais")
            id_tipo_cliente = data.get("id_tipo_cliente")
            razon_social = data.get("razon_social")
            id_tipo_doc = data.get("id_tipo_doc")
            numero_documento = data.get("numero_documento")
            f_nacimiento = data.get("f_nacimiento")
            nombres = data.get("nombres")
            ape_paterno = data.get("ape_paterno")
            ape_materno = data.get("ape_materno")
            sexo = data.get("sexo")
            direccion = data.get("direccion")
            telefono = data.get("telefono")
            email = data.get("email")
            password = data.get("password")
            
            if password.strip():
                password_hash = hashlib.sha256(password.encode()).hexdigest()
            else:
                password_hash = None
            
            resultado = Cliente.actualizarPerfil(id_cliente, id_pais, id_tipo_cliente, id_tipo_doc, numero_documento,nombres, ape_paterno, ape_materno, sexo, f_nacimiento,razon_social, direccion, telefono, email, password_hash, usuario)

            if resultado.get('MSJ2'):  # Si hay mensaje de error
                return jsonify({"Status": 0, "Mensaje": resultado['MSJ2']})
            else:
                return jsonify({"Status": 1, "Mensaje": resultado['MSJ']})
        except Exception as e:
            return jsonify({"Status":0,"Mensaje":"Error: "+str(e)})


#Recuperar contraseña terminado y arreglado
@homeClientes_bp.route("/recuperarContrasena")
def recuperarContrasena():
    if request.method == "GET":
        return render_template("home/changePassword.html")
        
#End region

@homeClientes_bp.route('/register')
def register_cliente():
    if 'cliente' in session:
        return redirect(url_for('homeClientes.index'))
    else:
        TipoDocumentos=TipoDocumento.obtener_todos()
        Paises = Pais.obtener_todos()
        return render_template('Ecommerce/home/formRegistro.html', TipoDocumento=TipoDocumentos, Paises=Paises)
        
@homeClientes_bp.route('transferenciaPasaje')
def transferencia_pasaje():
    return render_template('Ecommerce/home/transferenciaPasaje.html')


@homeClientes_bp.route("/microservicios/<int:id>", methods = ["GET"])
def ver_microservicios(id):
    datos_servicio = Servicio.obtener_uno(id)
    datos_microservicio = MicroServicio.obtenerPorServicio(id)
    return render_template('Ecommerce/home/microservicios.html', servicio = datos_servicio, microservicios = datos_microservicio)

@homeClientes_bp.route('/miPasajeOperaciones')
def mi_pasaje_operaciones():
    datos_recibidos = {
        "contenido_venta": renderizarCompra()
    }
    result = ConfGeneral.obtener()
    TipoDocumentos=TipoDocumento.obtener_todos()
    TipoMetodosPago = TipoMetodoPago.obtener_todos()
    MetodoPagos = MetodoPago.obtener_todos()
    TipoComprobantes = TipoComprobante.obtener_todos()
    return render_template('Ecommerce/home/miPasajeOp.html', datos=datos_recibidos, TipoDocumento=TipoDocumentos, TipoMetodosPago=TipoMetodosPago, MetodosPagos=MetodoPagos, TipoComprobantes=TipoComprobantes, result=result)

@homeClientes_bp.route('/seguimientoViaje')
def seguimiento_viaje():
    return render_template('Ecommerce/home/seguimientoViaje.html')

@homeClientes_bp.route('/misBoletos')
def misboletos():
    if 'cliente' not in session:
        return redirect(url_for('homeClientes.index'))
    else:
        id_cliente = session.get('cliente', {}).get('id')
        boletos= Viaje.obtener_viajes_por_cliente(id_cliente)
        return render_template('Ecommerce/home/misBoletos.html', boletos=boletos)

@homeClientes_bp.route('/pago')
def pago_pasajes():
    return render_template('Ecommerce/home/pago.html')

@homeClientes_bp.route('/terminosYcondiciones')
def terminos_y_condiciones():
    return render_template('Ecommerce/home/terminosCondiciones.html')

# END VIEWS

# FUNCIONES

# REGIÓN CAMBIO DE RUTA #

@homeClientes_bp.route('/resumenViaje', methods=['POST'])
def resumen_viaje():
    try:
        # Obtener los datos del JSON recibido
        asiento_id = request.json.get('asiento_id')
        viaje = request.json.get('viaje')
        
        # Verificar que los datos se están recibiendo correctamente
        print(f"asiento_id: {asiento_id}, viaje: {viaje}")  # Verifica que los valores sean correctos

        if not asiento_id or not viaje:
            return jsonify({'Status': 'error', 'Msj': 'Falta el ID del asiento o el ID del viaje.'})

        # Obtener los datos del viaje usando el método de Pasaje
        datos = Pasaje.detalle_viaje(asiento_id, viaje)
        print(f'Información de resumen: {datos}')  # Verifica qué datos se están recuperando
        
        if not datos:
            return jsonify({'Status': 'error', 'Msj': 'No se encontraron datos para el asiento proporcionado.'})

        # Si los datos son correctos, se toma el primer elemento de la lista
        detalle = datos[0] if isinstance(datos, list) and datos else None
        
        if not detalle:
            return jsonify({'Status': 'error', 'Msj': 'No se encontró detalle válido del viaje.'})

        # Crear la respuesta con los detalles del viaje y el precio total
        resumen = {
            'detalle_viaje': detalle,
            'pasajeros': [{
                'numero': 1,
                'asiento': asiento_id,
                'precio': detalle.get('precio_total', 0),  # Se asegura de que el precio exista
            }],
            'precio_total': detalle.get('precio_total', 0)  # Usamos el precio_total
        }

        # Responder con éxito
        return jsonify({'Status': 'success', 'data': resumen, 'Msj': 'Datos del viaje obtenidos correctamente.'})
    
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al procesar el viaje: {repr(e)}'})
    

@homeClientes_bp.route('/resumenGeneral', methods=['POST'])
def resumen_general():
    try:
        asiento_ids = request.json.get('asiento_ids')  # Los IDs de los asientos
        viaje = request.json.get('viaje')  # El ID del viaje
        pasajeros = request.json.get('pasajeros')  # Los datos estructurados de los pasajeros

        if not asiento_ids or not viaje:
            return jsonify({'Status': 'error', 'Msj': 'Faltan los IDs de los asientos o el viaje.'})

        resumen = []

        # Procesar cada asiento para obtener el detalle del viaje
        for asiento_id, datos_pasajero in zip(asiento_ids, pasajeros):
            datos = Pasaje.detalle_viaje(asiento_id, viaje)
            
            if not datos:
                resumen.append({
                    'Status': 'error',
                    'Msj': f'No se encontraron datos para el asiento {asiento_id}.'
                })
                continue
            
            detalle = datos[0] if isinstance(datos, list) and datos else None
            if not detalle:
                resumen.append({
                    'Status': 'error',
                    'Msj': f'No se encontró detalle válido para el asiento {asiento_id}.'
                })
                continue

            # Agregar el detalle de cada asiento al resumen
            resumen.append({
                'detalle_viaje': detalle,
                'pasajero': datos_pasajero,  # Los datos del pasajero correspondientes
                'precio_total': detalle['precio_total']  # Total sin aplicar descuento
            })

        # Si todo está correcto, devolver el resumen con la información de todos los asientos
        return jsonify({'Status': 'success', 'data': resumen, 'Msj': 'Resumen general generado correctamente.'})

    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al procesar el resumen general: {repr(e)}'})

@homeClientes_bp.route('/obtenerPrecioPasaje', methods=['POST'])
def obtener_precio_cambio_ruta():
    try:
        num_comprobante = request.json.get('comprobante')
        codigo = request.json.get('codigo')
        if not num_comprobante or not codigo:
            return jsonify({'Status': 'error', 'Msj': 'Faltan datos para calcular el precio.'})
        precio = Pasaje.obtener_precio_ruta(num_comprobante, codigo)
        print(f"Precio obtenido: {precio}")
        return jsonify({'Status': 'success', 'precio': precio, 'Msj': 'Precio obtenido correctamente.'})
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al obtener el precio: {repr(e)}'}) 

@homeClientes_bp.route('/ObtenerPrecioCambioRuta', methods=['GET'])
def obtenerRutaPrecio():
    try:
        precio = ConfGeneral.obtener_precio_cambio_ruta()
        if precio is None:
            return jsonify({'Status': 'error', 'Msj': 'No se pudo obtener el precio de cambio de ruta.'})
        return jsonify({'Status': 'success', 'precio': precio, 'Msj': 'Precio obtenido correctamente.'})
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al obtener el precio: {repr(e)}'})
    

@homeClientes_bp.route('/cambiarEstadoPasaje', methods=['POST'])
def cambiarEstadoPasaje():
    try:
        comprobante = request.json.get('comprobante')
        print(f"Comprobante recibido: {comprobante}")
        if not comprobante:
            return jsonify({'Status': 'error', 'Msj': 'Falta el número de comprobante.'})
        cambiarEstado = Pasaje.esCambioRuta(comprobante)
        if cambiarEstado is None:
            return jsonify({'Status': 'error', 'Msj': 'No se encontró el pasaje con el comprobante proporcionado.'})
        return jsonify({'Status': 'success', 'Msj': 'Estado del pasaje cambiado correctamente.'})
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al cambiar el estado del pasaje: {repr(e)}'})
    
@homeClientes_bp.route('/referenciarPasaje', methods=['POST'])
def referenciar_pasaje():
    try:
        num_comprobante = request.json.get('num_comprobante')
        if not num_comprobante:
            return jsonify({'Status': 'error', 'Msj': 'Falta el número de comprobante.'})
        ref = Pasaje.obtener_id_por_comprobante(num_comprobante)
        if ref is None:
            return jsonify({'Status': 'error', 'Msj': 'No se encontró el pasaje con el comprobante proporcionado.'})
        execute = Pasaje.actualizar_id_pasaje_ultimo()    
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al referenciar el pasaje : {repr(e)}'})
    

# END REGIÓN CAMBIO DE RUTA #

@homeClientes_bp.route('/GetConfApariencia')
def get_ConfApariencia():
    try:
        conf_apariencia = Conf_Plantillas.obtener_PlantillaActiva()
        if conf_apariencia:
            return jsonify({'data': conf_apariencia, 'Status': 'success', 'Msj': 'Configuración obtenida exitosamente.'})
        else:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontró configuración activa.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al obtener la configuración: {repr(e)}'})
    
@homeClientes_bp.route('/GetRutasConcatenadas')
def get_rutasConcatenadas():
    try:
        lista_rutas = Viaje.obtenerDestinos()
        if lista_rutas:
            return jsonify({'data': lista_rutas, 'Status': 'success', 'Msj': 'Rutas obtenidas correctamente.'})
        else:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron rutas activas.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al obtener la ruta: {repr(e)}'})

@homeClientes_bp.route('/GetRutasConcatenadasA', methods=['POST'])
def get_rutasA():
    try:
        payload = request.get_json(force=True)
        s_origen  = payload.get('origen')
        s_destino = payload.get('destino')
        lista_pasajes = Viaje.obtenerDestinosMenosActual(s_origen, s_destino)
        if lista_pasajes:
            return jsonify({'data': lista_pasajes, 'Status': 'success', 'Msj': 'Rutas obtenidas correctamente.'})
        else:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron rutas distintas.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al obtener la ruta: {repr(e)}'})


@homeClientes_bp.route('/GetRutasConcatenadasSinLaActusal', methods=['GET', 'POST'])
def get_rutas_concatenadas_sin_la_actual():
    try:
        # 1) Intentamos GET ?numeroComprobante=XXX
        num_comprobante = request.args.get('A000-00000007')
        # 2) Si no vino, miramos en JSON POST (por compatibilidad)
        if not num_comprobante and request.is_json:
            num_comprobante = request.get_json().get('numeroComprobante')
        if not num_comprobante:
            return jsonify({
                'data': {}, 'Status': 'error',
                'Msj': 'Falta numeroComprobante.'
            }), 400

        datos = Pasaje.obtenerDatosPasaje(num_comprobante)
        if not datos:
            return jsonify({
                'data': {}, 'Status': 'error',
                'Msj': 'No se encontró pasaje para ese comprobante.'
            }), 404

        rutas = Viaje.obtenerDestinosMenosActual(
            datos['idSucursalOrigen'], datos['idSucursalDestino']
        )
        return jsonify({
            'data': rutas or [], 
            'Status': rutas and 'success' or 'error',
            'Msj': rutas and 'Rutas obtenidas.' or 'No hay rutas distintas.'
        })
    except Exception as e:
        return jsonify({
            'data': {}, 'Status': 'error',
            'Msj': f'Error interno: {e!r}'
        }), 500   
    
# API NET RENIEC
# controller_clientes.py
@homeClientes_bp.route('/api/get_persona_data', methods=['GET'])
def get_persona_data():
    def responder(datos):
        if datos:
            f_nacimiento = datos.get("f_nacimiento")
            datos["f_nacimiento"] = f_nacimiento.strftime("%Y-%m-%d %H:%M:%S") if f_nacimiento else None
            return jsonify({'data': datos, 'Status': 'success', 'Msj': 'Datos obtenidos correctamente'})
        return None  # Si no hay datos, no responde nada aún

    try:
        tipo_doc = request.args.get('tipoDoc')
        num_doc = request.args.get('numDoc')

        if not tipo_doc or not num_doc:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'Debe proporcionar un tipo y número de documento'})

        api_pasajero = Pasajero()
        api_clientes = Cliente()
        api = ApiNetPe()

        fuentes_por_tipo = {
            'DNI': [
                lambda: api_clientes.obtener_por_numero_documento(num_doc),
                lambda: api_pasajero.obtener_por_numero_documento(num_doc),
                lambda: api.get_person(num_doc)
            ],
            'CE': [
                lambda: api_pasajero.obtener_por_numero_documento(num_doc),
                lambda: api.get_person(num_doc),
            ],
            'RUC': [
                lambda: api_clientes.obtener_por_numero_documento(num_doc),
                lambda: api.get_company(num_doc)
            ]
        }

        fuentes = fuentes_por_tipo.get(tipo_doc, [])

        for fuente in fuentes:
            datos = fuente()
            respuesta = responder(datos)
            if respuesta:
                return respuesta

        # Si no se encontró nada, devuelve una lista vacía
        return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron datos para el documento proporcionado'})

    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Error en el servidor: {repr(e)}'})


# FIN API NET RENIEC


@homeClientes_bp.route("/RegistrarClienteForm", methods=["POST"])
def registrar_cliente_form():
    try:
        id_tipo_doc = request.form.get("tipo-doc")
        numero_documento = request.form.get("ytrx-doc-number", "").strip()
        nombres = request.form.get("ytrx-fullname", "").strip()
        ape_paterno = request.form.get("ytrx-lastname-father", "").strip()
        ape_materno = request.form.get("ytrx-lastname-mother", "").strip()
        sexo = request.form.get("ytrx-gender")
        f_nacimiento = request.form.get("ytrx-birthdate")
        telefono = request.form.get("ytrx-phone", "").strip()
        direccion = request.form.get("ytrx-address", "").strip()
        id_pais = request.form.get("ytrx-country").strip()
        email = request.form.get("ytrx-email", "").strip()
        password = request.form.get("ytrx-password", "").strip()
        abreviatura = TipoDocumento.obtener_por_id(id_tipo_doc)
        
        if  abreviatura['abreviatura']== "RUC":
            id_tipoCliente = TipoCliente.obtener_por_nombre("Empresa")
        else:
            id_tipoCliente = TipoCliente.obtener_por_nombre("Adulto")
        
        # Registrar cliente
        mensajes = Cliente.registrar(
            id_pais=id_pais,
            id_tipo_doc=id_tipo_doc,
            id_tipo_cliente=id_tipoCliente['ID'],
            numero_documento=numero_documento,
            nombre=nombres,
            ape_paterno=ape_paterno,
            ape_materno=ape_materno,
            sexo=sexo,
            f_nacimiento=f_nacimiento,
            direccion=direccion,
            telefono=telefono,
            email=email,
            password=password,
            estado=1,
            usuario=None
        )
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "error", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar cliente"})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

# REGION TERMINOS Y CONDICIONES
@homeClientes_bp.route('/ApiTerminosCondicionesActivo', methods=['GET'])
def api_terminos_condiciones_activo():
    try:
        UPLOAD_FOLDER = "Static/utilities/terminos_condiciones/"

        activo = TerminosCondiciones.obtener_activos()
        if not activo:
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": "No hay términos y condiciones activos."
            })
        
        termino = activo[0]
        filename = termino['archivo']
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        if not os.path.exists(file_path):
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": f"El archivo {filename} no existe en el servidor."
            })
        
        texto = open(file_path, encoding='utf-8').read()
        
        # Regex que captura cada sección y su contenido hasta la siguiente sección o fin de texto
        pattern = re.compile(
            r"\*(COMPRAS EN INTERNET|PASAJES|ENCOMIENDAS|BASE LEGAL)\*\s*([\s\S]*?)(?=\*(?:COMPRAS EN INTERNET|PASAJES|ENCOMIENDAS|BASE LEGAL)\*|$)",
            re.IGNORECASE
        )
        matches = {m[0].upper(): m[1].strip() for m in pattern.findall(texto)}

        # Aseguramos el orden fijo
        secciones = ["COMPRAS EN INTERNET", "PASAJES", "ENCOMIENDAS", "BASE LEGAL"]
        resultado = []
        for sec in secciones:
            resultado.append({
                "seccion":  sec,
                "contenido": matches.get(sec, "")
            })

        return jsonify({
            "Status": "success",
            "data":   resultado
        })

    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj":    f"Ocurrió un error al obtener términos: {e}",
            "data":   []
        })


# END REGION TERMINOS Y CONDICIONES

# REGION PREGUNTAS FRECUENTES

@homeClientes_bp.route('/obtenerPreguntasFrecuentes', methods=['GET'])
def obtener_preguntas_frecuentes():
    try:
        preguntas = PreguntasFrecuentes.obtener_todos()
        if preguntas:
            return jsonify({"Status": "success", "data": preguntas})
        return jsonify({"Status": "info", "Msj": "Aún no hay preguntas frecuentes registradas", "data": []})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener las preguntas frecuentes: {repr(e)}", "data": []})

# END REGION PREGUNTAS FRECUENTES

@homeClientes_bp.route('/obtenerOrigenesDestinos',methods=['GET'])
def obtenerOrigenesDestinos():
    try:

        return {"data":[],"Msj":"Se ha obtenido correctamente los datos","Status":"success"}
    except Exception as e:
        return {"data":[],"Msj":f"Error al obtener los origenes:{repr(e)}","Status":"error"}

# END FUNCIONES

# REGIÓN COMPRA PASAJE
@homeClientes_bp.route('/buscarViajes',methods=['POST'])
def buscarViajes():
    try:
        datos_viaje_ida = []
        datos_viaje_vuelta = []

        origen = request.form.get('origen')
        destino = request.form.get('destino')
        fecha_ida = request.form.get('fecha_ida')
        fecha_vuelta = request.form.get('fecha_vuelta')
        datos_viaje_ida = Viaje.buscarViajePorRutaYFecha(origen=origen, destino=destino, fecha= fecha_ida)
        if fecha_vuelta:
            datos_viaje_vuelta = Viaje.buscarViajePorRutaYFecha(origen=destino, destino=origen, fecha= fecha_vuelta)
        return jsonify({
            "data_ida":datos_viaje_ida,
            "data_vuelta":datos_viaje_vuelta,
            "Msg":"Listado retornado correctamente",
            "Status": "success"
        })
    except Exception as e:
        return jsonify({
            "data_ida":[],
            "data_vuelta":[],
            "Msg":"Hubo un error al buscar los viajes; " + repr(e),
            "Status": "error"
        })


@homeClientes_bp.route("/obtener_diseno_vehiculo", methods=['POST'])
def obtener_diseno_vehiculo():
    detalle_viaje_id = request.json.get("id_dv")
    datos = Viaje.obtener_asientos(detalle_viaje_id)
    niveles = Viaje.obtener_tamano_niveles(detalle_viaje_id)
    return jsonify({
        "data": datos,
        "niveles": niveles,
        "Status": "success",
        "msg": "Retornado con éxito" 
    })

@homeClientes_bp.route("/cargar_metodos",methods=["GET"])
def cargar_metodos():
    try:
        lista = TipoMetodoPago.obtener_tipos_y_metodos()
        por_tipo = dict()
        for elemento in lista:
            id_tipo_metodo = str(elemento["id_tipo_metodo"])  # convertimos a str para usar como clave
            elemento_sin_id = elemento.copy()
            elemento_sin_id.pop("id_tipo_metodo", None)

            if id_tipo_metodo in por_tipo:
                por_tipo[id_tipo_metodo].append(elemento_sin_id)
            else:
                por_tipo[id_tipo_metodo] = [elemento_sin_id]
            
        return {"data":por_tipo, "msg":"Listado correctamente de los métodos","status":1}
    except Exception as e:
        return {"data":[], "msg":f"Error al listar los métodos: {repr(e)}","status":-1}

@homeClientes_bp.route("/ocuparAsiento", methods=["POST"])
def ocupar_asiento():
    try:
        id_asiento = request.json.get("asiento_id")
        
        estado_actual = Asiento.obtener_estado(id_asiento)
        if estado_actual['estado'] == 0:
            return {"data": [], "msg": "El asiento ya está ocupado", "status": 0}
        Asiento.ocupar_asiento(id_asiento)
        return {"data": [], "msg": "Asiento ocupado correctamente", "status": 1}
    except Exception as e:
        return {"data": [], "msg": f"Error al ocupar el asiento: {repr(e)}", "status": -1}

@homeClientes_bp.route("/liberarAsiento", methods=["POST"])
def liberar_asiento():
    try:
        id_asiento = request.json.get("asiento_id")
        
        estado_actual = Asiento.obtener_estado(id_asiento)
        if estado_actual['estado'] == 1:
            return {"data": [], "msg": "El asiento ya está libre", "status": 0}
        
        Asiento.liberar_asiento(id_asiento)
        return {"data": [], "msg": "Asiento liberado correctamente", "status": 1}
    except Exception as e:
        return {"data": [], "msg": f"Error al liberar el asiento: {repr(e)}", "status": -1}

@homeClientes_bp.route("/procesar_pago_x", methods=["POST"])
def procesar_pago_x():
    try:
        data = request.get_json()

        contacto = data.get("contacto", {})
        pago = data.get("pago", {})
        ventas = data.get("ventas", {})
        precio_venta_total = data.get("precio_venta_total", 0.0)  # Obtener el precio total
        datos_viaje = data.get("datos_viaje", {})  # Obtener datos del viaje
            
        resultado = Venta.registrar_operacion_x(contacto, pago, ventas, precio_venta_total, datos_viaje)

        if resultado["status"] == 1:
            return jsonify({"Status": "success", "codigo_confirmacion": f"VENTA-{resultado['id_venta']}"})
        else:
            return jsonify({"Status": "error", "Msj": resultado["msg"]})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

@homeClientes_bp.route("/procesar_pago", methods=["POST"])
def procesar_pago():
    try:
        data = request.get_json()

        contacto = data.get("contacto", {})
        pago = data.get("pago", {})
        ventas = data.get("ventas", {})
            
        resultado = Venta.registrar_operacion(contacto, pago, ventas)

        if resultado["status"] == 1:
            return jsonify({"tickets":resultado["tickets"],"Status": "success", "codigo_confirmacion": f"VENTA-{resultado['id_venta']}"})
        else:
            return jsonify({"Status": "error", "Msj": resultado["msg"]})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

@homeClientes_bp.route("/obtenerMetodosPago")
def obtener_metodos_pago():
    try:
        metodos = MetodoPago.obtener_todos()
        return jsonify({"Status": "success", "data": metodos})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

@homeClientes_bp.route("/convertirPasajeLibre", methods=["POST"])
def convertir_pasaje_libre():
    try:
        id_pasaje = request.json.get("pasaje_id")
        id_detalle_viaje_asiento = request.json.get("detViaje")
        resultado = Pasaje.convertirPasajeLibre(id_pasaje, id_detalle_viaje_asiento)

        if resultado.get("msj"):
            return jsonify({"Status": "success", "Msj": resultado["msj"]})
        else:
            return jsonify({"Status": "error", "Msj": resultado.get("msj2", "Error desconocido")})  
        
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {e}"})

@homeClientes_bp.route("/realizarTransferencia", methods=["POST"])
def realizar_transferencia():
    try:
        payload    = request.get_json() or {}
        id_pasaje  = payload.get("pasaje", {})
        persona1   = payload.get("persona1", {})
        persona2   = payload.get("persona2", {})

        if not id_pasaje:
            return jsonify({"Status":"error", "Msj":"Falta el ID del pasaje"})

        resultado = Pasaje.realizarTransferencia(id_pasaje, persona1, persona2)

        if resultado.get("msj"):
            return jsonify({"Status":"success", "Msj": resultado["msj"]})
        else:
            return jsonify({"Status":"error",   "Msj": resultado.get("msj2", "Error desconocido")})

    except Exception as e:
        return jsonify({"Status":"error", "Msj": f"Error inesperado: {e}"})

@homeClientes_bp.route("/modalPasarelaPago", methods=["POST"])
def modal_pasarela_pago():
    tipo_comprobante = TipoComprobante.obtener_todos()
    metodo_pago = MetodoPago.obtener_todos()
    return render_template('Ecommerce/home/pasarelaPagos.html', metodo_pago=metodo_pago, tipo_comprobante=tipo_comprobante)

@homeClientes_bp.route("/verificarEstadoPasaje", methods=["GET"])
def verificar_estado_pasaje():
    try:
        id_pasaje = request.args.get("idPasaje", type=int)
        estado = Pasaje.obtener_estados_pasaje(id_pasaje)
        if estado:
            return jsonify({"Status": "success", "data": estado})
        else:
            return jsonify({"Status": "error", "Msj": "No se encontró el pasaje proporcionado"})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {e}"})

# END REGION COMPRA PASAJE

# REGION RUTAS SEGUIMIENTO
@homeClientes_bp.route('/obtenerRutasSeguimiento', methods=['GET'])
def obtener_rutas_seguimiento():
    try:
        rutas = Ruta.obtener_rutas_activas_viaje()
        if not rutas:
            return jsonify({"Status": "info", "data": [], "Msj": "No hay rutas activas para seguimiento."})

        # Formatear las rutas para el seguimiento
        rutas_seguimiento = []
        for ruta in rutas:
            ruta_info = {
                "id": ruta['ID'],
                "nombre": ruta['nombre'],
                "descripcion": ruta['descripcion'],
                "fecha_inicio": ruta['fecha_inicio'],
                "fecha_fin": ruta['fecha_fin'],
                "estado": ruta['estado']
            }
            rutas_seguimiento.append(ruta_info)

        return jsonify({"Status": "success", "data": rutas_seguimiento, "Msj": "Rutas obtenidas correctamente."})
    except Exception as e:
        return jsonify({"Status": "error", "data": [], "Msj": f"Error al obtener las rutas: {repr(e)}"})

# END RUTAS SEGUIMIENTO

#REGION TRANSACCIONES PASAJE
@homeClientes_bp.route("/obtenerDatosPasaje", methods=["GET"])
def obtenerDatosPasaje():
    try:
        numComprobante = request.args.get("comprobante")
        pasaje = Pasaje.obtenerDatosPasaje(numComprobante)
        if pasaje:
            return jsonify({
                "Status": "success",
                "data": pasaje,
                "Msj": "Datos del pasaje obtenidos correctamente"
            })
        else:
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": "No se encontró el pasaje con el número de comprobante proporcionado"
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "data": {},
            "Msj": f"Error al obtener los datos del pasaje: {repr(e)}"
        })

@homeClientes_bp.route("/cambiarEnTransaccion", methods=["GET"])
def cambiarEnTransaccion():
    id_pasaje = request.args.get("pasId")
    if not id_pasaje:
        return jsonify(status="error", message="Falta parámetro pasId"), 400

    try:
        resultado = Pasaje.cambiar_estado_transaccion(id_pasaje)
        if "error" in resultado:
            return jsonify(status="error", message=resultado["error"]), 404

        return jsonify(status="success", nuevoEstado=resultado["nuevoEstado"]), 200

    except Exception as e:
        return jsonify(status="error", message=str(e)), 500
        
@homeClientes_bp.route("/listarTiposComprobante")
def listadoTiposComprobantes():
    try:
        listado = TipoComprobante.obtener_todos()
        return listado
    except Exception as e:
        return [e]

@homeClientes_bp.route("/listadoMetodosPago")
def listadoMetodosPago():
    try:
        listado = MetodoPago.obtener_todos()
        return listado
    except Exception as e:
        return [e]

@homeClientes_bp.route('/reservarPasaje', methods=["POST"])
def reservarPasaje():
    try:
        id_detalle_asiento = int(request.form["id_detalle_asiento"])
        numero_comprobante   = request.form["numero_comprobante"]
        id_venta             = int(request.form["id_venta"])
        codigo               = request.form["codigo"]

        resultado = Pasaje.registrarReserva(
            id_detalle_asiento,
            numero_comprobante,
            id_venta,
            codigo
        )

        if resultado.get("msj"):
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado["msj2"]
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado["msj2"]
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": str(e),
            "Msj2": ""
        })
        
#END REGION

# REGION CONF_GENERAL

@homeClientes_bp.route("/GetConfGeneral")
def get_conf_general():
    try:
        result = ConfGeneral.obtener()
        
        # Convertir los valores a flotantes antes de devolverlos
        if result:
            result['igv'] = float(result['igv'])
            result['max_pasajes_venta'] = float(result['max_pasajes_venta'])
            result['precioPasajeLibre'] = float(result['precioPasajeLibre'])
            result['tiempo_maximo_venta_minutos'] = float(result['tiempo_maximo_venta_minutos'])
            result['precioCambioRuta'] = float(result['precioCambioRuta'])
            result['precioTransferencia'] = float(result['precioTransferencia'])
            result['viajesReprogramables'] = int(result['viajesReprogramables'])  # Puedes usar int si es un valor booleano 0/1
            result['horaTransaccion'] = int(result['horaTransaccion'])
            
        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Configuración general recuperada exitosamente'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al listar configuración general: {repr(e)}'})

# END REGION CONF_GENERAL


# REGION REEMBOLSO


@homeClientes_bp.route("/validarPasajeDadoBaja", methods=["POST"])
def validar_pasaje_dado_baja():
    try:
        numero_comprobante = request.json.get("numeroComprobante")
        if not numero_comprobante:
            return jsonify({"Status": "error", "Msj": "Número de comprobante es requerido"}), 400
        reembolso = Reembolso.validar_pasaje_dadoBaja(numero_comprobante)
        if reembolso:
            if (reembolso["estado_viaje"] == 0 or reembolso["fechaReprogramacion"] is not None):
                if reembolso["esReserva"] != 1:
                    return jsonify({"Status": "success", "data": reembolso, "Msj": "Pasaje validado correctamente"})
                else:
                    return jsonify({
                        "Status": "error",
                        "data": {},
                        "Msj": "No se cumple con las políticas de reembolso"
                    }), 400
            else:
                return jsonify({
                    "Status": "error",
                    "data": {},
                    "Msj": "No se cumple con las políticas de reembolso"
                }), 400
        else:
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": "Pasaje no encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "Status": "error",
            "data": {},
            "Msj": f"Error al validar el pasaje: {repr(e)}"
        }), 500

@homeClientes_bp.route("/registrarReembolso", methods=["POST"])
def registrar_reembolso():
    try:
        data = request.get_json()
        numero_comprobante = data.get("numeroComprobante")
        motivo = data.get("motivo") or "Reembolso solicitado"
        id_cliente = Cliente.obtener_id_por_numero_documento(data.get("numeroDoc"))
        id_pasaje = Pasaje.obtener_id_por_numComprobante(data.get("numeroComprobante"))
        id_pasaje = id_pasaje["id"]
        id_cliente= id_cliente["id"]
        id_metodo_pago = data.get("metodoPago")
        id_tipo_comprobante = data.get("tipoComprobante")
        monto= Pasaje.obtener_por_id(id_pasaje)
        # Validar campos requeridos
        if not all([numero_comprobante, id_cliente, id_metodo_pago, id_tipo_comprobante, id_pasaje]):
            return jsonify({"Status": "error", "Msj": "Faltan datos requeridos"}), 400

        # Aquí puedes calcular el monto dinámicamente si es necesario
        pasaje=Pasaje.obtener_por_id(id_pasaje)
        print(pasaje)
        monto = monto["precio"]  # ← cambiar si se requiere consultar de otra tabla
        resultado = Reembolso.registrar(
            numeroComprobante=numero_comprobante,
            monto=monto,
            idPasaje=id_pasaje,
            idCliente=id_cliente,
            idTipoComprobante=id_tipo_comprobante,
            idMetodoPago=id_metodo_pago
        )

        if resultado and resultado.get("@MSJ"):
            return jsonify({"Status": "success", "Msj": resultado["@MSJ"]})
        else:
            return jsonify({"Status": "error", "Msj": resultado.get("@MSJ2", "Error desconocido al registrar")})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error interno: {str(e)}"}), 500

@homeClientes_bp.route("/validarSolicitudReembolso", methods=["POST"])
def validar_solicitud_reembolso():
    try:
        numero_comprobante = request.json.get("numeroComprobante")
        solicitud=Pasaje.validar_solicitud_reembolso(numero_comprobante)
        if solicitud:
            return jsonify({"Status": "success", "Msj": "El pasaje tiene una solicitud de reembolso pendiente", "data": solicitud})
        else:
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": "Ya existe una solicitud de reembolso para este pasaje"
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "data": {},
            "Msj": f"Error al validar el pasaje: {repr(e)}"
        }), 500

import traceback

@homeClientes_bp.route('/enviar_correos_reprogramacion', methods=['POST'])
def enviar_correos_reprogramacio():
    try:
        data = request.get_json()
        email = Viaje.obtener_clientes_por_viaje(data.get("idViaje"))
        # email = Viaje.obtener_clientes_por_viaje(1)
        dias_reprogramacion = ConfGeneral.obtener()
        if not email:
            return jsonify({
                'status': 'error',
                'message': 'No se encontraron correos electrónicos para enviar la notificación.'
            }), 404
        dias_vigencia = str(dias_reprogramacion.get("max_dias_vigencia_reprogramacion", "X"))
        for datos in email:
            correo = datos.get("email")
            codigo = datos.get("codigo")
            asiento = datos.get("asiento")
            fecha_reprogramacion = datos.get("fecha_salida")
            if not correo or not codigo:
                print(f"[WARN] Datos incompletos: {datos}")
                continue
            fecha_formateada = fecha_reprogramacion.strftime("%d/%m/%Y")
            hora_formateada = fecha_reprogramacion.strftime("%H:%M")
            datosEnvio = {
                'asunto': 'Viaje reprogramado',
                'remitente': 'yatraxyatusa@gmail.com',
                'destinatario': correo,
                'mensaje': (
                    f"Estimado cliente, su viaje ha sido reprogramado para el dia {fecha_formateada} a las {hora_formateada}.\n"
                    f"Si no desea viajar en la fecha reprogramada, por favor solicite su reembolso en nuestro apartado de mi pasaje. \n"
                    f"Para más información visite nuestra página web.\n"
                    f"Su código de reembolso para el asiento {asiento} es: {codigo}"
                )
            }
            resultado = enviar_correo(current_app.extensions['mail'], datosEnvio)
            
        return jsonify({'status': 'ok'})
    except Exception as e:
        print("[ERROR] Excepción capturada en el controlador:")
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': 'Ocurrió un error interno.'}), 500
    
@homeClientes_bp.route('/enviar_correos_darBaja_Viaje', methods=['POST'])
def enviar_correos_DarBajaViaje():
    try:
        data = request.get_json()
        email = Viaje.obtener_clientes_por_viaje(data.get("idViaje"))
        # email = Viaje.obtener_clientes_por_viaje(1)
        if not email:
            return jsonify({
                'status': 'error',
                'message': 'No se encontraron correos electrónicos para enviar la notificación.'
            }), 404
        for datos in email:
            correo = datos.get("email")
            codigo = datos.get("codigo")
            asiento = datos.get("asiento")

            if not correo or not codigo:
                continue

            datosEnvio = {
                'asunto': 'Viaje cancelado',
                'remitente': 'yatraxyatusa@gmail.com',
                'destinatario': correo,
                'mensaje': (
                    f"Estimado cliente, su viaje ha sido cancelado. "
                    f"Por favor solicite su reembolso en nuestro apartado de mi pasaje. \n"
                    f"Para más información visite nuestra página web.\n"
                    f"Su código de reembolso para el asiento {asiento} es: {codigo}"
                )
            }
            resultado = enviar_correo(current_app.extensions['mail'], datosEnvio)
        return jsonify({'status': 'ok'})
    except Exception as e:
        print("[ERROR] Excepción capturada en el controlador:")
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': 'Ocurrió un error interno.'}), 500


# END REEMBOLSO

# REGION REPROGRAMACION

@homeClientes_bp.route("/getTiposMetodoPago")
def get_tipos_metodo_pago():
    conexion = bd.Conexion()
    try:
        tipos = conexion.obtener("SELECT idTipoMetodoPago AS id, nombre FROM tipo_metodopago")
        return jsonify({"Status": "success", "data": tipos})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": str(e)})
    finally:
        conexion.cerrar()


@homeClientes_bp.route("/get_metodos_pago_por_tipo/<int:id_tipo>", methods=["GET"])
def get_metodos_pago_por_tipo(id_tipo):
    try:
        metodos = bd.Conexion().obtener("""
            SELECT id, nombre FROM metodo_pago 
            WHERE id_tipo_metodoPago = %s AND LOWER(nombre) NOT LIKE '%%efectivo%%' AND estado = 1
        """, (id_tipo,))
        return jsonify({"Status": "success", "data": metodos})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": str(e)})


@homeClientes_bp.route("/validarCodigoReprogramacion", methods=["POST"])
def validar_codigo_reprogramacion():
    try:
        numero_comprobante = request.json.get("numeroComprobante")
        codigo = request.json.get("codigoReprogramacion")
        if not numero_comprobante or not codigo:
            return jsonify({"Status": "error", "Msj": "Número de comprobante y código son requeridos"}), 400
        reprogramacion = Pasaje.validar_codigo_reprogramacion(numero_comprobante, codigo)
        if reprogramacion:
            return jsonify({"Status": "success", "data": reprogramacion, "Msj": "Código de reprogramación validado correctamente"})
        else:
            return jsonify({"Status": "error", "data": {}, "Msj": "Código de reprogramación inválido"}), 400
    except Exception as e:
        return jsonify({"Status": "error", "data": {}, "Msj": f"Error al validar el código: {repr(e)}"}), 500

# END REPROGRAMACION

@homeClientes_bp.route("/descargar_ticket", methods=["POST"])
def descargar_ticket():
    try:
        from flask import send_file, abort
        import os
        
        nombre_archivo = request.form.get("nombre_archivo")
        if not nombre_archivo:
            abort(400, "Nombre de archivo requerido")
        
        # Validar que el archivo tenga extensión .pdf
        if not nombre_archivo.lower().endswith('.pdf'):
            nombre_archivo += '.pdf'
        
        # Construir la ruta del archivo
        ruta_archivo = os.path.join("Static", "tickets", nombre_archivo)
        
        # Verificar que el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"❌ Archivo no encontrado: {ruta_archivo}")
            abort(404, "Archivo no encontrado")
        
        print(f"✅ Enviando archivo: {ruta_archivo}")
        
        # Enviar el archivo
        return send_file(
            ruta_archivo,
            as_attachment=True,
            download_name=nombre_archivo,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"❌ Error en descarga de ticket: {repr(e)}")
        abort(500, f"Error al descargar archivo: {str(e)}")

@homeClientes_bp.route("/verificar_ticket/<nombre_archivo>")
def verificar_ticket(nombre_archivo):
    try:
        import os
        
        # Validar que el archivo tenga extensión .pdf
        if not nombre_archivo.lower().endswith('.pdf'):
            nombre_archivo += '.pdf'
        
        # Construir la ruta del archivo
        ruta_archivo = os.path.join("Static", "tickets", nombre_archivo)
        
        # Verificar que el archivo existe
        existe = os.path.exists(ruta_archivo)
        
        return jsonify({
            "Status": "success" if existe else "error",
            "existe": existe,
            "ruta": ruta_archivo,
            "nombre": nombre_archivo
        })
        
    except Exception as e:
        return jsonify({
            "Status": "error",
            "existe": False,
            "error": str(e)
        })