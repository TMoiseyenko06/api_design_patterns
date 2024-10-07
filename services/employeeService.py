from sqlalchemy.orm import Session
from database import db
from models.models import Employee, Production
from middleware.schemas import employee_schema,employees_schema, production_group_schema
from flask import jsonify
from sqlalchemy import func

def add(employee_data):
    with Session(db.engine) as session:
        with session.begin():
            new_employee = Employee(name=employee_data['name'],position=employee_data['position'])
            session.add(new_employee)
            session.commit()
        session.refresh(new_employee)
        return new_employee
    
def remove(id):
    with Session(db.engine) as session:
        with session.begin():
            employee = session.get(Employee,id)
            if employee:
                session.delete(employee)
                session.commit()
            else:
                raise ValueError
            
def update(id,employee_data):
    with Session(db.engine) as session:
        with session.begin():
            employee = session.get(Employee, id)
            if employee:
                employee.name = employee_data['name']
                employee.position = employee_data['position']
                session.commit()
            else:
                raise ValueError
            
def get(id):
    with Session(db.engine) as session:
        with session.begin():
            employee = session.get(Employee,id)
            if employee:
                return employee_schema.jsonify(employee)
            else:
                return jsonify({"error":"employee not found"})
            
def get_all():
    try:
        with Session(db.engine) as session:
            with session.begin():
                results = session.query(Employee).all()
                return employees_schema.jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_produced():
    with Session(db.engine) as session:
        with session.begin():
            results = session.query(Production.employee_id, func.sum(Production.quantity_produced).label('total_produced')).group_by(Production.employee_id).all()
            return production_group_schema.jsonify(results)