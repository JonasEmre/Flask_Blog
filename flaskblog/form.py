from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı Adı',
                           validators=[DataRequired(),
                                       Length(min=2, max=8)])
    email = StringField('E-posta', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    confirm_password = PasswordField('Şifreyi Onayla',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Katıl')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Giriş')
    remember = BooleanField('Hatırla')