from __init__ import  db


like = db.Table('like',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('Post.id'), primary_key=True),
)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    age = db.Column(db.Integer)
    mail = db.Column(db.String(255))
    password = db.Column(db.String(255))

    post = db.relationship('Post', backref='post')

    comment = db.relationship('Post', secondary='comment', backref=db.backref('user', lazy='dynamic'))

    message = db.relationship('Message', backref='message')

    like = db.relationship('Post', secondary=like, backref=db.backref('like', lazy='dynamic'))


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    image = db.Column(db.String(255))
    publication_date = db.Column(db.String(255))
    modification_date = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comment = db.relationship('User', secondary='comment', backref=db.backref('post', lazy='dynamic'))


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    set_date = db.Column(db.DateTime)
    send_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receive_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.content)


class Comment(db.Model):
    __tablename__ = 'comment'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    content = db.Column(db.String(255))
    publication_date = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.content)
