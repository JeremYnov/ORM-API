from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User, Post, Comment, Message, Follow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, current_user, logout_user
import requests

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

@main.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/login')
def login():
    userLog = current_user
    if userLog:
        return redirect(url_for('main.profil'))
    return render_template('pages/login.html')

@main.route('/signup')
def signup():  
    userLog = current_user
    if userLog:
        return redirect(url_for('main.profil'))  
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
    print(user)

    if not user or not check_password_hash(user.password, password):
        flash('Vérifiez vos informations de connexion et reéssayez')
        return redirect(url_for('main.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profil'))



@main.route('/profil/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
@main.route('/profil/',  methods=['GET', 'POST'], strict_slashes=False)
def profil(id=None):
    URL_ROOT = request.url_root
    error = None

    if(id == None):
        # user connecter
        url = URL_ROOT + 'api/post/user/' + str(1)
        user = User.query.filter_by(id=1).first()
        if request.method == 'POST':
            username = request.form['username']
            age = request.form['age']
            if username == "":
                error = "vous n'avez pas mis votre username"
            elif age == "":
                error = "vous n'avez pas mis votre age"   
            else:
                user.username = username
                user.age = age
                db.session.commit()
    # 1 est la personne connecter
    elif id == 1:            
        return redirect(url_for('main.profil', id=None))
    else:
        url = URL_ROOT + 'api/post/user/' + str(id)
        user = User.query.filter_by(id=id).first()
        # follower_id=1 etant la personne connecter
           
    following = Follow.query.filter_by(follower_id=user.id).count()
    followers = Follow.query.filter_by(followby_id=user.id).count()
    numberPosts = Post.query.filter_by(user_id=user.id).count()
    stats = {"followers": followers, "following": following, "posts": numberPosts}

    follow = Follow.query.filter_by(follower_id=1, followby_id=id).first()
    if not(follow):
        follow = 1

    if request.method == 'POST':
        if follow == 1:
            # 1 personne connecter
            userLog = User.query.filter_by(id=1).first()
            following = Follow(userLog, user)
            db.session.add(following)
        else:
            db.session.delete(follow)

        db.session.commit()
        return redirect(url_for('main.profil', id=id))

    response = requests.get(url)
    user = response.json()

    return render_template('pages/user/profil.html', stats=stats, error=error, id=id, user=user, follow=follow)


@main.route('/profil/<int:id>/followers', methods=['GET', 'POST'], strict_slashes=False)
@main.route('/profil/followers', methods=['GET', 'POST'], strict_slashes=False)
def followers(id=None):
    userLog = User.query.filter_by(id=1).first()
    button = []
    if id == None:
        # personne connecter le 1
        followers = Follow.query.filter_by(follower_id=userLog.id).all()

        if request.method == 'POST':
            follower = request.form.get('follower')
            userLogUnFollow = Follow.query.filter_by(follower_id=userLog.id, followby_id=follower).first()
            db.session.delete(userLogUnFollow)
            db.session.commit()
            return redirect(url_for('main.followers', id=None))
    else: 
        user = User.query.filter_by(id=id).first()
        followers = Follow.query.filter_by(follower_id=user.id).all()      
        followerUserLog = Follow.query.filter_by(follower_id=userLog.id).all() 
    
        for follower in followers:
            status = False
            if follower.followby_id == userLog.id:
                    button.append({'followBy': follower.followby_id, 'value': 2})
                    status = True
            for followerUser in followerUserLog:
                if follower.followby_id == followerUser.followby_id and status == False:
                    button.append({'followBy': follower.followby_id, 'value': 0})
                    status = True
            if status == False:
                button.append({'followBy': follower.followby_id, 'value': 1})
            
        if request.method == 'POST':  
            unfollowUser = request.form.get('unfollowUser')  
            followUser = request.form.get('followUser') 

            if unfollowUser != None:
                userLogUnFollow = Follow.query.filter_by(follower_id=userLog.id, followby_id=unfollowUser).first()
                db.session.delete(userLogUnFollow)
            else:
                userFollow = User.query.filter_by(id=followUser).first()
                following = Follow(userLog, userFollow)
                db.session.add(following)
            db.session.commit()
            return redirect(url_for('main.followers', id=id))    


    return render_template('pages/user/follow.html', followers=followers, id=id, userLog=userLog, button=button)

