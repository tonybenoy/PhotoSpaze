from flask_wtf import FlaskForm 
from wtforms import SelectField, BooleanField, SubmitField, IntegerField, PasswordField, RadioField,StringField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length,Regexp

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=4, max=35)])  
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6, max=35),Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,35}$")])
    passwordrep = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')]) 
    submit = SubmitField("Register")