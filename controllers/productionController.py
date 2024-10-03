from flask import request, jsonify
from middleware.schemas import production_schema
from marshmallow import ValidationError
from services import productionService

def add():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    production_add = productionService.get(production_data)
    return production_schema.jsonify(production_add)

def remove(id):
    try:
        productionService.remove(id)
        return jsonify({"message":f"production {id} removed"}), 200
    except ValueError:
        return jsonify({"error":"production not found"}),400
    
def update(id):
    try:
        production_data = production_schema.load(request.json)
        productionService.update(id,production_data)
        return jsonify({"message":f"production {id} updated"})
    except ValueError:
        return jsonify({"error":"production not found"}),400
    except ValidationError as e:
        return jsonify(e.messages),400
    
def get(id):
    return productionService.get(id)

def get_all():
    return productionService.get_all()
