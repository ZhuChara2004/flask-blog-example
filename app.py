import os, datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    from models import Post
    return render_template('index.html', posts=Post.query.order_by(Post.created_at.desc()).all())


@app.route('/posts/<id>', methods=['GET'])
def show(id):
    from models import Post
    return render_template('show.html', post=Post.query.get(id))


@app.route('/posts/new', methods=['GET'])
def new():
    return render_template('new.html')


@app.route('/posts', methods=['POST'])
def create():
    from models import Post
    from app import db
    post = Post(request.form['title'], request.form['body'], datetime.datetime.now(), datetime.datetime.now())
    db.session.add(post)
    db.session.commit()
    return render_template('index.html', posts=Post.query.order_by(Post.created_at.desc()).all())


@app.route('/posts/<id>/edit', methods=['GET'])
def edit(id):
    from models import Post
    return render_template('edit.html', post=Post.query.get(id))


@app.route('/posts/<id>', methods=['POST'])
def update(id):
    from models import Post
    from app import db
    post = Post.query.get(id)
    post.title = request.form['title']
    post.body = request.form['body']
    db.session.add(post)
    db.session.commit()
    return render_template('show.html', post=post)


@app.route('/posts/<id>/delete', methods=['GET'])
def delete(id):
    from models import Post
    from app import db
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return render_template('index.html', posts=Post.query.order_by(Post.created_at.desc()).all())


if __name__ == '__main__':
    app.run()
