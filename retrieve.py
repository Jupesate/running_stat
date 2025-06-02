import requests
import json
import os

##In this file is the script for retrieving the data from the strava API

#https://www.strava.com/api/v3/athlete \
#-H 'Authorization: Bearer YOURACCESSTOKEN'

#Documentation for api is here:
#https://developers.strava.com/docs/reference/
##We will do this via HTTP request for convenience
# The URL for the Strava API endpoint to retrieve athlete activities

url = 'https://www.strava.com/api/v3/athlete/activities'
access_token = os.getenv("Access_Token_viimeinen")    

#http get "https://www.strava.com/api/v3/athlete" "Authorization: Bearer [[token]]"

##Retrieving athelete data
def get_athlete_info(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://www.strava.com/api/v3/athlete", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving athlete info: {response.status_code} - {response.text}")


def get_latest_activity(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://www.strava.com/api/v3/athlete/activities?per_page=1", headers=headers)
    if response.status_code == 200:
        activities = response.json()
        if activities:
            return activities[0]
        else:
            raise Exception("No activities found.")
    else:
        raise Exception(f"Error retrieving latest activity: {response.status_code} - {response.text}")
    
    
    
    
    
    
    
#headers = {"Authorization": f"Bearer {access_token}"}
#response = requests.get("https://www.strava.com/api/v3/athlete/activities?per_page=1", headers=headers)
#latest_activity = response.json()[0]
#
#print(latest_activity['name'], latest_activity['distance'], latest_activity['moving_time'])



##Create main method to run the script
if __name__ == "__main__":
    try:
        athlete_info = get_athlete_info(access_token)
        print(f"Athlete Name: {athlete_info['firstname']} {athlete_info['lastname']}")
        with open("response_athelete.json", "w", encoding="utf-8") as f:
            json.dump(athlete_info, f, indent=4)
        
        latest_activity = get_latest_activity(access_token)
        print(f"Latest Activity: {latest_activity['name']}, Distance: {latest_activity['distance']} meters, Moving Time: {latest_activity['moving_time']} seconds")
        with open("response_activity.json", "w", encoding="utf-8") as f:
            json.dump(latest_activity, f, indent=4)
    except Exception as e:
        print(e)