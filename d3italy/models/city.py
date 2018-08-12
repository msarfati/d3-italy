from d3italy import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    '''Name is the d3 name'''
    name = db.Column(db.String(50), nullable=False)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    capital = db.Column(db.Boolean)
    region = db.relationship('Region', backref='person', lazy=True)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"))