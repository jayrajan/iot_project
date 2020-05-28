import fitbit
import urllib.request
from urllib.parse import urlencode
import urllib3
import requests
import json
import ssl
import oauthlib
import http.client
from requests_oauthlib import OAuth2Session
import base64
import re
# FITBIT URLs
fit_redirect_uri = 'https://127.0.0.1:8080/callback'
fitbit_url = 'https://www.fitbit.com'
fitbit_api_url = 'api.fitbit.com'
url1 = 'https://www.fitbit.com/oauth2/authorize?'
fit_token_url =  'https://api.fitbit.com/oauth2/token'
# 'https://www.fitbit.com/oauth2/token'

# APPLICATION DETAILS
# OAuth 2.0 Client ID - Identify the application
CLIENT_ID = '22BR7W'
# Client Secret - Secret key which is stored on server side securely & not available to public
CLIENT_SECRET = 'd608a786153c83f7ed91ddfdcb839e29'
data_64 = (CLIENT_ID+":"+CLIENT_SECRET)
encodedBytes = base64.b64encode(data_64.encode("utf-8"))
base64_code_str = str(encodedBytes,'utf-8')
print(base64_code_str)
# base64_code = base64.b64encode(bytes((CLIENT_ID+":"+CLIENT_SECRET),'utf-8'))

responsetype = 'token'
expirytime_ms = '604800' 
fit_scope = ['heartrate']
# auth_url = url1+'?response_type='+responsetype+'&client_id='+CLIENT_ID+'&redirect_uri='+fit_redirect_uri+'&scope=heartrate'+'&expires_in='+expirytime_ms

# creating an OAuth2Session object
fitbit = OAuth2Session(client_id=CLIENT_ID, redirect_uri=fit_redirect_uri, scope=fit_scope)
# Generating authorisation url
authorisation_url, state = fitbit.authorization_url(url1)
print('Please go to %s and authorize access.' %authorisation_url)
# Asking for the Callback URL response
authorisation_response = input('Enter full callback URL response: ')
# print(authorisation_response)

# Regular expression - extracting the authorisation code - ONLY
authorisation_code = re.findall('code=[a-z0-9]+',authorisation_response)
auth_code= re.findall('[a-z0-9]+',authorisation_code[0])

# Authorisation code
auth_code_num = auth_code[1]
print(auth_code_num)

# Data Payloads
data = {'code' : auth_code_num,
        'redirect_uri' : fit_redirect_uri,
        'clientId' : CLIENT_ID,
        'state' : state,
        'grant_type' : 'authorization_code'}
dataURLencoded = urlencode(data).encode('utf-8')
# print(dataURLencoded)

# Create a request object
req = urllib.request.Request(fit_token_url,data=dataURLencoded, method='POST')

# Authorisation Header
req.add_header('Authorization', 'Basic '+base64_code_str)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
print(req.get_full_url())
# POST Request
try:
    response = urllib.request.urlopen(req)
    FullResponse = response.read()
    print(FullResponse)
except urllib.error.HTTPError as e:
    print('HTTP ERROR CODE:',e.code)
    print(e.msg)
    print(e.reason)
    print(e.headers)
