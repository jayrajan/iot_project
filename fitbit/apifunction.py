# Code written by Jerin Rajan on 04th Jun 2020
# This file would contain functions related to api call
# Input = Request URL to the server
# Output = JSON response from the server

import urllib.request
import json
def getresponse(url):

    try:
        response = urllib.request.urlopen(url)
        FullResponse = response.read()
        # Capture response in JSON format
        response = json.loads(FullResponse)
        

    # HTTP Error Handling
    except urllib.error.HTTPError as e:
        print('HTTP ERROR CODE:',e.code)
        print(e.msg)
        print(e.reason)
        print(e.headers)
    
    return response
