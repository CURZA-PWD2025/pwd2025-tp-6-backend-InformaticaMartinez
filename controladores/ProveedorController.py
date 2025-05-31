from modelos.ProveedorModel import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        proveedores = ProveedorModel.get_all()
        return [p.serializar() for p in proveedores]

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_one(id)
        return proveedor.serializar() if proveedor else {}

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        exito = proveedor.create()
        return {"success": exito}

    @staticmethod
    def update(data):
        proveedor = ProveedorModel.deserializar(data)
        exito = proveedor.update()
        return {"success": exito}

    @staticmethod
    def delete(id):
        exito = ProveedorModel.delete(id)
        return {"success": exito}
