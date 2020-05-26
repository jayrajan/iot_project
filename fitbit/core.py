import fitbit
import urllib.request, urllib.parse, urllib.error
import urllib3
import requests
import json
import ssl
import oauthlib
import http.client
from requests_oauthlib import OAuth2Session
import base64
# FITBIT URLs
fit_redirect_uri = 'http://127.0.0.1:8080/'
fitbit_url = 'https://www.fitbit.com'
fitbit_api_url = 'api.fitbit.com'
url1 = 'https://www.fitbit.com/oauth2/authorize?'
fit_token_url = 'https://www.fitbit.com/oauth2/token'

# APPLICATION DETAILS
# OAuth 2.0 Client ID - Identify the application
CLIENT_ID = '22BR7W'
# Client Secret - Secret key which is stored on server side securely & not available to public
CLIENT_SECRET = '9b3bea71b238d080962c589d6134fe51'
base64_code = base64.b64encode(bytes((CLIENT_ID+":"+CLIENT_SECRET),'utf-8'))
print(base64_code)
responsetype = 'token'
expirytime_ms = '604800' 
fit_scope = ['heartrate']
# auth_url = url1+'?response_type='+responsetype+'&client_id='+CLIENT_ID+'&redirect_uri='+fit_redirect_uri+'&scope=heartrate'+'&expires_in='+expirytime_ms

fitbit = OAuth2Session(client_id=CLIENT_ID, redirect_uri=fit_redirect_uri, scope=fit_scope)
authorisation_url, state = fitbit.authorization_url(url1)
print('Please go to %s and authorize access.' %authorisation_url)
authorisation_response = input('Enter callback response: ')
print(authorisation_response)

token = fitbit.fetch_token( token_url=fit_token_url, 
                            authorization_response=authorisation_response, 
                            include_client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET, 
                            body=' application/x-www-form-urlencoded')

# ACCESS TOKEN
# token = fitbit.fetch_token(token_url=fit_token_url, authorization_response=authorisation_response, 
#                             include_client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
#                             state=state, code_challenge_method='S256', responsetype='token', method='POST')

# token = fitbit.fetch_token( token_url=fit_token_url, 
#                             authorization_response=authorisation_response, 
#                             include_client_id=CLIENT_ID,
#                             client_secret=CLIENT_SECRET, 
#                             username='', 
#                             password='',
#                             body=' application/x-www-form-urlencoded')

# RESPONSE
# r = fitbit.get('https://api.fitbit.com/1/user/-/profile.json')


# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE







# # Defining a client
# client = WebApplicationClient(CLIENT_ID)
# client.prepare_request_uri(url1, redirect_uri=fit_redirect_uri,scope='heartrate', state=None,)

# print(auth_url)

# req = requests.Request('POST',auth_url)
# prepared = req.prepare()

# #Send and print response
# s = requests.Session()
# response = s.send(prepared)
# print("Response from fitbit: " + str(response))

# Making a REST Call
# response = requests.get(auth_url)
# # print(response.status_code)
# # print(response.text)
# # print(response.url)
# print(response.url)

# Authorisation
# http://127.0.0.1:8080/#access_token=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJSN1ciLCJzdWIiOiI1SFlCNjIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyaHIiLCJleHAiOjE1OTA0Mjc1OTAsImlhdCI6MTU4OTk4NzQzM30.yZw9-F0BXg-l63eBxfQQA3jnxNDL5_l9zDDLeK6PLn0&user_id=5HYB62&scope=heartrate&token_type=Bearer&expires_in=440157





# try:
#     # contents = urllib.request.urlopen(auth_url, context=ctx).read()
#     # print(contents)
#     # resp = urllib3.Request(auth_url)
    
# except urllib.error.URLError as e:
#     # response = http.request('GET', auth_url)
#     # print(response.data)
#     # print(response.data.decode('utf-8')) # Text.







# print(c.geturl())
# myfile = c.read()
# print(myfile)

# try:
#     js = json.loads(data)
# except:
#     js = None

# print(json.dumps(js, indent=4))

# https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=22BR7W&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2F&scope=heartrate&expires_in=604800


# Access token is used for making HTTPS requests to the Fitbit API



# print('hello Fit-World')













# # Callback URL

# urlbase = 'https://api.fitbit.com'
# # OAuth 2.0: Authorisation URI
# auth_uri = 'https://www.fitbit.com/oauth2/authorize'


# # client = fitbit.FitbitOauth2Client(CLIENT_ID,CLIENT_SECRET)
# # # Using the ID and Secret, we can obtain the access and refresh tokens that authorize us to get our data.
# # # print('hello fitworld')

# # # Access Token & Refresh Token - generated using Client secret & Client ID
# # # Authprise access
# ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9'

# # key = fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET, redirect_uri=urlbase,system='en_UK')
# # myobj = {'key': 'value'}
# # myjson = {'key': 'value'}
# # client = requests.post('https://api.fitbit.com/oauth2/token', 
# #                         data=myobj, json=myjson, auth=(CLIENT_SECRET, CLIENT_SECRET))
# # print(client.status_code)

# # https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=22942C&redirect_uri=https%3A%2F%2Fexample.com%2Ffitbit_auth&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight
# # response = requests.get(urlbase)
# # print(response)
# # print(response.status_code)

# # http://127.0.0.1:8080/#access_token=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkJSN1ciLCJzdWIiOiI1SFlCNjIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTg5NzE1Njc3LCJpYXQiOjE1ODkxMjc3NjV9.Z8KbDY_u_6osA0R272Uo06uQtX8nCf7rIje80Ubs2Yw&user_id=5HYB62&scope=settings+heartrate+nutrition+activity+weight+location+profile+social+sleep&token_type=Bearer&expires_in=587912

# # https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=22BR7W&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2F&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800

# client = fitbit.Fitbit(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, access_token = ACCESS_TOKEN, expires_at='604800', system='en_UK')
# client.sleep()

# response = requests.get('https://api.fitbit.com/1/user/-/profile.json')
# print(response)
