



#Nämä pitää muuttaa. Tehdään metodit näille
#      "name": "Lunch Run",         ###Halutaan nimi
#      "distance": 16277.2,         ###Halutaan matka muutettuna kilometriksi
#      "moving_time": 6275,         ### 1h, 44 min , 35s Pitää tehdä käännös tähän.
#      "type": "Run",               ##Tarvii, voidaan tämän mukaan filtteröidä aktiviteetit
#      "start_date": "2025-06-01T09:37:04Z",   ##Tämä hyvä näin
#      "average_speed": 2.594,         ##Tarvitaan tämä. 6:26/km on tässä. 
#      "average_watts": 201.1,         ##Otetaan tämä
#      "kilojoules": 1262.1,           ##Muutetaan kaloreiksi


#Metrit kilometreiksi, pyöristetään kahteen desimaalin tarkkuuteen
def convert_distance_to_km(distance_meters):
    kilometreina = distance_meters / 1000
    return round(kilometreina, 3)
def convert_moving_time_to_hms(moving_time_seconds):
    hours = moving_time_seconds // 3600
    minutes = (moving_time_seconds % 3600) // 60 #Tunneista ylijäänyt aika jaetaan 60, ja jakojäännös on minuutit
    seconds = moving_time_seconds % 60
    return [hours, minutes, seconds]
    
def average_speed_min_per_km(distance_km, moving_time_seconds):
    sekunnit_per_kilsa = moving_time_seconds / distance_km
    minuutit = sekunnit_per_kilsa // 60  # Lasketaan minuutit jakamalla sekunnit 60:llä
    sekunnit = sekunnit_per_kilsa % 60  # Jäljelle jääneet sekunnit
    return round(minuutit), round(sekunnit)  # Pyöristetään arvot kokonaisluvuiksi
#Saan siis average pace kim/km muodossa, eli minuutit ja sekunnit per kilometri



def convert_kilojoules_to_calories(kilojoules):
    # 1 kilojoule = 0.239006 kilokaloria
    calories = kilojoules * 0.239006
    return round(calories, 2)  # Pyöristetään kahden desimaalin tarkkuuteen
##Tämä on oikea muunnos, mutta stravan api palauttaa väärät kilojoulet, tai ei ainakaan ole samat kuin 
#kalorit arvot stravan sovelluksessa. Joten tämä on selvitettävä vielä.


#main metodi testaukseen
if __name__ == "__main__":
    try:
        # Test the conversion functions
        distance_km = convert_distance_to_km(16277.2)
        print(f"Distance in km: {distance_km} km")
        
        moving_time_hms = convert_moving_time_to_hms(6275)
        print(f"Moving time: {moving_time_hms[0]} hours, {moving_time_hms[1]} minutes, {moving_time_hms[2]} seconds")
        
        average_speed = average_speed_min_per_km(distance_km, 6275)
        print(f"Average speed: {average_speed[0]}:{average_speed[1]} Min/km")
        ##    
    except Exception as e:
        print(e)