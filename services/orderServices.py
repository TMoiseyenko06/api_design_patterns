from sqlalchemy.orm import Session
from database import db
from models.models import Order, Product
from middleware.schemas import order_schema, orders_schema
from flask import jsonify

def add(order_data):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product,order_data['product_id'])
            new_order = Order(
                customer_id=order_data['customer_id'],
                product_id=order_data['product_id'],
                quantity=order_data['quantity'],
                total_price=(product.price * int(order_data['quantity']))
                              )
            session.add(new_order)
            session.commit()
        session.refresh(new_order)
        return new_order

def remove(id):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order, id)
            if order:
                session.delete(order)
                session.commit()
            else:
                raise ValueError
            
def update(id,order_data):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order, id)
            product = session.get(Product, order_data['product_id'])
            if order:
                order.customer_id = order_data['customer_id']
                order.product_id = order_data['product_id']
                order.quantity = order_data['quantity']
                order.total_price = (product.price * int(order_data['quantity']))
                session.commit()
            else:
                raise ValueError
            
def get(id):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order,id)
            if order:
                return order_schema.jsonify(order)
            else:
                return jsonify({"error":"order not found"})
            
def get_all(page,per_page):
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = db.paginate(Order, page=page,per_page=per_page)
                return orders_schema.jsonify(results),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500