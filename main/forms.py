from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class CommentForm(FlaskForm):
    description = TextAreaField('',validators=[Required()])
	submit = SubmitField()
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about your self.',validators = [Required()])
    submit = SubmitField('Submit')
class BlogForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    description = TextAreaField('Blog Description', validators=[Required()]) 
    submit = SubmitField('Submit')



