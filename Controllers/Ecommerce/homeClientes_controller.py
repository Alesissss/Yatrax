import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort
from Models.conf_plantillas import Conf_Plantillas
from Models.api_net import ApiNetPe
from Models.servicio import Servicio
from Models.cliente import Cliente

from Models.tipoDocumento import TipoDocumento
from Models.tipoCliente import TipoCliente
from Models.pais import Pais
from Models.cliente import Cliente
homeClientes_bp = Blueprint('homeClientes', __name__, url_prefix='/ecommerce/home')

# # ERRORES 
# # Manejar errores 401 (Página no autorizada)
# @homeClientes_bp.errorhandler(401)
# def error_401(error):
#     return render_template("Ecommerce/error.html", error="Página no autorizada"), 401

# # Manejar errores 403 (Página no autorizada para este usuario)
# @homeClientes_bp.errorhandler(403)
# def error_403(error):
#     return render_template("Ecommerce/error.html", error="Página restringida"), 403

# # Manejar errores 404 (Página no encontrada)
# @homeClientes_bp.errorhandler(404)
# def error_404(error):
#     return render_template("Ecommerce/error.html", error="Página no encontrada"), 404

# # Manejar errores 500 (Error interno del servidor)
# @homeClientes_bp.errorhandler(500)
# def error_500(error):
#     return render_template("Ecommerce/error.html", error="Error interno del servidor"), 500

# # Manejar cualquier otro error genérico
# @homeClientes_bp.errorhandler(Exception)
# def error_general(error):
#    return render_template("Ecommerce/error.html", error="Ocurrió un error inesperado"), 500

# VIEWS
@homeClientes_bp.route('/inicio')
def index():
    datos_recibidos = {
        "servicios":Servicio.obtener_todos()
    }
    return render_template('Ecommerce/home/home.html', active_page="home",datos=datos_recibidos)

@homeClientes_bp.route("/sobreNosotros")
def sobreNosotros():
    return render_template('Ecommerce/home/sobreNosotros.html')

@homeClientes_bp.route('/error')
def error():
    return render_template('Ecommerce/error.html')

@homeClientes_bp.route('/login',methods=["GET","POST"])
def login_cliente():
    if request.method == "GET":
        return render_template('Ecommerce/home/modalLogin.html')
    else:
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        cliente = Cliente.logear_cliente(correo,contrasena)

        if cliente != None:
            session["cliente"] = cliente
            return redirect("/ecommerce/home/inicio")
        else:
            return jsonify({"msj": "Ingreso de credenciales incorrecto. Vuelva a intentarlo"})

@homeClientes_bp.route("/logout")
def logoutCliente():
    if 'cliente' in session:
        session.pop('cliente',None)
        return redirect("/ecommerce/home/inicio")
    
#REGION POR TERMINAR    
@homeClientes_bp.route("/miPerfil",methods=["GET","POST"])
def perfilCliente():
    if request.method == "GET":
        paises = Pais.obtener_todos()
        tipoCliente = TipoCliente.obtener_todos()
        tipoDocumentos = TipoDocumento.obtener_todos()
        return render_template("Ecommerce/home/miPerfil.html",paises=paises,tiposCliente=tipoCliente,tipoDocumentos=tipoDocumentos)
    else:
        pass

#Los HTML para recuperar contraseña del lado del cliente aun no existen
@homeClientes_bp.route("",methods=["GET","POST"])
def cambiarContrasena():
    if request.method == "GET":
        return render_template("Ecommerce/home/forgotPassword.html")
    else:
        email = request.form["correo"]
        respuesta = Cliente.verificar_correo_cliente(email)
        if respuesta == 1:
            return jsonify({"mensaje":"Correo valido, a continuación se enviará el código de verificación","status":1})
        else:
            return jsonify({"mensaje":"Correo no valido, vuelva a intentarlo","status":0})
            
# END POR TERMINAR
@homeClientes_bp.route('/forgotPass')
def forgot_password():
    return render_template('Ecommerce/home/forgotPassword.html')

@homeClientes_bp.route('/register')
def register_cliente():
    TipoDocumentos=TipoDocumento.obtener_todos()
    Paises = Pais.obtener_todos()
    return render_template('Ecommerce/home/formRegistro.html', TipoDocumento=TipoDocumentos, Paises=Paises)

@homeClientes_bp.route('transferenciaPasaje')
def transferencia_pasaje():
    return render_template('Ecommerce/home/transferenciaPasaje.html')

@homeClientes_bp.route('/pago')
def pago_pasajes():
    return render_template('Ecommerce/home/pago.html')

@homeClientes_bp.route('/terminosYcondiciones')
def terminos_y_condiciones():
    return render_template('Ecommerce/home/terminosCondiciones.html')
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
    
# API NET RENIEC
# controller_clientes.py
@homeClientes_bp.route('/api/get_persona_data', methods=['GET'])
def get_persona_data():
    try:
        tipo_doc = request.args.get('tipoDoc')
        num_doc = request.args.get('numDoc')
        if not tipo_doc:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'Debe proporcionar un DNI'})

        api = ApiNetPe()

        if tipo_doc == 'DNI':
            datos = api.get_person(num_doc)

            if datos:
                return jsonify({'data': datos, 'Status': 'success', 'Msj': 'Datos obtenidos correctamente'})
            else:
                return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron datos para el DNI proporcionado'})
        elif tipo_doc =='RUC':
            datos = api.get_company(num_doc)
            
            if datos:
                return jsonify({'data': datos, 'Status': 'success', 'Msj': 'Datos obtenidos correctamente'})
            else:
                return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron datos para el RUC proporcionado'})
        else:
            return jsonify({'data': {}, 'Status': 'success', 'Msj': 'No hay datos para el tipo de documento ingresado'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Error en el servidor: {repr(e)}'})
    

# FIN API NET RENIEC


@homeClientes_bp.route("/RegistrarClienteForm", methods=["POST"])
def registrar_cliente_form():
    try:
        # Obtener datos del formulario (coinciden con los IDs en tu HTML)
        id_tipo_doc = request.form.get("tipo-doc")
        numero_documento = request.form.get("ytrx-doc-number", "").strip()
        razon_social = request.form.get("ytrx-razon-social", "").strip()
        nombres = request.form.get("ytrx-fullname", "").strip()
        ape_paterno = request.form.get("ytrx-lastname-father", "").strip()
        ape_materno = request.form.get("ytrx-lastname-mother", "").strip()
        sexo = request.form.get("ytrx-gender")
        f_nacimiento = request.form.get("ytrx-birthdate")
        telefono = request.form.get("ytrx-phone", "").strip()
        direccion = request.form.get("ytrx-address", "").strip()
        id_pais = request.form.get("ytrx-country")
        email = request.form.get("ytrx-email", "").strip()
        password_raw = request.form.get("ytrx-password", "").strip()

        # Validaciones básicas

        # Hash de la contraseña (SHA-256)
        import hashlib
        password = hashlib.sha256(password_raw.encode()).hexdigest()

        # Determinar tipo de cliente

        # Registrar cliente
        mensajes = Cliente.registrarForm(
            id_pais=id_pais,
            id_tipo_cliente=1,
            id_tipo_doc=id_tipo_doc,
            numero_documento=numero_documento,
            nombres=nombres,
            ape_paterno=ape_paterno,
            ape_materno=ape_materno,
            sexo=sexo,
            f_nacimiento=f_nacimiento,
            razon_social=razon_social,
            direccion=direccion,
            telefono=telefono,
            email=email,
            password=password,
            usuario=email
        )
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar cliente"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
# END FUNCIONES
