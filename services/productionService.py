from sqlalchemy.orm import Session
from flask import jsonify
from database import db
from models.models import Production, Order
from middleware.schemas import production_schema, productions_schema
from sqlalchemy import func

def add(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production  = Production(product_id=production_data['product_id'],employee_id=production_data['employee_id'],quantity_produced=production_data['quantity_produced'])
            session.add(new_production)
            session.commit()
        session.refresh(new_production)
        return new_production    
    
def remove(id):
    with Session(db.engine) as session:
        with session.begin():
            production = session.get(Production, id)
            if production:
                session.delete(production)
                session.commit()
            else:
                raise ValueError("production not found")
            
def update(id, production_data):
    with Session(db.engine) as session:
        with session.begin():
            production = session.get(Production, id)
            if production:
                production.product_id = production_data['product_id']
                production.quantity_produced = production_data['quantity_produced']
                session.commit()
            else:
                raise ValueError('product not found')
            
def get(id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Production, id)
            if product:
                return production_schema.jsonify(product), 200
            else:
                return jsonify({"error":"production not found"}), 400
            
def get_all():
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = session.query(Production).all()
                return productions_schema.jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
