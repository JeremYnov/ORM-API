from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


like = db.Table('like',
                db.Column('user_id', db.Integer, db.ForeignKey(
                    'user.id'), primary_key=True),
                db.Column('post_id', db.Integer, db.ForeignKey(
                    'post.id'), primary_key=True),
                )
    

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    age = db.Column(db.Integer)
    mail = db.Column(db.String(255))
    password = db.Column(db.String(255))
    avatar = db.Column(db.String(255))

    post = db.relationship('Post', backref='user')

    comment = db.relationship('Comment')

    like = db.relationship('Post', secondary=like,
                           backref=db.backref('like', lazy='dynamic'))

    send_by = db.relationship("Message", foreign_keys='Message.send_by_id', back_populates="send_by")
    receive_by = db.relationship("Message", foreign_keys='Message.receive_by_id', back_populates="receive_by")   

    send_by = db.relationship("Follow", foreign_keys='Follow.follower_id', back_populates="follower")
    receive_by = db.relationship("Follow", foreign_keys='Follow.followby_id', back_populates="followby")                    

    def __init__(self, username, age, mail, password, avatar):
        self.username = username
        self.age = age
        self.mail = mail
        self.password = password
        self.avatar = avatar

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    image = db.Column(db.String(255))
    publication_date = db.Column(db.DateTime)
    modification_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, image, publication_date, modification_date, user_id):
        self.title = title
        self.content = content
        self.image = image
        self.publication_date = publication_date
        self.modification_date = modification_date
        self.user_id = user_id.id


class Comment(db.Model):
    __tablename__ = 'comment'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    content = db.Column(db.String(50))
    publication_date = db.Column(db.DateTime)
    post = db.relationship("Post")


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    set_date = db.Column(db.DateTime)
    send_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receive_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    send_by = db.relationship("User", backref="userSendBy", uselist=False, foreign_keys=[send_by_id])
    receive_by = db.relationship("User", backref="userReceiveBy", uselist=False, foreign_keys=[receive_by_id])

    def __init__(self, content, set_date, send_by_id, receive_by_id):
        self.content = content
        self.set_date = set_date
        self.send_by_id = send_by_id.id
        self.receive_by_id = receive_by_id.id


class Follow(db.Model):
    __tablename__ = 'follow'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followby_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
   
    follower = db.relationship("User", backref="follower", uselist=False, foreign_keys=[follower_id])
    followby = db.relationship("User", backref="followby", uselist=False, foreign_keys=[followby_id])

    def __init__(self, follower_id, followby_id):
        self.follower_id = follower_id.id
        self.followby_id = followby_id.id