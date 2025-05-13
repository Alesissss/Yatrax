import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.tipoPersonal import TipoPersonal
from Models.personal import Personal

personal_bp = Blueprint('personal', __name__, url_prefix='/trabajadores/personal')

# # ERRORES 
# # Manejar errores 401 (Página no autorizada)
# @personal_bp.errorhandler(401)
# def error_401(error):
#     return render_template("error.html", error="Página no autorizada"), 401

# # Manejar errores 403 (Página no autorizada para este usuario)
# @personal_bp.errorhandler(403)
# def error_403(error):
#     return render_template("error.html", error="Página restringida"), 403

# # Manejar errores 404 (Página no encontrada)
# @personal_bp.errorhandler(404)
# def error_404(error):
#     return render_template("error.html", error="Página no encontrada"), 404

# # Manejar errores 500 (Error interno del servidor)
# @personal_bp.errorhandler(500)
# def error_500(error):
#     return render_template("error.html", error="Error interno del servidor"), 500

# # Manejar cualquier otro error genérico
# @personal_bp.errorhandler(Exception)
# def error_general(error):
#     return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@personal_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 5 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_PERSONAL' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@personal_bp.route('/GestionarTipoPersonal')
def Menu_TipoPersonal():
    return render_template('personal/tipoPersonal.html', active_page="tipoPersonal", active_menu='mPersonal')

@personal_bp.route('/TipoPersonalNuevo')
def TipoPersonalNuevo():
    return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Registrar tipo personal', btnId='btn_Registrar')

@personal_bp.route('/GestionarPersonal')
def Menu_Personal():
    return render_template('personal/personal.html', active_page="personal", active_menu='mPersonal')

@personal_bp.route('/PersonalNuevo')
def PersonalNuevo():
    return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal={}, tittle='Registrar personal', btnId='btn_Registrar')

# END VIEWS

# FUNCIONES

# REGION TIPO PERSONAL

@personal_bp.route("/GetData_TipoPersonal", methods=["GET"])
def get_tiposPersonal():
    try:
        tiposPersonal = TipoPersonal.obtener_todos()
        return jsonify({'data': tiposPersonal, 'Status': 'success', 'Msj': 'Listado de tipos de personal retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de personal: {repr(e)}'})

@personal_bp.route("/RegistrarTipoPersonal", methods=["POST"])
def registrar_tipoPersonal():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = TipoPersonal.registrar(nombre, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar tipo de personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/EliminarTipoPersonal/<int:id>", methods=['POST'])
def eliminar_tipoPersonal(id):
    try:
        mensajes = TipoPersonal.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar tipo de personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/EditarTipoPersonal/<int:id>", methods=['GET', 'POST'])
def editar_tipoPersonal(id):
    try:
        tipoPersonal = TipoPersonal.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado")
            
            mensajes = TipoPersonal.editar(id, nombre, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar tipo de personal'})

        if tipoPersonal:
            return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal=tipoPersonal, tittle='Editar tipo personal', btnId='btn_Editar')
        return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Editar tipo personal', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/VerTipoPersonal/<int:id>", methods=['GET'])
def ver_tipoPersonal(id):
    try:
        tipoPersonal = TipoPersonal.obtener_por_id(id)
        if tipoPersonal:
            return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal=tipoPersonal, tittle='Ver tipo personal', btnId='btn_Aceptar')
        return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Ver tipo personal', btnId='btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/DarBajaTipoPersonal/<int:id>", methods=['POST'])
def darBaja_tipoPersonal(id):
    try:
        mensajes = TipoPersonal.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al tipo de personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO PERSONAL

# REGION PERSONAL

# Obtener todos los registros de personal
@personal_bp.route("/GetData_Personal", methods=["GET"])
def get_Personal():
    try:
        personal = Personal.obtener_todos()
        return jsonify({'data': personal, 'Status': 'success', 'Msj': 'Listado de personal retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar personal: {repr(e)}'})

# Registrar nuevo personal
@personal_bp.route("/RegistrarPersonal", methods=["POST"])
def registrar_personal():
    try:
        nombre = request.form.get("nombre").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        estado = request.form.get("estado")
        idTipoPersonal = request.form.get("idTipoPersonal")
        imagen = request.files.get("imagen")  # Recibir la imagen (archivo)

        # Guardar la imagen si es que se sube
        if imagen:
            imagen_path = os.path.join("Static/img/personal", imagen.filename)
            imagen.save(imagen_path)
        else:
            imagen_path = ""

        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Personal.registrar(nombre, email, password, imagen_path, estado, idTipoPersonal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Editar un registro de personal
@personal_bp.route("/EditarPersonal/<int:id>", methods=['GET', 'POST'])
def editar_personal(id):
    try:
        personal = Personal.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            email = request.form.get("email").strip()
            estado = request.form.get("estado")
            idTipoPersonal = request.form.get("idTipoPersonal")
            imagen = request.files.get("imagen")  # Recibir la imagen (archivo)

            # Guardar la imagen si es que se sube
            if imagen:
                imagen_path = os.path.join("Static/img/personal", imagen.filename)
                imagen.save(imagen_path)
            else:
                imagen_path = personal['imagen']  # Mantener la imagen actual si no se sube una nueva

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            mensajes = Personal.editar(id, nombre, email, imagen_path, estado, idTipoPersonal)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar personal'})

        if personal:
            return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal=personal, tittle='Editar personal', btnId='btn_Editar')
        return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal={}, tittle='Editar personal', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Dar de baja a un personal
@personal_bp.route("/DarBajaPersonal/<int:id>", methods=['POST'])
def darBaja_personal(id):
    try:
        mensajes = Personal.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Eliminar un registro de personal
@personal_bp.route("/EliminarPersonal/<int:id>", methods=['POST'])
def eliminar_personal(id):
    try:
        mensajes = Personal.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/VerPersonal/<int:id>", methods=['GET'])
def ver_personal(id):
    try:
        # Obtener el personal por ID
        personal = Personal.obtener_por_id(id)
        
        # Si el personal existe, se pasa al template
        if personal:
            return render_template('personal/personalCRUD.html', 
                                   active_page="personal", 
                                   active_menu='mPersonal', 
                                   personal=personal, 
                                   tittle='Ver personal', 
                                   btnId='btn_Aceptar')
        # Si no se encuentra el personal, mostrar un formulario vacío
        return render_template('personal/personalCRUD.html', 
                               active_page="personal", 
                               active_menu='mPersonal', 
                               personal={}, 
                               tittle='Ver personal', 
                               btnId='btn_Aceptar')
    except Exception as e:
        # En caso de error, devolver un mensaje en formato JSON
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})


#END REGION PERSONAL

# END FUNCIONES