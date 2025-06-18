from conexion import get_connection

class ArticuloModel:
    def __init__(self, id=None, descripcion=None, precio=None, stock=None,
                 marca_id=None, proveedor_id=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id
        self.categorias = categorias or []  

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id,
            "categorias": self.categorias
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca_id=data.get("marca_id"),
            proveedor_id=data.get("proveedor_id"),
            categorias=data.get("categorias", [])
        )

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        rows = cursor.fetchall()
        articulos = []
        for row in rows:
            articulo = ArticuloModel(**row)
            articulo.categorias = ArticuloModel.get_categorias(row["id"])
            articulos.append(articulo)
        cursor.close()
        conn.close()
        return articulos

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            articulo = ArticuloModel(**row)
            articulo.categorias = ArticuloModel.get_categorias(articulo.id)
            return articulo
        return None

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        )
        self.id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        self._actualizar_categorias()
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
        self._actualizar_categorias()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
        cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def get_categorias(articulo_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT C.id, C.nombre FROM CATEGORIAS C
            JOIN ARTICULOS_CATEGORIAS AC ON C.id = AC.categoria_id
            WHERE AC.articulo_id = %s
            """,
            (articulo_id,)
        )
        categorias = cursor.fetchall()
        cursor.close()
        conn.close()
        return categorias

    def _actualizar_categorias(self):
        if self.id is None:
            return
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,))
        for categoria in self.categorias:
            categoria_id = categoria["id"] if isinstance(categoria, dict) else categoria
            cursor.execute(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (self.id, categoria_id)
            )
        conn.commit()
        cursor.close()
        conn.close()
