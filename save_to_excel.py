from retrieve import get_latest_activity, get_athlete_info, access_token
import pandas as pd


def save_to_excel(activity, athlete_info):
    # Create a DataFrame for the activity
    activity_data = {
        'Name': [activity['name']],
        'Distance (m)': [activity['distance']],
        'Moving Time (s)': [activity['moving_time']],
        'Elapsed Time (s)': [activity['elapsed_time']],
        'Type': [activity['type']],
        'Start Date': [activity['start_date_local']],
        'Average Speed (m/s)': [activity['average_speed']],
        'Max Speed (m/s)': [activity['max_speed']]
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
        
        
##Create main method to run the script
if __name__ == "__main__":
    try:
        athlete_info = get_athlete_info(access_token)
        latest_activity = get_latest_activity(access_token)
    except Exception as e:
        print(e)