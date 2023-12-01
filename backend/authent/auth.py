import os
import base64
import jwt
import json
from flask import request, jsonify
from functools import wraps
from jwt.algorithms import RSAAlgorithm

CLERK_JWKS_KEYS_DATA_B64=os.getenv("CLERK_JWKS_KEYS_DATA_B64")

jwks_data=json.loads(base64.standard_b64decode(CLERK_JWKS_KEYS_DATA_B64.encode("utf-8")))

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token or len(token.split(' ')) < 2:
            return jsonify({'message' : 'Token is missing'}), 401
        try:
            public_key = RSAAlgorithm.from_jwk(jwks_data["keys"][0])
            user = jwt.decode(
                token.split(' ')[1],
                public_key,
                algorithms=["RS256"],
                verify=True
            )
        except Exception as e:
            print(e)
            return jsonify({
                'message' : 'Token is invalid'
            }), 401
        return  f(user, *args, **kwargs)
    return decorated