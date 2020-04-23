import os
import secrets
from flask import url_for, current_app
from flaskblog import mail
from PIL import Image
from flask_mail import Message


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_ext = os.path.splitext(form_picture.filename)[1]
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static\profile_pics', picture_fn)
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_mail(user):
    token = user.get_reset_token()
    msg = Message('Şifre Yenileme Linki', sender='y.emretoktas@gmail.com',
                  recipients=[user.email])
    msg.body = f'''Şifre yenileme için aşağıda gönderilen linke basınız.
    {url_for('users.reset_password', token=token, _external=True)}

    Eğer bu talebi oluşturmadıysanız görmezden gelebilirsiniz.
        '''
    mail.send(msg)
