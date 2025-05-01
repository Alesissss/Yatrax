import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.tipoCliente import TipoCliente

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

    if not any(menu['nombre'] == 'M_VENTAS' for menu in menus) and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@ventas_bp.route('/GestionarPasajes')
def Menu_Pasajes():
    return render_template('ventas/pasajes.html', active_page="pasajes", active_menu='mVentas')

@ventas_bp.route('/GestionarTipoCliente')
def Tipo_Clientes():
    return render_template('ventas/tipocliente.html', active_page="tipocliente", active_menu='mVentas')

@ventas_bp.route('/TipoClienteNuevo')
def TipoCliente_Nuevo():
    return render_template('ventas/tipoclienteCRUD.html', active_page="tipocliente", active_menu='mVentas')


# END VIEWS

# REGION TIPO CLIENTE #

@ventas_bp.route("/GetData_TipoCliente", methods=["GET"])
def get_tipo_cliente():
    try:
        tipos = TipoCliente.obtener_datos()
        return jsonify({'data': tipos, 'Status': 'success', 'Msj': 'Listado de tipos de cliente retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de cliente: {repr(e)}'})
    
@ventas_bp.route("/RegistrarTipoCliente", methods=["POST"])
def registrar_tipo_cliente():
    try:
        nombre = request.form.get("nombre", "").strip()

        if not nombre:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoCliente.insertarTipoCliente(nombre)
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


@ventas_bp.route("/EditarTipoCliente/<int:id>", methods=["POST"])
def editar_tipo_cliente(id):
    try:
        nombre = request.form.get("nombre", "").strip()
        estado = request.form.get("estado", "").strip()

        if not nombre or estado not in ["0", "1"]:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

        mensajes = TipoCliente.actualizarTipoCliente(id, nombre, int(estado))
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar tipo de cliente"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/DarBajaTipoCliente/<int:id>", methods=["POST"])
def dar_baja_tipo_cliente(id):
    try:
        mensajes = TipoCliente.darBajaTipoCliente(id)
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
        tipo_cliente = TipoCliente.obtenerUno(id)
        if tipo_cliente:
            return render_template("cliente/tipoClienteCRUD.html", tipo_cliente=tipo_cliente, tittle='Ver tipo cliente', btnId='btn_Aceptar')
        return render_template("cliente/tipoClienteCRUD.html", tipo_cliente={}, tittle='Ver tipo cliente', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@ventas_bp.route("/ObtenerTiposClientes", methods=["GET"])
def obtener_tipos_clientes():
    try:
        datos = TipoCliente.obtener_datos()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener tipos de cliente: {repr(e)}"})

# END REGION TIPO CLIENTE #

# FUNCIONES

# END FUNCIONES