from flask import Flask
from flask_cors import CORS
from app.rutas.MarcaRoutes import marca_bp
from app.rutas.ArticuloRoutes import articulo_bp
from app.rutas.CategoriaRoutes import categoria_bp
from app.rutas.ProveedorRoutes import proveedor_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(marca_bp)
    app.register_blueprint(articulo_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedor_bp)

    @app.route('/')
    def inicio():
        return '''
        <h1>TP 6 - Backend de Productos Informáticos</h1>
        <p>Rutas disponibles:</p>
        <ul>
            <li><a href="/marcas">marcas</a></li>
            <li><a href="/articulos">articulos</a></li>
            <li><a href="/categorias">categorias</a></li>
            <li><a href="/proveedores">proveedores</a></li>
        </ul>
        '''

    return app
