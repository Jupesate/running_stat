from retrieve import get_latest_activity, get_athlete_info, get_access_token, get_activities_by_time, change_timestamp_to_unix
from methods import convert_distance_to_km, convert_moving_time_to_hms, average_speed_min_per_km, maxspeed_miles_to_km, get_file_path
import pandas as pd
import calendar
import os


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
        

def save_multiple_activities_to_excel(activities, file_path, kuukauden_nimi):
    # Placeholder implementation to avoid syntax error
    all_activities_data = []
    for activity in activities:
        activity_data = {
        'Name': activity['name'],
        'Distance (km)': convert_distance_to_km(activity['distance']),
        'Moving Time (h:min)': convert_moving_time_to_hms(activity['moving_time']),     
        'Type': activity['type'],
        'Start Date': activity['start_date_local'],
        'Average Speed (min/km)': average_speed_min_per_km(convert_distance_to_km(activity['distance']),activity['moving_time']),
        'Average Speed (m/s)': activity['average_speed'],
    }
        if(activity['has_heartrate']):
            activity_data['Average Heart rate (b/min)'] = activity['average_heartrate']

        all_activities_data.append(activity_data)
    all_activity_df = pd.DataFrame(all_activities_data)
    os.makedirs(file_path,exist_ok=True)     
    with pd.ExcelWriter(f"{file_path}/Aktiviteetit_{kuukauden_nimi}.xlsx") as writer:
        all_activity_df.to_excel(writer, sheet_name=f'Activities_{kuukauden_nimi}', index=False)
    print("Succesful printing")

##Tätä käytetään kun halutaan tietyn kuukauden aika.
## int year = 2022, mikä vuosi
## int month = 7, mikä kuukausi
## string access_token
def get_months_activity(access_token, month, year):
    #Ensin pitää saada muutettua kuukausi muotoon "01/06/2025"
    #Eli pitää osata etsiä netistä tai jollain importilla 
    #Monta päivää kuukaudessa on ollut tiettynä vuotena.
    number_of_days = calendar.monthrange(year,month)[1] ##Palauttaa viimeisen päivän nimen ja toisena numeron
    print(number_of_days)
    after = f"1/{month}/{year}" 
    before = f"{number_of_days}/{month}/{year}"
    activities = get_activities_by_time(access_token, before, after)
    file_path, kuukauden_nimi = get_file_path(month, year)
    save_multiple_activities_to_excel(activities, file_path, kuukauden_nimi)
    #print(after + " " + before)
    
        
##Create main method to run the script
if __name__ == "__main__":
    #before = "1/7/2025"
    #after = "1/6/2025"
    while True:
        month = int(input("Give month number of the month you wish to get activities (e.g 1,2,3...12)\n > "))
        if(month <= 0 or month > 12):
            print(f"Annoitte viallisen kuukauden {month}")
            continue
        break
        
    year = int(input("Give the months year (e.g 2023,2024...2042)\n >"))
    try:
        access_token = get_access_token()
        print("Access token retrieved successfully.")
        print(f"Access Token: {access_token}")
        get_months_activity(access_token, month,year)
        #athlete_info = get_athlete_info(access_token)
        #latest_activity = get_latest_activity(access_token)
        #save_to_excel(latest_activity, athlete_info)
        print("Data saved successfully.")
    except Exception as e:
        print(e)
    