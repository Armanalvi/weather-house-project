
import requests

def get_weather(city):
    api_key = "cf1eac8f994deb7ebcc639b914359d22"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return "City not found"

    return f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"


if __name__ == "__main__":
    city = input("Enter city: ")
    print(get_weather(city))
