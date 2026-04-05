import requests

def fetch_weather(city_name):
    api_key = "YOUR_API_KEY_HERE"   # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    return temp, humidity, condition

def display_weather():
    print("=== Weather Checker ===")

    city = input("Enter city name: ")

    result = fetch_weather(city)

    if result:
        temperature, humidity, weather_desc = result

        print("\n--- Weather Details ---")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc}")

    else:
        print("City not found or API error!")

# Run program
display_weather()
