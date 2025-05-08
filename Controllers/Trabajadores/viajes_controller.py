import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.nivel import Nivel
from Models.tipoVehiculo import TipoVehiculo
from Models.vehiculo import Vehiculo
from Models.sucursal import Sucursal
from Models.horario import Horario
from Models.ubigeo import Ubigeo
from Models.marca import Marca
from Models.ruta import Ruta
from werkzeug.utils import secure_filename

viajes_bp = Blueprint('viajes', __name__, url_prefix='/trabajadores/viajes')

# ERRORES 
# # Manejar errores 401 (Página no autorizada)
# @viajes_bp.errorhandler(401)
# def error_401(error):
#     return render_template("error.html", error="Página no autorizada"), 401

# # Manejar errores 403 (Página no autorizada para este usuario)
# @viajes_bp.errorhandler(403)
# def error_403(error):
#     return render_template("error.html", error="Página restringida"), 403

# # Manejar errores 404 (Página no encontrada)
# @viajes_bp.errorhandler(404)
# def error_404(error):
#     return render_template("error.html", error="Página no encontrada"), 404

# # Manejar errores 500 (Error interno del servidor)
# @viajes_bp.errorhandler(500)
# def error_500(error):
#     return render_template("error.html", error="Error interno del servidor"), 500

# # Manejar cualquier otro error genérico
# @viajes_bp.errorhandler(Exception)
# def error_general(error):
#     return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@viajes_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 4 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_VIAJES' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@viajes_bp.route('/GestionarHorarios')
def Menu_Horarios():
    return render_template('viajes/horarios.html', active_page="horarios", active_menu='mViajes')

@viajes_bp.route('/GestionarTipoVehiculo')
def Menu_TipoVehiculo():
    return render_template('viajes/tipoVehiculo.html', active_page="tipoVehiculo", active_menu='mViajes')

@viajes_bp.route('/GestionarVehiculo')
def Menu_Vehiculo():
    return render_template('viajes/vehiculo.html', active_page="tipoVehiculo", active_menu='mViajes')

@viajes_bp.route('/GestionarSucursal')
def Menu_Sucursal():
    return render_template('viajes/sucursal.html', active_page="sucursal", active_menu='mViajes')

@viajes_bp.route('/SucursalNueva')
def SucursalNueva():
    return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal={}, tittle = 'Registrar sucursal', btnId = 'btn_Registrar')

@viajes_bp.route('/GestionarNivel')
def Menu_Nivel():
    return render_template('viajes/nivel.html', active_page="nivel", active_menu='mViajes')

@viajes_bp.route('/GestionarRutas')
def Menu_Rutas():
    return render_template('viajes/ruta.html', active_page="ruta", active_menu='mViajes')

@viajes_bp.route('/RutaNuevo')
def TipoUsuario_Nuevo():
    return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta={}, tittle = 'Registrar ruta', btnId = 'btn_Registrar')

# @viajes_bp.route('/GestionarMarcas')
# def Menu_Marcas():
#     return render_template('viajes/marcas.html', active_page="marcas", active_menu='mViajes')

# END VIEWS

# FUNCIONES

# REGION NIVEL
@viajes_bp.route("/GetData_Nivel", methods=["GET"])
def get_niveles():
    try:
        niveles = Nivel.obtener_todos()
        return jsonify({
            'data': niveles,
            'Status': 'success',
            'Msj': 'Listado de niveles retornado exitosamente'
        })
    except Exception as e:
        return jsonify({
            'data': [],
            'Status': 'error',
            'Msj': f'Ocurrió un error al listar los niveles: {repr(e)}'
        })

@viajes_bp.route('/registrarNivel', methods=["GET", "POST"])
def nuevo_nivel():
    if request.method == "GET":
        # Renderiza formulario para registrar un nuevo nivel
        return render_template(
            "viajes/nivelCRUD.html",  # Cambia el template a uno para nivel
            tittle="Nuevo nivel",
            nivel={
                "idNivel": None,
                "nroPiso": None,
                "tipoVehiculo": "",
                "cantidad": None,
                "estado": "activo"
            },
            btnId="btn_Registrar",
            active_page="nivel",
            active_menu='mViajes'
        )
    else:
        try:
            tipo_vehiculo = request.form["txt_tipoVehiculo"]
            cantidad = int(request.form["txt_cantidad"])

            msj1, msj2 = Nivel.insertar_nivel(tipo_vehiculo, cantidad)

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar nivel'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/verNivel/<int:idNivel>")
def ver_nivel(idNivel):
    try:
        nivel = Nivel.obtener_uno_por_idNivel(idNivel)

        return render_template(
            "viajes/nivelCRUD.html",
            tittle="Ver nivel",
            nivel=nivel,
            btnId="btn_Regresar",
            active_page="nivel",
            active_menu='mViajes'
        )
    except Exception as e:
        return f"Error al obtener nivel: {repr(e)}", 500

@viajes_bp.route("/editarNivel/<int:idNivel>", methods=["GET", "POST"])
def editar_nivel(idNivel):
    if request.method == "GET":
        try:
            nivel = Nivel.obtener_uno_por_idNivel(idNivel)

            return render_template(
                "viajes/nivelCRUD.html",
                tittle="Editar nivel",
                nivel=nivel,
                btnId="btn_Actualizar",
                active_page="nivel",
                active_menu='mViajes'
            )
        except Exception as e:
            return f"Error al obtener nivel: {repr(e)}", 500
    else:
        try:
            nroPiso = int(request.form["txt_nroPiso"])
            tipo_vehiculo = request.form["txt_tipoVehiculo"]
            cantidad = int(request.form["txt_cantidad"])
            estado = request.form["txt_estado"]

            msj1, msj2 = Nivel.actualizar_nivel(idNivel, nroPiso, tipo_vehiculo, cantidad,estado)

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al actualizar nivel'})

        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/DarBajaNivel/<int:idNivel>", methods=["POST"])
def dar_baja_nivel(idNivel):
    try:
        msj1, msj2 = Nivel.dar_baja_piso(idNivel)

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja el nivel'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/eliminarNivel/<int:idNivel>", methods=["POST"])
def eliminar_nivel(idNivel):
    try:
        msj1, msj2 = Nivel.eliminar_nivel(idNivel)

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar nivel'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION

# REGION TIPO VEHICULO

@viajes_bp.route("/GetData_TipoVehiculo", methods=["GET"])
def get_tipoVehiculo():
    try:
        tipoVehiculo = TipoVehiculo.obtener_todos()
        return jsonify({'data': tipoVehiculo, 'Status': 'success', 'Msj': 'Listado de tipos de vehiculo retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar los tipos de vehiculo: + {repr(e)}'})

@viajes_bp.route('/registrarTipoVehiculo',methods=["GET","POST"])
def nuevoTipoVehiculo():
    if request.method == "GET":
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            tittle="Nuevo tipo de vehículo",
            tipoVehiculo={},
            btnId="btn_Registrar",
            active_page="tipoVehiculo", 
            active_menu='mViajes'
        )
    else:
        try:
            nombre= request.form["txt_nombre"]
            marca = request.form["txt_marca"]
            cantidad = request.form["txt_cantidad"]

            mensajes = TipoVehiculo.insertarTipoVehiculo(nombre,marca,cantidad)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/verTipoVehiculo/<int:idVehiculo>")
def verTipoVehiculo(idVehiculo):
    return render_template(
        "viajes/tipoVehiculoCRUD.html",
        tittle="Ver tipo de vehículo",
        tipoVehiculo = TipoVehiculo.obtenerUno(idVehiculo),
        btnId="btn_Regresar",
        active_page="tipoVehiculo", 
        active_menu='mViajes'
    )

@viajes_bp.route("/editarTipoVehiculo/<int:idTipoVehiculo>",methods=["GET","POST"])
def editarTipoVehiculo(idTipoVehiculo):
    if request.method == "GET":
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            tittle="Editar tipo de vehículo",
            tipoVehiculo = TipoVehiculo.obtenerUno(idTipoVehiculo),
            btnId="btn_Actualizar"
        )
    else:
        try:
            nombre= request.form["txt_nombre"]
            marca = request.form["txt_marca"]
            cantidad = request.form["txt_cantidad"]
            estado = int(request.form["txt_estado"])

            mensajes = TipoVehiculo.actualizarTipoVehiculo(idTipoVehiculo,nombre,marca,estado,cantidad)

            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})

        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/DarBajaTipoVehiculo/<int:idTipVehiculo>",methods=["POST"])
def darBajaTipoVehiculo(idTipVehiculo):
    try:
        mensajes = TipoVehiculo.darBajaTipoVehiculo(idTipVehiculo)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/eliminarTipoVehiculo/<int:idTipoVehiculo>", methods=["POST"])
def eliminarTipoVehiculo(idTipoVehiculo):
    try:
        mensajes = TipoVehiculo.eliminarTipoVehiculo(idTipoVehiculo)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar tipo vehiculo'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO VEHICULO

# REGION VEHICULO
@viajes_bp.route("/GetData_Vehiculo")
def get_vehiculos():
    try:
        vehiculos = Vehiculo.obtenerVehiculos()
        return jsonify({'data': vehiculos, 'Status': 'success', 'Msj': 'Listado de vehículos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar los vehículos: {repr(e)}'})

@viajes_bp.route('/registrarVehiculo', methods=["GET", "POST"])
def nuevoVehiculo():
    if request.method == "GET":
        return render_template(
            "viajes/vehiculoCRUD.html",
            tittle="Nuevo vehículo",
            vehiculo={},
            btnId="btn_Registrar",
            active_page="vehiculo",
            active_menu='mViajes'
        )
    else:
        try:
            placa = request.form['txt_placa']
            anio = int(request.form['txt_anio'])
            color = request.form['txt_color']
            idTipoVehiculo = int(request.form['txt_idTipoVehiculo'])

            mensajes = Vehiculo.insertarVehiculo(placa, anio, color, idTipoVehiculo)
            msj1 = mensajes.get('MSJ') or mensajes.get('@MSJ')
            msj2 = mensajes.get('MSJ2') or mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al insertar vehículo'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/verVehiculo/<string:idVehiculo>")
def verVehiculo(idVehiculo):
    vehiculo = Vehiculo.obtener_unVehiculo(idVehiculo)
    return render_template(
        "viajes/vehiculoCRUD.html",
        tittle="Ver vehículo",
        vehiculo=vehiculo,
        btnId="btn_Regresar",
        active_page="vehiculo",
        active_menu='mViajes'
    )

@viajes_bp.route("/editarVehiculo/<int:idVehiculo>", methods=["GET", "POST"])
def editarVehiculo(idVehiculo):
    if request.method == "GET":
        vehiculo = Vehiculo.obtener_unVehiculo(idVehiculo)
        return render_template(
            "viajes/vehiculoCRUD.html",
            tittle="Editar vehículo",
            vehiculo=vehiculo,
            btnId="btn_Actualizar",
            active_page="vehiculo",
            active_menu='mViajes'
        )
    else:
        try:
            placa = request.form['txt_placa']
            anio = int(request.form['txt_anio'])
            color = request.form['txt_color']
            idTipoVehiculo = int(request.form['txt_idTipoVehiculo'])
            estado = int(request.form['txt_estado'])

            mensajes = Vehiculo.actualizarVehiculo(idVehiculo, placa, anio, color, idTipoVehiculo, estado)
            msj1 = mensajes.get('MSJ') or mensajes.get('@MSJ')
            msj2 = mensajes.get('MSJ2') or mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al actualizar vehículo'})
        except Exception as e:
            return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/DarBajaVehiculo/<int:idVehiculo>", methods=["POST"])
def darBajaVehiculo(idVehiculo):
    try:
        mensajes = Vehiculo.darBajaVehiculo(idVehiculo)
        msj1 = mensajes.get('MSJ') or mensajes.get('@MSJ')
        msj2 = mensajes.get('MSJ2') or mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja vehículo'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/eliminarVehiculo/<int:idVehiculo>", methods=["POST"])
def eliminarVehiculo(idVehiculo):
    try:
        mensajes = Vehiculo.eliminarVehiculo(idVehiculo)
        msj1 = mensajes.get('MSJ') or mensajes.get('@MSJ')
        msj2 = mensajes.get('MSJ2') or mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar vehículo'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
# END REGION

# REGIÓN HORARIO #

@viajes_bp.route("/GetData_Horario", methods=["GET"])
def get_horarios():
    try:
        horarios = Horario.obtener_todos()
        return jsonify({'data': horarios, 'Status': 'success', 'Msj': 'Listado de horarios retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar horarios: + {repr(e)}'})

@viajes_bp.route('/HorarioNuevo')
def horario_Nuevo():
    return render_template(
        'viajes/horarioCRUD.html', 
        active_page="horario", 
        active_menu='mViajes', 
        horario={},
        tittle = 'Registrar horario',
        btnId = 'btn_Registrar')

@viajes_bp.route("/RegistrarHorario", methods=["POST"])
def registrar_horario():
    try:
        hora_entrada = request.form.get("hora_entrada").strip()
        hora_salida = request.form.get("hora_salida").strip()
        estado = request.form.get("estado")

        if not hora_entrada or not hora_salida or not estado:
            return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

        mensajes = Horario.registrar(hora_entrada, hora_salida, estado)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar horario'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarHorario/<int:id>", methods=['POST'])
def eliminar_horario(id):  # Recibe el ID de la URL
    try:
        mensajes = Horario.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar horario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarHorario/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    try:
        horario_data = Horario.obtener_por_id(id)

        if request.method == 'POST':
            hora_entrada = request.form.get("hora_entrada").strip()
            hora_salida = request.form.get("hora_salida").strip()
            estado = request.form.get("estado")

            if not hora_entrada or not hora_salida or not estado:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})

            
            mensajes = Horario.editar(id, hora_entrada, hora_salida, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar horario'})
        if horario_data:
            return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario=horario_data, tittle = 'Editar horario', btnId = 'btn_Editar')
        return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario={}, tittle = 'Editar horario', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerHorario/<int:id>", methods=['GET'])
def ver_usuario(id):
    try:
        horario_data = Horario.obtener_por_id(id)
        if horario_data:
            return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', horario=horario_data, tittle = 'Ver horario', btnId = 'btn_Aceptar')
        return render_template('viajes/horarioCRUD.html', active_page="usuarios", active_menu='mUsuarios', usuario={}, tittle = 'Ver usuario', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaHorario/<int:id>", methods=['POST'])
def darBaja_horario(id):  # Recibe el ID de la URL
    try:
        mensajes = Horario.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al horario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGIÓN HORARIO #

# INICIO REGIÓN SUCURSAL #
@viajes_bp.route("/GetData_Sucursal", methods=["GET"])
def get_sucursal():
    try:
        sucursal = Sucursal.obtener_todos()
        return jsonify({'data': sucursal, 'Status': 'success', 'Msj': 'Listado de sucursales retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar las sucursales: + {repr(e)}'})
    
@viajes_bp.route('/SucursalNuevo')
def sucursal_Nuevo():
    return render_template(
        'viajes/sucursalCRUD.html', 
        active_page="sucursal", 
        active_menu='mViajes', 
        sucursal={},
        tittle = 'Registrar sucursal',
        btnId = 'btn_Registrar')

@viajes_bp.route('/RegistrarSucursal', methods=["POST"])
def registrar_sucursal():
    try:
        # Obtener datos del formulario
        nombre = request.form.get("txt_nombre", "").strip()
        direccion = request.form.get("txt_direccion", "").strip()
        latitud = request.form.get("txt_latitud")
        longitud = request.form.get("txt_longitud")
        departamento = request.form.get("txt_departamento", "").strip()
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

        # Validaciones básicas
        if not all([nombre, latitud, longitud, departamento]):
            return jsonify({"Status": "error", "Msj": "Todos los campos son requeridos"})

        resultado = Sucursal.registrar(
            departamento=departamento,
            nombre=nombre,
            direccion=direccion,
            latitud=latitud,
            longitud=longitud,
            usuario_actual=usuario_actual
        )
        
        msj1 = resultado.get('@MSJ')
        msj2 = resultado.get('@MSJ2')
        
        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar sucursal'})

    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": f"Error inesperado al registrar sucursal: {str(e)}"
        })

@viajes_bp.route("/EliminarSucursal/<int:idSucursal>", methods=['POST'])
def eliminar_sucursal(idSucursal):
    try:
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        mensajes = Sucursal.eliminar(idSucursal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar sucursal'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarSucursal/<int:idSucursal>",methods=["GET","POST"])
def editar_sucursal(idSucursal):
    try:
        sucursal = Sucursal.obtener_por_id(idSucursal)
        
        if request.method == "POST":
            nombre = request.form.get("txt_nombre").strip()
            direccion = request.form.get("txt_direccion").strip()
            latitud = request.form.get("txt_latitud").strip()
            longitud = request.form.get("txt_longitud").strip()
            departamento = request.form.get("txt_departamento").strip()
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
            
            mensajes = Sucursal.editar(idSucursal, departamento, direccion, nombre, latitud, longitud, usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar sucursal'})
        if sucursal:
            return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal=sucursal, tittle = 'Editar sucursal', btnId = 'btn_Editar')
        return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal={}, tittle = 'Editar sucursal', btnId = 'btn_Editar')
    
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerSucursal/<int:idSucursal>", methods=['GET'])
def ver_sucursal(idSucursal):
    try:
        sucursal = Sucursal.obtener_por_id(idSucursal)
        if sucursal:
            return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal=sucursal, tittle = 'Ver sucursal', btnId = 'btn_Aceptar')
        return render_template('viajes/sucursalCRUD.html', active_page="sucursal", active_menu='mViajes', sucursal={}, tittle = 'Ver sucursal', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaSucursal/<int:idSucursal>", methods=['POST'])
def darBaja_sucursal(idSucursal):
    try:
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
        mensajes = Sucursal.dar_baja(idSucursal, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': '', "ActualizarMapa":True})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja la sucursal'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/ObtenerSucursalesMapa", methods=['GET'])
def obtener_sucursales_mapa():
    try:
        sucursales = Sucursal.obtener_todos()
        
        # Convertir a formato JSON compatible
        sucursales_json = []
        for suc in sucursales:
            sucursales_json.append({
                'id': suc['id'],
                'nombre': suc['nombre'],
                'direccion': suc['direccion'],
                'departamento': suc['departamento'],
                'latitud': float(suc['latitud']) if suc['latitud'] else None,
                'longitud': float(suc['longitud']) if suc['longitud'] else None
            })
        
        return jsonify(sucursales_json)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": str(e)}), 500

@viajes_bp.route('/api/geocodificar', methods=['GET'])
def geocodificar_coordenadas():
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Coordenadas inválidas'}), 400
    
    try:
        resultado = Ubigeo.obtener_por_lat_lon(lat, lon)
        if resultado:
            return jsonify({
                'status': 'success',
                'data': resultado
            })
        return jsonify({
            'status': 'error',
            'message': 'No se pudo geocodificar las coordenadas'
        }), 404
    except Exception as e:
        print(f"Error en geocodificar_coordenadas: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Error interno del servidor'
        }), 500

# END REGIÓN SUCURSAL #

#REGION MARCA

# Ruta para gestionar las marcas
@viajes_bp.route('/GestionarMarcas')
def Menu_Marcas():
    msg = request.args.get('msg', '')
    tipotoast= request.args.get('tipotoast', '')
    return render_template('viajes/marca.html', active_page="marcas", active_menu='mViajes', msg=msg,tipotoast=tipotoast)

# Ruta para registrar una nueva marca
@viajes_bp.route('/MarcaNuevo', methods=['GET', 'POST'])
def Marca_Nueva():
    if request.method == 'POST':
        return registrar_marca()
    return render_template('viajes/marcaCRUD.html', tittle="Registrar marca", btnId="btn_Registrar", marca=None)


# Ruta para editar o ver una marca (con id)
@viajes_bp.route("/MarcaNuevo/<int:id>", methods=['GET', 'POST'])
def Marca_Editar_Ver(id):
    marca = Marca.obtener_por_id(id)
    if marca is None:
        return jsonify({"Status": "error", "Msj": "Marca no encontrada"})
    ver = request.args.get('ver', False)
    return render_template('viajes/marcaCRUD.html', marca=marca, tittle="Ver marca" if ver else "Editar marca", btnId="btn_Editar" if not ver else "btn_Ver", ver=ver)

# Función para registrar la nueva marca
@viajes_bp.route('/RegistrarMarca', methods=["POST"])
def registrar_marca():
    try:
        nombre = request.form.get("nombre")
        estado = request.form.get("estado")
        logo = request.files.get("logo")
        if not nombre or not nombre.strip():
            return jsonify({"Status": "error", "Msj": "El nombre es obligatorio."})
        if not estado or not estado.strip():
            return jsonify({"Status": "error", "Msj": "El estado es obligatorio."})
        if logo:
            logo_filename = secure_filename(logo.filename)
            logo_path = f"/Static/img/marca/{logo_filename}"
            logo.save(os.path.join("Static/img/marca", logo_filename))
        else:
            logo_path = "/Static/img/trabajadores/marca/logo.png"  # Logo por defecto
        mensajes = Marca.registrar(nombre.strip(), estado.strip(),  session.get('usuario', {}).get('email', 'SIN USUARIO').strip(),logo_path)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return redirect(url_for('viajes.Menu_Marcas', msg=msj1 ,tipotoast='success'))
        elif msj2:
            return redirect(url_for('viajes.Menu_Marcas', msg=msj2, tipotoast='error'))
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar la marca'})
        # Redirigir con un mensaje de éxito
        
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

# Ruta para editar una marca
@viajes_bp.route("/EditarMarca/<int:id>", methods=['GET', 'POST'])
def editar_marca(id):
    marca = Marca.obtener_por_id(id)
    if marca is None:
        return jsonify({"Status": "error", "Msj": "Método de pago no encontrado"})
    if request.method == 'POST':
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado").strip()
        logo = request.files.get("logo")
        if not nombre or not estado:
            return jsonify({"Status": "error", "Msj": "Nombre y estado son obligatorios"})
        if logo:
            logo_filename = secure_filename(logo.filename)
            logo_path = f"/Static/img/marca/{logo_filename}"
            logo.save(os.path.join("Static/img/marca", logo_filename))
        else:
            logo_path = marca['logo']
        mensajes = Marca.editar(id, nombre, estado, logo_path)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')
        # Redirigir con un mensaje de éxito
        if msj1:
            return redirect(url_for('viajes.Menu_Marcas', msg=msj1, tipotoast='success'))
        elif msj2:
            return redirect(url_for('viajes.Menu_Marcas', msg=msj2, tipotoast='error'))
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar la marca'})
    return render_template('viajes/marcaCRUD.html', marca=marca, tittle="Editar Marca", btnId="btn_Editar")

# Ruta para eliminar una marca
@viajes_bp.route("/EliminarMarca/<int:id>", methods=['POST'])
def eliminar_marca(id):
    try:
        mensajes = Marca.eliminar(id)
        return jsonify(mensajes)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

@viajes_bp.route("/dar_baja_marca/<int:id>", methods=["POST"])
def dar_baja_marca(id):
    try:
        # Ejecutar el procedimiento almacenado
        mensajes = Marca.darBaja(id)  # Asegúrate de que esta función esté llamando al SP correctamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al marca'})

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Ocurrió un error inesperado: {repr(e)}"})


# Ruta para obtener todas las marcas
@viajes_bp.route("/GetData_Marcas", methods=['GET'])
def get_marcas():
    try:
        marcas = Marca.obtener_todos()
        if marcas:
            return jsonify({"Status": "success", "data": marcas})
        return jsonify({"Status": "info", "Msj": "No se encontraron marcas."})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener las marcas: {repr(e)}"})

#END REGION MARCA

# REGION RUTA

@viajes_bp.route("/GetData_Ruta", methods=["GET"])
def get_rutas():
    try:
        tiposUsuarios = Ruta.obtener_todos()
        return jsonify({'data': tiposUsuarios, 'Status': 'success', 'Msj': 'Listado de rutas retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar rutas: + {repr(e)}'})

@viajes_bp.route("/GetSucursales", methods=["GET"])
def get_rutaSucursal():
    try:
        sucursal = Sucursal.obtener_todos()

        sucursal_filtrada = [
            {k: v for k, v in s.items() if k in ['id', 'nombre', 'estado']} 
            for s in sucursal if s.get('estado') == 1
        ]

        return jsonify({'data': sucursal_filtrada, 'Status': 'success', 'Msj': 'Listado de sucursales retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar las sucursales: + {repr(e)}'})


@viajes_bp.route("/RegistrarRuta", methods=["POST"])
def registrar_ruta():
    try:
        nombre = request.form.get("nombre").strip()
        origen = int(request.form.get("origen").strip())
        destino = int(request.form.get("destino").strip())
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Ruta.registrar(nombre, origen, destino, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar ruta'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarRuta/<int:id>", methods=['POST'])
def eliminar_ruta(id):  # Recibe el ID de la URL
    try:
        mensajes = Ruta.eliminar(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar ruta'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EditarRuta/<int:id>", methods=['GET', 'POST'])
def editar_ruta(id):
    try:
        ruta = Ruta.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            origen = int(request.form.get("origen").strip())
            destino = int(request.form.get("destino").strip())
            estado = request.form.get("estado")
            
            mensajes = Ruta.editar(id, nombre, origen, destino, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar ruta'})

        if ruta:
            return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta=ruta, tittle = 'Editar ruta', btnId = 'btn_Editar')
        return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta={}, tittle = 'Editar ruta', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerRuta/<int:id>", methods=['GET'])
def ver_ruta(id):
    try:
        ruta = Ruta.obtener_por_id(id)
        if ruta:
            return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta=ruta, tittle = 'Ver ruta', btnId = 'btn_Aceptar')
        return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta={}, tittle = 'Ver ruta', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaRuta/<int:id>", methods=['POST'])
def darBaja_ruta(id):  # Recibe el ID de la URL
    try:
        mensajes = Ruta.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja a la ruta'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION RUTA

# END FUNCIONES