from app import app
from flask_restful import Resource, Api, reqparse
from app.models import Bike

api = Api(app)


class HelloWorld(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bike_id', type=int)
        parser.add_argument('card_id', type=int)
        args = parser.parse_args()

        bike = Bike.get_bike(args['bike_id'])
        if not bike.is_rented:
            bike.rent_bike(args['card_id'])
            return '', 200
        else:
            return '', 418


api.add_resource(HelloWorld, '/access_locker')
