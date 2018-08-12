import enum
from d3italy import db


class RegionStatus(enum.Enum):
    ordinary = 0
    autonomous = 1


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    status = db.Column(db.Enum(RegionStatus))
    population = db.Column(db.Integer)
    area = db.Column(db.Integer)
    comuni = db.Column(db.Integer)
