from flask import Flask
from app import config
from app.models import db
from app.controller import user, post, message, fixtures
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object(config.Config)

db.init_app(app)


login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(id))

# with app.app_context():


app.register_blueprint(user.main)
app.register_blueprint(post.post)
app.register_blueprint(message.message)
app.register_blueprint(fixtures.fixtures)