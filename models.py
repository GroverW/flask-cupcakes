"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    " Cupcake "

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(24), nullable=False)
    size = db.Column(db.String(24), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default="https://tinyurl.com/demo-cupcake")

    @classmethod
    def serialize(self, cupcake):
        return {
            'id': cupcake.id,
            'flavor': cupcake.flavor,
            'size': cupcake.size,
            'rating': cupcake.rating,
            'image': cupcake.image
        }


def connect_db(app):
    " Connect this database to provided flask app. "

    db.app = app
    db.init_app(app)