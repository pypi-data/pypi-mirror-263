#########################################################################################
#                                                                                       #
# MIT License                                                                           #
#                                                                                       #
# Copyright (c) 2024 Ioannis D. (devcoons)                                              #
#                                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining a copy          #
# of this software and associated documentation files (the "Software"), to deal         #
# in the Software without restriction, including without limitation the rights          #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell             #
# copies of the Software, and to permit persons to whom the Software is                 #
# furnished to do so, subject to the following conditions:                              #
#                                                                                       #
# The above copyright notice and this permission notice shall be included in all        #
# copies or substantial portions of the Software.                                       #
#                                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR            #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,              #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE           #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,         #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE         #
# SOFTWARE.                                                                             #
#                                                                                       #
#########################################################################################

import jwt
import time

class AuthJWT:
    """
    The AuthJWT class provides mechanisms for JSON Web Token (JWT) based authentication.
    It includes functionalities for generating JWTs, validating JWTs in HTTP requests,
    invalidating JWTs, and checking token authorization with a specific key. It supports
    customizable token duration, authentication types, and maintains a list of invalidated tokens.
    
    Attributes:
        invalidated_tokens (dict): Class-level dictionary to store invalidated tokens and their expiry times.
        secret_key (str): Secret key used for signing JWT tokens.
        token_duration (int): Duration for which the token is valid, in seconds (default is 86400 seconds or 24 hours).
        auth_type (str): Type of the authentication scheme used in the Authorization header (default is 'Bearer').
    """

    # Class variable to store invalidated tokens and their expiry times
    invalidated_tokens = {}

    def __init__(self, secret_key, token_duration=86400, auth_type='Bearer'):
        """
        Initializes the AuthJWT instance.
        
        :param secret_key: The secret key used to sign JWT tokens.
        :param token_duration: Duration for which the token is valid, in seconds.
        :param auth_type: The type of authentication (e.g., 'Bearer').
        """
        self.secret_key = secret_key
        self.token_duration = token_duration
        self.auth_type = auth_type

    def generate_jwt(self, data):
        """
        Generates a JWT token with the specified data payload.
        
        :param data: The payload data to encode in the JWT token.
        :return: A JWT token as a string.
        """
        payload = {
            'data': data,
            'exp': int(time.time()) + self.token_duration  # Token expiration time
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    
    def is_authorized(self, request):
        """
        Determines if the request is authorized by validating the JWT token in the Authorization header.
        
        :param request: The request object to validate.
        :return: A tuple (payload data, True) if authorized, or (None, False) if not.
        """
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None, False
        parts = authorization_header.split()
        if parts[0] != self.auth_type or len(parts) != 2:
            return None, False
        token = parts[1]
        return self.is_authorized_token(token)

    def is_authorized_token(self, token):
        """
        Validates a given JWT token string.
        
        :param token: The JWT token string to validate.
        :return: A tuple (payload data, True) if the token is valid, or (None, False) if invalid.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            if token in self.invalidated_tokens and time.time() < self.invalidated_tokens[token]:
                return None, False  # Token is invalidated
            return payload['data'], True
        except jwt.ExpiredSignatureError:
            return None, False  # Token is expired
        except jwt.InvalidTokenError:
            return None, False  # Token is invalid

    def invalidate_token(self, token):
        """
        Invalidates a given JWT token.
        
        :param token: The JWT token to invalidate.
        :return: True if the token was successfully invalidated, False otherwise.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            self.invalidated_tokens[token] = payload['exp']  # Set the token's expiry in invalidated_tokens
            return True
        except jwt.InvalidTokenError:
            return False

    def invalidate_jwt(self, request):
        """
        Invalidates the JWT token found in the request's Authorization header.
        
        :param request: The request object containing the JWT token to invalidate.
        :return: True if the token was successfully invalidated, False otherwise.
        """
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return False
        parts = authorization_header.split()
        if parts[0] != self.auth_type or len(parts) != 2:
            return False
        token = parts[1]
        return self.invalidate_token(token)

    def is_authorized_with_key(self, request, key):
        """
        Validates the JWT token in the request's Authorization header using a specific key.
        
        :param request: The request object containing the JWT token to validate.
        :param key: The specific key to use for validation.
        :return: A tuple (payload data, True) if the token is valid with the given key, or (None, False) if invalid.
        """
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None, False
        parts = authorization_header.split()
        if parts[0] != self.auth_type or len(parts) != 2:
            return None, False
        token = parts[1]
        try:
            payload = jwt.decode(token, key, algorithms=['HS256'])
            if token in self.invalidated_tokens and time.time() < self.invalidated_tokens[token]:
                return None, False  # Token is invalidated
            return payload['data'], True
        except jwt.ExpiredSignatureError:
            return None, False  # Token is expired
        except jwt.InvalidTokenError:
            return None, False  # Token is invalid    