from flask import request, jsonify
from middleware.schemas import product_schema
from marshmallow import ValidationError
from services import productService

def add():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    
    product_add = productService.add(product_data)
    return product_schema.jsonify(product_add), 201

def remove(id):
    try:
        productService.remove(id)
        return jsonify({"message":f"product {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"product not found"}),400
    
def update(id):
    try:
        product_data = product_schema.load(request.json)
        productService.update(id,product_data)
        return jsonify({"message":f"product {id} updated"})
    except ValueError:
        return jsonify({"error":"product not found"}),400
    except ValidationError as e:
        return jsonify(e.messages),400
    
def get(id):
    return productService.get(id)

def get_all():
    return productService.get_all()

    

