from modelos.ArticuloModel import ArticuloModel

class ArticuloController:

    @staticmethod
    def get_all():
        articulos = ArticuloModel.get_all()
        return [a.serializar() for a in articulos]

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        return articulo.serializar() if articulo else {}

    @staticmethod
    def create(data):
        articulo = ArticuloModel.deserializar(data)
        return {"success": articulo.create()}

    @staticmethod
    def update(data):
        articulo = ArticuloModel.deserializar(data)
        return {"success": articulo.update()}

    @staticmethod
    def delete(id):
        return {"success": ArticuloModel.delete(id)}
