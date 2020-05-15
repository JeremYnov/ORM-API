from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, User, Post, Comment, Message, Follow
from sqlalchemy import or_
import datetime
from datetime import timedelta

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

@message.route('/talk/<int:id>', methods=['GET', 'POST'])
def talk(id):
    userLog = User.query.filter_by(id=1).first()
    messages = db.session.query(Message).filter(or_(Message.send_by_id==id, Message.receive_by_id==id)).filter(or_(Message.send_by_id==userLog.id, Message.receive_by_id==userLog.id)).order_by(Message.set_date).all()
    receiveUser = User.query.filter_by(id=id).first()
    error = None
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        if content == "":
            error = "vous n'avez pas écris de message"
        else:    
            now = datetime.datetime.utcnow() + timedelta(hours=2)
            message = Message(content, now.strftime('%Y-%m-%d %H:%M:%S'), userLog, receiveUser)
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('message.talk', id=id))


    return render_template('pages/message/talk.html', messages=messages, userLog=userLog, id=id, error=error)    