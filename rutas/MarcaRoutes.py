from flask import Blueprint, request, jsonify
from controladores.MarcaController import MarcaController

marca_bp = Blueprint('marca_bp', __name__)

@marca_bp.route('/marcas', methods=['GET'])
def get_all():
    return jsonify(MarcaController.get_all())

@marca_bp.route('/marcas/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(MarcaController.get_one(id))

@marca_bp.route('/marcas', methods=['POST'])
def create():
    data = request.json
    return jsonify(MarcaController.create(data))

@marca_bp.route('/marcas/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(MarcaController.update(data))

@marca_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(MarcaController.delete(id))