from flask import request, jsonify
from middleware.schemas import user_schema
from marshmallow import ValidationError
from services import userService
from utils.util import token_required, role_required

@token_required
@role_required('admin')
def add():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return userService.add(user_data)
    

def login():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return userService.login(user_data['username'],user_data['password'])
