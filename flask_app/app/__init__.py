from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Set the configuration for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example using SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, disables track modifications warning
    
    db.init_app(app)
    
    return app
