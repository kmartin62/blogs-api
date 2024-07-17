from flask import Blueprint, jsonify, request, make_response

from .utils import encode_jwt_token
from db.db_config import Session
from service.user_service import UserService
from werkzeug.security import check_password_hash

app_users = Blueprint('users', __name__, url_prefix="/api/v1/users")
user_service = UserService(session=Session)

@app_users.route("/sign_up", methods=["POST"])
def sign_up():
    data = request.get_json()
    inserted_user = user_service.insert(data)
    if not inserted_user:
      return jsonify({"message": "User creation failed"}), 500
    return jsonify({"message": "User created successfully"}), 201


@app_users.route("/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()
    user = user_service.get_by_email(data.get("email"))

    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"message": "Invalid credentials"}), 401
    
    token = encode_jwt_token(user)

    response = make_response()
    response.headers['Authorization'] = f"Bearer {token}"

    return response