import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from datetime import datetime
from Models.tipoPersonal import TipoPersonal
from Models.personal import Personal
from Models.sancion import Sancion
from Models.personal_sancion import Personal_Sancion

personal_bp = Blueprint('personal', __name__, url_prefix='/trabajadores/personal')

# RESTRICCIONES
@personal_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 5 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_PERSONAL' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@personal_bp.route('/GestionarTipoPersonal')
def Menu_TipoPersonal():
    return render_template('personal/tipoPersonal.html', active_page="tipoPersonal", active_menu='mPersonal')

@personal_bp.route('/TipoPersonalNuevo')
def TipoPersonalNuevo():
    return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Registrar tipo personal', btnId='btn_Registrar')

@personal_bp.route('/GestionarPersonal')
def Menu_Personal():
    return render_template('personal/personal.html', active_page="personal", active_menu='mPersonal')

@personal_bp.route('/PersonalNuevo')
def PersonalNuevo():
    return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal={}, tittle='Registrar personal', btnId='btn_Registrar')

@personal_bp.route('/GestionarSancion')
def Menu_Incidencia():
    return render_template('personal/sancion.html', active_page="sancion", active_menu='mPersonal')

@personal_bp.route('/SancionNuevo')
def SancionNuevo():
    return render_template('personal/sancionCRUD.html', active_page="sancion", active_menu="mPersonal", sancion = {}, tittle='Registrar sanción', btnId='btn_Registrar')

@personal_bp.route('/GestionarSancionPersonal')
def Menu_SancionPersonal():
    return render_template('personal/sancionPersonal.html', active_page="sancionPersonal", active_menu="mPersonal")

@personal_bp.route('/SancionPersonalNuevo')
def SancionPersonalNuevo():
    return render_template('personal/sancionPersonalCRUD.html', active_page='sancionPersonal', active_menu='mPersonal', sancion_personal = {}, tittle = 'Registrar sanción a personal', btnId = 'btn_Registrar')

# END VIEWS

# FUNCIONES

# REGION TIPO PERSONAL

@personal_bp.route("/GetData_TipoPersonal", methods=["GET"])
def get_tiposPersonal():
    try:
        tiposPersonal = TipoPersonal.obtener_todos()
        return jsonify({'data': tiposPersonal, 'Status': 'success', 'Msj': 'Listado de tipos de personal retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar tipos de personal: {repr(e)}'})

@personal_bp.route("/RegistrarTipoPersonal", methods=["POST"])
def registrar_tipoPersonal():
    try:
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = TipoPersonal.registrar(nombre, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar tipo de personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/EliminarTipoPersonal/<int:id>", methods=['POST'])
def eliminar_tipoPersonal(id):
    try:
        mensajes = TipoPersonal.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar tipo de personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/EditarTipoPersonal/<int:id>", methods=['GET', 'POST'])
def editar_tipoPersonal(id):
    try:
        tipoPersonal = TipoPersonal.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado")
            
            mensajes = TipoPersonal.editar(id, nombre, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar tipo de personal'})

        if tipoPersonal:
            return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal=tipoPersonal, tittle='Editar tipo personal', btnId='btn_Editar')
        return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Editar tipo personal', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/VerTipoPersonal/<int:id>", methods=['GET'])
def ver_tipoPersonal(id):
    try:
        tipoPersonal = TipoPersonal.obtener_por_id(id)
        if tipoPersonal:
            return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal=tipoPersonal, tittle='Ver tipo personal', btnId='btn_Aceptar')
        return render_template('personal/tipoPersonalCRUD.html', active_page="tipoPersonal", active_menu='mPersonal', tipoPersonal={}, tittle='Ver tipo personal', btnId='btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/DarBajaTipoPersonal/<int:id>", methods=['POST'])
def darBaja_tipoPersonal(id):
    try:
        mensajes = TipoPersonal.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al tipo de personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO PERSONAL

# REGION SANCION #

@personal_bp.route("/GetData_Sancion", methods=["GET"])
def get_Sancion():
    try:
        sancion = Sancion.obtener_todos()
        return jsonify({'data': sancion, 'Status': 'success', 'Msj': 'Listado de sanciones retornada exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error inesperado al listar sanciones: {repr(e)}'})
    
@personal_bp.route("/RegistrarSancion", methods=["POST"])
def registrar_sancion():
    try:
        nombre = request.form.get("nombre").strip()
        descripcion = request.form.get("descripcion").strip()
        duracion = request.form.get("duracion").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        
        mensajes = Sancion.registrar(nombre, descripcion, duracion, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar sanción'})
    except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/EliminarSancion/<int:id>", methods=["POST"])
def eliminar_sancion(id):
    try:
        mensajes = Sancion.eliminar_sancion(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar tipo de usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@personal_bp.route("/EditarSancion/<int:id>", methods=["POST", "GET"])
def editar_sancion(id):
    try:
        sancion = Sancion.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            descripcion = request.form.get("descripcion").strip()
            duracion = request.form.get("duracion").strip()
            estado = request.form.get("estado")
            
            mensajes = Sancion.editar(id, nombre, descripcion, duracion, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar sanción'})
        if sancion:
            return render_template('personal/sancionCRUD.html', active_page = "sancion", active_menu = "mPersonal", sancion = sancion, tittle = 'Editar sanción', btnId = 'btn_Editar')
        return render_template('personal/sancionCRUD.html', active_page = "sancion", active_menu = "mPersonal", sancion = {}, tittle = 'Editar sanción', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/VerSancion/<int:id>", methods=['GET'])
def ver_sancion(id):
    try:
        sancion = Sancion.obtener_por_id(id)
        if sancion:
            return render_template('personal/sancionCRUD.html', active_page = "sancion", active_menu = "mPersonal", sancion = sancion, tittle = 'Ver sanción', btnId = 'btn_Editar')
        return render_template('personal/sancionCRUD.html', active_page = "sancion", active_menu = "mPersonal", sancion = {}, tittle = 'Ver sanción', btnId = 'btn_Editar')
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@personal_bp.route("/DarBajaSancion/<int:id>", methods=['POST'])
def darBajaSancion(id):
    try:
        mensajes = Sancion.darBaja(id)  
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja a la sanción'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    


# END REGION SANCION #

# REGION SANCION_PERSONAL #

@personal_bp.route("/GetData_SancionPersonal", methods = ["GET"])
def get_SancionPersonal():
    try:
        sp = Personal_Sancion.obtener_todos()

        # Convertir fecha_fin si es string
        for item in sp:
            if isinstance(item["fecha_fin"], str):
                try:
                    item["fecha_fin"] = datetime.strptime(item["fecha_fin"], "%Y-%m-%d")
                except ValueError:
                    item["fecha_fin"] = None  # O lanza una excepción si prefieres

        return jsonify({'data': sp, 'Status': 'success', 'Msj': 'Listado de sanciones a personal retornado exitosamente'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})


@personal_bp.route("/RegistrarSancionPersonal", methods=["POST"])
def registrar_sancionPersonal():
    try:
        personalid = request.form.get("personalid")
        sancionid = request.form.get("sancionid")
        descripcion = request.form.get("descripcion").strip()
        estado = request.form.get("estado")
        usuario = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Personal_Sancion.registrar(personalid, sancionid, descripcion, estado, usuario)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@personal_bp.route("/EditarSancionPersonal/<int:personalid>/<int:sancionid>", methods=["GET", "POST"])
def editar_personalSancion(personalid, sancionid):
    try:
        sancion_personal = Personal_Sancion.obtener_por_id(personalid, sancionid)

        sancion_personal = Personal_Sancion.obtener_por_id(personalid, sancionid)
        if sancion_personal and isinstance(sancion_personal["fecha_fin"], str):
            try:
                sancion_personal["fecha_fin"] = datetime.strptime(sancion_personal["fecha_fin"], "%Y-%m-%d")
            except ValueError:
                sancion_personal["fecha_fin"] = None  # O manejar el error como prefieras
        
        if request.method == "POST":
            descripcion = request.form.get("descripcion").strip()
            estado = request.form.get("estado")

            mensajes = Personal_Sancion.editar(personalid, sancionid, descripcion, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar sanción a personal'})

        if sancion_personal:
            return render_template('personal/sancionPersonalCRUD.html', active_page='sancionPersonal', active_menu='mPersonal', sancion_personal = sancion_personal, tittle='Editar sanción a personal', btnId='btn_Editar')
        return render_template('personal/sancionPersonalCRUD.html', active_page='sancionPersonal', active_menu='mPersonal', sancion_personal = {}, tittle='Editar sanción a personal', btnId='btn_Editar')

    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al editar sanción a personal: {repr(e)}'})
    
@personal_bp.route("/DarBajaPersonalSancion/<int:personalid>/<int:sancionid>", methods=['POST'])
def darBaja_personalSancion(personalid,sancionid):
    try:
        mensajes = Personal_Sancion.darBaja(personalid, sancionid)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja la sanción del personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@personal_bp.route("/EliminarPersonalSancion/<int:personalid>/<int:sancionid>", methods=['POST'])
def eliminar_personalSancion(personalid, sancionid):
    try:
        mensajes = Personal_Sancion.eliminar_sancion(personalid, sancionid)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar sanción de personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@personal_bp.route("/VerPersonalSancion/<int:personalid>/<int:sancionid>", methods=['GET'])
def ver_personalSancion(personalid, sancionid):
    try:
        # Obtener el personal por ID
        sancion_personal = Personal_Sancion.obtener_por_id(personalid, sancionid)
        
        # Si el personal existe, se pasa al template
        if sancion_personal:
            return render_template('personal/sancionPersonalCRUD.html', 
                                   active_page="sancionPersonal", 
                                   active_menu='mPersonal', 
                                   sancion_personal=sancion_personal, 
                                   tittle='Ver sanción a personal', 
                                   btnId='btn_Aceptar')
        # Si no se encuentra el personal, mostrar un formulario vacío
        return render_template('personal/sancionPersonalCRUD.html', 
                                   active_page="sancionPersonal", 
                                   active_menu='mPersonal', 
                                   sancion_personal={}, 
                                   tittle='Ver sanción a personal', 
                                   btnId='btn_Aceptar')
    except Exception as e:
        # En caso de error, devolver un mensaje en formato JSON
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
# END REGION SANCION_PERSONAL #

# REGION PERSONAL

# Obtener todos los registros de personal

@personal_bp.route("/GetData_Personal", methods=["GET"])
def get_Personal():
    try:
        personal = Personal.obtener_todos()
        return jsonify({'data': personal, 'Status': 'success', 'Msj': 'Listado de personal retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar personal: {repr(e)}'})

# Registrar nuevo personal
@personal_bp.route("/RegistrarPersonal", methods=["POST"])
def registrar_personal():
    try:
        nombre = request.form.get("nombre").strip()
        apePat = request.form.get("apePat").strip()
        apeMat = request.form.get("apeMat").strip()
        estado = request.form.get("estado")
        idTipoPersonal = request.form.get("idTipoPersonal")
        imagen = request.files.get("imagen")  # Recibir la imagen (archivo)

        # Guardar la imagen si es que se sube
        if imagen:
            imagen_path = os.path.join("Static/img/personal", imagen.filename)
            imagen.save(imagen_path)
            imagen_path = '/' + imagen_path
        else:
            imagen_path = ""

        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Personal.registrar(nombre, apePat, apeMat, imagen_path, estado, idTipoPersonal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Editar un registro de personal
@personal_bp.route("/EditarPersonal/<int:id>", methods=['GET', 'POST'])
def editar_personal(id):
    try:
        personal = Personal.obtener_por_id(id)
        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            apePat = request.form.get("apePat").strip()
            apeMat = request.form.get("apeMat").strip()
            estado = request.form.get("estado")
            idTipoPersonal = request.form.get("idTipoPersonal")
            imagen = request.files.get("imagen")  # Recibir la imagen (archivo)

            # Guardar la imagen si es que se sube
            if imagen:
                imagen_path = os.path.join("Static/img/personal", imagen.filename)
                imagen.save(imagen_path)
                imagen_path = '/' + imagen_path
            else:
                imagen_path = personal['imagen']  # Mantener la imagen actual si no se sube una nueva

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            mensajes = Personal.editar(id, nombre, apePat, apeMat, imagen_path, estado, idTipoPersonal)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar personal'})

        if personal:
            return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal=personal, tittle='Editar personal', btnId='btn_Editar')
        return render_template('personal/personalCRUD.html', active_page="personal", active_menu='mPersonal', personal={}, tittle='Editar personal', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Dar de baja a un personal
@personal_bp.route("/DarBajaPersonal/<int:id>", methods=['POST'])
def darBaja_personal(id):
    try:
        mensajes = Personal.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al personal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Eliminar un registro de personal
@personal_bp.route("/EliminarPersonal/<int:id>", methods=['POST'])
def eliminar_personal(id):
    try:
        mensajes = Personal.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar personal'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@personal_bp.route("/VerPersonal/<int:id>", methods=['GET'])
def ver_personal(id):
    try:
        # Obtener el personal por ID
        personal = Personal.obtener_por_id(id)
        
        # Si el personal existe, se pasa al template
        if personal:
            return render_template('personal/personalCRUD.html', 
                                   active_page="personal", 
                                   active_menu='mPersonal', 
                                   personal=personal, 
                                   tittle='Ver personal', 
                                   btnId='btn_Aceptar')
        # Si no se encuentra el personal, mostrar un formulario vacío
        return render_template('personal/personalCRUD.html', 
                               active_page="personal", 
                               active_menu='mPersonal', 
                               personal={}, 
                               tittle='Ver personal', 
                               btnId='btn_Aceptar')
    except Exception as e:
        # En caso de error, devolver un mensaje en formato JSON
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})



#END REGION PERSONAL

# END FUNCIONES