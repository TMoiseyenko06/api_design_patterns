from flask import request, jsonify
from middleware.schemas import production_schema
from marshmallow import ValidationError
from services import productionService
from utils.util import token_required, role_required

@token_required
@role_required('employee')
def add():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    productionService.add(production_data)
    return jsonify({"message":"production added"}), 201

@token_required
@role_required('employee')
def remove(id):
    try:
        productionService.remove(id)
        return jsonify({"message":f"production {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"production not found"}),400
    
@token_required
@role_required('employee')
def update(id):
    try:
        production_data = production_schema.load(request.json)
        productionService.update(id,production_data)
        return jsonify({"message":f"production {id} updated"})
    except ValueError:
        return jsonify({"error":"production not found"}),400
    except ValidationError as e:
        return jsonify(e.messages),400
    
@token_required
@role_required('employee')
def get(id):
    return productionService.get(id)

@token_required
@role_required('employee')
def get_all():
    return productionService.get_all()

