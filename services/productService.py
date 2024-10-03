from sqlalchemy.orm import Session
from database import db
from models.models import Product
from middleware.schemas import product_schema, products_schema
from flask import jsonify

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
            
def get_all():
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = session.query(Product).all()
                return products_schema.jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    