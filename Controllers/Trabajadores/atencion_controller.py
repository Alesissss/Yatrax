import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.pasaje import Pasaje
from Models.tipoReclamo import Tipo_Reclamo
from Models.reclamo import Reclamo

atencion_bp = Blueprint('atencion', __name__, url_prefix='/trabajadores/atencion')

# ERRORES 
# Manejar errores 401 (Página no autorizada)
@atencion_bp.errorhandler(401)
def error_401(error):
    return render_template("error.html", error="Página no autorizada", error_code = 401), 401

# Manejar errores 403 (Página no autorizada para este usuario)
@atencion_bp.errorhandler(403)
def error_403(error):
    return render_template("error.html", error="Página restringida",error_code = 403), 403

# Manejar errores 404 (Página no encontrada)
@atencion_bp.errorhandler(404)
def error_404(error):
    return render_template("error.html", error="Página no encontrada",error_code = 404), 404

# Manejar errores 500 (Error interno del servidor)
@atencion_bp.errorhandler(500)
def error_500(error):
    return render_template("error.html", error="Error interno del servidor",error_code = 500), 500

# Manejar cualquier otro error genérico
@atencion_bp.errorhandler(Exception)
def error_general(error):
    return render_template("error.html", error="Ocurrió un error inesperado",error_code = 500), 500

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

@atencion_bp.route('/GestionarTipoReclamo')
def Menu_TipoReclamo():
    return render_template('atencion/tipoReclamo.html', active_page="ejemplo", active_menu='mAtencion')

@atencion_bp.route('/GestionarReclamo')
def Menu_Reclamo():
    return render_template('atencion/reclamo.html', active_page="ejemplo", active_menu='mAtencion')

# END VIEWS

# FUNCIONES
# REGION RESERVAS
@atencion_bp.route('/GetData_Reservas')
def listarReservas():
    try:
        reservas = Pasaje.obtener_todos()

        return jsonify({"Status": "success","data": reservas})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500

@atencion_bp.route('/RegistrarReserva', methods=["GET", "POST"])
def registrarReserva():
    if request.method == "GET":
        return render_template(
            "atencion/reservaCRUD.html",
            tittle="Registrar reserva",
            btnId="btn_Registrar"
        )
    # POST
    try:
        id_detalle_asiento = int(request.form["id_detalle_asiento"])
        numero_comprobante   = request.form["numero_comprobante"]
        id_venta             = int(request.form["id_venta"])
        codigo               = request.form["codigo"]

        resultado = Pasaje.registrarReserva(
            id_detalle_asiento,
            numero_comprobante,
            id_venta,
            codigo
        )

        if resultado.get("msj"):
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado["msj2"]
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado["msj2"]
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": str(e),
            "Msj2": ""
        })


@atencion_bp.route('/EditarReserva/<int:id>', methods=["GET", "POST"])
def editarReserva(id):
    if request.method == "GET":
        reserva = Pasaje.obtener_por_id(id)
        return render_template(
            "atencion/reservaCRUD.html",
            reserva=reserva,
            tittle="Editar reserva",
            btnId="btn_Editar"
        )
    # POST
    try:
        id_detalle_asiento = int(request.form["id_detalle_asiento"])
        numero_comprobante   = request.form["numero_comprobante"]
        es_pasaje_normal     = int(request.form.get("es_pasaje_normal", 0))
        es_pasaje_libre      = int(request.form.get("es_pasaje_libre", 0))
        es_transferencia     = int(request.form.get("es_transferencia", 0))
        es_reserva           = int(request.form.get("es_reserva", 0))
        es_cambio_ruta       = int(request.form.get("es_cambio_ruta", 0))
        id_venta             = int(request.form["id_venta"])
        codigo               = request.form["codigo"]
        id_pasaje_padre      = int(request.form.get("id_pasaje_padre", 0))

        resultado = Pasaje.modificarReserva(
            id,
            id_detalle_asiento,
            numero_comprobante,
            es_pasaje_normal,
            es_pasaje_libre,
            es_transferencia,
            es_reserva,
            es_cambio_ruta,
            id_venta,
            codigo,
            id_pasaje_padre
        )

        if resultado.get("msj"):
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado["msj2"]
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado["msj2"]
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": str(e),
            "Msj2": ""
        })


@atencion_bp.route('/EliminarReserva/<int:id>', methods=["POST"])
def eliminarReserva(id):
    try:
        resultado = Pasaje.eliminarReserva(id)
        if resultado.get("msj"):
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado["msj2"]
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado["msj2"]
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": str(e),
            "Msj2": ""
        })

@atencion_bp.route('/VerReserva/<int:idReserva>')
def verReserva(idReserva):
    reserva = Pasaje.obtener_por_id(idReserva)
    return render_template("atencion/reservaCRUD.html",tittle="Ver reserva",reserva=reserva,btnId="btn_Ver")

@atencion_bp.route('/CambiarEstado/<int:id_pasaje>', methods=["POST"])
def cambiarEstadoPasaje(id_pasaje):
    try:
        nuevo_estado = "P"
        resultado = Pasaje.pagarReserva(id_pasaje)
        if resultado["msj"] is not None:
            return jsonify({"Status": "success", "Msj": resultado["msj"],"Msj2":resultado["msj2"]})
        else:
            return jsonify({"Status": "error",   "Msj": resultado["msj"],"Msj2":resultado["msj2"]})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": repr(e), "Msj2": None}), 500

#END REGION RESERVAS
#REGION TIPO RECLAMO
@atencion_bp.route('/GetData_TiposReclamo')
def listarTiposReclamos():
    try:
        resultados = Tipo_Reclamo.obtener_todos()
        return jsonify({"Status":"success","data":resultados})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500
    
@atencion_bp.route('/RegistrarTipoReclamo',methods=["GET","POST"])
def registrarTipoReclamo():
    if request.method == "GET":
        return render_template("atencion/tipoReclamoCRUD.html",tittle="Nuevo tipo reclamo",btnId="btn_Registrar")
    else:
        try:
            nombre = request.form["nombre"]
            resultado = Tipo_Reclamo.registrar(nombre)
            if resultado.get("msj") is not None:
                return jsonify({
                    "Status": "success",
                    "Msj": resultado["msj"],
                    "Msj2": resultado.get("msj2")
                })
            else:
                return jsonify({
                    "Status": "error",
                    "Msj": "",
                    "Msj2": resultado.get("msj2")
                })
        except Exception as e:
                return jsonify({
                    "Status": "error",
                    "Msj": repr(e),
                    "Msj2": resultado.get("msj2")
                })

@atencion_bp.route('/EditarTipoReclamo/<int:idTipoReclamo>',methods=["GET","POST"])
def editarTipoReclamo(idTipoReclamo):
    if request.method == "GET":
        tipo = Tipo_Reclamo.obtener_por_id(idTipoReclamo)
        return render_template("atencion/tipoReclamoCRUD.html",tipoReclamo=tipo,tittle="Editar tipo reclamo",btnId="btn_Actualizar")
    else:
        try:
            nombre_tipo = request.form["nombre"]
            estado = request.form["estado"]
            resultado = Tipo_Reclamo.editar(idTipoReclamo,nombre_tipo,estado)

            if resultado.get("msj") is not None:
                return jsonify({
                    "Status": "success",
                    "Msj": resultado["msj"],
                    "Msj2": resultado.get("msj2")
                })
            else:
                return jsonify({
                    "Status": "error",
                    "Msj": "",
                    "Msj2": resultado.get("msj2")
                })
        except Exception as e:
                return jsonify({
                    "Status": "error",
                    "Msj": repr(e),
                    "Msj2": resultado.get("msj2")
                })

@atencion_bp.route('/EliminarTipoReclamo/<int:idTipoReclamo>',methods=["POST"])
def eliminarTipoReclamo(idTipoReclamo):
    try:
        resultado = Tipo_Reclamo.eliminar(idTipoReclamo)

        if resultado.get("msj") is not None:
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado.get("msj2")
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado.get("msj2")
            })
    except Exception as e:
            return jsonify({
                "Status": "error",
                "Msj": repr(e),
                "Msj2": resultado.get("msj2")
            })

@atencion_bp.route('/verTipoReclamo/<int:idTipoReclamo>')
def verTipoReclamo(idTipoReclamo):
    tipo = Tipo_Reclamo.obtener_por_id(idTipoReclamo)
    return render_template("atencion/tipoReclamoCRUD.html",tipoReclamo=tipo,tittle="Ver tipo reclamo",btnId="btn_Ver")  

@atencion_bp.route("/darBajaTipoReclamo/<int:idTipoReclamo>",methods=["POST"])
def darBajaTipoReclamo(idTipoReclamo):
    try:
        resultado = Tipo_Reclamo.darBaja(idTipoReclamo)
        if resultado.get("msj") is not None:
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado.get("msj2")
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado.get("msj2")
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": repr(e),
            "Msj2": resultado.get("msj2")
        })

#END REGION
#REGION RECLAMO
@atencion_bp.route('/GetData_Reclamo')
def listarReclamos():
    try:
        resultados = Reclamo.obtener_todos()
        return jsonify({"Status":"success","data":resultados})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500
    
@atencion_bp.route('/RegistrarReclamo',methods=["GET","POST"])
def registrarReclamo():
    if request.method == "GET":
        return render_template("atencion/reclamoCRUD.html",tittle="Nuevo reclamo",btnId="btn_Registrar")
    else:
        try:
            idTipoReclamo = int(request.form["idTipoReclamo"])
            detalle = request.form["detalle"]
            monto = request.form["monto"]
            idPasaje = request.form["id_pasaje"]
            motivo = request.form["motivo"]

            resultado = Reclamo.registrar(idTipoReclamo,detalle,monto,idPasaje,motivo)
            
            if resultado.get("msj") is not None:
                return jsonify({
                    "Status": "success",
                    "Msj": resultado["msj"],
                    "Msj2": resultado.get("msj2")
                })
            else:
                return jsonify({
                    "Status": "error",
                    "Msj": "",
                    "Msj2": resultado.get("msj2")
                })
        except Exception as e:
                return jsonify({
                    "Status": "error",
                    "Msj": repr(e),
                    "Msj2": resultado.get("msj2")
                })
    
@atencion_bp.route('/EditarReclamo/<int:idReclamo>', methods=["GET","POST"])
def editarReclamo(idReclamo):
    if request.method == "GET":
        reclamo = Reclamo.obtener_por_id(idReclamo)
        return render_template("atencion/reclamoCRUD.html",reclamo=reclamo,tittle="Editar reclamo",btnId="btn_Actualizar")
    else:
        try:
            idTipoReclamo = int(request.form["idTipoReclamo"])
            detalle = request.form["detalle"]
            monto = request.form["monto"]
            idPasaje = request.form["id_pasaje"]
            motivo = request.form["motivo"]
            estado = request.form["estado"]

            resultado = Reclamo.editar(idReclamo,idTipoReclamo,detalle,monto,idPasaje,motivo,estado)
            if resultado.get("msj") is not None:
                return jsonify({
                    "Status": "success",
                    "Msj": resultado["msj"],
                    "Msj2": resultado.get("msj2")
                })
            else:
                return jsonify({
                    "Status": "error",
                    "Msj": "",
                    "Msj2": resultado.get("msj2")
                })
        except Exception as e:
                return jsonify({
                    "Status": "error",
                    "Msj": repr(e),
                    "Msj2": resultado.get("msj2")
                })

@atencion_bp.route('/EliminarReclamo/<int:idReclamo>',methods=["POST"])
def eliminarReclamo(idReclamo):
    try:
        resultado = Reclamo.eliminar(idReclamo)
        if resultado.get("msj") is not None:
            return jsonify({
                    "Status": "success",
                    "Msj": resultado["msj"],
                    "Msj2": resultado.get("msj2")
                })
        else:
            return jsonify({
                    "Status": "error",
                    "Msj": "",
                    "Msj2": resultado.get("msj2")
                })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": repr(e),
            "Msj2": resultado.get("msj2")
        })

@atencion_bp.route('/VerReclamo/<int:idReclamo>')
def verReclamo(idReclamo):
    reclamo = Reclamo.obtener_por_id(idReclamo)
    return render_template("atencion/reclamoCRUD.html",reclamo=reclamo,tittle="Editar reclamo",btnId="btn_Ver")

@atencion_bp.route("/darBajaReclamo/<int:idReclamo>",methods=["POST"])
def darBajaReclamo(idReclamo):
    try:
        resultado = Reclamo.darBajaReclamo(idReclamo)

        if resultado.get("msj") is not None:
            return jsonify({
                "Status": "success",
                "Msj": resultado["msj"],
                "Msj2": resultado.get("msj2")
            })
        else:
            return jsonify({
                "Status": "error",
                "Msj": "",
                "Msj2": resultado.get("msj2")
            })
    except Exception as e:
        return jsonify({
            "Status": "error",
            "Msj": repr(e),
            "Msj2": ""
        })

#END REGION