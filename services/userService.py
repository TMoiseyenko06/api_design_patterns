from sqlalchemy.orm import Session
from database import db
from flask import jsonify
from middleware.schemas import user_schema, users_schema
from models.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token

def add(user_data):
    try:
        new_user = User(username=user_data['username'],password=generate_password_hash(user_data['password']),role=user_data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"user_added"}), 201
    except:
        return jsonify({"error":"username_error"}), 400
            
def login(username,password):
    user = (db.session.execute(db.select(User).where(User.username == username)).scalar_one_or_none())
    if user and check_password_hash(user.password,password):
        auth_token = encode_token(user.id,user.role)
        resp = {
            "status":"success",
            "message":"Successfully logged in",
            "auth_token":auth_token
        }
        return resp
    else:
        return None


