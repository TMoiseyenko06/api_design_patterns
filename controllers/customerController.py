from flask import request, jsonify
from middleware.schemas import customer_schema
from services import customerService
from marshmallow import ValidationError
from utils.util import token_required, role_required

@token_required
def add():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_add = customerService.add(customer_data)
    return customer_schema.jsonify(customer_add), 201

@token_required
@role_required('admin')
def remove(id):
    if id:
        try:
            customerService.remove(id)
            return jsonify({"message":f"customer {id} removed"}), 200
        except ValueError:
            return jsonify({"error":"customer not found"}),400
 
@token_required
@role_required('admin')
def update(id):
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    try:
        customerService.update(id,customer_data)
    except ValueError as e:
        return jsonify({"error":f"{e}"}), 400
    return jsonify({"message":"customer updated"}), 200

@token_required
@role_required('employee')
def get(id):
    try:
        return customerService.get(id)
    except ValueError:
        return jsonify({"message":"customer not found"}),400
    
@token_required
@role_required('employee')
def get_all():
    return customerService.get_all()

@token_required
@role_required('employee')
def get_orders():
    amount = request.args.get('amount',0,type=int)
    return customerService.get_orders(amount)