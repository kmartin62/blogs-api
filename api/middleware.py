from functools import wraps
from flask import request, g, jsonify
import jwt

from db.db_config import Session
from service.user_service import UserService

secret_key = 'my_secret_key_for_jwt_encoding_and_decoding' # TODO: Add into .env file

def authenticated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', '')
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        token = token.split()[-1]
        
        try:
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            user_service = UserService(session=Session)
            user = user_service.get_by_email(data.get('user_email'))
            g.user = user
            if not g.user:
                return jsonify({"message": "Invalid token"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401
        
        return func(*args, **kwargs)
    return wrapper