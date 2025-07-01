import os
from flask import Blueprint, request, jsonify, render_template, session, flash, redirect, url_for, abort
from Models.pasaje import Pasaje
from Models.tipoReclamo import Tipo_Reclamo
from Models.reclamo import Reclamo
from Models.reembolso import Reembolso

atencion_bp = Blueprint('atencion', __name__, url_prefix='/trabajadores/atencion')

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
    return render_template('atencion/reservas.html', active_page="reservas", active_menu='mAtencion')

@atencion_bp.route('/GestionarTipoReclamo')
def Menu_TipoReclamo():
    return render_template('atencion/tipoReclamo.html', active_page="tipoReclamo", active_menu='mAtencion')

@atencion_bp.route('/GestionarReclamo')
def Menu_Reclamo():
    return render_template('atencion/reclamo.html', active_page="reclamo", active_menu='mAtencion')

@atencion_bp.route('/GestionarReembolso')
def Menu_Reembolso():
    return render_template('atencion/reembolso.html', active_page="reembolso", active_menu='mAtencion')

# END VIEWS

# FUNCIONES
# REGION RESERVAS
@atencion_bp.route('/GetData_Reservas')
def listarReservas():
    try:
        reservas = Pasaje.obtener_todas_reservas()

        return jsonify({"Status": "success","data": reservas})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500

@atencion_bp.route('/RegistrarReserva', methods=["GET", "POST"])
def registrarReserva():
    if request.method == "GET":
        return render_template(
            "atencion/reservaCRUD.html",
            active_page="reservas", 
            active_menu='mAtencion',
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
    return render_template("atencion/reservaCRUD.html", active_page="reservas", active_menu='mAtencion', tittle="Ver reserva",reserva=reserva,btnId="btn_Ver")

@atencion_bp.route('/CambiarEstado/<int:id_pasaje>', methods=["POST"])
def cambiarEstadoPasaje(id_pasaje):
    try:
        numComprobante = Pasaje.generar_numComprobante()
        codigoUnico = Pasaje.generar_codigo_unico()
        resultado = Pasaje.pagarReserva(id_pasaje,numComprobante,codigoUnico)
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
        return render_template("atencion/tipoReclamoCRUD.html", active_page="tipoReclamo", active_menu='mAtencion', tittle="Nuevo tipo reclamo",btnId="btn_Registrar")
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
        return render_template("atencion/tipoReclamoCRUD.html", active_page="tipoReclamo", active_menu='mAtencion', tipoReclamo=tipo,tittle="Editar tipo reclamo",btnId="btn_Actualizar")
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
    return render_template("atencion/tipoReclamoCRUD.html",active_page="tipoReclamo", active_menu='mAtencion',tipoReclamo=tipo,tittle="Ver tipo reclamo",btnId="btn_Ver")  

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
        return render_template("atencion/reclamoCRUD.html",active_page="reclamo", active_menu='mAtencion',tittle="Nuevo reclamo",btnId="btn_Registrar")
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
        return render_template("atencion/reclamoCRUD.html",active_page="reclamo", active_menu='mAtencion',reclamo=reclamo,tittle="Editar reclamo",btnId="btn_Actualizar")
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
    return render_template("atencion/reclamoCRUD.html",active_page="reclamo", active_menu='mAtencion',reclamo=reclamo,tittle="Editar reclamo",btnId="btn_Ver")

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

# REGION REEMBOLSO

@atencion_bp.route('/GetData_Reembolsos')
def listarReembolsos():
    try:
        reembolso = Reembolso.obtener_todos_completo()
        return jsonify({"Status": "success","data": reembolso})
    except Exception as e:
        return jsonify({"Status": "error","Msg": str(e)}), 500
    

@atencion_bp.route("/cambiarEstadoReembolso", methods=["POST"])
def cambiar_estado_reembolso():
    try:
        data = request.get_json()
        id_reembolso = data.get("Id")
        nuevo_estado = data.get("estado")

        if not id_reembolso or nuevo_estado is None:
            return jsonify({"Status": "error", "Msj": "Faltan datos requeridos"}), 400

        resultado = Reembolso.cambiar_estado(id_reembolso, nuevo_estado)

        if resultado.get("@MSJ"):
            return jsonify({"Status": "success", "Msj": resultado["@MSJ"]})
        else:
            return jsonify({"Status": "error", "Msj": resultado.get("@MSJ2", "Ocurrió un error desconocido")})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error interno: {str(e)}"}), 500

    

# END REGION REEMBOLSO