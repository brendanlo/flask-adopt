"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.


    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet class"""

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
    # TODO: nullable = false
    name = db.Column(
        db.String(150)
    )
    species = db.Column(
        db.String(100)
    )
    photo_url = db.Column(
        db.Text,
        default=""
    )
    age = db.Column(
        db.String(20)
    )
    notes = db.Column(
        db.Text,
        nullable=True
    )
    available = db.Column(
        db.Boolean,
        default=True
    )
