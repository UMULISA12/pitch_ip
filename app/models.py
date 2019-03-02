from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(240))
    email = db.Column(db.String(240),unique = True,index = True)
    pass_secure = db.Column(db.String(240))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches=db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy="dynamic")
   

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    category = db.Column(db.String(200))
    pitch = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
   

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(id):
        pitches = Pitch.query.all()
        return pitches

    @classmethod
    def upvote(cls,id):
       pitch=Pitch.query.filter_by(pitch_id=id).all()
       upvotes=0
       upvotes=pitch.upvotes+1
       return upvotes

    @classmethod
    def downvote(cls,id):
       pitch=Pitch.query.filter_by(pitch_id=id).all()
       downvotes=0
       downvotes=pitch.downvotes+1
       return downvotes


class Comment(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(240))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))

    

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comment.query.filter_by(pitch_id=id).all()
