import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        feels_like = main['feels_like']
        weather_description = weather['description']
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Weather: {weather_description.capitalize()}")
    else:
        print("City not found. Please check the city name.")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
