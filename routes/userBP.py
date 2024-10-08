from flask import Blueprint
from controllers import userControllers

user_blueprint = Blueprint('user_bp',__name__)
user_blueprint.route('/',methods=['POST'])(userControllers.add)
user_blueprint.route('/login',methods=['GET'])(userControllers.login)