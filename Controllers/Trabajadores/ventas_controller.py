import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.tipoCliente import TipoCliente
from Models.tipoServicio import TipoServicio
from Models.tipoComprobante import TipoComprobante
from Models.tipoDocumento import TipoDocumento

ventas_bp = Blueprint('ventas', __name__, url_prefix='/trabajadores/ventas')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@ventas_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@ventas_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@ventas_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@ventas_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@ventas_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

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

@ventas_bp.route('/GestionarTipoCliente')
def Menu_TipoClientes():
    return render_template('ventas/tipocliente.html', active_page="tipoCliente", active_menu='mVentas')

@ventas_bp.route('/TipoClienteNuevo')
def TipoCliente_Nuevo():
    return render_template('ventas/tipoclienteCRUD.html', active_page="tipoCliente", active_menu='mVentas', tipocliente = {}, tittle = 'Registrar Tipo Cliente', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarTipoComprobante')
def Menu_TipoComprobante():
    return render_template('ventas/tipocomprobante.html', active_page="tipoComprobante", active_menu='mVentas')

@ventas_bp.route('/TipoComprobanteNuevo')
def TipoComprobante_Nuevo():
    return render_template('ventas/tipoComprobanteCRUD.html', active_page="tipoComprobante", active_menu='mVentas', tipocomprobante = {}, tittle = 'Registrar Tipo Comprobante', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarTipoServicio')
def Menu_TipoServicio():
    return render_template('ventas/tiposervicio.html', active_page="tipoServicio", active_menu = 'mVentas')

@ventas_bp.route('/TipoServicioNuevo')
def Menu_TipoServicioNuevo():
    return render_template('ventas/tiposervicioCRUD.html', active_page="tipoServicio", active_menu = 'mVentas', tiposervicio = {}, tittle = 'Registrar Tipo Servicio', btnId = 'btn_Registrar')

@ventas_bp.route('/GestionarTipoDocumento')
def Menu_TipoDocumento():
    return render_template('ventas/tipoDocumento.html', active_page="tipoDocumento", active_menu = 'mVentas')

@ventas_bp.route('/TipoDocumentoNuevo')
def Menu_TipoDocumentoNuevo():
    return render_template('ventas/tipoDocumentoCRUD.html', active_page="tipoDocumento", active_menu = 'mVentas', tipoDocumento = {}, tittle = 'Registrar Tipo Documento', btnId = 'btn_Registrar')
# END VIEWS

# FUNCIONES

# REGION TIPO CLIENTE #

@ventas_bp.route("/GetData_TipoCliente", methods=["GET"])
def get_tipo_cliente():
    try:
        tipos = TipoCliente.obtener_todos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de cliente retornado exitosamente'})
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

# REGION TIPO SERVICIO #

@ventas_bp.route("/GetData_TipoServicio", methods=["GET"])
def get_tipo_servicio():
    try:
        tipos = TipoServicio.obtener_todos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de servicios retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de servicio: {repr(e)}'})
    
@ventas_bp.route("/RegistrarTipoServicio", methods=["POST"])
def registrar_tipo_servicio():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        descripcion = request.form.get("descripcion").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()


        if not nombre:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoServicio.registrar(nombre, descripcion, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar tipo de servicio"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/EditarTipoServicio/<int:id>", methods=['GET','POST'])
def editar_tipo_servicio(id):
    try:
        tipoServicio =  TipoServicio.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            descripcion = request.form.get("descripcion").strip()
            estado = request.form.get("estado").strip()

            if not nombre or descripcion or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            mensajes = TipoServicio.editar(id, nombre, descripcion, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar tipo de servicio"})
        if TipoCliente:
            return render_template('ventas/tipoServicioCRUD.html', active_page = 'tipoServicio', active_menu = 'mVentas', tipoServicio = tipoServicio, tittle = 'Editar tipo servicio', btnId = 'btn_Editar')
        return render_template('ventas/tipoServicio.html', active_page = 'tipoServicio', active_menu = 'mVentas', tipoServicio = {}, tittle = 'Editar tipo servicio', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/DarBajaTipoServicio/<int:id>", methods=["POST"])
def dar_baja_tipo_servicio(id):
    try:
        mensajes = TipoServicio.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al dar de baja tipo de servicio"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/VerTipoServicio/<int:id>", methods=["GET"])
def ver_tipo_servicio(id):
    try:
        tipo_servicio = TipoServicio.obtener_por_id(id)
        if tipo_servicio:
            return render_template("ventas/tipoServicioCRUD.html", active_page="tipoServicio", active_menu='mVentas', tipo_servicio=tipo_servicio, tittle='Ver tipo servicio', btnId='btn_Aceptar')
        return render_template("ventas/tipoServicioCRUD.html", active_page="tipoServicio", active_menu='mVentas', tipo_servicio={}, tittle='Ver tipo servicio', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@ventas_bp.route("/EliminarTipoServicio/<int:id>", methods=['POST'])
def eliminar_tipo_servicio(id):
    try:
        mensajes = TipoServicio.eliminar_tipo_servicio(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
    except Exception as e:
        return jsonify({"Status": "Error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO SERVICIO #

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
        tipo_documento = TipoDocumento.obtener_por_id(id)
        if tipo_documento:
            return render_template("ventas/tipoDocumentoCRUD.html", active_page="tipo_documento", active_menu='mVentas', tipo_documento=tipo_documento, tittle='Ver tipo documento', btnId='btn_Aceptar')
        return render_template("ventas/tipoDocumentoCRUD.html", active_page="tipo_documento", active_menu='mVentas', tipo_documento={}, tittle='Ver tipo documento', btnId='btn_Aceptar')
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

# END FUNCIONES