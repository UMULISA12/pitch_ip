from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    category = StringField('Write a pitch category', validators=[Required()])
    pitch = TextAreaField('Write a pitch', validators=[Required()])
    author = StringField('enter your name', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    description= TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')