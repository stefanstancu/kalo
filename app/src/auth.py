import os
from google.oauth2 import id_token
from google.auth.transport import requests

client_id = os.environ['CLIENT_ID']

def login(token):
    ''' does the login
    @param token: the token from the request
    @returns user_id: the user_id to be used in the db
    @throws ValueError: if the issuer is wrong
    '''

    idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)

    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    return idinfo['sub']

