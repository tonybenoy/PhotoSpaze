from flask_wtf import FlaskForm 
from wtforms import SelectField, BooleanField, SubmitField, IntegerField, PasswordField, RadioField,StringField
from wtforms.validators import DataRequired, Regexp

class SearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    othersite = StringField('Other Site')
    facebook = BooleanField('Facebook')
    github = BooleanField('Github')
    twitter = BooleanField('Twitter')
    soundcloud = BooleanField('Soundcloud')
    instagram = BooleanField('Instagram')
    submit = SubmitField('Find')

