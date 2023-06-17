from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField
from wtforms.validators import email_validator


class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25)])
    password = PasswordField("Password", [validators.Length(min=8, max=40)])


class JoinForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25)])
    password = PasswordField("Password", [validators.Length(min=8, max=40)])
    email = EmailField("Email",[validators.Length(min=10, max=40)])