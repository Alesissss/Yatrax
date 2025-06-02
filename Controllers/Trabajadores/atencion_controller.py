import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.pasaje import Pasaje

atencion_bp = Blueprint('atencion', __name__, url_prefix='/trabajadores/atencion')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@atencion_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada"), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@atencion_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida"), 403

# Manejar errores 404 (Página no encontrada)
@atencion_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada"), 404

# Manejar errores 500 (Error interno del servidor)
@atencion_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor"), 500

# Manejar cualquier otro error genérico
@atencion_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado"), 500

# RESTRICCIONES
@atencion_bp.before_request
def verificar_sesion():
    rutas_permitidas = ['home.login', 'home.logout', 'static']  # Excluir login, logout y archivos estáticos
    usuario = session.get('usuario')
    menus = session.get('menus', [])

    if not usuario and request.endpoint not in rutas_permitidas:
        session.clear()
        return redirect(url_for('home.login'))  # No autenticado → redirigir

    if usuario and usuario['tipousuario'].upper() == 'CLIENTE' and request.endpoint not in rutas_permitidas:
        abort(401)  # Autenticado pero no autorizado para navegación general

    if 6 not in menus and request.endpoint not in rutas_permitidas:
        abort(403)  # Autenticado, pero no tiene permiso para ese módulo

    # if not any(menu['nombre'] == 'M_ATENCION' for menu in menus) and request.endpoint not in rutas_permitidas:
    #     abort(403)  # Autenticado, pero no tiene permiso para ese módulo

# VIEWS
@atencion_bp.route('/GestionarReservas')
def Menu_Atencion():
    return render_template('atencion/reservas.html', active_page="ejemplo", active_menu='mAtencion')

# END VIEWS

# FUNCIONES
# REGION RESERVAS
@atencion_bp.route('/GetData_Reservas')
def listarReservas():
    try:
        reservas = Pasaje.listarReservas()

        return jsonify({"Status": "success","data": reservas})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500

@atencion_bp.route('/RegistrarReserva',methods=["GET","POST"])
def registrarReserva():
    if request.method == "GET":
        return render_template("atencion/reservaCRUD.html",btnId="btn_Registrar")
    else:
        pass

@atencion_bp.route('/EditarReserva/<int:id>',methods=["GET","POST"])
def editarReserva(id):
    if request.method == "GET":
        reserva = Pasaje.obtener_una_reserva(id)
        return render_template("atencion/reservaCRUD.html",reserva=reserva,btnId="btn_Editar")
    else:
        pass

@atencion_bp.route('/EliminarReserva/<int:id>', methods=["POST"])
def eliminarReserva(id):
    try:
        resultado = Pasaje.eliminarReserva(id)
        if resultado["msj"] is not None:
            return jsonify({"Status": "success", "Msj": resultado["msj"],"Msj2":resultado["msj2"]})
        else:
            return jsonify({"Status": "error",   "Msj": resultado["msj"],"Msj2":resultado["msj2"]})
    except Exception as e:
        return jsonify({"Status": "error", "Msg": str(e)})


@atencion_bp.route('/VerReserva/<int:id>')
def verReserva(id):
    reserva = Pasaje.obtener_una_reserva(id)
    return render_template("atencion/reservaCRUD.html",reserva=reserva)
#END REGION RESERVAS
# END FUNCIONES