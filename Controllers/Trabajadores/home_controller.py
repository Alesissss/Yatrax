import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort
from Models.usuario import Usuario

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
    rutas_permitidas = ['home.login', 'home.logout', 'static']
    usuario = session.get('usuario')

    if (
        (not usuario and request.endpoint not in rutas_permitidas)
        or (usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas)
    ):
        session.clear()
        if not usuario:
            return redirect(url_for('home.login'))
        abort(401)


#Login
@home_bp.route('/')
@home_bp.route('/login', methods=['GET', 'POST'])
def login():
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
            session['usuario'] = usuario
            return jsonify({'Status': 'success', 'Msj': 'Inicio de sesión exitoso'})

        return jsonify({'Status': 'error', 'Msj': 'Credenciales incorrectas'})
    
    if 'usuario' in session:
        return redirect(url_for('home.index'))
    return render_template('/home/auth/login.html')

@home_bp.route('/logout', methods=['POST'])
def logout():
    if session.get('usuario'):
        session.pop('usuario')
        return redirect(url_for('home.login'))
    else:
        return redirect(url_for('home.index'))
#End Login

@home_bp.route('/inicio')
def index():
    if 'usuario' in session:
        return render_template('home/home.html', active_page="home")
    return redirect(url_for('home.login'))

@home_bp.route('/error')
def error():
    return render_template('error.html')
