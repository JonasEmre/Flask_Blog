from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.form import RegistrationForm, LoginForm

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} için üyelik oluşturuldu!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Üye Ol", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'nezu@nezublog.com' and form.password.data == '1234':
            flash('Başarılı şekilde giriş yapıldı', 'success')
            return redirect(url_for('home'))
        else:
            flash('Hatalı giriş. E-mail ya da şifrenizi kontrol edin.', 'danger')
    return render_template("login.html", title="Giriş", form=form)

