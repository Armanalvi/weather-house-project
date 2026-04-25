import requests

def get_weather(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "City not found"

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        return f"{city} → Temp: {temp}°C, Humidity: {humidity}%, {condition}"

    except:
        return "Error fetching weather"


def predict_price(area, bedrooms):
    price = (area * 3000) + (bedrooms * 500000)
    return price


print("1. Weather Forecast")
print("2. House Price Prediction")

choice = input("Enter choice: ")

if choice == "1":
    city = input("Enter city: ")
    print(get_weather(city))

elif choice == "2":
    area = int(input("Enter area: "))
    bedrooms = int(input("Enter bedrooms: "))
    print("Estimated Price:", predict_price(area, bedrooms))
