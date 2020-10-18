from flask_restful import Resource, reqparse
from chatbot_api.order.order_dto import OrderDto
from chatbot_api.order.order_dao import OrderDao

class OrderApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_id', type=int, required=True, help='This field cannot be left blank')
        # 수정 
        parser.add_argument('order_time', type=int, required=True, help='This field cannot be left blank')
        # 수정 : this field can be the empty space
        parser.add_argument('order_cmnt', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('userid', type=str, required=True, help='This field cannot be left blank')
        parser.add_argument('shop_id', type=int, required=True, help='This field cannot be left blank')
        parser.add_argument('food_id', type=int, required=True, help='This field cannot be left blank')
        parser.add_argument('review_id', type=int, required=True, help='This field cannot be left blank')

    def get(self, time) :
        order = self.dao.fetch_by_time(time)
        if order: 
            return order.json()
        return {'message' : 'Order not found'}, 404

    def get(self, userid) :
        order = self.dao.fetch_by_time(userid)
        if order: 
            return order.json()
        return {'message' : 'Order not found'}, 404

    def get(self, shop_id) :
        order = self.dao.fetch_by_time(shop_id)
        if order: 
            return order.json()
        return {'message' : 'Order not found'}, 404
    
    def get(self, food_id) :
        order = self.dao.fetch_by_time(food_id)
        if order: 
            return order.json()
        return {'message' : 'Order not found'}, 404

    def get(self, review_id) :
        order = self.dao.fetch_by_time(review_id)
        if order: 
            return order.json()
        return {'message' : 'Order not found'}, 404

class Orders(Resource):
    def get(self) :
        return {'orders': list(map(lambda order: order.json(), OrderDao.fetch_all()))}