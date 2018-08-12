from d3italy import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    capital = db.Column(db.Boolean, default=False)
    population = db.Column(db.Integer)
    region = db.relationship('Region', backref='person', lazy=True)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"))