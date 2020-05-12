from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from __init__ import  db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/social_network'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

db.init_app(app)
with app.app_context():
    db.create_all()  

@app.route('/')
def index():
    return render_template('pages/index.html')

if __name__ == '__main__':
    app.run(debug=True)

