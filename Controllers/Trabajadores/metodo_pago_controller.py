from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from Models.metodo_pago import MetodoPago
from werkzeug.utils import secure_filename
import os

metodo_pago_bp = Blueprint('metodo_pago', __name__, url_prefix='/trabajadores/metodos_pago')

@metodo_pago_bp.route('/GestionarMetodosPago')
def Menu_MetodosPago():
    # Captura el mensaje de la URL, si existe
    msg = request.args.get('msg', '')
    return render_template('metodo_pago/metodos_pago.html', active_page="metodos_pago", active_menu='mMetodosPago', msg=msg)

# Ruta para registrar un nuevo método de pago
@metodo_pago_bp.route('/MetodoPagoNuevo', methods=['GET', 'POST'])
def MetodoPago_Nuevo():
    if request.method == 'POST':
        return registrar_metodo_pago()
    
    return render_template('metodo_pago/metodo_pago_crud.html', 
                           tittle="Registrar método de pago", 
                           btnId="btn_Registrar", 
                           metodo_pago=None)

# Ruta para editar y ver un método de pago (con id)
@metodo_pago_bp.route("/MetodoPagoNuevo/<int:id>", methods=['GET', 'POST'])
def MetodoPago_Editar_Ver(id):
    metodo_pago = MetodoPago.obtener_por_id(id)
    if metodo_pago is None:
        return jsonify({"Status": "error", "Msj": "Método de pago no encontrado"})
    
    ver = request.args.get('ver', False)  # Verificar si el acceso es solo para ver
    return render_template('metodo_pago/metodo_pago_crud.html', 
                           metodo_pago=metodo_pago, 
                           tittle="Ver método de pago" if ver else "Editar método de pago", 
                           btnId="btn_Editar" if not ver else "btn_Ver", 
                           ver=ver)

# Función para registrar el nuevo método de pago
@metodo_pago_bp.route('/RegistrarMetodoPago', methods=["POST"])
def registrar_metodo_pago():
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
            logo_path = f"/Static/img/trabajadores/{logo_filename}"
            logo.save(os.path.join("Static/img/trabajadores", logo_filename))
        else:
            logo_path = "/Static/img/trabajadores/default-logo.png"  # Logo por defecto

        mensajes = MetodoPago.registrar(nombre.strip(), logo_path, estado.strip())
        
        # Redirigir con un mensaje de éxito
        return redirect(url_for('metodo_pago.Menu_MetodosPago', msg="Método de pago registrado exitosamente"))

    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

# Ruta para editar un método de pago
@metodo_pago_bp.route("/EditarMetodoPago/<int:id>", methods=['GET', 'POST'])
def editar_metodo_pago(id):
    metodo_pago = MetodoPago.obtener_por_id(id)
    if metodo_pago is None:
        return jsonify({"Status": "error", "Msj": "Método de pago no encontrado"})
    
    if request.method == 'POST':
        nombre = request.form.get("nombre").strip()
        estado = request.form.get("estado").strip()
        logo = request.files.get("logo")

        if not nombre or not estado:
            return jsonify({"Status": "error", "Msj": "Nombre y estado son obligatorios"})

        if logo:
            logo_filename = secure_filename(logo.filename)
            logo_path = f"/Static/img/trabajadores/{logo_filename}"
            logo.save(os.path.join("Static/img/trabajadores", logo_filename))
        else:
            logo_path = metodo_pago['logo']

        mensajes = MetodoPago.editar(id, nombre, logo_path, estado)
        
        # Redirigir con un mensaje de éxito
        return redirect(url_for('metodo_pago.Menu_MetodosPago', msg="Método de pago editado exitosamente"))

    return render_template('metodo_pago/metodo_pago_crud.html', metodo_pago=metodo_pago, tittle="Editar método de pago", btnId="btn_Editar")

# Ruta para eliminar un método de pago
@metodo_pago_bp.route("/EliminarMetodoPago/<int:id>", methods=['POST'])
def eliminar_metodo_pago(id):
    try:
        mensajes = MetodoPago.eliminar(id)
        return jsonify(mensajes)
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error: {repr(e)}"})

# Ruta para obtener todos los métodos de pago
@metodo_pago_bp.route("/GetData_MetodosPago", methods=['GET'])
def get_metodos_pago():
    try:
        metodos_pago = MetodoPago.obtener_todos()
        if metodos_pago:
            return jsonify({"Status": "success", "data": metodos_pago})
        return jsonify({"Status": "error", "Msj": "No se encontraron métodos de pago."})
    except Exception as e:
        return jsonify({"Status": "error", "Msj": f"Error al obtener los métodos de pago: {repr(e)}"})
