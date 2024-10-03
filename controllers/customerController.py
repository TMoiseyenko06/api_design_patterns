from flask import request, jsonify
from middleware.schemas import customer_schema
from services import customerService
from marshmallow import ValidationError

def add():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_add = customerService.add(customer_data)
    return customer_schema.jsonify(customer_add), 201

def remove(id):
    if id:
        try:
            customerService.remove(id)
            return jsonify({"message":f"customer {id} removed"}), 200
        except ValueError:
            return jsonify({"error":"customer not found"}),400
 
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

def get(id):
    try:
        return customerService.get(id)
    except ValueError:
        return jsonify({"message":"customer not found"}),400
    
def get_all():
    return customerService.get_all()
