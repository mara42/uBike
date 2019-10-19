from app import db
import flask_login

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rentals = db.relationship('Rental', backref='Bike', lazy=True)

    def __repr__(self):
        return '<Bike {}>'.format(self.id)

class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rentals = db.relationship('Rental', backref='Client', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.id)
    
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Rental {}>'.format(self.id)
