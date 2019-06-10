from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextField
from models import User


class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user= User.query.filter_by(username=username.data).first()
		if user :
			raise ValidationError('That username exists!!,please enter another')

	def validate_email(self,email):
		user= User.query.filter_by(email=email.data).first()
		if user :
			raise ValidationError('That email exists!!,please enter another')

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	password = PasswordField('Password',validators=[DataRequired(),Length(max=10)])
	remember = BooleanField('Remember Me')
	submit=SubmitField('Login')

class PickUpForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	location = StringField('Location',validators=[DataRequired()])
	trip = TextField('Trip',validators=[DataRequired()])
	submit=SubmitField('Submit')




class BookForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	trip_date = StringField('Trip Date',validators=[DataRequired()])
	destination = TextField('Destination',validators=[DataRequired()])
	submit=SubmitField('Submit')

	def validate_username(self,username):
		user= User.query.filter_by(username=username.data).first()
		if user :
			raise ValidationError('That username exists!!,please enter another')

