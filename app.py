import os
from flask import Flask, render_template, request, redirect, flash, jsonify, session, url_for, abort

# BLUEPRINTS TRABAJADORES
from Controllers.Trabajadores.home_controller import home_bp
from Controllers.Trabajadores.usuarios_controller import usuario_bp
from Controllers.Trabajadores.configuracion_controller import configuracion_bp
from Controllers.Trabajadores.ventas_controller import ventas_bp
from Controllers.Trabajadores.viajes_controller import viajes_bp
from Controllers.Trabajadores.atencion_controller import atencion_bp
from Controllers.Trabajadores.personal_controller import personal_bp
# BLUEPRINTS ECOMMERCE
from Controllers.Ecommerce.homeClientes_controller import homeClientes_bp
#Extra para email
from flask_mail import Mail, Message

app = Flask(__name__, template_folder="Views", static_folder="Static")
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yatraxyatusa@gmail.com'
app.config['MAIL_PASSWORD'] = 'coivuoyrrpjnostu'

mail = Mail(app)

# # Manejar errores 401 (Página no autorizada)
# @app.errorhandler(401)
# def error_401(error):
#     return render_template("error.html", error="Página no autorizada"), 401

# # Manejar errores 404 (Página no encontrada)
# @app.errorhandler(404)
# def error_404(error):
#     return render_template("error.html", error="Página no encontrada"), 404

# # Manejar errores 500 (Error interno del servidor)
# @app.errorhandler(500)
# def error_500(error):
#     return render_template("error.html", error="Error interno del servidor"), 500

# # Manejar cualquier otro error genérico
# @app.errorhandler(Exception)
# def error_general(error):
#     return render_template("error.html", error="Ocurrió un error inesperado"), 500

# Clave secreta para sesiones (necesaria para usar `session`)
app.secret_key = os.urandom(24)  # O usa una clave fija: app.secret_key = "mi_clave_secreta"

# Registrar blueprints
app.register_blueprint(home_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(configuracion_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(viajes_bp)
app.register_blueprint(atencion_bp)
app.register_blueprint(personal_bp)
app.register_blueprint(homeClientes_bp)

@app.route('/')
def home():
    ##return redirect(url_for('home.login'))
    return redirect(url_for('homeClientes.index'))


# @app.before_request
# def verificar_sesion():
#     rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
#     if 'usuario' not in session and request.endpoint not in rutas_permitidas:
#         session.clear()
#         return redirect(url_for('home.login'))

if __name__ == "__main__":
    app.run(debug=True)