from flask import Flask
from database import db
from schema import ma
from models.models import Employee, Order, Product, Customer, Production
from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint
from limiter import limiter
from utils.util import token_required, role_required

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':'rest_api_patterns'
    }
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    blue_print_config(app)
    config_rate_limit()
    with app.app_context():
        db.create_all()
    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customer')
    app.register_blueprint(product_blueprint, url_prefix='/product')
    app.register_blueprint(employee_blueprint,url_prefix='/employee')
    app.register_blueprint(order_blueprint,url_prefix='/order')
    app.register_blueprint(production_blueprint,url_prefix='/production')
    app.register_blueprint(user_blueprint,url_prefix='/user')
    app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)

def config_rate_limit():
    limiter.limit('100 per day')(customer_blueprint)
    limiter.limit('50 per day')(product_blueprint)
    limiter.limit('50 per day')(employee_blueprint)
    limiter.limit('20 per day')(order_blueprint)
    limiter.limit('100 per day')(production_blueprint)


app = create_app('DevelopmentConfig')
app.run(debug=True)

