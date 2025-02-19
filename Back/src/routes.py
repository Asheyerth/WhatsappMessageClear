from flask import Blueprint
from flask import request, jsonify
#Obtener el servicio
from src.services.message_service import procesarMsgBasic,procesarMsgUserSender,procesarMsgUserReplace

# Definir el Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "¡Hola desde Flask con Blueprints!"

@main_bp.route('/about')
def about():
    return "Acerca de la aplicación"

#######################
@main_bp.route('/BasicClean', methods=['POST'])
def BasicClean():
    print('Llegando')
    data = request.get_json()
    print('Llego')
    print(data)
    #Procesamiento
    processedData = procesarMsgBasic(data['input']['message']) 
    #Es un dict con llaves INPUT y luego MESSAGE: {'input': {'message': '[10:13 p.m., 23/1/2025] Rouge: es que es un random de Threads', 'name': 'nombre', 'age': 'edad'}}
    #Devolución
    response = jsonify({'Data': processedData})
    return response

@main_bp.route('/UserClean', methods=['POST'])
def UserClean():
    print('Llegando')
    data = request.get_json()
    print('Llego')
    print(data)
    #Procesamiento
    processedData = procesarMsgUserSender(data['input']['message'], data['input']['userSender']) 
    #Es un dict con llaves INPUT y luego MESSAGE: {'input': {'message': '[10:13 p.m., 23/1/2025] Rouge: es que es un random de Threads', 'name': 'nombre', 'age': 'edad'}}
    #Devolución
    response = jsonify({'Data': processedData})
    return response

@main_bp.route('/UserReplaceClean', methods=['POST'])
def UserReplaceClean():
    print('Llegando')
    data = request.get_json()
    print('Llego')
    print(data)
    #Procesamiento
    processedData = procesarMsgUserReplace(data['input']['message'], data['input']['userSender'], data['input']['userReplace']) 
    #Es un dict con llaves INPUT y luego MESSAGE: {'input': {'message': '[10:13 p.m., 23/1/2025] Rouge: es que es un random de Threads', 'name': 'nombre', 'age': 'edad'}}
    #Devolución
    response = jsonify({'Data': processedData})
    return response