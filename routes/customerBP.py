from flask import Blueprint
from controllers.customerController import add, remove, update, get
customer_blueprint = Blueprint('customer_bp',__name__)
customer_blueprint.route('/',methods=['POST'])(add)
customer_blueprint.route('/<int:id>',methods=['DELETE'])(remove)
customer_blueprint.route('/<int:id>',methods=['PUT'])(update)
customer_blueprint.route('/<int:id>',methods=['GET'])(get)