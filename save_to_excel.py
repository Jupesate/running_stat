from retrieve import get_latest_activity, get_athlete_info, get_access_token, get_activities_by_time, change_timestamp_to_unix
from methods import convert_distance_to_km, convert_moving_time_to_hms, average_speed_min_per_km, maxspeed_miles_to_km
import pandas as pd


## This script saves the latest Strava activity and athlete information to an Excel file.
def save_to_excel(activity, athlete_info):
    # Create a DataFrame for the activity
    activity_data = {
        'Name': [activity['name']],
        'Distance (km)': [convert_distance_to_km(activity['distance'])],
        'Moving Time (h:min)': [convert_moving_time_to_hms(activity['moving_time'])],
        'Moving Time (seconds)': [activity['moving_time']],
        'Elapsed Time (s)': [activity['elapsed_time']], ##Sinänsä turha tässä vian näkyy tauot + reeni. 
        'Type': [activity['type']],
        'Start Date': [activity['start_date_local']],
        'Average Speed (min/km)': [average_speed_min_per_km(convert_distance_to_km(activity['distance']),activity['moving_time'])],
        'Max Speed (m/s)': [maxspeed_miles_to_km(activity['max_speed'])]
    }
    
    activity_df = pd.DataFrame(activity_data)
    
    # Create a DataFrame for the athlete info
    athlete_data = {
        'Athlete Name': [f"{athlete_info['firstname']} {athlete_info['lastname']}"],
        'Athlete ID': [athlete_info['id']],
        'City': [athlete_info.get('city', '')],
        'Country': [athlete_info.get('country', '')]
    }
    athlete_df = pd.DataFrame(athlete_data)
    # Save both DataFrames to an Excel file
    with pd.ExcelWriter('strava_activity.xlsx') as writer:
        activity_df.to_excel(writer, sheet_name='Activity', index=False)
        athlete_df.to_excel(writer, sheet_name='Athlete Info', index=False)
        

def save_multiple_activities_to_excel(activities):
    # Placeholder implementation to avoid syntax error
    all_activities_data = []
    for activity in activities:
        activity_data = {
        'Name': activity['name'],
        'Distance (km)': convert_distance_to_km(activity['distance']),
        'Moving Time (h:min)': convert_moving_time_to_hms(activity['moving_time']),
        'Moving Time (seconds)': activity['moving_time'],
        'Elapsed Time (s)': activity['elapsed_time'], ##Sinänsä turha tässä vian näkyy tauot + reeni. 
        'Type': activity['type'],
        'Start Date': activity['start_date_local'],
        'Average Speed (min/km)': average_speed_min_per_km(convert_distance_to_km(activity['distance']),activity['moving_time']),
        'Max Speed (m/s)': maxspeed_miles_to_km(activity['max_speed'])
    }
        all_activities_data.append(activity_data)
     
    all_activity_df = pd.DataFrame(all_activities_data)     
    with pd.ExcelWriter('strava_activity.xlsx') as writer:
        all_activity_df.to_excel(writer, sheet_name='Activities', index=False)
    print("Succesful printing")

#
        
##Create main method to run the script
if __name__ == "__main__":
    before = "1/7/2025"
    after = "1/6/2025"
    try:
        access_token = get_access_token()
        print("Access token retrieved successfully.")
        print(f"Access Token: {access_token}")
        activities = get_activities_by_time(access_token, before, after)
        save_multiple_activities_to_excel(activities)
        #athlete_info = get_athlete_info(access_token)
        #latest_activity = get_latest_activity(access_token)
        #save_to_excel(latest_activity, athlete_info)
        print("Data saved to strava_activity.xlsx successfully.")
    except Exception as e:
        print(e)