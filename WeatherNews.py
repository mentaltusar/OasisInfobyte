import requests

KEY = "ce7d0359bba74835b15387d1f908be45"


def get_zip(zipcode):
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching coordinates")
        return None


def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data")
        return None


def display(weather_data):
    if weather_data:
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather = weather_data['weather'][0]['description']
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
    else:
        print("Failed to get weather data. Please check the location or try again later.")


def main():
    zipcode = input("Enter the ZIP code: ")
    location = get_zip(zipcode)
    if location:
        lat = location['lat']
        lon = location['lon']
        weather_data = get_weather(lat, lon)
        display(weather_data)
    else:
        print("Invalid ZIP code or unable to fetch location data")


if __name__ == "__main__":
    main()
