from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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
            raise ValidationError('E-posta adresi daha önce kullanılmış')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Giriş')
    remember = BooleanField('Hatırla')


class UpdateForm(FlaskForm):
    username = StringField('Kullanıcı Adı',
                           validators=[DataRequired(),
                                       Length(min=2, max=8)])
    email = StringField('E-posta', validators=[DataRequired(),
                                               Email()])
    file = FileField('Profil Resmi', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Bilgileri Güncelle')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Kullanıcı adı daha önce alınmış')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('E-posta adres daha önce kullanılmış')


class PostForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired()])
    content = TextAreaField('İçerik', validators=[DataRequired()])
    submit = SubmitField('Yayınla')


class RequestResetForm(FlaskForm):
    email = StringField('E-posta', validators=[DataRequired(),
                                               Email()])
    submit = SubmitField('Şifre Yenileme Talep Et')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Bu adrese kayıtlı bir hesap yok.')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Şifre', validators=[DataRequired()])
    confirm_password = PasswordField('Şifreyi Onayla',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Şireyi Güncelle')
