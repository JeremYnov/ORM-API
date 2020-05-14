from flask import Blueprint, render_template
from app.models import db, User, Post, Comment, Message, Follow
from sqlalchemy import or_

message = Blueprint('message', __name__, url_prefix='/')

@message.route('/message')
def list_message():
    # on recupere le user connecter
    userLog = User.query.filter_by(id=1).first()
    messages = db.session.query(Message).filter(or_(Message.send_by_id==1, Message.receive_by_id==1)).order_by(Message.set_date).all()
    listMessage = []
    statut = False
    for message in messages:
        statut = False
        if not(listMessage):
                listMessage.append(message) 
        for value in listMessage:
            if userLog == message.send_by:
                if message.receive_by == value.receive_by and message.send_by == value.send_by:
                    statut = True
                if message.send_by == value.receive_by and message.receive_by == value.send_by:
                    statut = True    
            else:
                if message.send_by == value.send_by and message.receive_by == value.receive_by:
                    statut = True
                if message.send_by == value.receive_by and message.receive_by == value.send_by:
                    statut = True

        if statut == False :      
            listMessage.append(message)      
            
                

    return render_template('pages/message/listMessage.html', listMessage=listMessage, userLog=userLog)

@message.route('/talk/<int:id>')
def talk(id):
    userLog = User.query.filter_by(id=1).first()
    messages = db.session.query(Message).filter(or_(Message.send_by_id==id, Message.receive_by_id==id)).filter(or_(Message.send_by_id==userLog.id, Message.receive_by_id==userLog.id)).order_by(Message.set_date).all()
    return render_template('pages/message/talk.html', messages=messages, userLog=userLog)    