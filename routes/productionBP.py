from flask import Blueprint
from controllers import productionController

production_blueprint = Blueprint('production_bp',__name__)
production_blueprint.route('/',methods=['POST'])(productionController.add)
production_blueprint.route('/<int:id>',methods=['DELETE'])(productionController.remove)
production_blueprint.route('/<int:id>',methods=['PUT'])(productionController.update)
production_blueprint.route('/<int:id>',methods=['GET'])(productionController.get)
production_blueprint.route('/all',methods=['GET'])(productionController.get)

