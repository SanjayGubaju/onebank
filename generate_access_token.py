import requests
from constants import *


"""
This part was from the nordeaab repo https://github.com/NordeaOB

This is an example how to generate the access token from the scratch.
We first call get_code and then get_access_token function.
Access token can be generated by calling generate_access_token
or by running this file i.e. 'nordea generate_access_token.py'
"""


def get_code():
    endpoint = 'v1/authentication'
    payload = {
        'client_id': NORDEA_CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': ''
    }
    r = requests.get(NORDEA_BASE_URL + endpoint, params=payload)
    if not r.status_code == requests.codes.ok:
        raise Exception(r.text)
    response = r.json()
    code = response['args']['code']
    return code


def get_access_token(code):
    endpoint = 'v1/authentication/access_token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-IBM-Client-Id': NORDEA_CLIENT_ID,
        'X-IBM-Client-Secret': NORDEA_CLIENT_SECRET
    }

    payload = {
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    r = requests.post(NORDEA_BASE_URL + endpoint, data=payload, headers=headers)
    if not r.status_code == requests.codes.ok:
        raise Exception(r.text)

    response = r.json()
    access_token = response['access_token']
    return access_token


def generate_access_token():
    code = get_code()
    access_token = get_access_token(code)
    return access_token

