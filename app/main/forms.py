from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    pitch = TextAreaField('Write a pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    review = TextAreaField('Leave a comment')
    submit = SubmitField('Submit')