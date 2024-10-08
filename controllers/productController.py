from flask import request, jsonify
from middleware.schemas import product_schema
from marshmallow import ValidationError
from services import productService
import datetime
from utils.util import token_required, role_required

@token_required
@role_required('employee')
def add():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    
    product_add = productService.add(product_data)
    return product_schema.jsonify(product_add), 201

@token_required
@role_required('admin')
def remove(id):
    try:
        productService.remove(id)
        return jsonify({"message":f"product {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"product not found"}),400
    
@token_required
@role_required('employee')
def update(id):
    try:
        product_data = product_schema.load(request.json)
        productService.update(id,product_data)
        return jsonify({"message":f"product {id} updated"})
    except ValueError:
        return jsonify({"error":"product not found"}),400
    except ValidationError as e:
        return jsonify(e.messages),400
    
@token_required
def get(id):
    return productService.get(id)

@token_required
def get_all():
    page = request.args.get('page',1,type=int)
    per_page = request.args.get('per_page',10,type=int)
    return productService.get_all(page,per_page)
    
@token_required
@role_required('employee')
def get_ordered():
    return productService.get_ordered()

@token_required
@role_required('employee')
def get_production():
    date = request.args.get('date',datetime.date.today())
    return productService.get_production(date)