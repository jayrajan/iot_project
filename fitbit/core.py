'''
Code written by Jerin Rajan on 09th May 2020
Project title: IoT project (Fitbit) 
The code allows configuring the Fitbit API to read fitness related data and present the data using graphical plots
Note: apifunction() should be included in same directory as this code
'''

import re
import json
import base64
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from urllib.parse import urlencode
from apifunction import getresponse
from requests_oauthlib import OAuth2Session

# FITBIT CREDENTIALS/URLs
fit_username = 'Jay'
fit_redirect_uri = 'https://127.0.0.1:8080/callback'
fit_auth_url = 'https://www.fitbit.com/oauth2/authorize?'
fit_token_url =  'https://api.fitbit.com/oauth2/token'

# APPLICATION DETAILS
# OAuth 2.0 Client ID - Identify the application
CLIENT_ID = '22BR7W'
# Client Secret - Secret key which is stored on server side securely & not available to public
CLIENT_SECRET = 'd608a786153c83f7ed91ddfdcb839e29'

# BASE64 ENCODE - CLIENT ID : CLIENT SECRET
data_64 = (CLIENT_ID+":"+CLIENT_SECRET)
encodedBytes = base64.b64encode(data_64.encode("utf-8"))
base64_code_str = str(encodedBytes,'utf-8')

# SCOPE - HEARTRATE
fit_scope = ['heartrate']

# OAUTH2 AUTHENTICATION
# creating an OAuth2Session object
fitbit = OAuth2Session(client_id=CLIENT_ID, redirect_uri=fit_redirect_uri, scope=fit_scope)
# Generating authorisation url
authorisation_url, state = fitbit.authorization_url(fit_auth_url)
print('Please go to %s and authorize access.' %authorisation_url)

# Asking for the Callback URL response
authorisation_response = input('Enter full callback URL response: ')

# Regular expression - extracting the authorisation code - ONLY
authorisation_code = re.findall('code=[a-z0-9]+',authorisation_response)
auth_code= re.findall('[a-z0-9]+',authorisation_code[0])

# Authorisation code
auth_code_num = auth_code[1]

# Data Payloads
data = {'code' : auth_code_num,
        'redirect_uri' : fit_redirect_uri,
        'clientId' : CLIENT_ID,
        'state' : state,
        'grant_type' : 'authorization_code'}
dataURLencoded = urlencode(data).encode('utf-8')

# Create a request object
req = urllib.request.Request(fit_token_url,data=dataURLencoded, method='POST')

# Authorisation Header
req.add_header('Authorization', 'Basic '+base64_code_str)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

# POST Request and get response from request object
js_response = getresponse(req)

# Print the JSON response
print('Response:',json.dumps(js_response,indent=4))

# Reading Access Token
fit_access_token = js_response['access_token']
# Reading Refresh Token
fit_refresh_token = js_response['refresh_token']
# Reading User ID
user_id = js_response['user_id']

# Input from user for getting the data - date, datapoints, start-time, end-time for API URL
date = input('Enter Date for which you want the hearrate data in format yyyy-MM-dd \n')
detail_level = input('Enter number of data points to include, Either 1sec or 1min \n')
start_time = input ('Enter start of the period in the format HH:mm \n')
end_time = input('Enter end of the period in the format HH:mm \n')

# API URL - to call Heartrate data
fit_api_url = 'https://api.fitbit.com/1/user/'+user_id+'/activities/heart/date/'+date+'/1d/'+detail_level+'/time/'+start_time+'/'+end_time+'.json'

# API CALL
# GET API Call Request - HeartRate data
api_req = urllib.request.Request(fit_api_url, method='GET')
# Authorisation Header
api_req.add_header('Authorization','Bearer ' + fit_access_token)

api_response = getresponse(api_req)
# print('Response:',json.dumps(api_response,indent=4))

# extracting the heartrate & timestamp data
my_hr_data = api_response['activities-heart-intraday']['dataset']
# print('My Fitbit Heart Rate data for the day',date,'between the hours',start_time,' - ',end_time,':\n',my_hr_data)

# convert into a dataframe
hr_data_df = pd.DataFrame(data=my_hr_data)
# print('Jays Fitbit Heart Rate data for the day',date,'between the hours',start_time,' - ',end_time,':\n',hr_data_df)

# Plot the data in Python and display it
plt.plot(hr_data_df['time'],hr_data_df['value'])
plt.grid('on')
plt.title ('Jays Fitbit Heart Rate data for '+date+' between '+start_time+' & '+end_time)
plt.xlabel('Time (Hrs)')
plt.xticks(rotation='vertical', fontsize=8)
plt.ylabel('Heart Rate (Bpm)')
plt.show()
