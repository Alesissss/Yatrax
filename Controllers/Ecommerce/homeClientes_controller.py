import hashlib
import os
import re
import random
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
from Models.metodo_pago import MetodoPago
from Models.tipoMetodoPago import TipoMetodoPago

homeClientes_bp = Blueprint('homeClientes', __name__, url_prefix='/ecommerce/home')

# FUNCIONES AUXILIARES
#REGION PROTOTIPO DE PRUEBA 
@homeClientes_bp.route('/registrar_venta', methods=['POST'])
def registrar_venta():
    data = request.json
    try:
        conn = bd.Conexion()
        cursor = conn.cursor()
        conn.autocommit = False

        # 1. Datos del cliente
        numero_documento = data['numero_documento']
        nombre = data['nombre']
        ape_paterno = data['ape_paterno']
        ape_materno = data['ape_materno']
        razon_social = data.get('razon_social')  # opcional
        sexo = data['sexo']
        f_nacimiento = data['f_nacimiento']
        direccion = data['direccion']
        telefono = data['telefono']
        email = data['email']
        password = data['password']
        estado = True
        id_pais =  1 #data['id_pais']
        id_tipo_cliente = data['id_tipo_cliente']
        id_tipo_doc = data['id_tipo_doc']
        usuario = data.get('usuario', 'sistema')

        # 2. Datos de la venta
        sub_total = data['subTotal']
        igv = 0.18 #data['igv']
        id_promocion = 1 #data['idPromocion']
        id_metodo_pago = data['idMetodoPago']
        id_tipo_comprobante = data['idTipoComprobante']

        # 3. Asiento y viaje
        id_asiento = data['idAsiento']
        id_detalle_viaje = data['idDetalleViaje']
        id_detalle_viaje_asiento = data['id_detalle_viaje_asiento']

        # Verificar que el asiento esté libre (estado = 0)
        cursor.execute("SELECT estado FROM asiento WHERE id = ?", id_asiento)
        estado = cursor.fetchone()
        if not estado or estado[0] != 0:
            return jsonify({'error': 'El asiento ya está ocupado o no existe'}), 400

        # Insertar cliente
        cursor.execute("INSERT INTO cliente (numero_documento, nombre, ape_paterno, ape_materno, razon_social, sexo, f_nacimiento, direccion, telefono, email, password, estado, id_pais, id_tipo_cliente, id_tipo_doc, usuario) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            numero_documento, nombre, ape_paterno, ape_materno, razon_social, sexo, f_nacimiento, direccion, telefono, email, password, estado, id_pais, id_tipo_cliente, id_tipo_doc, usuario)

        cursor.execute("SELECT @@IDENTITY")
        id_cliente = cursor.fetchone()[0]

        # Insertar venta
        cursor.execute("INSERT INTO venta (idCliente, subTotal, igv, idPromocion, idMetodoPago, idTipoComprobante) VALUES (?, ?, ?, ?, ?, ?)",
            id_cliente, sub_total, igv, id_promocion, id_metodo_pago, id_tipo_comprobante)
        cursor.execute("SELECT @@IDENTITY")
        id_venta = cursor.fetchone()[0]

        # Insertar pasaje
        cursor.execute("""
            INSERT INTO pasaje (
                idDetalleViajeAsiento, numeroComprobante,
                esPasajeNormal, esPasajeLibre, esTransferencia, esReserva, esCambioRuta,
                idVenta, codigo, idPasaje
            )
            VALUES (?, NULL, ?, ?, ?, ?, ?, ?, ?, NULL)
        """, id_detalle_viaje_asiento,
              1,  # esPasajeNormal
              0, 0, 0, 0,
              id_venta,
              "AA0001"  # código del pasaje, sugerido automatizar
        )

        # Insertar en detalle_viaje_asiento (marcar como no disponible)
        cursor.execute("INSERT INTO detalle_viaje_asiento (idDetalle_Viaje, idAsiento, esDisponible, usuario) VALUES (?, ?, 0, ?)",
            id_detalle_viaje, id_asiento, usuario)

        # Actualizar estado del asiento
        cursor.execute("UPDATE asiento SET estado = 1 WHERE id = ?", id_asiento)

        conn.commit()
        return jsonify({'mensaje': 'Venta registrada correctamente'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# END PROTOTIPO
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
    return render_template('Ecommerce/home/partials/ventaPasajes.html', herramientas = herramientas)


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
        "contenido_venta": renderizarCompra()
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
    print(f"Datos del pasajero: {datos_pasajero}")
    if not datos_pasajero:
        return jsonify(status="error", msg="Pasajero no encontrado"), 404

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
            id_cliente = request.form["id_cliente"]
            usuario = request.form["usuario"]
            id_pais = request.form["id_pais"]
            id_tipo_cliente = request.form["id_tipo_cliente"]
            razon_social = request.form["razon_social"]
            id_tipo_doc = request.form["id_tipo_doc"]
            numero_documento = request.form["numero_documento"]
            f_nacimiento = request.form["f_nacimiento"]
            nombres = request.form["nombres"]
            ape_paterno = request.form["ape_paterno"]
            ape_materno = request.form["ape_materno"]
            sexo = request.form["sexo"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            email = request.form["email"]
            password = request.form["password"]
            if password.strip():
                password_hash = hashlib.sha256(password.encode()).hexdigest()
            else:
                password_hash = None
            
            Cliente.actualizar_cliente(id_cliente,id_pais,id_tipo_cliente,id_tipo_doc,numero_documento,nombres,ape_paterno,ape_materno,sexo,f_nacimiento,razon_social,direccion,telefono,email,password_hash,usuario)

            return jsonify({"Status":1,"Mensaje":"Se ha actualizado los datos del cliente correctamente"})
        except Exception as e:
            return jsonify({"Status":0,"Mensaje":"Error: "+str(e)})


#Los HTML para recuperar contraseña del lado del cliente aun no existen
@homeClientes_bp.route("",methods=["GET","POST"])
def cambiarContrasena():
    if request.method == "GET":
        return render_template("Ecommerce/home/forgotPassword.html")
    else:
        email = request.form["correo"]
        respuesta = Cliente.verificar_correo_cliente(email)
        if respuesta == 1:
            return jsonify({"mensaje":"Correo valido, a continuación se enviará el código de verificación","status":1})
        else:
            return jsonify({"mensaje":"Correo no valido, vuelva a intentarlo","status":0})
            
# END POR TERMINAR
@homeClientes_bp.route('/forgotPass')
def forgot_password():
    return render_template('Ecommerce/home/forgotPassword.html')

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
    TipoDocumentos=TipoDocumento.obtener_todos()
    TipoMetodosPago = TipoMetodoPago.obtener_todos()
    MetodoPagos = MetodoPago.obtener_todos()
    TipoComprobantes = TipoComprobante.obtener_todos()
    return render_template('Ecommerce/home/miPasajeOp.html', datos=datos_recibidos, TipoDocumento=TipoDocumentos, TipoMetodosPago=TipoMetodosPago, MetodosPagos=MetodoPagos, TipoComprobantes=TipoComprobantes)

@homeClientes_bp.route('/seguimientoViaje')
def seguimiento_viaje():
    return render_template('Ecommerce/home/seguimientoViaje.html')

@homeClientes_bp.route('/pago')
def pago_pasajes():
    return render_template('Ecommerce/home/pago.html')

@homeClientes_bp.route('/terminosYcondiciones')
def terminos_y_condiciones():
    return render_template('Ecommerce/home/terminosCondiciones.html')

# END VIEWS

# FUNCIONES

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
    
# API NET RENIEC
# controller_clientes.py
@homeClientes_bp.route('/api/get_persona_data', methods=['GET'])
def get_persona_data():
    def responder(datos):
        if datos:
            print(datos)
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
        return jsonify([])

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
    return jsonify({
        "data": datos,
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
    
@homeClientes_bp.route("/procesar_pago", methods=["POST"])
def procesar_pago():
    try:
        data = request.get_json()

        contacto = data.get("contacto", {})
        pago = data.get("pago", {})
        ventas = data.get("ventas", {})

        resultado = Venta.registrar_operacion(contacto, pago, ventas)

        if resultado["status"] == 1:
            return jsonify({"Status": "success", "codigo_confirmacion": f"VENTA-{resultado['id_venta']}"})
        else:
            return jsonify({"Status": "error", "Msj": resultado["msg"]})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

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

        # Tu método devuelve {"msj": ..., "msj2": ...}
        if resultado.get("msj"):
            return jsonify({"Status":"success", "Msj": resultado["msj"]})
        else:
            return jsonify({"Status":"error",   "Msj": resultado.get("msj2", "Error desconocido")})

    except Exception as e:
        return jsonify({"Status":"error", "Msj": f"Error inesperado: {e}"})
    
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
        print (pasaje)
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
    try:
        numComprobante = request.args.get("comprobante")
        pasaje = Pasaje.obtenerDatosPasaje(numComprobante)
        if pasaje:
            if pasaje['estado_transaccion'] == 1:
                Pasaje.cambiar_a_transaccion_0(numComprobante)
            else:
                Pasaje.cambiar_a_transaccion_1(numComprobante)
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
            "Msj": f"Error al cambiar el estado del pasaje: {repr(e)}"
        })
        

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
            result['tarifaBase'] = float(result['tarifaBase'])
            result['tiempo_maximo_venta_minutos'] = float(result['tiempo_maximo_venta_minutos'])
            result['precioCambioRuta'] = float(result['precioCambioRuta'])
            result['precioTransferencia'] = float(result['precioTransferencia'])
            result['viajesReprogramables'] = int(result['viajesReprogramables'])  # Puedes usar int si es un valor booleano 0/1
        
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
            if reembolso["estado_viaje"] == 0 or reembolso["fechaInicioReprogramacion"] is not None or reembolso["fechaFinReprogramacion"] is not None:
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

        # Validar campos requeridos
        if not all([numero_comprobante, id_cliente, id_metodo_pago, id_tipo_comprobante, id_pasaje]):
            return jsonify({"Status": "error", "Msj": "Faltan datos requeridos"}), 400

        # Aquí puedes calcular el monto dinámicamente si es necesario
        pasaje=Pasaje.obtener_por_id(id_pasaje)
        print(pasaje)
        monto = 25.00  # ← cambiar si se requiere consultar de otra tabla
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

# END REEMBOLSO

# REGION REPROGRAMACION

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


# END REPROGRAMACION