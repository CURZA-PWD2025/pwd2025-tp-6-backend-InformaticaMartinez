from app.modelos.CategoriaModel import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        return CategoriaModel.get_one(id)

    @staticmethod
    def create(data):
        categoria = CategoriaModel.deserializar(data)
        return {"success": categoria.create()}

    @staticmethod
    def update(data):
        categoria = CategoriaModel.deserializar(data)
        return {"success": categoria.update()}

    @staticmethod
    def delete(id):
        return {"success": CategoriaModel.delete(id)}