from d3italy import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    '''Name is the d3 name'''
    name = db.Column(db.String(50), unique=True, nullable=False)
    name_en = db.Column(db.String(50))
    name_it = db.Column(db.String(50))
