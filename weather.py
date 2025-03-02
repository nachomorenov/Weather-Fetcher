import requests

API_KEY = "08de8a9b8229cd03eebc9a0023cc56b4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15) 
    print(f"{city} Meteorology:")
    print("Weather:",weather)
    print("Temperature:",temperature,"Celsius")
else:
    print("An error ocurred.")

