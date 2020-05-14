from flask import Flask
from app import config
from app.models import db

from app.controller import user

app = Flask(__name__)
app.config.from_object(config.Config)

app.register_blueprint(user.main)
db.init_app(app)

# with app.app_context():
