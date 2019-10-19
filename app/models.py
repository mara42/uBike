from app import db
import flask_login

from datetime import datetime


class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rentals = db.relationship('Rental', backref='Bike', lazy=True)
    location = db.Column(db.String)

    def __repr__(self):
        return '<Bike {}>'.format(self.id)

    @classmethod
    def get_bike(cls, id):
        return cls.query.filter_by(id=id).first()

    @property
    def is_rented(self):
        return bool(self.get_active_rental())

    def rent_bike(self, user_id):
        if self.is_rented:
            return False
        r = Rental(bike_id=self.id, client_id=user_id, return_date=None)
        db.session.add(r)
        db.session.commit()
        return True

    @classmethod
    def find_free_bikes(cls):
        return list(filter(lambda b: not b.is_rented, cls.query.all()))

    def return_bike(self):
        if not self.is_rented:
            return False
        r = self.get_active_rental()
        r.return_time = datetime.now()
        db.session.commit()

    def get_active_rental(self):
        return Rental.query.filter_by(bike_id=self.id,
                                      return_time=None).first()


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rentals = db.relationship('Rental', backref='Client', lazy=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))

    def __repr__(self):
        return '<User {}>'.format(self.id)

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    return_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<Rental {}>'.format(self.id)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.relationship('User', backref='Owner', lazy=True)

    def __repr__(self):
        return '<Card {}>'.format(self)
