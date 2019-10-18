from app import db

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Bike {}>'.format(self.id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User {}>'.format(self.id)
    
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Rental {}>'.format(self.id)