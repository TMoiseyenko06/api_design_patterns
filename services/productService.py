from sqlalchemy.orm import Session
from database import db
from models.models import Product, Order ,Production
from middleware.schemas import product_schema, products_schema, amount_order_schema, product_production_amount
from flask import jsonify
from sqlalchemy import func

def add(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'],price=product_data['price'])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
        return new_product
    
def remove(id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, id)
            if product:
                session.delete(product)
                session.commit()
            else:
                raise ValueError("product not found")
            

def update(id, product_data):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, id)
            if product:
                product.name = product_data['name']
                product.price = product_data['price']
                session.commit()
            else:
                raise ValueError('product not found')
            
def get(id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, id)
            if product:
                return product_schema.jsonify(product)
            else:
                return jsonify({"error":"product not found"})
            
def get_all(page,per_page):
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = db.paginate(Product, page=page,per_page=per_page)
                return products_schema.jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_ordered():
    with Session(db.engine) as session:
        with session.begin():
            results = session.query(Order.product_id, func.sum(Order.quantity).label('total_ordered')).group_by(Order.product_id).all()
            return amount_order_schema.jsonify(results)

def get_production(date):
    with Session(db.engine) as session:
        with session.begin():
            results = session.query(Production.product_id, func.sum(Production.quantity_produced).label('total_produced')).group_by(Production.product_id).where(Production.date_produced == date)
            return product_production_amount.jsonify(results)