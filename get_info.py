# import requests library
import requests

#import json library
import json

# put the desired api call as the value
api = 'https://api.ciscospark.com/v1/people/me'

# Provide your access token
auth_token = ""

#Content type must be included in the header
header = {"content-type": "application/json; charset=utf-8","Authorization" : "Bearer " + auth_token}

#Performs a GET on the specified api.
response= requests.get(api, headers=header)

# print the json that is returned
print(response.text)
