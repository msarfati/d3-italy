import enum
from d3italy import db


class Region(db.Model):
    __tablename = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    status = db.Column(db.String(25))
    population = db.Column(db.Integer)
    area = db.Column(db.Integer)
    comuni = db.Column(db.Integer)
    capital_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    capital = db.relationship('City', lazy=True, uselist=False, post_update=True, foreign_keys=capital_id)
