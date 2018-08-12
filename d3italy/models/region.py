from d3italy import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    '''Name is the d3 name'''
    name = db.Column(db.String(50), nullable=False)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
    # capital = db.relationship('City', backref='region', lazy=True)
    # capital_id = db.Column(db.Integer, db.ForeignKey("city.id"))