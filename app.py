import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/')
def index():
    from models import Post
    return render_template('index.html', posts=Post.query.all())


@app.route('/post/<id>')
def show(id):
    from models import Post
    post = Post.query.get(id)
    return render_template('show.html', post=post)

if __name__ == '__main__':
    app.run()
