from app.modelos.MarcaModel import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        return MarcaModel.get_one(id)

    @staticmethod
    def create(data):
        categoria = MarcaModel.deserializar(data)
        return {"success": categoria.create()}

    @staticmethod
    def update(data):
        categoria = MarcaModel.deserializar(data)
        return {"success": categoria.update()}

    @staticmethod
    def delete(id):
        return {"success": MarcaModel.delete(id)}