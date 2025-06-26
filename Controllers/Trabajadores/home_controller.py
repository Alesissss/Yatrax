import hashlib
import random
from datetime import datetime
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort, current_app
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario
from Models.conf_menus import Conf_Menus
from Models.personal import Personal
from correo import enviar_correo

home_bp = Blueprint('home', __name__, url_prefix='/trabajadores/home')

# RESTRICCIONES
@home_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static', 'home.cambiarContrasena','home.validarCorreo','home.ingresarCodigo','home.nuevaContrasena']  # Excluir login, logout y archivos estáticos
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
                claims_ids = [claim['nombre'] for claim in claims]
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
        return redirect(url_for('homeClientes.index'))
    else:
        return redirect(url_for('homeClientes.index'))
#End Login
# REGION Recuperar contraseña

@home_bp.route("/cambiarContrasena")
def cambiarContrasena():
    return render_template("/home/changePassword.html")

@home_bp.route("/validarCorreo/<mail>")
def validarCorreo(mail):
    lista = [usuario["email"] for usuario in Usuario.obtener_todos()]

    if mail in lista:
        session["tiempo_cambio"] = {
            "usuario":mail,
            "codVerificacion":None,
            "hora_realizado": datetime.now().timestamp(),
            "mostrado": False
        }
        return jsonify({
            "data": "Solicitud de cambio aprobada, tiene 5 min para realizar el cambio",
            "Status": 1
        })
    else:
        return jsonify({
            "data": "El correo ingresado es inválido",
            "Status": 0
        })

#
# Funcion para hacer el codigo de acceso aleatorio
# 

def generar_codigoVerificacion():
    return random.randint(100000000, 999999999)

# end funcion

@home_bp.route("/codigoAcceso",methods=["GET","POST"])
def ingresarCodigo():
    if request.method == "GET":
        datos = session["tiempo_cambio"]

        if datos:
            tiempo_guardado = datos.get("hora_realizado")
            ya_mostro = datos.get("mostrado", False)

            tiempo_actual = datetime.now().timestamp()
            diferencia = tiempo_actual - tiempo_guardado

            if diferencia <= 10 * 60:  # 10 minutos
                if not ya_mostro: #asunto remitente destinatario mensaje
                    datos["mostrado"] = True
                    datos["codVerificacion"]=generar_codigoVerificacion()
                    session["tiempo_cambio"] = datos

                    datosEnvio = {
                        'asunto':'Envio codigo de recuperacion Yatrax',
                        'remitente': 'yatraxyatusa@gmail.com',
                        'destinatario': datos["usuario"],
                        'mensaje': 'Tu codigo de recuperacion es : '+str(datos["codVerificacion"])
                    }

                    enviar_correo(current_app.extensions['mail'],datosEnvio)
                    return render_template("/home/controlPassword.html")
                else:
                    # Ya se mostró, no hacer nada
                    return "", 204
            else:
                # Tiempo vencido, limpiar sesión
                session.pop("tiempo_cambio", None)
                return redirect("/")
        else:
            return redirect("/")
    else:
        datos = session["tiempo_cambio"]
        codigoAcceso = request.form["codigo"]
        if int(codigoAcceso) == datos["codVerificacion"]:
            return jsonify({"redirect": url_for('home.nuevaContrasena')})
        else:
            return jsonify({"error": "Código incorrecto"})

        
@home_bp.route("/nuevaContrasena", methods=["GET", "POST"])
def nuevaContrasena():
    if 'tiempo_cambio' not in session:
        return jsonify({"Status": "error", "Msj": "Sesión expirada o inválida"})

    datos = session["tiempo_cambio"]

    if request.method == "GET":
        return render_template("/home/newPassword.html")

    try:
        data = request.get_json()
        print("📥 JSON recibido:", data)

        if not data or "clave" not in data:
            return jsonify({"Status": "error", "Msj": "Datos incompletos"})

        clave = data["clave"]
        usuario = datos["usuario"]

        print("🔐 Actualizando clave para:", usuario)

        respuesta = Usuario.actualizar_contrasena(usuario, clave)

        return jsonify({"Status": "success", "Msj": respuesta})
    except Exception as e:
        print("❌ Error interno:", repr(e))
        return jsonify({"Status": "error", "Msj": str(e)})

# END REGION

@home_bp.route('/VerificarViaje')
def verificarViaje():
    try:
        if (session['usuario']['tipoPersonal'] == 'CHOFER'):
            id = session['usuario']['id_personal']
            result = Personal.verificarViaje(id)
            return jsonify({"data": result, "Status": "success", "Msj": "Viaje encontrado exitosamente"})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": repr(e)})

@home_bp.route('/inicio')
def index():
    if (session.get('moduloSelected')):
        session.pop('moduloSelected')
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