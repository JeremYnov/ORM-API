from flask import Blueprint, render_template
from app.models import db, User, Post, Comment, Message, Follow

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    return render_template('pages/index.html')

@main.route('/test')
def test():    
    # test insertion ligne
    user = User("louis", 4, "aaa@ynov.com", "aaaa")
    db.session.add(user)

    receive = User(username="louisss", age=7, mail="aa@ynov.com", password="aa")
    db.session.add(receive)
    
    u = user.query.filter_by(id = 1).first()
    r = user.query.filter_by(id = 2).first()

    post = Post("louis", "aaa@ynov.com", "aaaa",
                '2019-01-16 00:00:00', '2019-01-16 00:00:00', u)
    db.session.add(post)

    user.like.append(post)

    comment = Comment(content="blabla", publication_date='2019-01-16 00:00:00')
    comment.post = post
    user.comment.append(comment)

    message = Message('aaa', '2019-01-16 00:00:00', u, r)
    db.session.add(message)

    follow = Follow(u, r)
    db.session.add(follow)

    db.session.commit()
    return "test"
    


@main.route('/user')
def user():
    return "controller user"
