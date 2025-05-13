import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario
from Models.conf_menus import Conf_Menus

home_bp = Blueprint('home', __name__, url_prefix='/trabajadores/home')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@home_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 404 (Página no encontrada)
@home_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@home_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@home_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@home_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

#Login
@home_bp.route('/')
@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            data = request.json
            email = data.get('email', '').strip()
            password = data.get('password', '').strip()

            # Para usar FormData
            # email = request.form.get('email', '').strip()
            # password = request.form.get('password', '').strip()

            password_hash = hashlib.sha256(password.encode()).hexdigest()

            usuario = Usuario.autenticar(email, password_hash)
            if usuario:
                menus = TipoUsuario.obtener_menus(usuario['id_tipousuario'])
                claims = TipoUsuario.obtener_claims(usuario['id_tipousuario'])
                menu_ids = [menu['id'] for menu in menus]  # List comprehension para obtener solo los IDs
                claims_ids = [claim['id'] for claim in claims]
                session['usuario'] = usuario
                session['menus'] = menu_ids
                session['claims'] = claims_ids
                return jsonify({'Status': 'success', 'Msj': 'Inicio de sesión exitoso'})

            return jsonify({'Status': 'error', 'Msj': 'Credenciales incorrectas'})
        
        if 'usuario' in session:
            return redirect(url_for('home.index'))
        return render_template('/home/auth/login.html')
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    

@home_bp.route('/logout', methods=['POST'])
def logout():
    if session.get('usuario'):
        session.clear()
        return redirect(url_for('home.login'))
    else:
        return redirect(url_for('home.index'))
#End Login

@home_bp.route('/inicio')
def index():
    return render_template('home/home.html', active_page="home")

@home_bp.route('/error')
def error():
    return render_template('error.html')

@home_bp.route('/SetModulo', methods=['POST'])
def SetModulo():
    try:
        data = request.json
        menuSelected = int(data.get('modulo', '').strip())

        menus = Conf_Menus.obtener_todos()

        if menuSelected:
            menu = next((menu for menu in menus if menu['id'] == menuSelected), None)

            if menu:
                session['moduloSelected'] = menuSelected
                return jsonify({'Status': 'success', 'Msj': 'Módulo escogido exitosamente'})

        return jsonify({'Status': 'error', 'Msj': 'El módulo seleccionado no existe'})
    except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@home_bp.route('/inicioUsuarios')
def inicioUsuarios():
    return render_template('home/homeUsuarios.html', active_menu="mUsuarios")

@home_bp.route('/inicioConfiguracion')
def inicioConfiguracion():
    return render_template('home/homeConfiguracion.html', active_menu="mConfiguracion")

@home_bp.route('/inicioVentas')
def inicioVentas():
    return render_template('home/homeVentas.html', active_menu="mVentas")

@home_bp.route('/inicioViajes')
def inicioViajes():
    return render_template('home/homeViajes.html', active_menu="mViajes")

@home_bp.route('/inicioPersonal')
def inicioPersonal():
    return render_template('home/homePersonal.html', active_menu="mPersonal")

@home_bp.route('/inicioAtencion')
def inicioAtencion():
    return render_template('home/homeAtencion.html', active_menu="mAtencion")