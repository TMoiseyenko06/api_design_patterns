from flask import request, jsonify
from middleware.schemas import order_schema
from marshmallow import ValidationError
from services import orderServices

def add():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    
    order_add = orderServices.add(order_data)
    return order_schema.jsonify(order_add)
    

def remove(id):
    try:
        orderServices.remove(id)
        return jsonify({"message":f"order {id} removed"}),200
    except ValueError:
        return jsonify({"error":"order not found"}),400
    
def update(id):
    try:
        order_data = order_schema.load(request.json)
        orderServices.update(id,order_data)
        return jsonify({"message":f"order {id} updated"})
    except ValidationError as e:
        return jsonify(e.messages),400
    except ValueError:
        return jsonify({"error":"order not found"}),400
    
def get(id):
    try:
        return orderServices.get(id)
    except ValueError:
        return jsonify({"error":"order not found"})
    
def get_all():
    return orderServices.get_all()
