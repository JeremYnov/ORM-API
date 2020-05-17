import os
import requests
import json

from flask import Blueprint, render_template, jsonify, request, url_for, redirect
from app.models import db, User, Post, Comment, Follow
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename


post = Blueprint('post', __name__, url_prefix='/')


@post.route('/', methods=['GET',  'POST'])
def index():
    id = 3

    user = User.query.get(id)

    url = request.url_root + 'api/post/' + str(id)

    response = requests.get(url)
    posts = response.json()

    if request.method == 'POST':

        title = request.form['title']
        content = request.form['content']
        image = request.files['image']

        resp = newPost(user, title, content, image, posts)

        return render_template('pages/post/index.html', posts=posts,
                               error=resp['error'], message=resp['message'])

    return render_template('pages/post/index.html', posts=posts)


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


def newPost(user, title, content, image, posts):
    if title or content:
        now = datetime.utcnow() + timedelta(hours=2)

        if image:
            if allowed_image(image.filename):
                if image.mimetype == 'image/png' or image.mimetype == 'image/jpg' or image.mimetype == 'image/jpeg':
                    post = Post(title, content,
                                image.filename, now, now, user)

                    db.session.add(post)
                    db.session.commit()

                    filename = secure_filename(image.filename)
                    uploads_dir = 'uploads/' + \
                        str(user.id) + '/posts/' + str(post.id) + '/'

                    os.makedirs(uploads_dir, exist_ok=True)
                    image.save(os.path.join(uploads_dir, filename))

                    error = False
                    message = "le post a bien été posté"

                else:
                    error = True
                    message = "c pas une image"

            else:
                error = True
                message = "c pas une image"

        else:
            post = Post(title, content, None, now, now, user)

            db.session.add(post)
            db.session.commit()

            error = False
            message = "le post a bien été posté"

    else:
        error = True
        message = "il manque le titre ou le contenue"

    response = {
        'error': error,
        'message': message
    }

    return response
