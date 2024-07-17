import jwt
from datetime import datetime, timedelta

def encode_jwt_token(user):
  token = jwt.encode({
        'user_id': user.id,
        'user_email': user.email,
        'exp': datetime.now() + timedelta(hours=1)
    }, 'my_secret_key_for_jwt_encoding_and_decoding', algorithm="HS256")
  
  return token