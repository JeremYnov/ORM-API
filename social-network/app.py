from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import  db




app = Flask(__name__)
app.config.from_object("config.Config")



from models import *

db.init_app(app)
with app.app_context():
    db.create_all()  # Create database tables for our data models

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

