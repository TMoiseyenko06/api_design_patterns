from flask import request, jsonify
from middleware.schemas import employee_schema
from marshmallow import ValidationError
from services import employeeService

def add():
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)

    employee_add = employeeService.add(employee_data)
    return employee_schema.jsonify(employee_add)

def remove(id):
    try:
        employeeService.remove(id)
        return jsonify({"message":f"employee {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"employee not found"}),400

def update(id):
    try:
        employee_data = employee_schema.load(request.json)
        employeeService.update(id,employee_data)
        return jsonify({"message":f"employee {id} updated"})
    except ValidationError as e:
        return jsonify(e.messages)
    except ValueError:
        return jsonify({"error":"employee not found"})
    
def get(id):
    return employeeService.get(id)

def get_all():
    return employeeService.get_all()

    