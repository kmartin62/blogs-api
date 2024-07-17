import jwt
from datetime import datetime, timedelta
import os

def encode_jwt_token(user):
  secret_key = os.getenv("JWT_SECRET_KEY") #TODO: Can be placed inside a container that stores env variables
  token = jwt.encode({
        'user_id': user.id,
        'user_email': user.email,
        'exp': datetime.now() + timedelta(hours=1)
    }, secret_key, algorithm="HS256")
  
  return token