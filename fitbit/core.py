import fitbit
import urllib.request, urllib.parse, urllib.error
import requests
import json
import ssl
import oauthlib

redirect_uri = 'http://127.0.0.1:8080/'
# 'http%3A%2F%2F127.0.0.1%3A8080%2F'
fitbit_url = 'www.fitbit.com'
fitbit_api_url = 'api.fitbit.com'

# OAuth 2.0 Client ID - Identify the application
CLIENT_ID = '22BR7W'

# Client Secret - Secret key which is stored on server side securely & not available to public
CLIENT_SECRET = 'aaf2c1c4ec24d6c8e732beb79cc3def7'
responsetype = 'token'
expirytime_ms = '604800' 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Defining a client
auth_url = fitbit_url+'/oauth2/authorize?'+'response_type='+responsetype+'&client_id='+CLIENT_ID+'&redirect_uri='+redirect_uri+'&scope=heartrate'+'&expires_in='+expirytime_ms
print(auth_url)
c = urllib.request.urlopen(auth_url)

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
