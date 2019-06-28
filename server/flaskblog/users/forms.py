from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # validate if user already exists
    def validate_username(self, username):
        user = User.objects(username=username.data)
        if user:
            raise ValidationError("That username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data)
        if user:
            raise ValidationError("That email is taken")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    # validate if user already exists
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data)
            if user:
                raise ValidationError("That username is taken")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.objects(email=email.data)
            if user:
                raise ValidationError("That email is taken")


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        user = User.objects(email=email.data)
        if user is None:
            raise ValidationError("There's no account with that email.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Reset Password')


