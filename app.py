from flask import Flask
from rutas.MarcaRoutes import marca_bp
from rutas.ArticuloRoutes import articulo_bp
from rutas.CategoriaRoutes import categoria_bp
from rutas.ProveedorRoutes import proveedor_bp

app = Flask(__name__)

app.register_blueprint(marca_bp)
app.register_blueprint(articulo_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(proveedor_bp)

@app.route('/')
def inicio():
    return '''
    <h1>TP 6 - Backend de Productos Informáticos</h1>
    <ul>
        <li><a href="/marcas">/marcas</a></li>
        <li><a href="/articulos">/articulos</a></li>
        <li><a href="/categorias">/categorias</a></li>
        <li><a href="/proveedores">/proveedores</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
