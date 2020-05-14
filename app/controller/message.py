from flask import Blueprint, render_template
from app.models import db, User, Post, Comment, Message, Follow
from sqlalchemy import or_

message = Blueprint('message', __name__, url_prefix='/')

@message.route('/message')
def list_message():
    # on recupere le user connecter
    userLog = User.query.filter_by(id=1).first()
    Messages = db.session.query(Message).filter(or_(Message.send_by_id==1, Message.receive_by_id==1)).all()
    listMessage = []
    for message in Messages:
        for value in listMessage:
            if userLog == message.send_by:
                if message.receive_by != value.receive_by:
                    listMessage.append(message)
            else:
                if message.send_by != value.send_by:
                    listMessage.append(message)
                

    return render_template('pages/message/listMessage.html', listMessage=Messages, userLog=userLog.id, m=listMessage)

@message.route('/talk/<int:id>')
def talk(id):
    return render_template('pages/message/talk.html', id=id)    