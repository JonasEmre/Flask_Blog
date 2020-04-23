from flask import Blueprint, flash, redirect, render_template, url_for, abort, request
from flaskblog import db
from flask_login import current_user, login_required
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Blog paylaştınız', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_post.html', title='Yeni Blog',
                           form=form, legend='Yeni Gönderi Oluştur')


@posts.route('/posts/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/posts/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Gönderi başarıyla güncellendi', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('new_post.html', title='Gönderi Güncelle',
                           form=form, legend='Gönderi Güncelle')


@posts.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Gönderi silindi!', 'success')
    return redirect(url_for('main.home'))
