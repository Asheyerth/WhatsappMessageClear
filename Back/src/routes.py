from flask import Blueprint
from flask import request, jsonify

# Definir el Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "¡Hola desde Flask con Blueprints!"

@main_bp.route('/about')
def about():
    return "Acerca de la aplicación"

#######################
@main_bp.route('/procesarMensaje', methods=['POST'])
def procesarMensaje():
    print('Llegando')
    data = request.get_json()
    print('Llego')
    print(data)
    #return jsonify({"mensaje": f"Hola, {data['message']}!"})
    response = jsonify({'Data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response