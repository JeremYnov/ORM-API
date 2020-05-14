from flask import Blueprint, render_template, jsonify, request
from app.models import db, User, Post, Comment, Follow
import requests


post = Blueprint('post', __name__, url_prefix='/')


@post.route('/')
def index():

    user = 1
    url = request.url_root + 'api/post/' + str(user)

    response = requests.request("GET", url)
    posts = response.json()

    return render_template('pages/post/index.html', posts=posts)


@post.route('/api/post/<int:id>', methods=['GET'])
def createApiPostFollowBy(id):
    try:
        follows = Follow.query.filter_by(follower_id=id).all()

        if not(follows):
            raise Exception({
                'success': False,
                'message': "l'utilisateur n'existe pas"
            })
        else:
            array = []

            for follow in follows:
                arrayPost = []

                for post in follow.followby.post:
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
