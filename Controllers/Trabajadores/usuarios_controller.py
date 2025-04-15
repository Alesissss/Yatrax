from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario

usuario_bp = Blueprint('usuario', __name__, url_prefix='/trabajadores/usuarios')

# RESTRICCIONES
@usuario_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    if (
        (not usuario and request.endpoint not in rutas_permitidas)
        or (usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas)
    ):
        session.clear()
        if not usuario:
            return redirect(url_for('home.login'))
        abort(401)

# VIEWS
@usuario_bp.route('/GestionarUsuarios')
def Modulo_Usuarios():
    return render_template('usuario/usuarios.html', active_page="usuarios")

@usuario_bp.route('/UsuarioNuevo')
def Usuario_Nuevo():
    return render_template('usuario/usuarioNuevo.html', active_page="usuarios")

@usuario_bp.route('TipoUsuarioNuevo')
def TipoUsuario_Nuevo():
    return render_template('usuario/modalTipoUsuarioNuevo.html')

# END VIEWS

# FUNCIONES
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
        data = request.json
        mensajes = Usuario.registrar(data["nombre"], data["email"], data["password"], data["idTipoUsuario"], session['usuario'].get('email', 'SIN USUARIO').strip())
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:  # Fallback
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
        usuario = Usuario.obtener_por_id(id)
        if request.method == 'POST':
            data = request.json

            mensajes = Usuario.editar(id, data["nombre"], data["email"], data["idTipoUsuario"])

            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar usuario'})
    
        if usuario:
            return render_template('usuario/usuarioEditar.html', active_page="usuarios", usuario=usuario)
        return render_template('usuario/usuarioEditar.html', active_page="usuarios", usuario={})
        
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

# END FUNCIONES