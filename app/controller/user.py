from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    # test insertion ligne
    # user = User(username="louis", age=4, mail="aaa@ynov.com", password="aaaa")
    # db.session.add(user)

    # post = Post(title="louis", content="aaa@ynov.com", image="aaaa",
    #             publication_date='2019-01-16 00:00:00', modification_date='2019-01-16 00:00:00', user=user)
    # db.session.add(post)

    # user.like.append(post)

    # comment = Comment(content="blabla", publication_date='2019-01-16 00:00:00')
    # comment.post = post
    # user.comment.append(comment)

    # db.session.commit()
    return render_template('pages/index.html')


@main.route('/user')
def user():
    return "controller user"
