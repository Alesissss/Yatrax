import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.tipoVehiculo import TipoVehiculo
from Models.sucursal import Sucursal
from Models.horario import horario

viajes_bp = Blueprint('viajes', __name__, url_prefix='/trabajadores/viajes')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@viajes_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@viajes_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@viajes_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@viajes_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@viajes_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@viajes_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 4 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_VIAJES' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@viajes_bp.route('/GestionarHorarios')
def Menu_Horarios():
    return render_template('viajes/horarios.html', active_page="horarios", active_menu='mViajes')

@viajes_bp.route('/GestionarTipoVehiculo')
def Menu_TipoVehiculo():
    return render_template('viajes/tipoVehiculo.html', active_page="tipoVehiculo", active_menu='mViajes')

@viajes_bp.route('/GestionarSucursal')
def Menu_Sucursal():
    return render_template('viajes/sucursal.html', active_page="sucursal", active_menu='mViajes')

# END VIEWS

# FUNCIONES

# REGION TIPO VEHICULO

@viajes_bp.route("/GetData_TipoVehiculo", methods=["GET"])
def get_tipoVehiculo():
    try:
        tipoVehiculo = TipoVehiculo.obtener_todos()
        return jsonify({'data': tipoVehiculo, 'Status': 'success', 'Msj': 'Listado de tipos de vehiculo retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar los tipos de vehiculo: + {repr(e)}'})

@viajes_bp.route('/registrarTipoVehiculo',methods=["GET","POST"])
def nuevoTipoVehiculo():
    if request.method == "GET":
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            tittle="Nuevo Tipo de Vehículo",
            tipoVehiculo={
                "id": "15",
                "nombre": "Autobús estandar",
                "capacidad": 45,
                "estado": "activo"
            },
            btnId="btn_Registrar",
            active_page="tipoVehiculo", 
            active_menu='mViajes'
        )
    else:
        try:
            nombre= request.form["txt_nombre"]
            capacidad = request.form["txt_capacidad"]

            mensajes = TipoVehiculo.insertarTipoVehiculo(nombre,capacidad)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/verTipoVehiculo/<int:idVehiculo>")
def verTipoVehiculo(idVehiculo):
    return render_template(
        "viajes/tipoVehiculoCRUD.html",
        tittle="Ver Tipo de Vehículo",
        tipoVehiculo = TipoVehiculo.obtenerUno(idVehiculo),
        btnId="btn_Regresar",
        active_page="tipoVehiculo", 
        active_menu='mViajes'
    )

@viajes_bp.route("/editarTipoVehiculo/<int:idTipoVehiculo>",methods=["GET","POST"])
def editarTipoVehiculo(idTipoVehiculo):
    if request.method == "GET":
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            tittle="Editar Tipo de Vehículo",
            tipoVehiculo = TipoVehiculo.obtenerUno(idTipoVehiculo),
            btnId="btn_Actualizar"
        )
    else:
        try:
            nombre= request.form["txt_nombre"]
            capacidad = request.form["txt_capacidad"]
            estado = int(request.form["txt_estado"])

            mensajes = TipoVehiculo.actualizarTipoVehiculo(idTipoVehiculo,nombre,capacidad,estado)

            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})

        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/DarBajaTipoVehiculo/<int:idTipVehiculo>",methods=["POST"])
def darBajaTipoVehiculo(idTipVehiculo):
    try:
        mensajes = TipoVehiculo.darBajaTipoVehiculo(idTipVehiculo)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/eliminarTipoVehiculo/<int:idTipoVehiculo>", methods=["POST"])
def eliminarTipoVehiculo(idTipoVehiculo):
    try:
        mensajes = TipoVehiculo.eliminarTipoVehiculo(idTipoVehiculo)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO VEHICULO

# REGIÓN HORARIO #

@viajes_bp.route("/GetData_Horario", methods=["GET"])
def get_horarios():
    try:
        horarios = horario.obtener_todos()
        return jsonify({'data': horarios, 'Status': 'success', 'Msj': 'Listado de horarios retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar horarios: + {repr(e)}'})

@viajes_bp.route('/HorarioNuevo')
def horario_Nuevo():
    return render_template(
        'viajes/horarioCRUD.html', 
        active_page="horario", 
        active_menu='mViajes', 
        horario={},
        tittle = 'Registrar horario',
        btnId = 'btn_Registrar')

@viajes_bp.route("/RegistrarHorario", methods=["POST"])
def registrar_horario():
    try:
        hora_entrada = request.form.get("hora_entrada").strip()
        hora_salida = request.form.get("hora_salida").strip()
        estado = request.form.get("estado")

        if not hora_entrada or not hora_salida or not estado:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = horario.registrar(hora_entrada, hora_salida, estado)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar horario'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarHorario/<int:id>", methods=['POST'])
def eliminar_horario(id):  # Recibe el ID de la URL
    try:
        mensajes = horario.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar horario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarHorario/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    try:
        horario_data = horario.obtener_por_id(id)

        if request.method == 'POST':
            hora_entrada = request.form.get("hora_entrada").strip()
            hora_salida = request.form.get("hora_salida").strip()
            estado = request.form.get("estado")

            if not hora_entrada or not hora_salida or not estado:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

            
            mensajes = horario.editar(id, hora_entrada, hora_salida, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar horario'})
        if horario_data:
            return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario=horario_data, tittle = 'Editar horario', btnId = 'btn_Editar')
        return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario={}, tittle = 'Editar horario', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerHorario/<int:id>", methods=['GET'])
def ver_usuario(id):
    try:
        horario_data = horario.obtener_por_id(id)
        if horario_data:
            return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario=horario_data, tittle = 'Ver horario', btnId = 'btn_Aceptar')
        return render_template('viajes/horarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaHorario/<int:id>", methods=['POST'])
def darBaja_horario(id):  # Recibe el ID de la URL
    try:
        mensajes = horario.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al horario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGIÓN HORARIO #

# INICIO REGIÓN SUCURSAL #
@viajes_bp.route("/GetData_Sucursal", methods=["GET"])
def get_sucursal():
    try:
        sucursal = Sucursal.obtener_todos()
        return jsonify({'data': sucursal, 'Status': 'success', 'Msj': 'Listado de sucursales retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar las sucursales: + {repr(e)}'})

@viajes_bp.route('/RegistrarSucursal',methods=["GET","POST"])
def registrar_sucursal():
    try:
        ubigeo = request.form.get("txt_ubigeo").strip()
        nombre = request.form.get("txt_nombre").strip()
        direccion = request.form.get("txt_direccion").strip()
        latitud = request.form.get("txt_latitud").strip()
        longitud = request.form.get("txt_longitud").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        
        mensajes = Sucursal.registrar(ubigeo, nombre, direccion, latitud, longitud, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar sucursal'})
    
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarSucursal/<int:idSucursal>", methods=['GET'])
def eliminar_sucursal(idSucursal, usuario_actual):
    try:
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        mensajes = Sucursal.eliminar(idSucursal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar sucursal'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarSucursal/<int:idSucursal>",methods=["GET","POST"])
def editar_sucursal(idSucursal, usuario_actual):
    try:
        sucursal = Sucursal.obtener_por_id(idSucursal)
        
        if request.method == "POST":
            ubigeo = request.form.get("txt_ubigeo").strip()
            nombre = request.form.get("txt_nombre").strip()
            direccion = request.form.get("txt_direccion").strip()
            latitud = request.form.get("txt_latitud").strip()
            longitud = request.form.get("txt_longitud").strip()
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            mensajes = Sucursal.editar(idSucursal, ubigeo, nombre, direccion, latitud, longitud, usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar sucursal'})
        if sucursal:
            return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal=sucursal, tittle = 'Editar sucursal', btnId = 'btn_Editar')
        return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal={}, tittle = 'Editar sucursal', btnId = 'btn_Editar')
    
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerSucursal/<int:idSucursal>", methods=['GET'])
def ver_sucursal(idSucursal):
    try:
        sucursal = Sucursal.obtener_por_id(idSucursal)
        if sucursal:
            return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal=sucursal, tittle = 'Ver sucursal', btnId = 'btn_Aceptar')
        return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal={}, tittle = 'Ver sucursal', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaSucursal/<int:idSucursal>", methods=['POST'])
def darBaja_sucursal(idSucursal):
    try:
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        mensajes = Sucursal.darBaja(idSucursal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja la sucursal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGIÓN SUCURSAL #

# END FUNCIONES