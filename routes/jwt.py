import jwt
from functools import wraps
from flask import jsonify, request
from configs.config import app

def tocken_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        access_token = request.headers.get('Authorization')
        print("------token-----------", access_token)
        try:
            if access_token is None:
                response =jsonify({"alert": "Unauthorized Access!!"})
                response.status_code = 401
                return response

            # Check if the token starts with "Bearer " and remove it
            if access_token.startswith('Bearer '):
                access_token = access_token[len('Bearer '):]
            else:
                response =jsonify({"alert": "Invalid Token format!!"})
                response.status_code = 401
                return response
        except jwt.ExpiredSignatureError:
            response =jsonify({"alert": "Expired Token!!"})
            response.status_code = 401
            return response
        except jwt.InvalidTokenError:
            response =jsonify({"alert": "Invalid Token!!"})
            response.status_code = 401
            return response
        
        return func(*args, **kwargs)

    return decorated
