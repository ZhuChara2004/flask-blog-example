from app import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, body, created_at, updated_at):
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id: %r, title: %s, body: %s>' % (self.id, self.title, self.body)
