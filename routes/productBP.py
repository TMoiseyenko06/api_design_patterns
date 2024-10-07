from flask import Blueprint
from controllers import productController

product_blueprint = Blueprint('product_bp',__name__)
product_blueprint.route('/',methods=['POST'])(productController.add)
product_blueprint.route('/<int:id>',methods=['DELETE'])(productController.remove)
product_blueprint.route('/<int:id>',methods=['PUT'])(productController.update)
product_blueprint.route('/<int:id>',methods=['GET'])(productController.get)
product_blueprint.route('/ordered',methods=['GET'])(productController.get_ordered)
product_blueprint.route('/production/',methods=["GET"])(productController.get_production)