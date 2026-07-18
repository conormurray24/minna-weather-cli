import requests
import sys

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data["current_condition"][0]
        location = data["nearest_area"][0]
        
        print(f"\n📍 {location['areaName'][0]['value']}, {location['country'][0]['value']}")
        print(f"🌡️  Temperature: {current['temp_C']}°C (feels like {current['FeelsLikeC']}°C)")
        print(f"☁️  Weather: {current['weatherDesc'][0]['value']}")
        print(f"💨 Wind: {current['windspeedKmph']} km/h")
        print(f"💧 Humidity: {current['humidity']}%")
        print(f"👁️  Visibility: {current['visibility']} km\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city name>")
        print("Example: python weather.py Minna")
        sys.exit(1)
    
    city = " ".join(sys.argv[1:])
    get_weather(city)
