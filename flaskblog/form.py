from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Kullanıcı adı daha önce alınmış')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-posta adres daha önce kullanılmış')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Giriş')
    remember = BooleanField('Hatırla')
