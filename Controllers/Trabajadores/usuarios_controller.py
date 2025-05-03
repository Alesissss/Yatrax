import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from werkzeug.utils import secure_filename
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario

usuario_bp = Blueprint('usuario', __name__, url_prefix='/trabajadores/usuarios')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@usuario_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@usuario_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@usuario_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@usuario_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@usuario_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@usuario_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 1 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_USUARIOS' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@usuario_bp.route('/GestionarUsuarios')
def Menu_Usuarios():
    return render_template('usuario/usuarios.html', active_page="usuarios", active_menu='mUsuarios')

@usuario_bp.route('/UsuarioNuevo')
def Usuario_Nuevo():
    return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Registrar usuario', btnId = 'btn_Registrar')

@usuario_bp.route('TipoUsuarioNuevo')
def TipoUsuario_Nuevo():
    return render_template('usuario/modalTipoUsuarioNuevo.html')

# END VIEWS

# FUNCIONES

# REGION USUARIOS
# Función para validar el tipo de archivo
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@usuario_bp.route("/GetData_Usuarios", methods=["GET"])
def get_usuarios():
    try:
        usuarios = Usuario.obtener_todos()
        return jsonify({'data': usuarios, 'Status': 'success', 'Msj': 'Listado de usuarios retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar usuarios: + {repr(e)}'})

@usuario_bp.route("/GetTiposUsuarios", methods=["GET"])
def GetTiposUsuarios():
    try:
        tiposUsuarios = TipoUsuario.obtener_todos()
        result = [{'id': tu['id'], 'nombre': tu['nombre']} for tu in tiposUsuarios]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de tipos de usuarios retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de usuarios: {repr(e)}'})

@usuario_bp.route("/RegistrarUsuario", methods=["POST"])
def registrar_usuario():
    try:
        UPLOAD_FOLDER = "Static/img/trabajadores/"
        nombre = request.form.get("nombre").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password")
        estado = request.form.get("estado")
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

        mensajes = Usuario.registrar(nombre, email, password, ruta_imagen, estado, idTipoUsuario, usuario_actual)
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

@usuario_bp.route("/EliminarUsuario/<int:id>", methods=['POST'])
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

@usuario_bp.route("/EditarUsuario/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    try:
        UPLOAD_FOLDER = "Static/img/trabajadores/"
        usuario = Usuario.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            email = request.form.get("email").strip()
            estado = request.form.get("estado")
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
            
            mensajes = Usuario.editar(id, nombre, email, ruta_imagen, estado, idTipoUsuario)
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
    
@usuario_bp.route("/VerUsuario/<int:id>", methods=['GET'])
def ver_usuario(id):
    try:
        usuario = Usuario.obtener_por_id(id)
        if usuario:
            return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario=usuario, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        return render_template('usuario/usuarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@usuario_bp.route("/DarBajaUsuario/<int:id>", methods=['POST'])
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
    
@usuario_bp.route("/RegistrarTipoUsuario", methods=["POST"])
def registrar_tipoUsuario():
    try:
        data = request.json
        mensajes = TipoUsuario.registrar(data["nombre"], session['usuario'].get('email', 'SIN USUARIO').strip())
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:  # Fallback
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar tipo de usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION USUARIO

# END FUNCIONES