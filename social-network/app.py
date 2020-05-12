from flask import Flask
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
    # test insertion ligne
    user = User(username="louis", age=4, mail="aaa@ynov.com", password="aaaa")
    db.session.add(user)

    post = Post(title="louis", content="aaa@ynov.com", image="aaaa", publication_date='2019-01-16 00:00:00', modification_date='2019-01-16 00:00:00', user=user)
    db.session.add(post)

    user.like.append(post)

    comment = Comment(content="blabla", publication_date='2019-01-16 00:00:00')
    comment.post = post
    user.comment.append(comment)

    db.session.commit()
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

