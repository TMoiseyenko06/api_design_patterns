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
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=False,missing=datetime.date.today())

    class Meta:
        fields = ('id','product_id','quantity_produced','date_produced')


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