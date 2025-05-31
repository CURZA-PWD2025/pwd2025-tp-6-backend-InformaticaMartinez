from conexion import get_connection

class ArticuloModel:
    def __init__(self, id=None, descripcion=None, precio=None, stock=None, marca_id=None, proveedor_id=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca_id=data.get("marca_id"),
            proveedor_id=data.get("proveedor_id")
        )

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [ArticuloModel(**row) for row in rows]

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return ArticuloModel(**row) if row else None

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE ARTICULOS SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ARTICULOS WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
