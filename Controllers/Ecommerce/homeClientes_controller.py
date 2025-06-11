import hashlib
import os
import re
import random
from correo import enviar_correo
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort,current_app

from flask_mail import Mail

from Models.conf_plantillas import Conf_Plantillas
from Models.api_net import ApiNetPe
from Models.servicio import Servicio
from Models.cliente import Cliente

from Models.tipoDocumento import TipoDocumento
from Models.tipoCliente import TipoCliente
from Models.pais import Pais
from Models.terminos_condiciones import TerminosCondiciones
from Models.viaje import Viaje
from Models.pasaje import Pasaje
from Models.tipoComprobante import TipoComprobante
from Models.metodo_pago import MetodoPago

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
        # return render_template('Ecommerce/home/modalLogin.html')
        return render_template('Ecommerce/home/modalLoginNewVer.html')
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
    else:
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
        try:
            id_cliente = request.form["id_cliente"]
            usuario = request.form["usuario"]
            id_pais = request.form["id_pais"]
            id_tipo_cliente = request.form["id_tipo_cliente"]
            razon_social = request.form["razon_social"]
            id_tipo_doc = request.form["id_tipo_doc"]
            numero_documento = request.form["numero_documento"]
            f_nacimiento = request.form["f_nacimiento"]
            nombres = request.form["nombres"]
            ape_paterno = request.form["ape_paterno"]
            ape_materno = request.form["ape_materno"]
            sexo = request.form["sexo"]
            direccion = request.form["direccion"]
            telefono = request.form["telefono"]
            email = request.form["email"]
            password = request.form["password"]
            if password.strip():
                password_hash = hashlib.sha256(password.encode()).hexdigest()
            else:
                password_hash = None
            
            Cliente.actualizar_cliente(id_cliente,id_pais,id_tipo_cliente,id_tipo_doc,numero_documento,nombres,ape_paterno,ape_materno,sexo,f_nacimiento,razon_social,direccion,telefono,email,password_hash,usuario)

            return jsonify({"Status":1,"Mensaje":"Se ha actualizado los datos del cliente correctamente"})
        except Exception as e:
            return jsonify({"Status":0,"Mensaje":"Error: "+str(e)})


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
    if 'cliente' in session:
        return redirect(url_for('homeClientes.index'))
    else:
        TipoDocumentos=TipoDocumento.obtener_todos()
        Paises = Pais.obtener_todos()
        return render_template('Ecommerce/home/formRegistro.html', TipoDocumento=TipoDocumentos, Paises=Paises)
        
@homeClientes_bp.route('transferenciaPasaje')
def transferencia_pasaje():
    return render_template('Ecommerce/home/transferenciaPasaje.html')

@homeClientes_bp.route('/miPasajeOperaciones')
def mi_pasaje_operaciones():
    return render_template('Ecommerce/home/miPasajeOp.html')

@homeClientes_bp.route('/pago')
def pago_pasajes():
    return render_template('Ecommerce/home/pago.html')

@homeClientes_bp.route('/terminosYcondiciones')
def terminos_y_condiciones():
    return render_template('Ecommerce/home/terminosCondiciones.html')

@homeClientes_bp.route('/cambioRuta')
def cambio_ruta():
    return render_template('Ecommerce/home/cambioRutamod.html')
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
    
@homeClientes_bp.route('/GetRutasConcatenadas')
def get_rutasConcatenadas():
    try:
        lista_rutas = Viaje.obtenerDestinos()
        if lista_rutas:
            return jsonify({'data': lista_rutas, 'Status': 'success', 'Msj': 'Rutas obtenidas correctamente.'})
        else:
            return jsonify({'data': {}, 'Status': 'error', 'Msj': 'No se encontraron rutas activas.'})
    except Exception as e:
        return jsonify({'data': {}, 'Status': 'error', 'Msj': f'Ocurrió un error al obtener la ruta: {repr(e)}'})
    
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
        id_pais = request.form.get("ytrx-country").strip()
        email = request.form.get("ytrx-email", "").strip()
        password = request.form.get("ytrx-password", "").strip()
        abreviatura = TipoDocumento.obtener_por_id(id_tipo_doc)
        if  abreviatura['abreviatura']== "RUC":
            id_tipoCliente = TipoCliente.obtener_por_nombre("Empresa")
        else:
            id_tipoCliente = TipoCliente.obtener_por_nombre("Adulto")
        
        # Registrar cliente
        mensajes = Cliente.registrarForm(
            id_pais=id_pais,
            id_tipo_cliente=id_tipoCliente['ID'],
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
            usuario=None
        )
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        elif msj2:
            return jsonify({"Status": "error", "Msj": "", "Msj2": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar cliente"})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})
# REGION TERMINOS Y CONDICIONES
@homeClientes_bp.route('/ApiTerminosCondicionesActivo', methods=['GET'])
def api_terminos_condiciones_activo():
    try:
        UPLOAD_FOLDER = "Static/utilities/terminos_condiciones/"

        activo = TerminosCondiciones.obtener_activos()
        if not activo:
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": "No hay términos y condiciones activos."
            })
        
        termino = activo[0]
        filename = termino['archivo']
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        if not os.path.exists(file_path):
            return jsonify({
                "Status": "error",
                "data": {},
                "Msj": f"El archivo {filename} no existe en el servidor."
            })
        
        texto = open(file_path, encoding='utf-8').read()
        
        # Regex que captura cada sección y su contenido hasta la siguiente sección o fin de texto
        pattern = re.compile(
            r"\*(COMPRAS EN INTERNET|PASAJES|ENCOMIENDAS|BASE LEGAL)\*\s*([\s\S]*?)(?=\*(?:COMPRAS EN INTERNET|PASAJES|ENCOMIENDAS|BASE LEGAL)\*|$)",
            re.IGNORECASE
        )
        matches = {m[0].upper(): m[1].strip() for m in pattern.findall(texto)}

        # Aseguramos el orden fijo
        secciones = ["COMPRAS EN INTERNET", "PASAJES", "ENCOMIENDAS", "BASE LEGAL"]
        resultado = []
        for sec in secciones:
            resultado.append({
                "seccion":  sec,
                "contenido": matches.get(sec, "")
            })

        return jsonify({
            "Status": "success",
            "data":   resultado
        })

    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj":    f"Ocurrió un error al obtener términos: {e}",
            "data":   []
        })


# END REGION TERMINOS Y CONDICIONES
@homeClientes_bp.route('/obtenerOrigenesDestinos',methods=['GET'])
def obtenerOrigenesDestinos():
    try:

        return {"data":[],"Msj":"Se ha obtenido correctamente los datos","Status":"success"}
    except Exception as e:
        return {"data":[],"Msj":f"Error al obtener los origenes:{repr(e)}","Status":"error"}

# END FUNCIONES

# REGIÓN COMPRA PASAJE
@homeClientes_bp.route('/buscarViajes',methods=['POST'])
def buscarViajes():
    try:
        datos_viaje_ida = []
        datos_viaje_vuelta = []

        origen = request.form.get('origen')
        destino = request.form.get('destino')
        fecha_ida = request.form.get('fecha_ida')
        fecha_vuelta = request.form.get('fecha_vuelta')
        datos_viaje_ida = Viaje.buscarViajePorRutaYFecha(origen=origen, destino=destino, fecha= fecha_ida)
        if fecha_vuelta:
            datos_viaje_vuelta = Viaje.buscarViajePorRutaYFecha(origen=origen, destino=destino, fecha= fecha_ida)
        return jsonify({
            "data_ida":datos_viaje_ida,
            "data_vuelta":datos_viaje_vuelta,
            "Msg":"Listado retornado correctamente",
            "Status": "success"
        })
    except Exception as e:
        return jsonify({
            "data_ida":datos_viaje_ida,
            "data_vuelta":datos_viaje_vuelta,
            "Msg":"Hubo un error al buscar los viajes; " + repr(e),
            "Status": "error"
        })


    

# END REGION COMPRA PASAJE

#REGION RESERVA
@homeClientes_bp.route("/listarTiposComprobante")
def listadoTiposComprobantes():
    try:
        listado = TipoComprobante.obtener_todos()
        return listado
    except Exception as e:
        return [e]

@homeClientes_bp.route("/listadoMetodosPago")
def listadoMetodosPago():
    try:
        listado = MetodoPago.obtener_todos()
        return listado
    except Exception as e:
        return [e]

@homeClientes_bp.route('/reservarPasaje', methods=["POST"])
def reservarPasaje():
    try:
        id_metodo_pago = request.form["metodo_pago"]
        id_tipo_comprobante = request.form["tipo_comprobante"]
        id_cliente = request.form["cliente"]
        id_promocion = request.form.get("promocion", 0)
        id_viaje = request.form["viaje"]
        codigo_aleatorio = random.randint(10**11, 10**12 - 1)

        resultado = Pasaje.registrarReserva(id_metodo_pago,id_tipo_comprobante,id_cliente,id_promocion,id_viaje,codigo_aleatorio)

        if resultado.get("msj"):
            #correoCliente = request.form["correo_cliente"]
            datosEnvio = {
                'asunto':'Reserva de pasaje Yatrax',
                'remitente': 'yatraxyatusa@gmail.com',
                'destinatario': "christiancubasjaramillo@gmail.com",
                'mensaje': 'El codigo de su reserva es : '+str(codigo_aleatorio)
            }

            enviar_correo(current_app.extensions['mail'],datosEnvio)

            return jsonify({"status": 1,"mensaje": resultado["msj"],"codigo_reserva":codigo_aleatorio})
        else:
            return jsonify({"status": 0,"mensaje": resultado.get("msj2", "Ocurrió un error inesperado.")})
    except Exception as e:
        return jsonify({"status": -1,"mensaje": "Ha ocurrido un error","error": repr(e)})

#END REGION