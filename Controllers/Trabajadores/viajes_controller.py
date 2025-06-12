import os
import requests
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort, json
from werkzeug.utils import secure_filename

from Models.nivel import Nivel
from Models.tipoVehiculo import TipoVehiculo
from Models.vehiculo import Vehiculo
from Models.sucursal import Sucursal
from Models.ciudad import Ciudad
from Models.horario import Horario
from Models.ubigeo import Ubigeo
from Models.marca import Marca
from Models.ruta import Ruta
from Models.asiento import Asiento
from Models.tipo_herramienta import TipoHerramienta
from Models.herramienta import Herramienta
from Models.servicio import Servicio
from Models.viaje import Viaje
from Models.personal import Personal
from Models.api_enrutar import ApiEnrutar

viajes_bp = Blueprint('viajes', __name__, url_prefix='/trabajadores/viajes')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@viajes_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@viajes_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@viajes_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@viajes_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@viajes_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

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
    return render_template('viajes/vehiculo.html', active_page="vehiculo", active_menu='mViajes')

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

@viajes_bp.route('/GestionarAsiento')
def Menu_Asiento():
    return render_template('viajes/asiento.html', active_page="asiento", active_menu='mViajes')

@viajes_bp.route('/RutaNuevo')
def TipoUsuario_Nuevo():
    return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta={}, escalas=[], tittle = 'Registrar ruta', btnId = 'btn_Registrar')

@viajes_bp.route('/ProgramarViaje')
def Menu_ProgramarViaje():
    return render_template('viajes/programarViaje.html', active_page="programarViaje", active_menu='mViajes')

@viajes_bp.route('/ProgramarViajeNuevo')
def Menu_ProgramarViajeNuevo():
    return render_template('viajes/programarViajeCRUD.html', active_page="programarViaje", active_menu='mViajes', viaje={}, personal=[], tittle = 'Registrar viaje', btnId = 'btn_Registrar')

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
        lista_tipo_herramienta = TipoHerramienta.obtener_todos()
        lista_herramienta = Herramienta.obtener_todos()
        # Renderiza formulario para registrar un nuevo nivel
        return render_template(
            "viajes/nivelCRUD.html",  # Cambia el template a uno para nivel
            title="Nuevo nivel",
            nivel={},
            tipo_herramientas = lista_tipo_herramienta,
            herramientas = lista_herramienta,
            botones = [],
            btnId="btn_Registrar",
            active_page="nivel",
            active_menu='mViajes'
        )
    else:
        try:
            data = request.get_json()
            nroPiso = int(data["nroPiso"])
            id_tipo_vehiculo = int(data["id_tipo_vehiculo"])
            x_dimension = int(data["x_dimension"])
            y_dimension = int(data["y_dimension"])
            estado = int(data["estado"])
            herramientas = data["herramientas"]  # Lista de dicts

            # Validación mínima
            if not herramientas:
                return jsonify({"Status": "error", "Msj": "No se ha añadido ninguna herramienta"})

            # Convertir herramientas a objetos si es necesario
           
            Nivel.insertar_nivel(nroPiso, id_tipo_vehiculo, x_dimension, y_dimension, estado, herramientas)
            return jsonify({"Status": "success", "Msj": "Nivel registrado exitosamente"})

        except Exception as e:
            return jsonify({"Status": "error", "Msj": f"Error inesperado: {repr(e)}"})

@viajes_bp.route("/verNivel/<int:idNivel>")
def ver_nivel(idNivel):
    try:
        datos_nivel,datos_botones = Nivel.obtener_uno_por_idNivel(idNivel)
        lista_tipo_herramienta = TipoHerramienta.obtener_todos()
        lista_herramienta = Herramienta.obtener_todos()
        return render_template(
            "viajes/nivelCRUD.html",
            title="Ver nivel",
            tipo_herramientas = lista_tipo_herramienta,
            herramientas = lista_herramienta,
            nivel=datos_nivel,
            botones=datos_botones,
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
            datos_nivel,datos_botones = Nivel.obtener_uno_por_idNivel(idNivel)
            lista_tipo_herramienta = TipoHerramienta.obtener_todos()
            lista_herramienta = Herramienta.obtener_todos()
            return render_template(
                "viajes/nivelCRUD.html",
                title="Editar nivel",
                tipo_herramientas = lista_tipo_herramienta,
                herramientas = lista_herramienta,
                nivel=datos_nivel,
                botones = datos_botones,
                btnId="btn_Actualizar",
                active_page="nivel",
                active_menu='mViajes'
            )
        except Exception as e:
            return f"Error al obtener nivel: {repr(e)}", 500
    else:
        try:
            data = request.get_json()
            nroPiso = int(data.get("nroPiso"))
            tipo_vehiculo = int(data.get("id_tipo_vehiculo"))
            x_dimension = int(data.get("x_dimension"))
            y_dimension = int(data.get("y_dimension"))
            estado = int(data.get("estado"))
            herramientas = data.get("herramientas", [])

            Nivel.actualizar_nivel(idNivel, nroPiso, tipo_vehiculo, x_dimension, y_dimension, estado, herramientas)

            return jsonify({"Status": "success", "Msj": "Nivel actualizado correctamente"})
        except Exception as e:
            return jsonify({"Status": "error", "Msj": f"Error al actualizar: {repr(e)}"})

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

@viajes_bp.route("/GetMarcasTipoVehiculo", methods=['GET'])
def get_tipovehiculo_marcas():
    try:
        marcas = Marca.obtener_todos()
        result = [{'id': tu['id'], 'nombre': tu['nombre']} for tu in marcas if tu['estado'] == 1]

        return jsonify({"Status": "success", "data": result, "Msj": "Listado de marcas retornado exitosamente"})
    except Exception as e:
        return jsonify({"Status": "error", "data": [], "Msj": f"Error al obtener las marcas: {repr(e)}"})
    
@viajes_bp.route("/GetServiciosTipoVehiculo", methods=['GET'])
def get_tipovehiculo_servicios():
    try:
        servicios = Servicio.obtener_todos()
        result = [{'id': tu['id'], 'nombre': tu['nombre']} for tu in servicios if tu['estado'] == 1]

        return jsonify({"Status": "success", "data": result, "Msj": "Listado de servicios retornado exitosamente"})
    except Exception as e:
        return jsonify({"Status": "error", "data": [], "Msj": f"Error al obtener las marcas: {repr(e)}"})


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
        lista_tipo_herramienta = TipoHerramienta.obtener_todos()
        lista_herramienta = Herramienta.obtener_todos()
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            title="Nuevo tipo de vehículo",
            nivel={},
            tipoVehiculo={},
            tipo_herramientas = lista_tipo_herramienta,
            herramientas = lista_herramienta,
            botones = [],
            btnId="btn_Registrar",
            active_page="tipoVehiculo", 
            active_menu='mViajes'
        )
    else:
        try:
            nombre = request.form.get("nombre")
            marca = request.form.get("marca")
            estado = request.form.get("estado")
            servicio = request.form.get("servicio")
            cantidad_pisos = request.form.get("cantidadPisos")

            niveles_json = request.form.get("niveles")
            niveles = json.loads(niveles_json) if niveles_json else []

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            # Convertir tipos si es necesario
            marca = int(marca) if marca else None
            estado = int(estado) if estado else None
            servicio = int(servicio) if servicio else None
            cantidad_pisos = int(cantidad_pisos) if cantidad_pisos else 0

            # Llamar al método de inserción
            TipoVehiculo.insertarTipoVehiculo(
                nombre=nombre,
                idmarca=marca,
                estado=estado,
                servicio=servicio,
                usuario=usuario_actual,
                niveles=niveles
            )

            return jsonify({"Status": "success", 'Msj': 'Tipo de vehículo registrado con éxito', 'Msj2': ''})

        except Exception as e:
            return jsonify({
                "Status": "error",
                "Msj": f"Ocurrió un error inesperado: {str(e)}"
            })

@viajes_bp.route("/verTipoVehiculo/<int:idVehiculo>")
def verTipoVehiculo(idVehiculo):
    niveles = TipoVehiculo.obtener_niveles_por_tipoVehiculo(idVehiculo)

    botones = []
    for nivel in niveles:
        for herramienta in nivel["herramientas"]:
            botones.append({
                "x_dimension": herramienta["x_dimension"],
                "y_dimension": herramienta["y_dimension"],
                "id_herramienta": herramienta["id_herramienta"],
                "piso": nivel["nroPiso"]
            })

    lista_tipo_herramienta = TipoHerramienta.obtener_todos()
    lista_herramienta = Herramienta.obtener_todos()
    return render_template(
        "viajes/tipoVehiculoCRUD.html",
        title="Ver tipo de vehículo",
        tipo_herramientas = lista_tipo_herramienta,
        herramientas = lista_herramienta,
        niveles=niveles,
        botones = botones,
        tipoVehiculo = TipoVehiculo.obtenerUno(idVehiculo),
        btnId="btn_Regresar",
        active_page="tipoVehiculo", 
        active_menu='mViajes'
    )

@viajes_bp.route("/editarTipoVehiculo/<int:idTipoVehiculo>",methods=["GET","POST"])
def editarTipoVehiculo(idTipoVehiculo):
    if request.method == "GET":
        niveles = TipoVehiculo.obtener_niveles_por_tipoVehiculo(idTipoVehiculo)
        botones = []
        for nivel in niveles:
            for herramienta in nivel["herramientas"]:
                botones.append({
                    "x_dimension": herramienta["x_dimension"],
                    "y_dimension": herramienta["y_dimension"],
                    "id_herramienta": herramienta["id_herramienta"],
                    "piso": nivel["nroPiso"]
                })
        lista_tipo_herramienta = TipoHerramienta.obtener_todos()
        lista_herramienta = Herramienta.obtener_todos()
        return render_template(
            "viajes/tipoVehiculoCRUD.html",
            title="Editar tipo de vehículo",
            tipo_herramientas = lista_tipo_herramienta,
            herramientas = lista_herramienta,
            niveles=niveles,
            tipoVehiculo = TipoVehiculo.obtenerUno(idTipoVehiculo),
            botones = botones,
            btnId="btn_Actualizar",
            active_page="tipoVehiculo", 
            active_menu='mViajes'
        )
    else:
        try:
            nombre = request.form.get("nombre")
            marca = request.form.get("marca")
            cantidad = int(request.form.get("cantidadPisos"))
            estado = int(request.form.get("estado"))
            servicio = request.form.get("servicio")

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            # Parsear niveles desde el formData
            niveles_json = request.form.get("niveles")
            niveles = json.loads(niveles_json) if niveles_json else []

            # 1. Actualizar tipo vehículo
            mensajes = TipoVehiculo.actualizarTipoVehiculo(
                idTipoVehiculo, nombre, marca, estado, servicio,niveles
            )
            
            msj1 = mensajes.get('MSJ')
            msj2 = mensajes.get('MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al actualizar tipo vehículo'})

        except Exception as e:
            print(f"Error en editarTipoVehiculo: {e}")
            return jsonify({"Status": "error", 'Msj': 'Error interno en el servidor'})
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
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja tipo vehiculo'})
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
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar tipo vehiculo'})
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION TIPO VEHICULO

# REGION VEHICULO
@viajes_bp.route("/GetTiposVehiculo_Vehiculo", methods=['GET'])
def get_tipovehiculo_vehiculo():
    try:
        tipos = TipoVehiculo.obtener_todos()
        result = [{'id': tu['id'], 'nombre': tu['nombre']} for tu in tipos if tu['estado'] == 1]

        return jsonify({"Status": "success", "data": result, "Msj": "Listado de tipos de vehículo retornado exitosamente"})
    except Exception as e:
        return jsonify({"Status": "error", "data": [], "Msj": f"Error al obtener los tipos de vehículo: {repr(e)}"})

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
            placa = request.form.get('placa')
            anio = int(request.form.get('anio'))
            color = request.form.get('color')
            idTipoVehiculo = int(request.form.get('idTipoVehiculo'))
            estado = int(request.form.get('estado'))

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

            valor = Vehiculo.insertarVehiculo(placa, anio, color, idTipoVehiculo, estado, usuario_actual)

            if valor:
                return jsonify({"Status": "success", 'Msj': "Insertado con éxito", 'Msj2': ''})
            elif valor:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': "Error al insertar el vehículo"})
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
            placa = request.form.get('placa')
            anio = int(request.form.get('anio'))
            color = request.form.get('color')
            idTipoVehiculo = int(request.form.get('idTipoVehiculo'))
            estado = int(request.form.get('estado'))

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
        return render_template('viajes/horarioCRUD.html', active_page="horarios", active_menu='mViajes', usuario={}, tittle = 'Ver horario', btnId = 'btn_Aceptar')
        
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
        ciudad = request.form.get("txt_provincia", "").strip()
        abreviatura = request.form.get("txt_abreviatura", "").strip()
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO')

        # Validaciones básicas
        if not all([nombre, latitud, longitud, ciudad, abreviatura, direccion]):
            return jsonify({"Status": "error", "Msj": "Todos los campos son requeridos"})

        resultado = Sucursal.registrar(
            ciudad=ciudad,
            nombre=nombre,
            direccion=direccion,
            latitud=latitud,
            longitud=longitud,
            estado=estado,
            abreviatura=abreviatura,
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
            ciudad = request.form.get("txt_provincia").strip()
            abreviatura = request.form.get("txt_abreviatura").strip()
            estado = request.form.get("estado")
            # Obtener el usuario actual desde la sesión
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()
            
            if not all([nombre, latitud, longitud, ciudad, abreviatura, direccion]):
                return jsonify({"Status": "error", "Msj": "Todos los campos son requeridos"})
            
            mensajes = Sucursal.editar(idSucursal, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario_actual)
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
                'ciudad': suc['ciudad'],
                'latitud': float(suc['latitud']) if suc['latitud'] else None,
                'longitud': float(suc['longitud']) if suc['longitud'] else None
            })
        
        return jsonify(sucursales_json)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": str(e)}), 500

@viajes_bp.route('/BuscarAbreviatura', methods=['POST'])
def buscar_abreviatura():
    try:
        data = request.get_json()
        provincia = data.get('provincia', '').strip()
        if not provincia:
            return jsonify({'Status': 'error', 'message': 'El parámetro "provincia" es obligatorio.'}), 400

        # 1. Si ya hay abreviatura registrada, la devolvemos
        resultado = Ciudad.obtener_abreviatura(provincia)
        if resultado:
            return jsonify({'Status': 'success', 
                            'data': resultado}), 200

        # 2. Generamos una nueva abreviatura única
        nueva_abbr = Ciudad._generar_abreviatura_recursivo(provincia)

        # 3. La registramos en la base de datos
        Ciudad.registrar_abreviatura(provincia, nueva_abbr)
        # 4. Devolvemos la nueva abreviatura
        aux_resultado = Ciudad.obtener_abreviatura(provincia)
        return jsonify({'Status': 'success', 
                        'data': aux_resultado}), 200

    except Exception as e:
        return jsonify({'Status': 'error', 
                        'message': 'Error interno del servidor.'}), 500

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

@viajes_bp.route("/API_ENRUTAR", methods=["GET"])
def api_enrutar():
    try:
        start = request.args.get('start')  # "lat,lng"
        end = request.args.get('end')      # "lat,lng"

        start_lat, start_lng = map(float, start.split(','))
        end_lat, end_lng = map(float, end.split(','))

        enrutar = ApiEnrutar()
        resultado = enrutar.obtener_ruta(start_lat, start_lng, end_lat, end_lng)

        if resultado:
            return jsonify(resultado)
        else:
            return jsonify({'error': 'No se pudo obtener la ruta'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@viajes_bp.route("/GetData_Ruta", methods=["GET"])
def get_rutas():
    try:
        tiposUsuarios = Ruta.obtener_todos()
        return jsonify({'data': tiposUsuarios, 'Status': 'success', 'Msj': 'Listado de rutas retornado exitosamene'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar rutas: + {repr(e)}'})

@viajes_bp.route("/GetData_SucursalesMapaRuta", methods=['GET'])
def obtener_sucursales_mapa_ruta():
    try:
        sucursales = Sucursal.obtener_todos()
        
        # Convertir a formato JSON compatible
        sucursales_json = []
        for suc in sucursales:
            if suc['estado'] == 1:
                sucursales_json.append({
                    'id': suc['id'],
                    'nombre': suc['nombre'],
                    'direccion': suc['direccion'],
                    'ciudad': suc['ciudad'],
                    'latitud': float(suc['latitud']) if suc['latitud'] else None,
                    'longitud': float(suc['longitud']) if suc['longitud'] else None
                })
        
        return jsonify(sucursales_json)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": str(e)}), 500

@viajes_bp.route("/RegistrarRuta", methods=["POST"])
def registrar_ruta():
    try:
        nombre = request.form.get("nombre").strip()
        distancia = float(request.form.get("distancia"))
        tiempo = float(request.form.get("tiempo"))
        estado = request.form.get("estado")
        escalas_json = request.form.get("escalas")

        escalas = json.loads(escalas_json) if escalas_json else []
        tipo = "ESCALA" if len(escalas) > 2 else "DIRECTO"

        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Ruta.registrar(nombre, distancia, tiempo, estado, tipo, escalas, usuario_actual)
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
        escalas = Ruta.obtener_escalas_por_ruta(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            distancia = float(request.form.get("distancia"))
            tiempo = float(request.form.get("tiempo"))
            estado = request.form.get("estado")
            escalas_json = request.form.get("escalas")

            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            escalas = json.loads(escalas_json) if escalas_json else []
            tipo = "ESCALA" if len(escalas) > 2 else "DIRECTO"
            
            mensajes = Ruta.editar(id, nombre, distancia, tiempo, tipo, estado, escalas, usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar ruta'})

        return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta = ruta if ruta else {}, escalas = escalas if escalas else [], tittle = 'Editar ruta', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerRuta/<int:id>", methods=['GET'])
def ver_ruta(id):
    try:
        ruta = Ruta.obtener_por_id(id)
        escalas = Ruta.obtener_escalas_por_ruta(id)
        return render_template('viajes/rutaCRUD.html', active_page="ruta", active_menu='mViajes', ruta = ruta if ruta else {}, escalas = escalas if escalas else [], tittle = 'Ver ruta', btnId = 'btn_Aceptar')
        
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

# REGION DE ASIENTO
@viajes_bp.route('/AsientoNuevo')
def asiento_nuevo():
    return render_template(
        'viajes/asientoCRUD.html', 
        active_page="asiento", 
        active_menu='mViajes',  
        asiento={}, 
        tittle = 'Registrar asiento', 
        btnId = 'btn_Registrar')

# Obtener todos los asientos
@viajes_bp.route("/GetData_Asientos", methods=["GET"])
def get_asientos():
    try:
        asientos = Asiento.obtener_todos()
        return jsonify({'data': asientos, 'Status': 'success', 'Msj': 'Listado de asientos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar asientos: {repr(e)}'})

# Registrar asiento
@viajes_bp.route("/RegistrarAsiento", methods=["POST"])
def registrar_asiento():
    try:
        nro_asiento = request.form.get("nro_asiento").strip()
        nivel = request.form.get("nivel")
        tipo_asiento = request.form.get("tipo")
        estado = request.form.get("estado")
        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        if not nro_asiento or not nivel or not tipo_asiento or not estado:
            return jsonify({"Status": "error", "Msj": f"Todos los campos son obligatorios {nro_asiento},{nivel},{tipo_asiento},{estado}"})

        mensajes = Asiento.registrar(nro_asiento, nivel, tipo_asiento, estado, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar asiento'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Eliminar asiento
@viajes_bp.route("/EliminarAsiento/<int:id>", methods=['POST'])
def eliminar_asiento(id):
    try:
        mensajes = Asiento.eliminar(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al eliminar asiento'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Editar asiento
@viajes_bp.route("/EditarAsiento/<int:id>", methods=['GET', 'POST'])
def editar_asiento(id):
    try:
        asiento = Asiento.obtener_por_id(id)

        if request.method == 'POST':
            nro_asiento = request.form.get("nro_asiento").strip()
            nivel = request.form.get("nivel")
            tipo_asiento = request.form.get("tipo")
            estado = request.form.get("estado")
            usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

            if not nro_asiento or not nivel or not tipo_asiento or not estado:
                return jsonify({"Status": "error", "Msj": "Todos los campos son obligatorios"})
            

            mensajes = Asiento.editar(id, nro_asiento, nivel, tipo_asiento, estado,usuario_actual)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar asiento'})

        if asiento:
            return render_template('viajes/asientoCRUD.html', active_page="asientos", active_menu='mAsientos', asiento=asiento, tittle='Editar asiento', btnId='btn_Editar')
        return render_template('viajes/asientoCRUD.html', active_page="asientos", active_menu='mAsientos', asiento={}, tittle='Editar asiento', btnId='btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Ver asiento
@viajes_bp.route("/VerAsiento/<int:id>", methods=['GET'])
def ver_asiento(id):
    try:
        asiento = Asiento.obtener_por_id(id)
        if asiento:
            return render_template('viajes/asientoCRUD.html', active_page="asientos", active_menu='mAsientos', asiento=asiento, tittle='Ver asiento', btnId='btn_Aceptar')
        return render_template('viajes/asientoCRUD.html', active_page="asientos", active_menu='mAsientos', asiento={}, tittle='Ver asiento', btnId='btn_Aceptar')
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# Dar de baja asiento
@viajes_bp.route("/DarBajaAsiento/<int:id>", methods=['POST'])
def dar_baja_asiento(id):
    try:
        mensajes = Asiento.darBaja(id)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja el asiento'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION ASIENTO


# SECCIÓN HERRAMIENTA
@viajes_bp.route("/GetData_Herammientas")
def obtener_herramientas():
    try:
        objTipoHerramienta = TipoHerramienta()
        lista_herramientas = objTipoHerramienta.obtener_todos()
        return jsonify({
            "data":lista_herramientas,
            "msg":"Listado de herramientas correctamente",
            "status":"succes"
        })
    except Exception as e:
        return jsonify({
            "data":"",
            "msg":f"Ha ocurrido un error al listar las herramientas: {e}",
            "status":"succes"
        }) 

# END SECCIÓN HERRAMIENTA

# REGION VIAJE

@viajes_bp.route("/GetData_ViajesProgramados", methods=["GET"])
def get_viajesProgramados():
    try:
        viajes = Viaje.obtener_todos()
        return jsonify({'data': viajes, 'Status': 'success', 'Msj': 'Listado de viajes retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar viajes: + {repr(e)}'})
    
@viajes_bp.route("/GetData_PersonalViajes", methods=["GET"])
def get_personal_viaje():
    try:
        personal = Personal.obtener_todos()
        result = [{'id': pe['id'], 'nombre': pe['nombre'], 'id_tipopersonal': pe['id_tipopersonal'], 'tipoPersonal': pe['tipopersonal']} for pe in personal if pe['estado'] == 1]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de personal retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar personal: + {repr(e)}'})
    
@viajes_bp.route("/GetData_RutasViajes", methods=["GET"])
def get_rutas_viaje():
    try:
        result = [{'id': ru['id'], 'nombre': ru['nombre'], 'distancia_estimada': ru['distancia_estimada'], 'tiempo_estimado': ru['tiempo_estimado'], 'tipo': ru['tipo'], 'escalas': [{'id': esc['id'], 'nro_orden': esc['nro_orden'], 'idSucursal': esc['idSucursal'], 'distancia_estimada': esc['distancia_estimada'], 'tiempo_estimado': float(esc['tiempo_estimado']) + 30, 'nombre': esc['nombre'], 'idRuta': esc['idRuta']} for esc in Ruta.obtener_escalas_por_ruta(ru['id'])]} for ru in Ruta.obtener_todos() if ru['estado'] == 1]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de rutas retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar las rutas: + {repr(e)}'})
    
@viajes_bp.route("/GetData_ServiciosViajes", methods=["GET"])
def get_servicios_viaje():
    try:
        servicios = Servicio.obtener_todos()
        result = [{'id': s['id'], 'nombre': s['nombre']} for s in servicios if s['estado'] == 1]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de servicios retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar servicios: + {repr(e)}'})

@viajes_bp.route("/GetData_TipoVehiculosViajes", methods=["GET"])
def get_tipovehiculo_viaje():
    try:
        tipoVehiculo = TipoVehiculo.obtener_todos()
        result = [{'id': tv['id'], 'nombre': tv['nombre'], 'id_servicio': tv['id_servicio']} for tv in tipoVehiculo if tv['estado'] == 1]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de tipos de vehículos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar vehículos: + {repr(e)}'})

@viajes_bp.route("/GetData_VehiculosViajes", methods=["GET"])
def get_vehiculo_viaje():
    try:
        vehiculos = Vehiculo.obtenerVehiculos()
        result = [{'id': ve['id'], 'placa': ve['placa'], 'id_tipo_vehiculo': ve['idTipoVehiculo']} for ve in vehiculos if ve['estado'] == 1]

        return jsonify({'data': result, 'Status': 'success', 'Msj': 'Listado de vehículos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar vehículos: + {repr(e)}'})
    
@viajes_bp.route("/GetData_AsientosViajes", methods=["GET"])
def get_asientos_viaje():
    try:
        id = request.args.get('id', type=int)
        idTipo = request.args.get('idTipo', type=int)

        asientos = len(Asiento.obtener_por_id_vehiculo(id))
        niveles = len([{'id': ni['id']} for ni in Nivel.obtener_por_tipo_vehiculo(idTipo) if ni['estado'] == 1])

        return jsonify({'data': [{'asientos': asientos, 'niveles': niveles}], 'Status': 'success', 'Msj': 'Listado de asientos retornado exitosamente'})
    except Exception as e:
        return jsonify({'data': [], 'Status': 'error', 'Msj': f'Ocurrió un error al listar asientos: + {repr(e)}'})

@viajes_bp.route("/RegistrarViaje", methods=["POST"])
def registrar_viaje():
    try:
        fechaHoraSalida = request.form.get("fechaHoraSalida")
        fechaHoraLlegada = request.form.get("fechaHoraLlegada")
        idRuta = request.form.get("idRuta")
        idVehiculo = request.form.get("idVehiculo")
        estado = request.form.get("estado")

        # Subviajes
        detalles_viajes_json = request.form.get("detalles_viajes")
        detalles_viajes = json.loads(detalles_viajes_json) if detalles_viajes_json else []

        # Asientos de subiajes
        asientos = [{'id': a['id'], 'nombre': a['nombre'], 'estado': a['estado']} for a in Asiento.obtener_por_id_vehiculo(idVehiculo) if a["estado"] == 1]

        # Choferes
        choferes_json = request.form.get("choferes")
        choferes = json.loads(choferes_json) if choferes_json else []

        # Tripulantes
        tripulantes_json = request.form.get("tripulantes")
        tripulantes = json.loads(tripulantes_json) if tripulantes_json else []

        usuario_actual = session.get('usuario', {}).get('email', 'SIN USUARIO').strip()

        mensajes = Viaje.registrar(idRuta, idVehiculo, estado, fechaHoraSalida, fechaHoraLlegada, detalles_viajes, choferes, tripulantes, asientos, usuario_actual)
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al registrar viaje'})

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

@viajes_bp.route("/EliminarViaje/<int:id>", methods=['POST'])
def eliminar_viaje(id):  # Recibe el ID de la URL
    try:
        mensajes = Viaje.eliminar(id)  # Se usa el ID directamente
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

@viajes_bp.route("/EditarViaje/<int:id>", methods=['GET', 'POST'])
def editar_viaje(id):
    try:
        tipoUsuario = Viaje.obtener_por_id(id)

        if request.method == 'POST':
            nombre = request.form.get("nombre").strip()
            estado = request.form.get("estado")
            
            mensajes = Viaje.editar(id, nombre, estado)
            msj1 = mensajes.get('@MSJ')
            msj2 = mensajes.get('@MSJ2')

            if msj1:
                return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
            elif msj2:
                return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
            else:
                return jsonify({"Status": "error", 'Msj': 'Error desconocido al editar tipo de usuario'})

        if tipoUsuario:
            return render_template('usuario/tipoUsuarioCRUD.html', active_page="tipoUsuario", active_menu='mUsuarios', tipoUsuario=tipoUsuario, tittle = 'Editar tipo usuario', btnId = 'btn_Editar')
        return render_template('usuario/tipoUsuarioCRUD.html', active_page="tipoUsuario", active_menu='mUsuarios', tipoUsuario={}, tittle = 'Editar tipo usuario', btnId = 'btn_Editar')

    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/VerViaje/<int:id>", methods=['GET'])
def ver_viaje(id):
    try:
        tipoUsuario = Viaje.obtener_por_id(id)
        if tipoUsuario:
            return render_template('usuario/tipoUsuarioCRUD.html', active_page="tipoUsuario", active_menu='mUsuarios', tipoUsuario=tipoUsuario, tittle = 'Ver tipo usuario', btnId = 'btn_Aceptar')
        return render_template('usuario/tipoUsuarioCRUD.html', active_page="tipoUsuario", active_menu='mUsuarios', tipoUsuario={}, tittle = 'Ver tipo usuario', btnId = 'btn_Aceptar')
        
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})
    
@viajes_bp.route("/DarBajaViaje/<int:id>", methods=['POST'])
def darBaja_viaje(id):  # Recibe el ID de la URL
    try:
        mensajes = Viaje.darBaja(id)  # Se usa el ID directamente
        msj1 = mensajes.get('@MSJ')
        msj2 = mensajes.get('@MSJ2')

        if msj1:
            return jsonify({"Status": "success", 'Msj': msj1, 'Msj2': ''})
        elif msj2:
            return jsonify({"Status": "success", 'Msj': '', 'Msj2': msj2})
        else:
            return jsonify({"Status": "error", 'Msj': 'Error desconocido al dar de baja al tipo de usuario'})
    except Exception as e:
        return jsonify({"Status": "error", 'Msj': f'Ocurrió un error inesperado: {repr(e)}'})

# END REGION VIAJE

# END FUNCIONES