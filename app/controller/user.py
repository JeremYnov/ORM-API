from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User, Post, Comment, Message, Follow

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/zeaafae')
def index():
    return render_template('pages/index.html')


@main.route('/test')
def test():
    # test insertion ligne
    user = User("louis", 4, "aaa@ynov.com", "aaaa")
    db.session.add(user)

    receive = User(username="louisss", age=7,
                   mail="aa@ynov.com", password="aa")
    db.session.add(receive)
    db.session.commit()

    u = user.query.filter_by(id=1).first()
    r = user.query.filter_by(id=2).first()

    post = Post("louis", "aaa@ynov.com", "aaaa",
                '2019-01-16 00:00:00', '2019-01-16 00:00:00', u)
    db.session.add(post)

    user.like.append(post)

    comment = Comment(content="blabla", publication_date='2019-01-16 00:00:00')
    comment.post = post
    user.comment.append(comment)

    message = Message('aaa', '2019-01-16 00:00:00', u, r)
    db.session.add(message)

    follow = Follow(user, receive)
    db.session.add(follow)

    db.session.commit()
    return "test"


@main.route('/user')
def user():
    return "controller user"


@main.route('/createdb')
def createdb():
    db.drop_all()
    db.create_all()
    return "la db a été créer"

@main.route('/login')
def login():
    return render_template('pages/login.html')

@main.route('/signup')
def signup():    
    return render_template('pages/signup.html')

@main.route('/signup', methods = ['POST'])
def signup_post():
    username = request.form.get('username')
    age = request.form.get('age')
    email = request.form.get('email')
    password = request.form.get('password')
    passwordRepeat = request.form.get('repassword')

    user = User.query.filter_by(email=email).first

    if user:
        flash('L\'adresse email utilisée est déjà utilisée')
        return redirect(url_for('user.signup'))
    
    newUser = User(username=username, age=age, mail=email, password=password)

    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for('user.login'))