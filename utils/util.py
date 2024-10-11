import os
import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def encode_token(user_id,role):
    payload = {
        'exp' : datetime.now() + timedelta(days=1),
        'iat' : datetime.now(),
        'usr' : user_id,
        'role' : role
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
    return token


def verify_token():
    token = None
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization'].split(" ")[1]
            jwt.decode(token,SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return jsonify({"message":"token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message":"invalid token"}), 401
    if not token:
        return jsonify({'message':'Authentication token is missing'}), 401
    return None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        error_response = verify_token()
        if error_response:
            return jsonify(error_response)
        return f(*args, **kwargs)
    return decorated

def verify_role(role):
    token = None
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization'].split(" ")[1]
            payload = jwt.decode(token,SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return jsonify({"message":"token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message":"invalid token"}), 401   
    if not (payload['role'] == role  or payload['role'] == 'admin'):
        return jsonify({"message":"user does not have required role"}), 403
            

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            error_response = verify_role(role)
            if error_response:
                return jsonify(error_response)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
    