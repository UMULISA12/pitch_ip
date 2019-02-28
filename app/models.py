# from . import db
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
# from . import login_manager

# # @login_manager.user_loader
# # def load_user(user_id):
# #     return User.query.get(int(user_id))

# # # class Movie:
# # #     '''
# # #     Movie class to define Movie Objects
# # #     '''

# # #     def __init__(self,id,title,overview,poster,vote_average,vote_count):
# # #         self.id =id
# # #         self.title = title
# # #         self.overview = overview
# # #         self.poster = "https://image.tmdb.org/t/p/w500/" + poster
# # #         self.vote_average = vote_average
# # #         self.vote_count = vote_count



# # class Pitch:

# #     all_pitches = []

# #     def __init__(self,pitch_id,pitch):
# #         self.pitch_id = pitch_id
# #         self.pitch = pitch

# #     def save_pitch(self):
# #         Pitch.all_pitches.append(self)


# #     @classmethod
# #     def clear_pitches(cls):
# #         Pitch.all_pitches.clear()

# #     @classmethod
# #     def get_pitches(cls,id):

# #         response = []

# #         for pitch in cls.all_pitches:
# #             if pitch.pitch_id == id:
# #                 response.append(pitch)

# #         return response



# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     pass_secure = db.Column(db.String(255))

#     def __repr__(self):
#         return f'User {self.username}'

#     @property
#     def password(self):
#             raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#             self.pass_secure = generate_password_hash(password)


#     def verify_password(self,password):
#             return check_password_hash(self.pass_secure,password)



# # class Comment(db.Model):
# #     __tablename__ = 'comments'

# #     id = db.Column(db.Integer,primary_key = True)
# #     name = db.Column(db.String(255))
# #     users = db.relationship('User',backref = 'role',lazy="dynamic")


# #     def __repr__(self):
# #         return f'User {self.name}'


# # from . import db
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from flask_login import UserMixin
# # from . import login_manager
# # from datetime import datetime

# # Pitch Model


# class Pitch(db.Model):  # (db.Model)
#     """
#     Defining the pitch object
#     """
#     __tablename__ = 'pitches'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     Description = db.Column(db.String)
#     writer = db.Column(db.String)
#     category = db.Column(db.String)
#     upvotes = db.Column(db.Integer)
#     downvotes = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     # posted = db.Column(db.DateTime, default=datetime.utcnow)

#     # def save_pitches(self):
#     #     db.session.add(self)
#     #     db.session.commit()

#     @classmethod
#     def get_pitches(cls):
#         pitches = Pitch.query.all()
#         return pitches

#     @classmethod
#     def get_categories(cls, category):
#         pitch_cat = Pitch.query.filter_by(category=category)
#         return pitch_cat

#     all_pitches = []

#     def __init__(self,title,description,writer,category,upvotes,downvotes,users):
#         self.title = title
#         self.description = description
#         self.writer = writer
#         self.category = category
#         self.upvotes = upvotes
#         self.downvotes = downvotes
#         self.users = users


# class Comment(db.Model):  # (db.Model)
#     """
#     Defining the pitch object
#     """
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     comment = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls):
#         comments = Comment.query.all()
#         return comments

#     all_comments = []

#     def __init__(self,title,comment,user):
#         self.title = title
#         self.comment = comment
#         self.user = user


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# # User Model


# # class User(UserMixin, db.Model):
# #     """
# #     Defining the user object
# #     """
# #     __tablename__ = 'users'

# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(255), index=True)
# #     email = db.Column(db.String(255), unique=True, index=True)
# #     password_hash = db.Column(db.String(255))
# #     # pitches = db.relationship('Pitch', backref='user', lazy="dynamic")

# #     @property
# #     def password(self):
# #         raise AttributeError("You cannot read the password attribute")

# #     @password.setter
# #     def password(self, password):
# #         self.password_hash = generate_password_hash(password)

# #     def verify_password(self, password):
# #         return check_password_hash(self.password_hash, password)

# #     def __repr__(self):
# #         return f'Pitch {self.username}'
# #     # pass


# # class Review(db.Model):
# #     """
# #     Defining the review object
# #     """
# #     pass

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
    category = db.Column(db.String(200))
    pitch = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
   

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(Pitch.posted.desc())
        return pitches


class Comment(db.Model):

    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(240))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))

    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comment.query.filter_by(pitch_id=id).all()
            return comments
