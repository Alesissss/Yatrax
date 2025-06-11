import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.usuario import Usuario
from Models.tipoUsuario import TipoUsuario
from Models.metodo_pago import MetodoPago
from Models.conf_menus import Conf_Menus
from Models.conf_claims import Conf_Claims
from Models.conf_plantillas import Conf_Plantillas
from Models.tipoMetodoPago import TipoMetodoPago
from Models.terminos_condiciones import TerminosCondiciones
from Models.preguntas_frecuentes import PreguntasFrecuentes
from Models.promocion import Promocion
from werkzeug.utils import secure_filename

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

    if 2 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_CONFIGURACION' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

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

@configuracion_bp.route('/GestionarPromociones')
def Menu_Promociones():
    return render_template('configuracion/promociones.html', active_page="promociones", active_menu='mConfiguracion')

@configuracion_bp.route('/Menu_TipoMetodoPago')
def Menu_TipoMetodoPago():
    return render_template('configuracion/tipoMetodoPago.html', active_page="TipometodosPago", active_menu='mConfiguracion')


@configuracion_bp.route('/TipoMetodoPagoNuevo')
def Menu_TipoServicioNuevo():
    return render_template('configuracion/tipoMetodoPagoCRUD.html', active_page="TipometodosPago", active_menu='mConfiguracion', tipoMetodoPago = {}, tittle = 'Registrar tipo de metodo de Pago', btnId = 'btn_Registrar')

@configuracion_bp.route('/GestionarTerminosCondiciones')
def Menu_TerminosCondiciones():
    return render_template('configuracion/terminosYCondiciones.html', active_page="terminosCondiciones", active_menu='mConfiguracion')

@configuracion_bp.route('/TerminosCondicionesNuevo')
def TerminosCondiciones_Nuevo():
    return render_template('configuracion/terminosYCondicionesCRUD.html', active_page="terminosCondiciones", active_menu='mConfiguracion', terminosCondiciones={}, tittle = 'Registrar términos y condiciones', btnId = 'btn_Registrar')

@configuracion_bp.route('/GestionarPreguntasFrecuentes')
def Menu_PreguntasFrecuentes():
    return render_template('configuracion/preguntasFrecuentes.html', active_page="preguntasFrecuentes", active_menu='mConfiguracion')

@configuracion_bp.route('/PreguntasFrecuentesNuevo')
def PreguntasFrecuentes_Nuevo():
    return render_template('configuracion/preguntasFrecuentesCRUD.html', active_page="preguntasFrecuentes", active_menu='mConfiguracion', preguntaFrecuente={}, tittle = 'Registrar pregunta frecuente', btnId = 'btn_Registrar')

@configuracion_bp.route('/PromocionNuevo')
def PromocionNuevo():
    return render_template('configuracion/promocionCRUD.html', active_page="promociones", active_menu = 'mConfiguracion', promocion = {}, tittle = 'Registrar promocion', btnId = 'btn_Registrar')

# END VIEWS

# FUNCIONES

# REGION PERMISOS
@configuracion_bp.route("/GetData_TiposUsuario", methods=["GET"])
def get_tipoUsuarios():
    try:
        tiposUsuario = TipoUsuario.obtener_todos()
        return jsonify({'data': tiposUsuario, 'Status': 'success', 'Msj': 'Listado de tipos de usuario retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de usuarios: + {repr(e)}'})

@configuracion_bp.route('/EditarPermisos/<int:id>', methods=['GET', 'POST'])
def Editar_Permisos(id):
    try:
        tipoUsuario = TipoUsuario.obtener_por_id(id)

        dmnus = TipoUsuario.obtener_menus(id)
        menus = Conf_Menus.obtener_todos()

        dclaims = TipoUsuario.obtener_claims(id)
        claims = Conf_Claims.obtener_todos()

        dmnus_ids = [menu['id'] for menu in dmnus]
        dclaims_ids = [claim['id'] for claim in dclaims]

        # menus_jerarquicos = []
        # for menu in menus:
        #     # Menú principal
        #     if menu['idPadre'] is None:
        #         menu['submenus'] = []
        #         menus_jerarquicos.append(menu)
        #     else:
        #         # Submenú
        #         parent_menu = next((m for m in menus_jerarquicos if m['id'] == menu['idPadre']), None)
        #         if parent_menu:
        #             parent_menu['submenus'].append(menu)

        menus_jerarquicos = construir_menu_con_claims(menus, claims)

        if request.method == 'POST':
            idMenu = int(request.form.get('idMenu').strip())
            idTipoUsuario = int(request.form.get('idTipoUsuario').strip())
            accion = int(request.form.get('accion').strip())
            esClaim = int(request.form.get('esClaim').strip())

            if esClaim == 0:
                
                if accion == 1:
                    mensajes = TipoUsuario.agregar_menu(idMenu, idTipoUsuario)
                    msj1 = mensajes.get('@MSJ')
                    msj2 = mensajes.get('@MSJ2')
                else:
                    mensajes = TipoUsuario.eliminar_menu(idMenu, idTipoUsuario)
                    msj1 = mensajes.get('@MSJ')
                    msj2 = mensajes.get('@MSJ2')

            elif esClaim == 1:

                if accion == 1:
                    mensajes = TipoUsuario.agregar_claim(idMenu, idTipoUsuario)
                    msj1 = mensajes.get('@MSJ')
                    msj2 = mensajes.get('@MSJ2')
                else:
                    mensajes = TipoUsuario.eliminar_claim(idMenu, idTipoUsuario)
                    msj1 = mensajes.get('@MSJ')
                    msj2 = mensajes.get('@MSJ2')
            
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar permisos'})

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar permisos'})

        if tipoUsuario:
            return render_template('configuracion/permisosEditar.html', active_page="permisos", active_menu='mConfiguracion', tipoUsuario=tipoUsuario, dmnus=dmnus, dmnus_ids=dmnus_ids, dclaims=dclaims, dclaims_ids=dclaims_ids, menus=menus_jerarquicos)
        return render_template('configuracion/permisosEditar.html', active_page="permisos", active_menu='mConfiguracion', tipoUsuario={}, dmnus=[], dmnus_ids=[], dclaims=[], dclaims_ids=[], menus=[])

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

def construir_menu_con_claims(menus, claims):
    menu_dict = {m['id']: {**m, 'submenus': []} for m in menus}
    jerarquia = []

    for menu in menu_dict.values():
        id_padre = menu.get('idPadre')
        if id_padre is None:
            # Menú principal
            jerarquia.append(menu)
        else:
            # Submenú (nivel 2)
            padre = menu_dict.get(id_padre)
            if padre:
                padre['submenus'].append(menu)

    for claim in claims:
        id_padre = claim.get('idPadre')
        if id_padre in menu_dict:
            padre = menu_dict[id_padre]
            if 'submenus' in padre:
                padre['submenus'].append(claim)
            else:
                padre['submenus'] = [claim]

    return jerarquia

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

@configuracion_bp.route("/ActivarPlantilla/<int:id>", methods=['POST'])
def activar_plantilla(id):  # Recibe el ID de la URL
    try:
        mensajes = Conf_Plantillas.activar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al activar plantilla'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION PLANTILLAS    

#REGION METODOS DE PAGO
@configuracion_bp.route('/GestionarMetodosPago')
def Menu_MetodosPago():
    # Captura el mensaje de la URL, si existe
    msg = request.args.get('msg', '')
    tipotoast = request.args.get('tipotoast', '')
    return render_template('configuracion/metodos_pago.html', active_page="metodosPago", active_menu='mConfiguracion', msg=msg, tipotoast=tipotoast)

# Ruta para registrar un nuevo método de pago
@configuracion_bp.route('/MetodoPagoNuevo', methods=['GET', 'POST'])
def MetodoPago_Nuevo():
    if request.method == 'POST':
        return registrar_metodo_pago()
    
    return render_template('configuracion/metodo_pago_crud.html',
                           tittle="Registrar método de pago", 
                           btnId="btn_Registrar",
                           active_menu='mConfiguracion',
                           active_page='metodosPago',
                           metodo_pago=None)

# Ruta para editar y ver un método de pago (con id)
@configuracion_bp.route("/MetodoPagoNuevo/<int:id>", methods=['GET', 'POST'])
def MetodoPago_Editar_Ver(id):
    metodo_pago = MetodoPago.obtener_por_id(id)
    if metodo_pago is None:
        return jsonify({"Status": "error", "Msj": "Método de pago no encontrado"})
    
    ver = request.args.get('ver', False)  # Verificar si el acceso es solo para ver
    return render_template('configuracion/metodo_pago_crud.html', 
                           metodo_pago=metodo_pago, 
                           tittle="Ver método de pago" if ver else "Editar método de pago", 
                           btnId="btn_Editar" if not ver else "btn_Ver", 
                           ver=ver)

# Función para registrar el nuevo método de pago
@configuracion_bp.route('/RegistrarMetodoPago', methods=["POST"])
def registrar_metodo_pago():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado").strip()
        logo = request.files.get("logo")
        tipo_pago = request.form.get("tipo_pago").strip()
        logo = request.files.get("logo")
        if not nombre or not nombre.strip():
            return jsonify({"Status": "error", "Msj": "El nombre es obligatorio."})
        if not estado or not estado.strip():
            return jsonify({"Status": "error", "Msj": "El estado es obligatorio."})

        if logo:
            logo_filename = secure_filename(logo.filename)
            logo_path = f"/Static/img/metodos_pago/logo/{logo_filename}"
            logo.save(os.path.join("Static/img/metodos_pago/logo/", logo_filename))
        else:
            logo_path = "/Static/img/metodos_pago/logo/default_metodopago.png"  # Logo por defecto
        qr = request.files.get("qr")
        if qr:
            qr_filename = secure_filename(qr.filename)
            qr_path = f"/Static/img/metodos_pago/qr/{qr_filename}"
            qr.save(os.path.join("Static/img/metodos_pago/qr", qr_filename))
        else:
            qr_path = None
            
        mensajes = MetodoPago.registrar(nombre, logo_path, estado, session.get('usuario', {}).get('email', 'SIN USUARIO').strip(), tipo_pago, qr_path)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return redirect(url_for('configuracion.Menu_MetodosPago', msg=msj1 ,tipotoast='success'))
        elif msj2:
            return redirect(url_for('configuracion.Menu_MetodosPago', msg=msj2, tipotoast='error'))
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar el metodo de pago'})
        # Redirigir con un mensaje de éxito

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

# Ruta para editar un método de pago
@configuracion_bp.route("/EditarMetodoPago/<int:id>", methods=['GET', 'POST'])
def editar_metodo_pago(id):
    metodo_pago = MetodoPago.obtener_por_id(id)
    tipos_pago = TipoMetodoPago.obtener_todos()
    if metodo_pago is None:
        return jsonify({"Status": "error", "Msj": "Método de pago no encontrado"})
    
    if request.method == 'POST':
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado").strip()
        tipo_pago = request.form.get("tipo_pago").strip()
        logo = request.files.get("logo")
        if not nombre or not estado:
            return jsonify({"Status": "error", "Msj": "Nombre y estado son obligatorios"})

        if logo:
            logo_filename = secure_filename(logo.filename)
            logo_path = f"/Static/img/metodos_pago/{logo_filename}"
            logo.save(os.path.join("Static/img/metodos_pago", logo_filename))
        else:
            logo_path = metodo_pago['logo']
            
        qr = request.files.get("qr")
        if qr:
            qr_filename = secure_filename(qr.filename)
            qr_path = f"/Static/img/metodos_pago/qr/{qr_filename}"
            qr.save(os.path.join("Static/img/metodos_pago/qr", qr_filename))
        else:
            qr_path = metodo_pago['qr']
            
        mensajes = MetodoPago.editar(id, nombre, logo_path, estado, tipo_pago, qr_path)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return redirect(url_for('configuracion.Menu_MetodosPago', msg=msj1 ,tipotoast='success'))
        elif msj2:
            return redirect(url_for('configuracion.Menu_MetodosPago', msg=msj2, tipotoast='error'))
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar el metodo de pago'})
        # Redirigir con un mensaje de éxito
    return render_template('configuracion/metodo_pago_crud.html', metodo_pago=metodo_pago, tipos_metodo_pago=tipos_pago, tittle="Editar método de pago", btnId="btn_Editar")

# Ruta para eliminar un método de pago
@configuracion_bp.route("/EliminarMetodoPago/<int:id>", methods=['POST'])
def eliminar_metodo_pago(id):
    try:
        mensajes = MetodoPago.eliminar(id)
        return jsonify(mensajes)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

# Ruta para obtener todos los métodos de pago
@configuracion_bp.route("/GetData_MetodosPago", methods=['GET'])
def get_metodos_pago():
    try:
        metodos_pago = MetodoPago.obtener_todos()
        if metodos_pago:
            return jsonify({"Status": "success", "data": metodos_pago})
        return jsonify({"Status": "info", "Msj": "Aun no hay metodos de pago registrados"})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener los métodos de pago: {repr(e)}"})


@configuracion_bp.route("/dar_baja_metodo_pago/<int:id>", methods=["POST"])
def dar_baja_metodo_pago(id):
    try:
        # Ejecutar el procedimiento almacenado
        mensajes = MetodoPago.darBaja(id)  # Asegúrate de que esta función esté llamando al SP correctamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al metodo de pago'})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

# ENG REGION METODOS DE PAGO

# REGION TIPO METODO PAGO

@configuracion_bp.route("/RegistrarTipoMetodoPago", methods=["POST"])
def registrar_tipo_metodo_pago():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')
        if not nombre or not estado:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = TipoMetodoPago.registrar(nombre, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1})
        elif msj2:
            return jsonify({"Status": "error", 'Msj': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar tipo método de pago'})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

@configuracion_bp.route("/EditarTipoMetodoPago/<int:id>", methods=['GET', 'POST'])
def editar_tipo_metodo_pago(id):
    try:
        tipoMetodoPago = TipoMetodoPago.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado").strip()
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            if not nombre or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            estado = estado == "1"  # Convertimos a booleano para SP

            mensajes = TipoMetodoPago.editar(id, nombre, estado, usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar el tipo de método de pago"})

        if tipoMetodoPago:
            return render_template('configuracion/tipoMetodoPagoCRUD.html',
                                   active_page='tipoMetodoPago',
                                   active_menu='mConfiguracion',
                                   tipoMetodoPago=tipoMetodoPago,
                                   tittle='Editar tipo método de pago',
                                   btnId='btn_Editar')
        return render_template('configuracion/tipoMetodoPagoCRUD.html',
                               active_page='tipoMetodoPago',
                               active_menu='mConfiguracion',
                               tipoMetodoPago={},
                               tittle='Editar tipo método de pago',
                               btnId='btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@configuracion_bp.route("/VerTipoMetodoPago/<int:id>", methods=['GET'])
def ver_TipoMetodoPago(id):
    try:
        tipo_metodo_pago  = TipoMetodoPago.obtener_por_id(id)
        if tipo_metodo_pago :
            return render_template('configuracion/tipoMetodoPagoCRUD.html', active_page="tipoMetodoPago", active_menu='mConfiguracion', tipoMetodoPago=tipo_metodo_pago , tittle='Ver tipo metodo Pago', btnId='btn_Aceptar')
        return render_template('configuracion/tipoMetodoPagoCRUD.html', active_page="tipoMetodoPago", active_menu='mConfiguracion', tipoMetodoPago={}, tittle='Ver tipo metodo Pago', btnId='btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/DarBajaTipoMetodoPago/<int:id>", methods=['POST'])
def darBaja_TipoMetodoPago(id):
    try:
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')
        mensajes = TipoMetodoPago.darBaja(id,usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja el tipo de método de pago'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/EliminarTipoMetodoPago/<int:id>", methods=['POST'])
def eliminar_TipoMetodoPago(id):
    try:
        mensajes = TipoMetodoPago.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja el tipo de método de pago'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})



@configuracion_bp.route("/GetData_TipoMetodoPago", methods=["GET"])
def get_tipo_metodos_pago():
    try:
        metodos = TipoMetodoPago.obtener_todos()
        if metodos:
            return jsonify({"Status": "success", "data": metodos})
        return jsonify({"Status": "info", "Msj": "Aún no hay tipos de métodos de pago registrados", "data": []})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener los tipos de métodos de pago: {repr(e)}", "data": []})

# END REGION TIPO METODO PAGO

# REGION PREGUNTAS FRECUENTES

@configuracion_bp.route("/RegistrarPreguntaFrecuente", methods=["POST"])
def registrar_pregunta_frecuente():
    try:
        pregunta = request.form.get("pregunta").strip()
        respuesta = request.form.get("respuesta").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')
        
        if not pregunta or not respuesta or not estado:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = PreguntasFrecuentes.registrar(pregunta, respuesta, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1})
        elif msj2:
            return jsonify({"Status": "error", 'Msj': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar pregunta frecuente'})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

@configuracion_bp.route("/EditarPreguntaFrecuente/<int:id>", methods=['GET', 'POST'])
def editar_pregunta_frecuente(id):
    try:
        pregunta_frecuente = PreguntasFrecuentes.obtener_por_id(id)
        if request.method == 'POST':
            pregunta = request.form.get("pregunta").strip()
            respuesta = request.form.get("respuesta").strip()
            estado = request.form.get("estado").strip()
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            if not pregunta or not respuesta or estado not in ["0", "1"]:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios y válidos"})

            estado = estado == "1"  # Convertimos a booleano para SP

            mensajes = PreguntasFrecuentes.editar(id, pregunta, respuesta, estado, usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
            elif msj2:
                return jsonify({"Status": "success", "Msj": "", "Msj2": msj2})
            else:
                return jsonify({"Status": "error", "Msj": "Error desconocido al actualizar la pregunta frecuente"})

        if pregunta_frecuente:
            return render_template('configuracion/preguntasFrecuentesCRUD.html',
                                   active_page='preguntasFrecuentes',
                                   active_menu='mConfiguracion',
                                   preguntaFrecuente=pregunta_frecuente,
                                   tittle='Editar pregunta frecuente',
                                   btnId='btn_Editar')
        return render_template('configuracion/preguntasFrecuentesCRUD.html',
                               active_page='preguntasFrecuentes',
                               active_menu='mConfiguracion',
                               preguntaFrecuente={},
                               tittle='Editar pregunta frecuente',
                               btnId='btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})

@configuracion_bp.route("/VerPreguntaFrecuente/<int:id>", methods=['GET'])
def ver_pregunta_frecuente(id):
    try:
        pregunta_frecuente = PreguntasFrecuentes.obtener_por_id(id)
        if pregunta_frecuente:
            return render_template('configuracion/preguntasFrecuentesCRUD.html', 
                                 active_page="preguntasFrecuentes", 
                                 active_menu='mConfiguracion', 
                                 preguntaFrecuente=pregunta_frecuente, 
                                 tittle='Ver pregunta frecuente', 
                                 btnId='btn_Aceptar')
        return render_template('configuracion/preguntasFrecuentesCRUD.html', 
                             active_page="preguntasFrecuentes", 
                             active_menu='mConfiguracion', 
                             preguntaFrecuente={}, 
                             tittle='Ver pregunta frecuente', 
                             btnId='btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/DarBajaPreguntaFrecuente/<int:id>", methods=['POST'])
def dar_baja_pregunta_frecuente(id):
    try:
        estado = PreguntasFrecuentes.obtener_por_id(id)
        
        if estado['estado'] == 0:
            return jsonify({"Status": "error", 'Msj': 'La pregunta frecuente ya está NO VIGENTE'})
        
        mensajes = PreguntasFrecuentes.dar_baja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja la pregunta frecuente'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/EliminarPreguntaFrecuente/<int:id>", methods=['POST'])
def eliminar_pregunta_frecuente(id):
    try:
        mensajes = PreguntasFrecuentes.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar la pregunta frecuente'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/GetData_PreguntasFrecuentes", methods=["GET"])
def get_preguntas_frecuentes():
    try:
        preguntas = PreguntasFrecuentes.obtener_todos()
        if preguntas:
            return jsonify({"Status": "success", "data": preguntas})
        return jsonify({"Status": "info", "Msj": "Aún no hay preguntas frecuentes registradas", "data": []})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener las preguntas frecuentes: {repr(e)}", "data": []})

# END REGION PREGUNTAS FRECUENTES

# REGION TERMINOS Y CONDICIONES
def allowed_file_txt(filename):
    ALLOWED_EXTENSIONS = {"txt"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def validar_estructura_txt(texto):
    """
    Verifica que el texto contenga exactamente, en este orden,
    las cuatro secciones marcadas con asteriscos.
    """
    secciones = ["COMPRAS EN INTERNET", "PASAJES", "ENCOMIENDAS", "BASE LEGAL"]
    indices = []
    for sec in secciones:
        marcador = f"*{sec}*"
        pos = texto.find(marcador)
        if pos == -1:
            return False, f"No se encontró la sección «{marcador}»."
        indices.append(pos)
    # Comprueba el orden
    if indices != sorted(indices):
        return False, "Las secciones no están en el orden correcto."
    return True, ""

@configuracion_bp.route("/GetData_Terminos", methods=["GET"])
def get_terminos():
    try:
        terminos = TerminosCondiciones.obtener_todos()
        return jsonify({'data': terminos, 'Status': 'success', 'Msj': 'Listado de términos y condiciones retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar términos y condiciones: + {repr(e)}'})

@configuracion_bp.route("/RegistrarTerminos", methods=["POST"])
def registrar_terminos():
    try:
        UPLOAD_FOLDER = "Static/utilities/terminos_condiciones/"
        nombre         = request.form.get("nombre", "").strip()
        archivo_file   = request.files.get('archivo')
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

        if not nombre:
            return jsonify({"Status": "error", "Msj": "El nombre es obligatorio"})
        if not archivo_file or not allowed_file_txt(archivo_file.filename):
            return jsonify({"Status": "error", "Msj": "Debe seleccionar un archivo TXT válido"})

        # Leer el contenido del archivo para validar la estructura
        contenido = archivo_file.read().decode('utf-8')
        valido, mensaje = validar_estructura_txt(contenido)
        if not valido:
            return jsonify({"Status": "error", "Msj": mensaje})
        
        # Guardar el fichero físico
        archivo_file.seek(0)  # Reiniciar el puntero del archivo
        extension = archivo_file.filename.rsplit(".", 1)[1].lower()
        filename  = f"{nombre}.{extension}"
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        path      = os.path.join(UPLOAD_FOLDER, filename)
        archivo_file.save(path)

        # Registrar en BD sólo el nombre de fichero
        mensajes = TerminosCondiciones.registrar(nombre, filename, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        if msj1:
            return jsonify({"Status": "success", "Msj": msj1, "Msj2": ""})
        else:
            return jsonify({"Status": "error", "Msj": "", "Msj2": msj2})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {e}"})
    
@configuracion_bp.route("/EliminarTerminos/<int:id>", methods=['POST'])
def eliminar_terminos(id):
    try:
        mensajes = TerminosCondiciones.eliminar(id)
        msj = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj:
            return jsonify({"Status": "success", 'Msj': msj, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar términos y condiciones'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route('/EditarTerminos/<int:id>', methods=['GET', 'POST'])
def editar_terminos(id):
    try:
        UPLOAD_FOLDER = "Static/utilities/terminos_condiciones/"
        
        termino = TerminosCondiciones.obtener_por_id(id)  # método correcto
        contenido = ""
        
        if request.method == "GET" and termino and termino.get('archivo'):
            path = os.path.join(UPLOAD_FOLDER, termino['archivo'])
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    contenido = f.read()
        
        if request.method == 'POST':
            nombre       = request.form.get("nombre", "").strip()
            archivo_file = request.files.get('archivo')
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            if not nombre:
                return jsonify({"Status": "error", "Msj": "El nombre es obligatorio"})

            # Determinar si subieron un nuevo TXT o mantenemos el existente
            if archivo_file and allowed_file_txt(archivo_file.filename):
                contenido_txt = archivo_file.read().decode('utf-8')
                valido, mensaje = validar_estructura_txt(contenido_txt)
                if not valido:
                    return jsonify({"Status": "error", "Msj": mensaje})
                archivo_file.seek(0)
                extension = archivo_file.filename.rsplit(".", 1)[1].lower()
                filename  = f"{nombre}.{extension}"
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                archivo_file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                filename = termino['archivo']

            mensajes = TerminosCondiciones.editar(id, nombre, filename, usuario_actual)
            msj = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')
            if msj:
                return jsonify({"Status": "success", "Msj": msj})
            else:
                return jsonify({"Status": "success", "Msj2": msj2})
        
        if termino:
            return render_template('configuracion/terminosYCondicionesCRUD.html', 
                                 active_page="terminosCondiciones", 
                                 active_menu='mConfiguracion', 
                                 termino=termino,
                                 contenido=contenido, 
                                 tittle='Editar términos y condiciones', 
                                 btnId='btn_Editar')
        return render_template('configuracion/terminosYCondicionesCRUD.html', 
                             active_page="terminosCondiciones", 
                             active_menu='mConfiguracion', 
                             termino={}, 
                             contenido={}, 
                             tittle='Editar términos y condiciones', 
                             btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 
                        'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/VerTerminos/<int:id>", methods=['GET'])
def ver_terminos(id):
    try:
        UPLOAD_FOLDER = "Static/utilities/terminos_condiciones/"
        termino = TerminosCondiciones.obtener_por_id(id)
        contenido = ""

        if termino and termino.get('archivo'):
            path = os.path.join(UPLOAD_FOLDER, termino['archivo'])
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    contenido = f.read()
        if termino:
            return render_template('configuracion/terminosYCondicionesCRUD.html', 
                                 active_page="terminosCondiciones", 
                                 active_menu='mConfiguracion', 
                                 termino=termino, 
                                 contenido=contenido,
                                 tittle='Ver términos y condiciones', 
                                 btnId='btn_Aceptar')
        return render_template('configuracion/terminosYCondicionesCRUD.html', 
                             active_page="terminosCondiciones", 
                             active_menu='mConfiguracion', 
                             termino={},
                             contenido={},
                             tittle='Ver términos y condiciones', 
                             btnId='btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@configuracion_bp.route("/ActivarTerminos/<int:id>", methods=['POST'])
def activar_terminos(id):
    try:
        mensajes = TerminosCondiciones.activar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al activar términos y condiciones'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TERMINOS Y CONDICIONES
# REGION PROMOCIONES
@configuracion_bp.route("/GetData_Promociones", methods=["GET"])
def get_promociones():
    try:
        promociones = Promocion.obtener_todos()
        if promociones:
            return jsonify({"Status": "success", "data": promociones})
        return jsonify({"Status": "info", "Msj": "Aún no hay tipos de métodos de pago registrados", "data": []})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener los tipos de métodos de pago: {repr(e)}", "data": []})
    
    
@configuracion_bp.route("/RegistrarPromocion", methods=["POST"])
def registrar_promocion():
    try:
        nombre = request.form.get("nombre", "").strip()
        codigo = request.form.get("codigo", "").strip()
        monto_promo = request.form.get("monto_promo", "").strip()
        fecha_inicio = request.form.get("fecha_inicio", "").strip()
        fecha_fin = request.form.get("fecha_fin", "").strip()
        estado = request.form.get("estado", "").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

        # Validaciones básicas
        if not all([nombre, codigo, monto_promo, fecha_inicio, fecha_fin, estado]):
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        # Validar formato decimal
        try:
            monto_promo = float(monto_promo)
        except ValueError:
            return jsonify({"Status": "error", "Msj": "Monto de promoción inválido"})

        # Llamar al modelo
        mensajes = Promocion.registrar(nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo)

        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", "Msj": msj1})
        elif msj2:
            return jsonify({"Status": "error", "Msj": msj2})
        else:
            return jsonify({"Status": "error", "Msj": "Error desconocido al registrar promoción"})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


@configuracion_bp.route("/EliminarPromocion/<int:id>", methods=["POST"])
def eliminar_promocion(id):
    try:
        promocion = Promocion.obtener_por_id(id)
        
        if not promocion:
            return jsonify({"Status": "error", "Msj": "Promoción no encontrada"})

        mensajes = Promocion.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar la promoción'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f"Ocurrió un error inesperado: {repr(e)}"})


@configuracion_bp.route("/DarBajaPromocion/<int:id>", methods=["POST"])
def dar_baja_promocion(id):
    try:
        promocion = Promocion.obtener_por_id(id)
        
        if not promocion:
            return jsonify({"Status": "error", "Msj": "Promoción no encontrada"})
        
        if promocion['estado'] == 0:
            return jsonify({"Status": "info", "Msj": "La promoción ya está inactiva"})

        mensajes = Promocion.dar_baja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja la promoción'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f"Ocurrió un error inesperado: {repr(e)}"})

# END FUNCIONES