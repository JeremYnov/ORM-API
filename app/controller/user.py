from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User, Post, Comment, Message, Follow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, current_user, logout_user
import requests

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/zeaafae')
def index():
    return render_template('pages/index.html')


@main.route('/user')
def user():
    return "controller user"


@main.route('/createdb')
def createdb():
    db.drop_all()
    db.create_all()
    return "la db a été créer"

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profil'))
    return render_template('pages/login.html')

@main.route('/signup')
def signup():  
    if current_user.is_authenticated:
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
    if not(current_user.is_authenticated):
        return redirect(url_for('main.login'))
    userLog = current_user
    URL_ROOT = request.url_root
    error = None
    follow = 0
    if(id == None):
        # user connecter
        url = URL_ROOT + 'api/post/user/' + str(userLog.id)
        user = User.query.filter_by(id=userLog.id).first()

        if request.method == 'POST':
            username = request.form.get('username')
            age = request.form.get('age')

            if username != None:
                
                if username == "":
                    error = "vous n'avez pas mis votre username"

                elif age == "":
                    error = "vous n'avez pas mis votre age"  

                else:
                    user.username = username
                    user.age = age
                    db.session.commit()

    elif id == userLog.id:            
        return redirect(url_for('main.profil', id=None))

    else:
        url = URL_ROOT + 'api/post/user/' + str(id)
        user = User.query.filter_by(id=id).first()

        follow = Follow.query.filter_by(follower_id=userLog.id, followby_id=id).first()
        if not(follow):
            follow = 1

        if request.method == 'POST':

            if follow == 1:
                following = Follow(userLog, user)
                db.session.add(following)

            else:
                db.session.delete(follow)
           
    following = Follow.query.filter_by(follower_id=user.id).count()
    followers = Follow.query.filter_by(followby_id=user.id).count()
    numberPosts = Post.query.filter_by(user_id=user.id).count()
    stats = {"followers": followers, "following": following, "posts": numberPosts}

    

    if request.method == 'POST':
        post = request.form.get('post')
        if post != None:
            postDelete = Post.query.filter_by(id=post).first()
            print("AAAAAAAAAAAAAAAAAAA : " + str(postDelete.like_post))
            for like in postDelete.like_post:
                like.like.remove(like)
            commentDelete = Comment.query.filter_by(id=post).all()  
            for comment in commentDelete:
                db.session.delete(comment)
           
            db.session.delete(postDelete)


        db.session.commit()
        return redirect(url_for('main.profil', id=id))

    response = requests.get(url)
    user = response.json()

    return render_template('pages/user/profil.html', stats=stats, error=error, id=id, user=user, follow=follow)


@main.route('/profil/<int:id>/followers', methods=['GET', 'POST'], strict_slashes=False)
@main.route('/profil/followers', methods=['GET', 'POST'], strict_slashes=False)
def followers(id=None):
    if not(current_user.is_authenticated):
        return redirect(url_for('main.login'))

    route = 0
    url = request.url_rule

    if str(url) == "/profil/followers":
        route = 1

    elif id != None:
        route = 2 

    userLog = current_user
    button = []
    if id == None:
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


    return render_template('pages/user/follow.html', followers=followers, id=id, userLog=userLog, button=button,route=route)



@main.route('/profil/<int:id>/following', methods=['GET', 'POST'], strict_slashes=False)
@main.route('/profil/following', methods=['GET', 'POST'], strict_slashes=False)
def following(id=None):
    if not(current_user.is_authenticated):
        return redirect(url_for('main.login'))

    route = 0    
    url = request.url_rule
    if str(url) == "/profil/following":
        route = 3
    elif id != None:
        route = 4
    userLog = current_user
    button = []
    followerUserLog = Follow.query.filter_by(follower_id=userLog.id).all() 
    if id == None:
        followers = Follow.query.filter_by(followby_id=userLog.id).all()

        for follower in followers:
            status = False

            for followerUser in followerUserLog:
                
                if follower.follower_id == followerUser.followby_id:
                    button.append({'followBy': follower.follower_id, 'value': 0})
                    status = True

            if status == False:
                button.append({'followBy': follower.follower_id, 'value': 1})

    else: 
        user = User.query.filter_by(id=id).first()
        followers = Follow.query.filter_by(followby_id=user.id).all()      
        followerUserLog = Follow.query.filter_by(follower_id=userLog.id).all() 
    
        for follower in followers:
            status = False

            if follower.follower_id == userLog.id:
                    button.append({'followBy': follower.follower_id, 'value': 2})
                    status = True

            for followerUser in followerUserLog:
                print(followerUser.follower_id)
                print(followerUser.followby_id)
                if follower.follower_id == followerUser.followby_id and status == False:
                    button.append({'followBy': follower.follower_id, 'value': 0})
                    status = True

            if status == False:
                button.append({'followBy': follower.follower_id, 'value': 1})
            
    if request.method == 'POST':  
        unfollowUser = request.form.get('unfollowUser')  
        followUser = request.form.get('followUser') 

        if unfollowUser != None:
            userLogUnFollow = Follow.query.filter_by(followby_id=unfollowUser, follower_id=userLog.id).first()
            db.session.delete(userLogUnFollow)

        else:
            userFollow = User.query.filter_by(id=followUser).first()
            following = Follow(userLog, userFollow)
            db.session.add(following)  

        db.session.commit()
        return redirect(url_for('main.following', id=id))    


    return render_template('pages/user/follow.html', followers=followers, id=id, userLog=userLog, button=button, route=route)
