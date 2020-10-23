import logging
from flask import Buleprint
from flask_restful import Api
from sba_chabot.api.chatbot_api.order_review.api import Order

order = Buleprint('order', __name__, url_prefix='/api')
api = Api(order)

api.add_resource(Order, '/api')


@order.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during order request. %s' % str(e))
    return 'An internal error occurred.', 500