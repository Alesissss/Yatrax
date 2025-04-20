from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.usuario import Usuario
from Models.conf_menus import Conf_Menus

configuracion_bp = Blueprint('configuracion', __name__, url_prefix='/trabajadores/configuracion')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@configuracion_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@configuracion_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@configuracion_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@configuracion_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@configuracion_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@configuracion_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if not any(menu['nombre'] == 'M_CONFIGURACION' for menu in menus) and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@configuracion_bp.route('/GestionarPermisos')
def Menu_Permisos():
    return render_template('configuracion/permisos.html', active_page="permisos", active_menu='mConfiguracion')

# END VIEWS

# FUNCIONES
@configuracion_bp.route("/GetData_Usuarios", methods=["GET"])
def get_usuarios():
    try:
        usuarios = Usuario.obtener_todos()
        return jsonify({'data': usuarios, 'Status': 'success', 'Msj': 'Listado de usuarios retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar usuarios: + {repr(e)}'})

@configuracion_bp.route('/EditarPermisos/<int:id>', methods= ['GET', 'POST'])
def Editar_Permisos(id):
    try:
        usuario = Usuario.obtener_por_id(id)
        dmnus = Usuario.obtener_menus(id)
        menus = Conf_Menus.obtener_todos()

        if request.method == 'POST':
            idMenu = int(request.form.get('idMenu').strip())
            idUsuario = int(request.form.get('idUsuario').strip())
            accion = int(request.form.get('accion').strip())
            
            if accion == 1:
                mensajes = Usuario.agregar_menu(idMenu, idUsuario)
                msj1 = mensajes.get('@MSJ')
                msj2 = mensajes.get('@MSJ2')
            else:
                mensajes = Usuario.eliminar_menu(idMenu, idUsuario)
                msj1 = mensajes.get('@MSJ')
                msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar permisos'})

        if usuario:
            return render_template('configuracion/permisosEditar.html', active_page="permisos", active_menu='mConfiguracion', usuario = usuario, dmnus = dmnus, menus = menus)
        return render_template('configuracion/permisosEditar.html', active_page="permisos", active_menu='mConfiguracion', usuario = {}, dmnus = [], menus = [])

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END FUNCIONES