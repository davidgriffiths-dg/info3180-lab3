from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea



class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    subject = StringField('subject', validators =[DataRequired()])
    message = StringField('message',validators =[DataRequired()], widget = TextArea())
