import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.tipoVehiculo import TipoVehiculo
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

    if not any(menu['nombre'] == 'M_VIAJES' for menu in menus) and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@viajes_bp.route('/GestionarHorarios')
def Menu_Viajes():
    return render_template('viajes/horarios.html', active_page="horarios", active_menu='mViajes')

@viajes_bp.route('/GestionarTipoVehiculo')
def Menu_TipoVehiculo():
    return render_template('viajes/tipoVehiculo.html', active_page="tipoVehiculo", active_menu='mViajes')


@viajes_bp.route('/nuevoTipoVehiculo')
def nuevoTipoVehiculo():
    return render_template(
        "viajes/tipoVehiculoCRUD.html",
        tittle="Nuevo Tipo de Vehículo",
        tipoVehiculo={
            "id": "15",
            "nombre": "Autobús estandar",
            "largo": 12.5,
            "ancho": 2.8,
            "capacidad": 45,
            "combustible": "diesel",
            "consumo": 3.2,
            "estado": "activo"
        },
        btnId="btn_Registrar",
        active_page="tipoVehiculo", 
        active_menu='mViajes'
    )

# END VIEWS

# FUNCIONES

# REGION TIPO VEHICULO
@viajes_bp.route("/registrarTipoVehiculo",methods=["POST"])
def registrarTipoVehiculo():
    try:
        nombre= request.form["txt_nombre"]
        largo= request.form["txt_largo"]
        ancho= request.form["txt_ancho"]
        capacidad = request.form["txt_capacidad"]
        combustible= request.form["txt_combustible"]
        consumo= request.form["txt_consumo"]
        estado= request.form["txt_estado"]

        TipoVehiculo.insertarTipoVehiculo(nombre,largo,ancho,capacidad,combustible,consumo)
        return jsonify({
            "Status": "success",
            "Msj": "Tipo de vehículo registrado correctamente."
        })
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al listar los tipos de vehiculo: + {repr(e)}'})

@viajes_bp.route("/GetData_TipoVehiculo", methods=["GET"])
def get_tipoVehiculo():
    try:
        tipoVehiculo = TipoVehiculo.obtener_todos()
        return jsonify({'data': tipoVehiculo, 'Status': 'success', 'Msj': 'Listado de tipos de vehiculo retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar los tipos de vehiculo: + {repr(e)}'})
    
@viajes_bp.route("/DarBajaTipoVehiculo/<int:id>", methods=["POST"])
def darBajaTipovehiculo(id):
    try:
        TipoVehiculo.darBajaTipoVehiculo(id)
        return jsonify({
            "Status": "success",
            "Msj": f"Tipo de vehículo {id} dado de baja",
        })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": "Error al dar de baja el tipo de vehiculo =>"+repr(e),
        })  

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

@viajes_bp.route("/EditarTipoVehiculo/<int:idTipoVehiculo>")
def editarTipoVehiculo(idTipoVehiculo):
    return render_template(
        "viajes/tipoVehiculoCRUD.html",
        tittle="Editar Tipo de Vehículo",
        tipoVehiculo = TipoVehiculo.obtenerUno(idTipoVehiculo),
        btnId="btn_Actualizar"
    )

@viajes_bp.route("/guardarCambiosTipoVehiculo",methods=["POST"])
def guardarCambiosTipoVehiculo():
    try:
        idTipVehiculo = request.form["txt_id"]
        nombre= request.form["txt_nombre"]
        largo= request.form["txt_largo"]
        ancho= request.form["txt_ancho"]
        capacidad = request.form["txt_capacidad"]
        combustible= request.form["txt_combustible"]
        consumo= request.form["txt_consumo"]
        estado= request.form["txt_estado"]
        
        TipoVehiculo.actualizarTipoVehiculo(idTipVehiculo,nombre, largo, ancho, capacidad, combustible, consumo,estado)

        return jsonify({
            "Status": "success",
            "Msj": "Tipo de vehículo registrado correctamente."
        })
    
    except Exception as e:
        return jsonify({'Status': 'error', 'Msj': f'Ocurrió un error al listar los tipos de vehiculo: + {repr(e)}'})

# END REGION TIPO VEHICULO

# REGIÓN HORARIO #

@viajes_bp.route("/GetData_Horario", methods=["GET"])
def get_usuarios():
    try:
        horarios = horario.obtener_todos()
        return jsonify({'data': horarios, 'Status': 'success', 'Msj': 'Listado de horarios retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar horarios: + {repr(e)}'})

@viajes_bp.route("/RegistrarUsuario", methods=["POST"])
def registrar_usuario():
    try:
        UPLOAD_FOLDER = "Static/img/trabajadores/"
        nombre = request.form.get("nombre").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password")
        idTipoUsuario = request.form.get("idTipoUsuario")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        if not nombre or not email or not password or not idTipoUsuario:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        ruta_imagen = "/Static/img/trabajadores/default-user.png"

        if 'imagen' in request.files:
            imagen = request.files['imagen']

            if imagen and allowed_file(imagen.filename):
                extension = imagen.filename.rsplit(".", 1)[1].lower()
                filename = f"{email}.{extension}"
                ruta_imagen = f"/{UPLOAD_FOLDER}{filename}"

        mensajes = Usuario.registrar(nombre, email, password, ruta_imagen, idTipoUsuario, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            if 'imagen' in request.files and imagen and allowed_file(imagen.filename):
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                imagen.save(filepath)
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar usuario'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarUsuario/<int:id>", methods=['POST'])
def eliminar_usuario(id):  # Recibe el ID de la URL
    try:
        mensajes = Usuario.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarUsuario/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    try:
        UPLOAD_FOLDER = "Static/img/trabajadores/"
        usuario = Usuario.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            email = request.form.get("email").strip()
            idTipoUsuario = request.form.get("idTipoUsuario")

            if not nombre or not email or not idTipoUsuario:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

            ruta_imagen = usuario['imagen'] if usuario and 'imagen' in usuario else "/Static/img/trabajadores/default-user.png"

            if 'imagen' in request.files:
                imagen = request.files['imagen']
                
                if imagen and allowed_file(imagen.filename):
                    extension = imagen.filename.rsplit(".", 1)[1].lower()
                    filename = f"{email}.{extension}"
                    ruta_imagen = f"/{UPLOAD_FOLDER}{filename}"
            
            mensajes = Usuario.editar(id, nombre, email, ruta_imagen, idTipoUsuario)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                if 'imagen' in request.files and imagen and allowed_file(imagen.filename):
                    filepath = os.path.join(UPLOAD_FOLDER, filename)
                    imagen.save(filepath)
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar usuario'})

        if usuario:
            return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario=usuario, tittle = 'Editar usuario', btnId = 'btn_Editar')
        return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Editar usuario', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerUsuario/<int:id>", methods=['GET'])
def ver_usuario(id):
    try:
        usuario = Usuario.obtener_por_id(id)
        if usuario:
            return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario=usuario, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaUsuario/<int:id>", methods=['POST'])
def darBaja_usuario(id):  # Recibe el ID de la URL
    try:
        mensajes = Usuario.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGIÓN HORARIO #

# END FUNCIONES