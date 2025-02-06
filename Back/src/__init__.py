from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
print("Hola")

def create_app():
    app = Flask(__name__)

    # Importar las rutas después de crear app (para evitar importaciones circulares)
    from src.routes import main_bp
    app.register_blueprint(main_bp)

    return app