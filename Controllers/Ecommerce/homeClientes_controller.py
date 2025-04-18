import hashlib
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, abort

homeClientes_bp = Blueprint('homeClientes', __name__, url_prefix='/ecommerce/home')

@homeClientes_bp.route('/inicio')
def index():
    return render_template('Ecommerce/home/home.html', active_page="home")

@homeClientes_bp.route('/error')
def error():
    return render_template('Ecommerce/error.html')
