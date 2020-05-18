from flask import Blueprint, render_template
from app.models import db, User, Post, Comment, Message, Follow

fixtures = Blueprint('fixtures', __name__, url_prefix='/')


@fixtures.route('/createdb')
def createdb():
    db.drop_all()
    db.create_all()
    return "la db a été créer"


@fixtures.route('/fixtures')
def fixture():

    for i in range(5):
        user = User("user" + str(i), i, "user" + str(i) +
                    "@ynov.com", "aaaa", "default.png")
        receive = User("user1" + str(i), i, "user" + str(i) +
                       "@ynov.com", "aaaa", "default.png")
        db.session.add(user)
        db.session.add(receive)

        db.session.commit()

        follow = Follow(user, receive)
        db.session.add(follow)

        db.session.commit()

        for j in range(5):
            post = Post("post" + str(i), "vdbziego", "default.png",
                        '2019-01-16 00:00:00', '2019-01-16 00:00:00', user)
            db.session.add(post)

            user.like.append(post)

            commentary = Comment(
                content="blabla", publication_date='2019-01-16 00:00:00')
            commentary.post = post
            user.comment.append(commentary)

        for k in range(5):
            message = Message('message' + str(k),
                              '2019-01-16 00:00:00', user, receive)
            db.session.add(message)

    return 'fixtures'
