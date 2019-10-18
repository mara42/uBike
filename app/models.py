from app import db

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rentals = db.relationship('Rental', backref='Bike', lazy=True)
    location = db.Column(db.String)

    def __repr__(self):
        return '<Bike {}>'.format(self.id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rentals = db.relationship('Rental', backref='Client', lazy=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))

    def __repr__(self):
        return '<User {}>'.format(self.id)
    
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    return_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Rental {}>'.format(self.id)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.relationship('User', backref='Client', lazy=True)

    def __repr__(self):
        return '<Card {}>'.format(self)