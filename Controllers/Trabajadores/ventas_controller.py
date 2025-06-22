import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort, json
from xml.etree import ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from werkzeug.utils import secure_filename
from Models.tipoCliente import TipoCliente
from Models.microservicio import MicroServicio
from Models.servicio import Servicio
from Models.tipoComprobante import TipoComprobante
from Models.tipoDocumento import TipoDocumento
from Models.cliente import Cliente
from Models.pais import Pais
from Models.pasaje import Pasaje
from Models.herramienta import Herramienta

ventas_bp = Blueprint('ventas', __name__, url_prefix='/trabajadores/ventas')

# RESTRICCIONES
@ventas_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 3 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_VENTAS' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS

# AUXILIARES

def renderizarCompra():
    herramientas = Herramienta.obtener_todos()
    return render_template('Ecommerce/home/partials/ventaPasajes.html', herramientas = herramientas)

@ventas_bp.route('/renderizar_itinerario', methods=['POST'])
def renderizar_itinerario():
    data = request.get_json()
    itinerarios = data.get('itinerarios', [])
    sufijo = data.get('sufijo')
    # Renderiza el HTML del itinerario con Jinja
    html_renderizado = render_template('Ecommerce/home/partials/itinerario.html', itinerarios=itinerarios, sufijo = sufijo)
    return jsonify({'html': html_renderizado})

# END AUXILIARES

@ventas_bp.route('/GestionarTipoCliente')
def Menu_TipoClientes():
    return render_template('ventas/tipocliente.html', active_page="tipoCliente", active_menu='mVentas')

@ventas_bp.route('/TipoClienteNuevo')
def TipoCliente_Nuevo():
    return render_template('ventas/tipoclienteCRUD.html', active_page="tipoCliente", active_menu='mVentas', tipocliente = {}, tittle = 'Registrar tipo cliente', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarTipoComprobante')
def Menu_TipoComprobante():
    return render_template('ventas/tipocomprobante.html', active_page="tipoComprobante", active_menu='mVentas')

@ventas_bp.route('/TipoComprobanteNuevo')
def TipoComprobante_Nuevo():
    return render_template('ventas/tipoComprobanteCRUD.html', active_page="tipoComprobante", active_menu='mVentas', tipocomprobante = {}, tittle = 'Registrar tipo comprobante', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarMicroservicios')
def Menu_Microservicio():
    return render_template('ventas/microservicio.html', active_page="microservicio", active_menu = 'mVentas')

@ventas_bp.route('/GestionarServicio')
def Menu_Servicio():
    return render_template('ventas/servicio.html', active_page="servicio", active_menu = 'mVentas')

@ventas_bp.route('/GestionarClientes')
def Menu_Clientes():
    return render_template('ventas/cliente.html', active_page="cliente", active_menu='mVentas')

@ventas_bp.route('/ClienteNuevo')
def Cliente_Nuevo():
    return render_template('ventas/clienteCRUD.html', active_page="cliente", active_menu='mVentas', cliente = {}, tittle = 'Registrar cliente', btnId = 'btn_Registrar')

@ventas_bp.route('/MicroservicioNuevo')
def Microservicio_Nuevo():
    return render_template('ventas/microservicioCRUD.html', active_page="microservicio", active_menu = 'mVentas', microservicio = {}, tittle = 'Registrar microservicio', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarTipoDocumento')
def Menu_TipoDocumento():
    return render_template('ventas/tipoDocumento.html', active_page="tipoDocumento", active_menu = 'mVentas')

@ventas_bp.route('/TipoDocumentoNuevo')
def TipoDocumento_Nuevo():
    return render_template('ventas/tipoDocumentoCRUD.html', active_page="tipoDocumento", active_menu = 'mVentas', tipoDocumento = {}, tittle = 'Registrar tipo documento', btnId = 'btn_Registrar')

@ventas_bp.route('/VenderPasajes')
def Menu_VenderPasajes():
    return render_template('ventas/pasajes.html', active_page="venderPasajes", active_menu='mVentas')

@ventas_bp.route('/VenderPasajesNuevo')
def VenderPasajes_Nuevo():
    datos_recibidos = {
        "contenido_venta": renderizarCompra()
    }
    return render_template('ventas/pasajesCRUD.html', active_page="venderPasajes", active_menu='mVentas', pasaje = {}, tittle = 'Registrar pasaje', btnId = 'btn_Registrar',datos=datos_recibidos)

@ventas_bp.route('/TransaccionesPasajes')
def Menu_TransaccionesPasajes():
    return render_template('ventas/pasajesTransacciones.html', active_page="transaccionesPasajes", active_menu='mVentas')

@ventas_bp.route('/TransaccionesPasajesNuevo')
def TransaccionesPasajes_Nuevo():
    return render_template('ventas/pasajesTransaccionesCRUD.html', active_page="transaccionesPasajes", active_menu='mVentas', transaccion = {}, tittle = 'Registrar transacción de pasajes', btnId = 'btn_Registrar')

@ventas_bp.route('/cambioRuta')
def cambio_ruta():
    return render_template('ventas/cambioRuta.html', active_page="cambioRuta", active_menu="home")

@ventas_bp.route('/cambioRutaNuevo')
def cambio_ruta_nuevo():
    return render_template('ventas/cambioRutaCRUD.html', active_page="cambioRutaNuevo", active_menu="home", cambioRuta = {}, tittle = 'Registrar cambio de ruta', btnId = 'btn_Registrar')



# END VIEWS

# FUNCIONES



## REGIÓN CAMBIO DE RUTA ##

@ventas_bp.route('/GetDataCambioRuta', methods=['GET'])
def get_data_cambio_ruta():
    try:
        cambioRuta =  Pasaje.obtener_todos_cambiados_ruta()
        if cambioRuta:
            return jsonify({'data': cambioRuta, 'Status': 'success', 'Msj': 'Datos obtenidos correctamente.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': 'Ocurrió un error al obtener los datos de cambio de ruta.'})
    
##@ventas_bp.route('/RegistrarCambioRuta', methods=['POST'])
##def registrar_cambio_ruta():


## END REGIÓN CAMBIO DE RUTA ##



# REGION TIPO CLIENTE #

@ventas_bp.route("/GetData_TipoCliente", methods=["GET"])
def get_tipo_cliente():
    try:
        tipos = TipoCliente.obtener_todos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de cliente retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de cliente: {repr(e)}'})
    
@ventas_bp.route("/GetData_Paises", methods=["GET"])
def get_paises():
    try:
        paises = Pais.obtener_todos()
        return jsonify({'data': paises, 'Status': 'success', 'Msj': 'Listado de países retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de cliente: {repr(e)}'})
    
@ventas_bp.route("/RegistrarTipoCliente", methods=["POST"])
def registrar_tipo_cliente():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()


        if not nombre:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoCliente.registrar(nombre, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar tipo de cliente"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/EditarTipoCliente/<int:id>", methods=['GET','POST'])
def editar_tipo_cliente(id):
    try:
        tipoCliente = TipoCliente.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado").strip()

            if not nombre or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            mensajes = TipoCliente.editar(id, nombre, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar tipo de cliente"})
        if TipoCliente:
            return render_template('ventas/tipoclienteCRUD.html', active_page = 'tipoCliente', active_menu = 'mVentas', tipocliente = tipoCliente, tittle = 'Editar tipo cliente', btnId = 'btn_Editar')
        return render_template('ventas/tipoclienteCRUD.html', active_page = 'tipoCliente', active_menu = 'mVentas', tipoCliente = {}, tittle = 'Editar tipo cliente', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/DarBajaTipoCliente/<int:id>", methods=["POST"])
def dar_baja_tipo_cliente(id):
    try:
        mensajes = TipoCliente.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al dar de baja tipo de cliente"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/VerTipoCliente/<int:id>", methods=["GET"])
def ver_tipo_cliente(id):
    try:
        tipo_cliente = TipoCliente.obtener_por_id(id)
        if tipo_cliente:
            return render_template("ventas/tipoClienteCRUD.html", active_page="tipoCliente", active_menu='mVentas', tipocliente=tipo_cliente, tittle='Ver tipo cliente', btnId='btn_Aceptar')
        return render_template("ventas/tipoClienteCRUD.html", active_page="tipoCliente", active_menu='mVentas', tipo_cliente={}, tittle='Ver tipo cliente', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@ventas_bp.route("/EliminarTipoCliente/<int:id>", methods=['POST'])
def eliminar_tipo_cliente(id):
    try:
        mensajes = TipoCliente.eliminar_tipo_cliente(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
    except Exception as e:
        return jsonify({"Status": "Error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO CLIENTE #

# REGION TIPO COMPROBANTE #

@ventas_bp.route("/GetData_TipoComprobante", methods=["GET"])
def get_tipo_comprobante():
    try:
        tipos = TipoComprobante.obtener_todos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de comprobante retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de comprobante: {repr(e)}'})
    
@ventas_bp.route("/RegistrarTipoComprobante", methods=["POST"])
def registrar_tipo_comprobante():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()


        if not nombre:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoComprobante.registrar(nombre, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar tipo de comprobante"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/EditarTipoComprobante/<int:id>", methods=['GET','POST'])
def editar_tipo_comprobante(id):
    try:
        tipoComprobante =  TipoComprobante.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado").strip()

            if not nombre or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            mensajes = TipoComprobante.editar(id, nombre, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar tipo de comprobante"})
        if TipoCliente:
            return render_template('ventas/tipocomprobanteCRUD.html', active_page = 'tipoComprobante', active_menu = 'mVentas', tipocomprobante = tipoComprobante, tittle = 'Editar tipo comprobante', btnId = 'btn_Editar')
        return render_template('ventas/tipocomprobante.html', active_page = 'tipoComprobante', active_menu = 'mVentas', tipoComprobante = {}, tittle = 'Editar tipo comprobante', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/DarBajaTipoComprobante/<int:id>", methods=["POST"])
def dar_baja_tipo_comprobante(id):
    try:
        mensajes = TipoComprobante.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al dar de baja tipo de comprobante"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/VerTipoComprobante/<int:id>", methods=["GET"])
def ver_tipo_comprobante(id):
    try:
        tipo_comprobante = TipoComprobante.obtener_por_id(id)
        if tipo_comprobante:
            return render_template("ventas/tipoComprobanteCRUD.html", active_page="tipoComprobante", active_menu='mVentas', tipocomprobante=tipo_comprobante, tittle='Ver tipo comprobante', btnId='btn_Aceptar')
        return render_template("ventas/tipoComprobanteCRUD.html", active_page="tipoComprobante", active_menu='mVentas', tipo_comprobante={}, tittle='Ver tipo comprobante', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@ventas_bp.route("/EliminarTipoComprobante/<int:id>", methods=['POST'])
def eliminar_tipo_comprobante(id):
    try:
        mensajes = TipoComprobante.eliminar_tipo_comprobante(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
    except Exception as e:
        return jsonify({"Status": "Error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO COMPROBANTE #

# REGION MICROSERVICIO #

@ventas_bp.route("/GetData_Microservicios", methods=["GET"])
def get_microservicios():
    try:
        microservicios = MicroServicio.obtener_todos()
        return jsonify({'data': microservicios, 'Status': 'success', 'Msj': 'Listado de microservicios retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar microservicios: {repr(e)}'})
    
@ventas_bp.route("/RegistrarMicroservicio", methods=["POST"])
def registrar_microservicio():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        descripcion = request.form.get("descripcion").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        if not nombre or not descripcion or not estado:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = MicroServicio.registrar(nombre, descripcion, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar microservicio"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/EditarMicroservicio/<int:id>", methods=['GET','POST'])
def editar_microservicio(id):
    try:
        microservicio =  MicroServicio.obtener_uno(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            descripcion = request.form.get("descripcion").strip()
            estado = request.form.get("estado").strip()

            if not nombre or not descripcion or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            mensajes = MicroServicio.editar(id, nombre, descripcion, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar microservicio"})
            
        if TipoCliente:
            return render_template('ventas/microservicioCRUD.html', active_page = 'microservicio', active_menu = 'mVentas', microservicio = microservicio, tittle = 'Editar microservicio', btnId = 'btn_Editar')
        return render_template('ventas/microservicio.html', active_page = 'microservicio', active_menu = 'mVentas', microservicio = {}, tittle = 'Editar microservicio', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/DarBajaMicroservicio/<int:id>", methods=["POST"])
def dar_baja_microservicio(id):
    try:
        mensajes = MicroServicio.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al dar de baja al microservicio"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/VerMicroservicio/<int:id>", methods=["GET"])
def ver_microservicio(id):
    try:
        microservicio = MicroServicio.obtener_uno(id)
        if microservicio:
            return render_template("ventas/microservicioCRUD.html", active_page="microservicio", active_menu='mVentas', microservicio=microservicio, tittle='Ver microservicio', btnId='btn_Aceptar')
        return render_template("ventas/microservicioCRUD.html", active_page="microservicio", active_menu='mVentas', microservicio={}, tittle='Ver microservicio', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@ventas_bp.route("/EliminarMicroservicio/<int:id>", methods=['POST'])
def eliminar_microservicio(id):
    try:
        mensajes = MicroServicio.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al eliminar microservicio"})
    except Exception as e:
        return jsonify({"Status": "Error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION MICROSERVICIO #

# REGION SERVICIO

@ventas_bp.route("/GetData_Servicio")
def get_servicios():
    try:
        servicios = Servicio.obtener_todos()
        return jsonify({
            'data': servicios,
            'Status': 'success',
            'Msj': 'Listado de servicios retornado exitosamente'
        })
    except Exception as e:
        return jsonify({
            'data': [],
            'Status': 'error',
            'Msj': f'Ocurrió un error al listar los servicios: {repr(e)}'
        })

@ventas_bp.route("/Get_Microservicios_Servicio", methods=["GET"])
def get_microserviicos_servicio():
    try:
        microservicios = MicroServicio.obtener_todos()
        result = [m for m in microservicios if (m.get('estado') == 1)]
        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de microservicios retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar microservicios: {repr(e)}'})


def extension_valida(nombre_archivo):
    EXTENSIONES_PERMITIDAS = {'jpg', 'jpeg', 'png'}
    return '.' in nombre_archivo and \
           nombre_archivo.rsplit('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS

@ventas_bp.route('/registrarServicio', methods=["GET", "POST"])
def nuevo_servicio():
    if request.method == "GET":
        return render_template(
            "ventas/servicioCRUD.html",
            tittle="Nuevo servicio",
            servicio={},
            microservicios=[],
            btnId="btn_Registrar",
            active_page="servicio",
            active_menu='mVentas'
        )
    else:
        try:
            UPLOAD_FOLDER = "Static/img/servicios/"
            nombre = request.form.get('nombre').strip()
            descripcion = request.form.get('descripcion').strip()
            estado = request.form.get('estado')
            microservicios_json = request.form.get("microservicios")
            microservicios = json.loads(microservicios_json) if microservicios_json else []
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            imagen_file = request.files.get('imagen')
            imagen_path = ''

            if imagen_file and imagen_file.filename:
                if not extension_valida(imagen_file.filename):
                    return jsonify({"Status": "error", "Msj": "Formato de imagen no permitido. Solo JPG y PNG."})

                nombre_archivo = secure_filename(imagen_file.filename)
                ruta_imagen = f"/{UPLOAD_FOLDER}{nombre_archivo}"
                ruta_guardado = os.path.join(UPLOAD_FOLDER, nombre_archivo)
                imagen_file.save(ruta_guardado)
                imagen_path = ruta_guardado

            mensajes = Servicio.registrar(nombre, descripcion, estado, usuario_actual, ruta_imagen, microservicios)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar servicio'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@ventas_bp.route("/verServicio/<int:idServicio>")
def ver_servicio(idServicio):
    servicio = Servicio.obtener_uno(idServicio)
    microservicios = Servicio.obtener_micros_por_servicio(idServicio)
    return render_template(
        "ventas/servicioCRUD.html",
        tittle="Ver servicio",
        servicio=servicio if servicio else {},
        microservicios=microservicios if microservicios else [],
        btnId="btn_Regresar",
        active_page="servicio",
        active_menu='mVentas'
    )

@ventas_bp.route("/editarServicio/<int:idServicio>", methods=["GET", "POST"])
def editar_servicio(idServicio):
    if request.method == "GET":
        servicio = Servicio.obtener_uno(idServicio)
        microservicios = Servicio.obtener_micros_por_servicio(idServicio)
        return render_template(
            "ventas/servicioCRUD.html",
            tittle="Editar servicio",
            servicio=servicio if servicio else {},
            microservicios=microservicios if microservicios else [],
            btnId="btn_Actualizar",
            active_page="servicio",
            active_menu='mVentas'
        )
    else:
        try:
            UPLOAD_FOLDER = "Static/img/servicios/"
            nombre = request.form.get('nombre').strip()
            descripcion = request.form.get('descripcion').strip()
            estado = request.form.get('estado')
            microservicios_json = request.form.get("microservicios")
            microservicios = json.loads(microservicios_json) if microservicios_json else []
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            imagen_file = request.files.get('imagen')
            imagen_path = ''

            if imagen_file and imagen_file.filename:
                if not extension_valida(imagen_file.filename):
                    return jsonify({"Status": "error", "Msj": "Formato de imagen no permitido. Solo JPG y PNG."})

                nombre_archivo = secure_filename(imagen_file.filename)
                ruta_imagen = f"/{UPLOAD_FOLDER}{nombre_archivo}"
                ruta_guardado = os.path.join(UPLOAD_FOLDER, nombre_archivo)
                imagen_file.save(ruta_guardado)
                imagen_path = ruta_guardado
            else:
                servicio = Servicio.obtener_uno(idServicio)
                ruta_imagen = servicio.get("imagen", "")

            mensajes = Servicio.editar(idServicio, nombre, descripcion, estado, ruta_imagen, usuario_actual, microservicios)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar el servicio'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@ventas_bp.route("/DarBajaServicio/<int:idServicio>", methods=["POST"])
def dar_baja_servicio(idServicio):
    try:
        mensajes = Servicio.darBaja(idServicio)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja servicio'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@ventas_bp.route("/eliminarServicio/<int:idServicio>", methods=["POST"])
def eliminar_servicio(idServicio):
    try:
        mensajes = Servicio.eliminar(idServicio)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar servicio'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION SERVICIO

# REGION TIPO DOCUMENTO #
@ventas_bp.route("/GetData_TipoDocumento", methods=["GET"])
def get_tipo_documento():
    try:
        tipos = TipoDocumento.obtener_todos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de documentos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de documentos: {repr(e)}'})

@ventas_bp.route("/RegistrarTipoDocumento", methods=["POST"])
def registrar_tipo_documento():
    try:
        nombre = request.form.get("nombre").strip()
        abreviatura = request.form.get("abreviatura").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()


        if not nombre or not abreviatura:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoDocumento.registrar(nombre, abreviatura, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar tipo de documento"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
    
@ventas_bp.route("/EditarTipoDocumento/<int:id>", methods=['GET','POST'])
def editar_tipo_documento(id):
    try:
        tipoDocumento =  TipoDocumento.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            abreviatura = request.form.get("abreviatura").strip()
            estado = request.form.get("estado").strip()

            if not nombre or  not abreviatura or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            mensajes = TipoDocumento.editar(id, nombre, abreviatura, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar tipo de documento"})
        if tipoDocumento:
            return render_template('ventas/tipoDocumentoCRUD.html', active_page = 'tipoDocumento', active_menu = 'mVentas', tipoDocumento = tipoDocumento, tittle = 'Editar tipo documento', btnId = 'btn_Editar')
        return render_template('ventas/tipoDocumento.html', active_page = 'tipoDocumento', active_menu = 'mVentas', tipoDocumento = {}, tittle = 'Editar tipo documento', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
    
@ventas_bp.route("/DarBajaTipoDocumento/<int:id>", methods=["POST"])
def dar_baja_tipo_documento(id):
    try:
        mensajes = TipoDocumento.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al dar de baja tipo de documento"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
    
@ventas_bp.route("/VerTipoDocumento/<int:id>", methods=["GET"])
def ver_tipo_documento(id):
    try:
        tipoDocumento = TipoDocumento.obtener_por_id(id)
        if tipoDocumento:
            return render_template("ventas/tipoDocumentoCRUD.html", active_page="tipo_documento", active_menu='mVentas', tipoDocumento=tipoDocumento, tittle='Ver tipo documento', btnId='btn_Aceptar')
        return render_template("ventas/tipoDocumentoCRUD.html", active_page="tipo_documento", active_menu='mVentas', tipoDocumento={}, tittle='Ver tipo documento', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
    
@ventas_bp.route("/EliminarTipoDocumento/<int:id>", methods=['POST'])
def eliminar_tipo_documento(id):
    try:
        mensajes = TipoDocumento.eliminar_tipo_documento(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
    except Exception as e:
        return jsonify({"Status": "Error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO DOCUMENTO #

# REGION CLIENTE
@ventas_bp.route('/GetData_Cliente', methods=['GET'])
def get_cliente():
    try:
        tipo_doc = request.args.get('tipo_doc').strip()  # Obtener el tipo de documento del query string
        print(f"Tipo de documento recibido: {tipo_doc}")  # Para depuración
        clientes = Cliente.obtener_todos(tipo_doc)
        if not clientes:
            return jsonify({'data': [], 'Status': 'success', 'Msj': 'No se encontraron clientes'})
        return jsonify({'data': clientes, 'Status': 'success', 'Msj': 'Listado de clientes retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar clientes: {repr(e)}'})

@ventas_bp.route("/RegistrarCliente", methods=["POST"])
def registrar_cliente():
    try:
        tipo_documento = request.form.get("tipo_documento", "").strip()
        numero_documento = request.form.get("numero_documento", "").strip()
        pais = request.form.get("pais", "").strip()
        sexo = request.form.get("Sexo", "").strip()
        ape_pat = request.form.get("ape_pat", "").strip()
        ape_mat = request.form.get("ape_mat", "").strip()
        nombre = request.form.get("nombre", "").strip()
        fecha_nac = request.form.get("fecha_nac", "").strip()
        telefono = request.form.get("telefono", "").strip()
        correo = request.form.get("correo", "").strip()
        contrasena = request.form.get("contraseña", "").strip()
        direccion = request.form.get("direccion", "").strip()
        estado = request.form.get("estado").strip()  # Asignar estado por defecto a 1 (activo)
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Cliente.registrar(pais, tipo_documento, 3, numero_documento, nombre, ape_pat, ape_mat, sexo, fecha_nac, direccion, telefono, correo, contrasena, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar cliente'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@ventas_bp.route("/EliminarCliente/<int:id>", methods=['POST'])
def eliminar_cliente(id):  # Recibe el ID de la URL
    try:
        mensajes = Cliente.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar tipo de usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@ventas_bp.route("/EditarCliente/<int:id>", methods=['GET', 'POST'])
def editar_cliente(id):
    try:
        cliente = Cliente.obtener_por_id(id)

        if request.method == 'POST':
            tipo_documento = request.form.get("tipo_documento", "").strip()
            numero_documento = request.form.get("numero_documento", "").strip()
            pais = request.form.get("pais", "").strip()
            sexo = request.form.get("Sexo", "").strip()
            ape_pat = request.form.get("ape_pat", "").strip()
            ape_mat = request.form.get("ape_mat", "").strip()
            nombre = request.form.get("nombre", "").strip()
            fecha_nac = request.form.get("fecha_nac", "").strip()
            telefono = request.form.get("telefono", "").strip()
            direccion = request.form.get("direccion", "").strip()
            estado = request.form.get("estado").strip()  # Asignar estado por defecto a 1 (activo)
            email = request.form.get("correo", "").strip()
            password = request.form.get("contraseña", "").strip()
            tipo_cliente = 3  # si lo estás fijando manualmente
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            mensajes = Cliente.actualizar_cliente(id, pais, tipo_cliente, tipo_documento, numero_documento, nombre, ape_pat, ape_mat, sexo, fecha_nac, direccion, telefono, email, password, estado, usuario_actual)
            print(f"Mensajes de actualización de cliente: {sexo}")            
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar cliente'})

        if cliente:
            return render_template('ventas/clienteCRUD.html', active_page="cliente", active_menu='mVentas', cliente=cliente, tittle='Editar cliente', btnId='btn_Editar')
        return render_template('ventas/clienteCRUD.html', active_page="cliente", active_menu='mVentas', cliente={}, tittle='Editar cliente', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@ventas_bp.route("/VerCliente/<int:id>", methods=['GET'])
def ver_cliente(id):
    try:
        cliente = Cliente.obtener_por_id(id)
        if cliente:
            print(cliente)
            return render_template('ventas/clienteCRUD.html', active_page="cliente", active_menu='mVentas', cliente=cliente, tittle = 'Ver cliente', btnId = 'btn_Aceptar')
        return render_template('ventas/clienteCRUD.html', active_page="cliente", active_menu='mVentas', cliente={}, tittle = 'Ver cliente', btnId = 'btn_Aceptar')        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

    
@ventas_bp.route("/DarBajaCliente/<int:id>", methods=['POST'])
def dar_baja_cliente(id):  # Recibe el ID de la URL
    try:
        mensajes = Cliente.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al cliente'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION CLIENTE 

# REGION PASAJES Y OPRERACIONES

# END REGION PASAJES Y OPRERACIONES

@ventas_bp.route("/registrar_comprobantes_y_generar_xml", methods=["POST"])
def registrar_comprobantes_y_generar_xml():
    rutas_xml = []

    ultimaVenta = Pasaje.obtener_ultima_venta()
    if not ultimaVenta:
        return []

    idVenta = ultimaVenta.get('numero')
    comprobantes = Pasaje.obtener_numComprobante_venta(idVenta)

    for comprobante in comprobantes:
        numero = comprobante.get('numeroComprobante')
        if numero:
            data = Pasaje.obtenerDatosPasaje(numero)
            ruta_xml = Pasaje.generar_xml_comprobante(data)
            rutas_xml.append(ruta_xml)

    return rutas_xml

@ventas_bp.route("/generar_comprobante_pdf", methods=["POST"])
def generar_comprobante_pdf():
    rutas_pdf = []
    rutas_xml = registrar_comprobantes_y_generar_xml()

    for ruta_xml in rutas_xml:
        ruta_pdf = Pasaje.generar_pdf_desde_xml(ruta_xml)
        rutas_pdf.append(ruta_pdf)

    return rutas_pdf


# END FUNCIONES