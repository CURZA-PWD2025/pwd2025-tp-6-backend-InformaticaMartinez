from flask import Blueprint, request, jsonify
from app.controladores.CategoriaController import CategoriaController

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def get_all():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route('/categorias/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(CategoriaController.get_one(id))

@categoria_bp.route('/categorias', methods=['POST'])
def create():
    data = request.json
    return jsonify(CategoriaController.create(data))

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(CategoriaController.update(data))

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(CategoriaController.delete(id))