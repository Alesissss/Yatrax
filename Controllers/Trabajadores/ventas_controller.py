import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from werkzeug.utils import secure_filename
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario

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
@ventas_bp.route('/GestionarHorarios')
def Menu_Horarios():
    return render_template('ventas/horarios.html', active_page="horarios", active_menu='mVentas')

# END VIEWS

# FUNCIONES
# Función para validar el tipo de archivo

# END FUNCIONES