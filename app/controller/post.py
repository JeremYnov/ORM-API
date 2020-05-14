from flask import Blueprint, render_template, jsonify
from app.models import db, User, Post, Comment, Follow
import json

post = Blueprint('post', __name__, url_prefix='/')


@post.route('/')
def index(id):

    return render_template('pages/post/index.html')


@post.route('/api/post/<int:id>', methods=['GET'])
def apiPost(id):

    try:
        follows = Follow.query.filter_by(follower_id=id).all()

        array = []

        if not(follows):
            raise Exception({
                'success': False,
                'message': "l'utilisateur n'existe pas"
            })
        else:
            for follow in follows:
                arrayPost = []

                for post in follow.followby.post:
                    like = Follow.query.filter_by(post_id=post.id).all()
                    arrayPost.append(
                        {
                            'id': post.id,
                            'title': post.title,
                            'content': post.content,
                            'image': post.image,
                            'publication_date': post.publication_date,
                            'modification_date': post.modification_date,
                            'user_id': post.user_id,
                            'likes': len(like)
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
