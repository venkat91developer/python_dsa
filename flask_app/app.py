from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
import click

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the PostgreSQL database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres$321@localhost/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    @app.cli.command("create_db")
    @with_appcontext
    def create_db():
        """Create the database."""
        db.create_all()
        print("Database created!")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)