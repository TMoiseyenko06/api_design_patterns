from flask import Blueprint
from controllers import orderController

order_blueprint = Blueprint('order_bp',__name__)
order_blueprint.route('/',methods=['POST'])(orderController.add)
order_blueprint.route('/<int:id>',methods=['DELETE'])(orderController.remove)
order_blueprint.route('/<int:id>',methods=['PUT'])(orderController.update)
order_blueprint.route('/<int:id>',methods=['GET'])(orderController.get)
order_blueprint.route('/',methods=['GET'])(orderController.get_all)
