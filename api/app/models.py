from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UrlModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    views = db.Column(db.Integer)
    publish_date = db.Column(db.DateTime)
    author = db.Column(db.String(80))
    length = db.Column(db.Integer)
    watch_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Url {self.watch_url}>'
