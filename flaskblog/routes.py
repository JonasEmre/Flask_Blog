from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'title': 'Vegan Post',
        'author': 'John Doe',
        'content': 'Bu blogun içeriği et yememe üzerine kurulu anlatımlardır',
        'date': 'Nisan 16 2020'
    },
    {
        'title': 'Syrian War',
        'author': 'World News',
        'content': 'Bu blogun içeriği haber ile ilgili yazılar falan olmaktadır',
        'date': 'Nisan 23 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Ana Sayfa")


@app.route("/about")
def about():
    return render_template("about.html", title="Hakkımda")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        flash('Başarılı üyelik', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Üye Ol", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                next_page = next_page[1:]
            return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))
        else:
            flash('Hatalı giriş. E-mail ya da şifrenizi kontrol edin.', 'danger')
    return render_template("login.html", title="Giriş", form=form)


@app.route('/logout')
def log_out():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Hesabım', image_file=image_file)
