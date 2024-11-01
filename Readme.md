###Steps to Get Started:

1. Sign up at OpenWeatherMap and get your free API key.


2. Install the requests library if you haven't already (you can do this by running pip install requests in your terminal).


###Explanation of the Code

1. get_weather(city, api_key) function:

Constructs the API URL with the city name and API key.

Fetches data from OpenWeatherMap.

Extracts the temperature, feels-like temperature, and weather description from the JSON response.



2. Error Handling:

If the API request is successful (status_code == 200), it displays the weather details.

If not, it informs the user that the city was not found.



3. main() function:

Prompts the user to enter a city name.

Calls the get_weather() function with the entered city name.




###Usage

Run the code, enter the name of a city, and it will display the current temperature, feels-like temperature, and weather description for that location.
