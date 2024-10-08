from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.orm import Mapped,mapped_column
from schema import ma
import datetime

ma = Marshmallow()

class Employee(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    position = fields.String(required=True)

    class Meta:
        fields = ('id','name','position')

class Product(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ('id','name','price')

class Order(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=False)

    class Meta:
        fields = ('id','customer_id','product_id','quantity','total_price')

class Customer(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ('id','name','email','phone')

class Production(ma.Schema):
    id = fields.Integer(required=False)
    employee_id = fields.Integer(required=False)
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=False,missing=datetime.date.today())

    class Meta:
        fields = ('id','employee_id','product_id','quantity_produced','date_produced')

class User(ma.Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.String(required=False,default='employee')
    class Meta:
        fields = ('id','username','password','role')

class ProductionGroup(ma.Schema):
    employee_id = fields.Integer()
    total_produced = fields.Integer()

class OrderAmount(ma.Schema):
    product_id = fields.Integer()
    total_ordered = fields.Integer()

class CustomerOrderAmount(ma.Schema):
    customer_id = fields.Integer()
    total_ordered = fields.Integer()

class ProductProductionAmount(ma.Schema):
    product_id = fields.Integer()
    total_produced = fields.Integer()

employee_schema = Employee()
employees_schema = Employee(many=True)

product_schema = Product()
products_schema =Product(many=True)

order_schema = Order()
orders_schema = Order(many=True)

customer_schema = Customer()
customers_schema = Customer(many=True)

production_schema = Production()
productions_schema = Production(many=True)

production_group_schema = ProductionGroup(many=True)
amount_order_schema = OrderAmount(many=True)
customer_amount_order = CustomerOrderAmount(many=True)
product_production_amount = ProductProductionAmount(many=True)

user_schema = User()
users_schema = User(many = True)