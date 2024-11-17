from flask import Flask
from flask_cors import CORS
from app.routes import main_routes
from .models.UrlModel import db
from config import Config
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_app():
    """Cria a aplicação Flask e registra os blueprints.
    
    Retorna a aplicação Flask configurada.
    """
    app = Flask(__name__)
    CORS(app)
    
    # Carregar as configurações
    app.config.from_object(Config)
    
    # Inicializar o banco de dados
    db.init_app(app)

    # Criar as tabelas no banco de dados (caso ainda não existam)
    with app.app_context():
        db.create_all()

    # Registrar os blueprints
    app.register_blueprint(main_routes)
    
    return app
