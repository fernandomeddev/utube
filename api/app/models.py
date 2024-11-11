from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UrlModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    watch_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Url {self.watch_url}>'
