from flask import Blueprint
from controllers import employeeController

employee_blueprint = Blueprint('employee_bp',__name__)
employee_blueprint.route('/',methods=['POST'])(employeeController.add)
employee_blueprint.route('/<int:id>',methods=['DELETE'])(employeeController.remove)
employee_blueprint.route('/produced',methods=['GET'])(employeeController.get_produced)