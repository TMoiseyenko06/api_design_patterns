from flask import request, jsonify
from middleware.schemas import employee_schema
from marshmallow import ValidationError
from services import employeeService
from utils.util import token_required, role_required

@token_required
@role_required('admin')
def add():
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)

    employee_add = employeeService.add(employee_data)
    return employee_schema.jsonify(employee_add)

@token_required
@role_required('admin')
def remove(id):
    try:
        employeeService.remove(id)
        return jsonify({"message":f"employee {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"employee not found"}),400

@token_required
@role_required('admin')
def update(id):
    try:
        employee_data = employee_schema.load(request.json)
        employeeService.update(id,employee_data)
        return jsonify({"message":f"employee {id} updated"})
    except ValidationError as e:
        return jsonify(e.messages)
    except ValueError:
        return jsonify({"error":"employee not found"})
    
@token_required
@role_required('employee')
def get(id):
    return employeeService.get(id)

@token_required
@role_required('employee')
def get_all():
    return employeeService.get_all()

@token_required
@role_required('employee')
def get_produced():
    return employeeService.get_produced()