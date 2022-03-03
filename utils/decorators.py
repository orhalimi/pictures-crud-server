from functools import wraps
from flask import request
from google.oauth2 import id_token
from google.auth.transport import requests as googleRequests


def sqlalchemy_repr(org_class):
    def __repr__(self):
       dict = {k: self.__dict__.get(k) for k in self.__dict__ if not k.startswith('_')}
       return ' '.join(f'{k}={v}' for k, v in dict.items())

    org_class.__repr__ = __repr__
    return org_class


def authentication(func):
    @wraps(func)
    def with_auth(*args, **kwargs):
        error_tuple = {"message": "Unauthorized"}, 401
        if not 'Authorization' in request.headers:
            return error_tuple
        bearer = request.headers.get('Authorization')
        token = bearer.split()[1]
        g_request = googleRequests.Request()
        try:
            user = id_token.verify_oauth2_token(
                token, g_request, '247689045321-cm5s2rjpqjomdm2u0df1f8304p9j9g4n.apps.googleusercontent.com')
            user['id'] = user['sub']
        except Exception as e:
            print(e)
            return error_tuple
        return func(user, *args, **kwargs)

    return with_auth

