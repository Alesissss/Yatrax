import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort
from Models.conf_plantillas import Conf_Plantillas

homeClientes_bp = Blueprint('homeClientes', __name__, url_prefix='/ecommerce/home')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@homeClientes_bp.errorhandler(401)
def error_401(error):
    return render_template("Ecommerce/error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@homeClientes_bp.errorhandler(403)
def error_403(error):
    return render_template("Ecommerce/error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@homeClientes_bp.errorhandler(404)
def error_404(error):
    return render_template("Ecommerce/error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@homeClientes_bp.errorhandler(500)
def error_500(error):
    return render_template("Ecommerce/error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@homeClientes_bp.errorhandler(Exception)
def error_general(error):
   return render_template("Ecommerce/error.html", error="Ocurrió un error inesperado"), 500

# VIEWS
@homeClientes_bp.route('/inicio')
def index():
    return render_template('Ecommerce/home/home.html', active_page="home")

@homeClientes_bp.route("/sobreNosotros")
def sobreNosotros():
    return render_template('Ecommerce/home/sobreNosotros.html')

@homeClientes_bp.route('/error')
def error():
    return render_template('Ecommerce/error.html')

@homeClientes_bp.route('/login')
def login_cliente():
    return render_template('Ecommerce/home/modalLogin.html')

@homeClientes_bp.route('/forgotPass')
def forgot_password():
    return render_template('Ecommerce/home/forgotPassword.html')

@homeClientes_bp.route('/register')
def register_cliente():
    return render_template('Ecommerce/home/formRegistro.html')
# END VIEWS

# FUNCIONES
@homeClientes_bp.route('/GetConfApariencia')
def get_ConfApariencia():
    try:
        conf_apariencia = Conf_Plantillas.obtener_PlantillaActiva()
        if conf_apariencia:
            return jsonify({'data': conf_apariencia, 'Status': 'success', 'Msj': 'Configuración obtenida exitosamente.'})
        else:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontró configuración activa.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al obtener la configuración: {repr(e)}'})

# END FUNCIONES
