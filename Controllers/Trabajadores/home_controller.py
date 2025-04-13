import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort
from Models.usuario import Usuario

home_bp = Blueprint('home', __name__, url_prefix='/trabajadores/home')

# RESTRICCIONES
@home_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
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
