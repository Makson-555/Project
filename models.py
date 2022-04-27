from app import app, db
from datetime import datetime
from sqlalchemy.orm import relationship


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'login': self.login,
            'password': self.password,
        }
    def __repr__(self):
        return '<Article %r>' % self.id


class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)
    comments = relationship("Comments", back_populates = "article")

    def __repr__(self):
        return '<Article %r>' % self.id


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = relationship("Article", back_populates = "comments")

    def __repr__(self):
        return '<Article %r>' % self.id