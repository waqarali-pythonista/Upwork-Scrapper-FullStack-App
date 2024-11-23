from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
db = SQLAlchemy()

def create_app():
    # Load environment variables
    load_dotenv()
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config.from_object('config.Config')
    
    CORS(app)
    db.init_app(app)

    # Register blueprints
    from app.routes.job_routes import job_bp
    app.register_blueprint(job_bp)

    with app.app_context():
        db.create_all()

    return app
