from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User, Post, Comment, Message, Follow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user


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

    searchUser = User.query.filter_by(mail=email).first()

    if searchUser:
        flash("L'adresse email entrée est déjà utilisée")
        return redirect(url_for('main.signup'))
    
    if password != passwordRepeat:
        flash("Les mots de passes ne sont pas similaires")
        return redirect(url_for('main.signup'))
        
    
    newUser = User(username=username, age=age, mail=email, password=generate_password_hash(password, method="pbkdf2:sha256", salt_length=8), avatar = None)

    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for('main.login'))


@main.route('/login', methods = ['POST'])
def login_post():
    
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(mail=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))


@main.route('/profil/<int:id>', strict_slashes=False)
@main.route('/profil/',  methods=['GET', 'POST'], strict_slashes=False)
def profil(id=None):
    if(id == None):
        user = User.query.filter_by(id=1).first()
        followers = Follow.query.filter_by(follower_id=user.id).count()
        following = Follow.query.filter_by(followby_id=user.id).count()
        numberPosts = Post.query.filter_by(user_id=user.id).count()
        stats = {"followers": followers, "following": following, "posts": numberPosts}

        posts = Post.query.filter_by(user_id=user.id).all()

        error = None
        if request.method == 'POST':
            username = request.form['username']
            age = request.form['age']
            if username == "":
                error = "vous n'avez pas écris de message"
            elif age == "":
                error = "vous n'avez pas mis votre age"   
            else:
                user.username = username
                user.age = age
                db.session.commit()

    return render_template('pages/user/profil.html', user=user, stats=stats, posts=posts, error=error)