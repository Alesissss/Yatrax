import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.usuario import Usuario
from Models.conf_menus import Conf_Menus
from Models.conf_plantillas import Conf_Plantillas

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

@configuracion_bp.route('/GestionarPlantillas')
def Menu_Plantillas():
    return render_template('configuracion/plantillas.html', active_page="plantillas", active_menu='mConfiguracion')

@configuracion_bp.route('/PlantillaNuevo')
def Plantilla_Nuevo():
    return render_template('configuracion/plantillaCRUD.html', active_page="plantillas", active_menu='mConfiguracion', plantilla={}, tittle = 'Registrar plantilla', btnId = 'btn_Registrar')

# END VIEWS

# FUNCIONES

# REGION PERMISOS
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

# END REGION PERMISOS

# REGION PLANTILLAS
# Función para validar el tipo de archivo
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@configuracion_bp.route("/GetData_Plantillas", methods=["GET"])
def get_plantillas():
    try:
        plantillas = Conf_Plantillas.obtener_Plantillas()
        return jsonify({'data': plantillas, 'Status': 'success', 'Msj': 'Listado de plantillas retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar plantillas: + {repr(e)}'})
    
@configuracion_bp.route("/RegistrarPlantilla", methods=["POST"])
def registrar_plantilla():
    try:
        UPLOAD_FOLDER = "Static/img/plantillas/"
        nombre = request.form.get("nombre").strip()
        color_header = request.form.get("colorHeader").strip()
        color_footer = request.form.get("colorFooter").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        if not nombre or not color_header or not color_footer:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        ruta_logo = "/Static/img/plantillas/logo_yatusa.png"

        if 'logo' in request.files:
            logo = request.files['logo']

            if logo and allowed_file(logo.filename):
                extension = logo.filename.rsplit(".", 1)[1].lower()
                filename = f"{nombre}.{extension}"
                ruta_logo = f"/{UPLOAD_FOLDER}{filename}"

        mensajes = Conf_Plantillas.registrar(nombre, color_header, color_footer, ruta_logo, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            if 'logo' in request.files and logo and allowed_file(logo.filename):
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                logo.save(filepath)
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar plantilla'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/EliminarPlantilla/<int:id>", methods=['POST'])
def eliminar_plantilla(id):  # Recibe el ID de la URL
    try:
        mensajes = Conf_Plantillas.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar plantilla'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route('/EditarPlantilla/<int:id>', methods=['GET', 'POST'])
def editar_plantilla(id):
    try:
        UPLOAD_FOLDER = "Static/img/plantillas/"
        conf_plantilla = Conf_Plantillas.obtener_PlantillaPorId(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            color_header = request.form.get("colorHeader").strip()
            color_footer = request.form.get("colorFooter").strip()

            if not nombre or not color_header or not color_footer:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

            ruta_logo = conf_plantilla['logo'] if conf_plantilla and 'logo' in conf_plantilla else "/Static/img/plantillas/logo_yatusa.png"

            if 'logo' in request.files:
                logo = request.files['logo']
                
                if logo and allowed_file(logo.filename):
                    extension = logo.filename.rsplit(".", 1)[1].lower()
                    filename = f"{nombre}.{extension}"
                    ruta_logo = f"/{UPLOAD_FOLDER}{filename}"
            
            mensajes = Conf_Plantillas.editar(id, nombre, color_header, color_footer, ruta_logo)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                if 'logo' in request.files and logo and allowed_file(logo.filename):
                    filepath = os.path.join(UPLOAD_FOLDER, filename)
                    logo.save(filepath)
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar plantilla'})

        if conf_plantilla:
            return render_template('configuracion/plantillaCRUD.html', active_page="plantillas", active_menu='mConfiguracion', plantilla=conf_plantilla, tittle = 'Editar plantilla', btnId = 'btn_Editar')
        return render_template('configuracion/plantillaCRUD.html', active_page="plantillas", active_menu='mConfiguracion', plantilla={}, tittle = 'Editar plantilla', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@configuracion_bp.route("/VerPlantilla/<int:id>", methods=['GET'])
def ver_plantilla(id):
    try:
        conf_plantilla = Conf_Plantillas.obtener_PlantillaPorId(id)
        if conf_plantilla:
            return render_template('configuracion/plantillaCRUD.html', active_page="plantillas", active_menu='mConfiguracion', plantilla=conf_plantilla, tittle = 'Ver plantilla', btnId = 'btn_Aceptar')
        return render_template('configuracion/plantillaCRUD.html', active_page="plantillas", active_menu='mConfiguracion', plantilla={}, tittle = 'Ver plantilla', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION PLANTILLAS    

# END FUNCIONES