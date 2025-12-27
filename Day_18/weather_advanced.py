import requests

def get_valid_pin():
    """Loop until user enters a valid 6-digit PIN."""
    while True:
        pin = input("\nPlease enter your 6-digit PIN code: ").strip()

        if not pin.isdigit():
            print("⚠️ Please enter digits only.")
        elif len(pin) != 6:
            print("⚠️ PIN must be 6 digits.")
        else:
            print(f"✅ PIN {pin} accepted.")
            return pin


def fetch_location(pin):
    """Fetch location details from Zippopotam API."""
    geo_url = f"http://api.zippopotam.us/in/{pin}"

    response = requests.get(geo_url, timeout=5)
    response.raise_for_status()

    data = response.json()

    places = data.get("places", [])
    if not places:
        print("❌ No location details available for this PIN.")
        return None

    place = places[0]

    return {
        "city": place["place name"],
        "state": place["state"],
        "lat": float(place["latitude"]),
        "lon": float(place["longitude"])
    }


def fetch_weather(lat, lon):
    """Fetch weather details from Open-Meteo API."""
    weather_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(weather_url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()

    return data.get("current_weather", {})


def run_app():
    while True:

        pin = get_valid_pin()

        try:
            # Get Location
            location = fetch_location(pin)
            if not location:
                continue

            city = location["city"]
            state = location["state"]
            lat = location["lat"]
            lon = location["lon"]

            print("\n📍 Location Found")
            print(f"City: {city}")
            print(f"State: {state}")
            print(f"Coordinates: ({lat}, {lon})")

            # Get Weather
            weather = fetch_weather(lat, lon)

            temperature = weather.get("temperature", "N/A")
            windspeed = weather.get("windspeed", "N/A")
            time = weather.get("time", "N/A")

            print("\n🌤 Current Weather")
            print(f"Temperature: {temperature}°C")
            print(f"Windspeed: {windspeed} km/h")
            print(f"Time: {time}")

        except requests.exceptions.ConnectionError:
            print("❌ No Internet: Please check your connection.")

        except requests.exceptions.Timeout:
            print("❌ Slow API: The server took too long to respond.")

        except requests.exceptions.HTTPError as e:
            print(f"❌ Server Error: API returned {e.response.status_code}")

        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

        # Ask to search again
        while True:
            choice = input("\n🔁 Search another PIN? (y/n): ").strip().lower()

            if choice == "y":
                break
            elif choice == "n":
                print("\n👋 Exiting Weather App. Goodbye!")
                return
            else:
                print("⚠️ Please enter y or n.")


# Run program
run_app()
