import requests

pin = input("Enter pin code of your area: ").strip()

try:
    # STEP 1 — Get location from PIN
    geo_url = f"http://api.zippopotam.us/in/{pin}"
    geo_r = requests.get(geo_url, timeout=5)

    if geo_r.status_code != 200:
        print("Invalid PIN code or no data found.")
        exit()

    geo_data = geo_r.json()
    place = geo_data['places'][0]

    city = place['place name']
    state = place['state']
    lat = float(place['latitude'])
    lon = float(place['longitude'])

    print(f"\n Location Found")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Coordinates: ({lat}, {lon})")

    # STEP 2 — Get weather using coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    parameters = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    weather_r = requests.get(weather_url, params=parameters, timeout=5)
    weather_data = weather_r.json()

    curr = weather_data["current_weather"]

    print("\n🌤 Current Weather")
    print(f"Temperature: {curr['temperature']}°C")
    print(f"Windspeed: {curr['windspeed']} km/h")
    print(f"Time: {curr['time']}")

except requests.exceptions.Timeout:
    print(" Error: The server took too long to respond.")

except requests.exceptions.ConnectionError:
    print(" Error: No internet connection.")

except Exception as e:
    print(f" Unexpected error: {e}")
