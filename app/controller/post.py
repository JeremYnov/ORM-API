from flask import Blueprint, render_template, jsonify, request, url_for, redirect
from app.models import db, User, Post, Comment, Follow
import requests
from datetime import datetime, timedelta


post = Blueprint('post', __name__, url_prefix='/')


@post.route('/')
def index():
    user = 1
    url = request.url_root + 'api/post/' + str(user)

    response = requests.request("GET", url)
    posts = response.json()

    URL_ROOT = request.url_root
    error = None
    message = None

    return render_template('pages/post/index.html', posts=posts, URL_ROOT=URL_ROOT, error=error, message=message)


@post.route('/add/new/post', methods=['POST'])
def newPost():
    id = 1
    user = User.query.get(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']

        if title or content:
            now = datetime.utcnow() + timedelta(hours=2)

            if image:
                if allowed_image(image.filename):
                    post = Post(title, content, image.filename, now, now, user)
                else:
                    error = True
                    message = "c pas une image"
                    return redirect(url_for('post.index'))

            else:
                post = Post(title, content, None, now, now, user)

            db.session.add(post)
            db.session.commit()

        else:
            error = True
            message = "il manque le titre ou le contenue"
            return redirect(url_for('post.index'))

        error = False
        message = "le post a bien été posté"

    return redirect(url_for('post.index'))


@post.route('/api/post/<int:id>', methods=['GET'])
def createApiPostFollowBy(id):
    try:
        follows = Follow.query.filter_by(followby_id=id).all()

        if not(follows):
            raise Exception({
                'success': False,
                'message': "l'utilisateur n'a pas de follower avec des posts"
            })
        else:
            array = []

            for follow in follows:
                arrayPost = []

                for post in follow.follower.post:
                    arrayPost.append(
                        {
                            'id': post.id,
                            'title': post.title,
                            'content': post.content,
                            'image': post.image,
                            'publication_date': post.publication_date,
                            'modification_date': post.modification_date,
                            'user_id': post.user_id,
                            'likes': len(post.like_post)
                        }
                    )

                array.append({
                    'user': {
                        'id': follow.followby.id,
                        'username': follow.followby.username
                    },
                    'post': arrayPost,
                })

            success = True
            message = "Tout fonctionne bien"

        api = jsonify(message=message,
                      success=success,
                      count=len(array),
                      results=array
                      )

    except Exception as e:
        api = jsonify(e.args)

    return api


@post.route('/api/post/user/<int:id>', methods=['GET'])
def createApiPostUser(id):
    try:
        user = User.query.get(id)
        follower = Follow.query.filter_by(follower_id=id).all()
        followby = Follow.query.filter_by(followby_id=id).all()

        if user is None:
            raise Exception({
                'success': False,
                'message': "l'utilisateur n'existe pas"
            })
        else:
            arrayPost = []

            for post in user.post:
                arrayPost.append(
                    {
                        'id': post.id,
                        'title': post.title,
                        'content': post.content,
                        'image': post.image,
                        'publication_date': post.publication_date,
                        'modification_date': post.modification_date,
                        'user_id': post.user_id,
                        'likes': len(post.like_post)
                    }
                )

            apiUser = {
                'id': user.id,
                'username': user.username,
                'age': user.age,
                'mail': user.mail,
                'avatar': user.avatar,
                'posts': arrayPost,
                'follower': len(follower),
                'followby': len(followby)
            }

            success = True
            message = "Tout fonctionne bien"

        api = jsonify(message=message,
                      success=success,
                      results=apiUser
                      )

    except Exception as e:
        api = jsonify(e.args)

    return api


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in ["JPEG", "JPG", "PNG"]:
        return True
    else:
        return False
