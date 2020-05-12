from flask import Flask
from app import config
from app.models import db

from app.controller.user import main

app = Flask(__name__)
app.config.from_object(config.Config)

app.register_blueprint(main)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
