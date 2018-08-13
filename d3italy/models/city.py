from d3italy import db

class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    population = db.Column(db.Integer)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"))
    region = db.relationship('Region', backref='city', foreign_keys=region_id, lazy=True)