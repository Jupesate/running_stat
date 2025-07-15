import requests
import json
import os
from dotenv import load_dotenv, set_key


#Refresh_tokens.py
#Author: Juho Tepponen, Github: Jupesate
#Version: 15.7.2025
#Haetaan pääohjelmaa varten access token, jotta voidaan käyttää strava Apia.

load_dotenv()
access_token = os.getenv('Access_Token_final')
refresh_token = os.getenv('Refresh_token_final')
Client_ID = int(os.getenv('Client_ID'))
Client_Secret = os.getenv('Client_Secret') 

def refresh_tokens():
    # Tehdään pyyntö strava apiin
    data = {
        "client_id": Client_ID,
        "client_secret": Client_Secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    posti = requests.post("https://www.strava.com/oauth/token", data=data)
    if posti.status_code == 200:
        answer = posti.json()
        #print(answer)
        #print(answer['access_token'])
        #print(answer['refresh_token'])
        return answer["access_token"], answer["refresh_token"]
    else:
        raise Exception(f"Error retrieving refresh token: {posti.status_code} - {posti.text}")


def save_tokens_to_env(access, refresh):
    
    dotenv_path = '.env'
    set_key(dotenv_path, "Access_Token_final", access)
    set_key(dotenv_path, "Refresh_token_final", refresh)

    print("Tokens saved to .env successfully.")
    
## Create main method to run the script
if __name__ == "__main__":
    try:
        access, refresh = refresh_tokens()
        #print("access token: " + access + " ja \n refresh token: " + refresh)
        save_tokens_to_env(access, refresh)
    except Exception as e:
        print(e)





