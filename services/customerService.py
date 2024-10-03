from sqlalchemy.orm import Session
from flask import jsonify
from database import db
from models.models import Customer
from middleware.schemas import customer_schema, customers_schema

def add(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'],phone=customer_data['phone'])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
        return new_customer
    
def remove(id):
    with Session(db.engine) as session:
        with session.begin():
            customer = session.get(Customer, id)
            if customer:
                session.delete(customer)
                session.commit()
            else:
                raise ValueError

def update(id, customer_data):
    with Session(db.engine) as session:
        with session.begin():
            customer = session.get(Customer, id)
            if customer:
                customer.name = customer_data['name']
                customer.email = customer_data['email']
                customer.phone = customer_data['phone']
                session.commit()
            else:
                raise ValueError("Customer Not Found")
            
def get(id):
    with Session(db.engine) as session:
        with session.begin():
            customer = session.get(Customer, id)
            if customer:
                return customer_schema.jsonify(customer)
            else:
                raise ValueError("Customer Not found")
            
def get_all():
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = session.query(Customer).all()
                return customers_schema.jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
            

                
                
