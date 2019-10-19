from app import db
from app.models import Bike, Rental, Card, User

for i in range(1, 10):
    db.session.add(Bike())
    db.session.add(Card())
    db.session.add(User(card_id = i))
    if i % 2:
        db.session.add(Rental(bike_id = i, client_id = i))
db.session.commit()