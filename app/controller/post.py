import os
import requests
import json

from flask import Blueprint, render_template, jsonify, request, url_for, redirect
from app.models import db, User, Post, Comment, Follow
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask_login import current_user


post = Blueprint('post', __name__, url_prefix='/')


@post.route('/', methods=['GET',  'POST'])
def index():
    if not(current_user.is_authenticated):
        return redirect(url_for('main.login'))

    user = current_user
    url = request.url_root + 'api/post/' + str(user.id)

    currentUser = {
        'id': str(user.id),
        'username': user.username,
        'age': str(user.age),
        'mail': user.mail,
        'avatar': user.avatar
    }

    response = requests.get(url)
    posts = response.json()

    if request.method == 'POST':
        if request.form['type'] == 'newPost':

            title = request.form['title']
            content = request.form['content']
            image = request.files['image']

            resp = newPost(user, title, content, image, posts)

            response = requests.get(url)
            posts = response.json()

            return render_template('pages/post/index.html', posts=posts, currentUser=currentUser,
                                   error=resp['error'], message=resp['message'])

        elif request.form['type'] == 'newComment':

            comment = request.form['comment']
            postId = request.form['postId']

            resp = newComment(user, comment, postId)

            response = requests.get(url)
            posts = response.json()

            return render_template('pages/post/index.html', posts=posts, currentUser=currentUser,
                                   error=resp['error'], message=resp['message'])

        elif request.form['type'] == 'like':

            like = request.form['like']
            postId = request.form['postId']

            resp = newlike(user, postId, like)

            response = requests.get(url)
            posts = response.json()

            return render_template('pages/post/index.html', posts=posts, currentUser=currentUser,
                                   error=resp['error'], message=resp['message'])

    return render_template('pages/post/index.html', posts=posts, currentUser=currentUser)
    # return jsonify(posts)


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
            results = {}
            arrayPost = []

            for follow in follows:

                for post in follow.follower.post:
                    arrayComment = []

                    comments = Comment.query.filter_by(
                        post_id=post.id).order_by(Comment.publication_date.desc()).all()

                    for comment in comments:
                        arrayComment.append({
                            'post_id': str(comment.post_id),
                            'user': {
                                'id': str(comment.user.id),
                                'username': comment.user.username,
                                'avatar': str(comment.user.avatar)
                            },
                            'content': comment.content,
                            'publication_date': comment.publication_date
                        })

                    arrayPost.append(
                        {
                            'id': str(post.id),
                            'title': post.title,
                            'content': post.content,
                            'image': post.image,
                            'publication_date': post.publication_date,
                            'modification_date': post.modification_date,
                            'user': {
                                'id': str(follow.follower.id),
                                'username': follow.follower.username
                            },
                            'likes': str(len(post.like_post)),
                            'comments': arrayComment
                        }
                    )

                results = {
                    'posts': arrayPost
                }

            success = True
            message = "Tout fonctionne bien"

        api = jsonify(message=message,
                      success=success,
                      count=len(arrayPost),
                      results=results
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


def newlike(user, postId, like):
    if postId and like:

        if like == 'like':

            post = Post.query.get(int(postId))

            user.like.append(post)
            db.session.commit()

            error = False
            message = "like"

    else:
        error = True
        message = "pas like"

    response = {
        'error': error,
        'message': message
    }

    return response


def newComment(user, content, postId):
    if postId and content:
        post = Post.query.get(int(postId))
        now = datetime.now()

        comment = Comment(user, post, content, now)

        db.session.add(comment)
        db.session.commit()

        error = False
        message = "le commentaire a bien été posté"

    else:
        error = True
        message = "le commentaire n'a pas été posté"

    response = {
        'error': error,
        'message': message
    }

    return response


def newPost(user, title, content, image, posts):
    if title and content:
        now = datetime.utcnow() + timedelta(hours=2)

        if image:
            if allowed_image(image.filename):
                if image.mimetype == 'image/png' or image.mimetype == 'image/jpg' or image.mimetype == 'image/jpeg':
                    post = Post(title, content,
                                image.filename, now, now, user)

                    db.session.add(post)
                    db.session.commit()

                    filename = secure_filename(image.filename)
                    uploads_dir = 'app/static/uploads/' + \
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
