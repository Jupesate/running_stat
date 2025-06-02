from __future__ import print_statement
import time
from stravalib.client import Client
from pprint import pprint
##In this file is the script for retrieving the data from the strava API

#https://www.strava.com/api/v3/athlete \
#-H 'Authorization: Bearer YOURACCESSTOKEN'

#Documentation for api is here:
#https://developers.strava.com/docs/reference/


url = 'https://www.strava.com/api/v3/athlete/activities'




# Configure OAuth2 access token for authorization: strava_oauth
# Configure OAuth2 access token for authorization: strava_oauth
access_token = '54e6b2339a51bb2a4ea77ed5f30d491f38192dc8'

# create an instance of the API client
client = Client()
client.access_token = access_token

try:
    # Get Authenticated Athlete
    athlete = client.get_athlete()
    pprint(athlete)
except Exception as e:
    print("Exception when calling get_athlete: %s\n" % e)