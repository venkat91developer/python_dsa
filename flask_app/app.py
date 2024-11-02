from app import create_app, db
from flask.cli import with_appcontext
import click

app = create_app()

@app.cli.command("create_db")
@with_appcontext
def create_db():
    pass
    # db.create_all()
    # print("Database created!")

if __name__ == '__main__':
    app.run(debug=True)
