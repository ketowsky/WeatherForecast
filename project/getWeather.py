import requests
import time

from project.resources.constants import appid
from project.resources.constants import lat
from project.resources.constants import lon


class Weather:
    def __init__(self, city='Krakow'):
        self.dict_final_data = None
        self.city_name = city
        self.latitude = lat
        self.longitude = lon
        self.general_final_info = "Nothing to show yet"
        self.specific_final_data = "Nothing to show yet"

    def get_final_results(self) -> (str, str):
        """
        description: getter for final result report on weather in form of tuple of strings
        parameter:
        return: tuple of strings with final report on weather
                First element represents essential data
                Second element represents additional weather data
        """
        return self.general_final_info, self.specific_final_data

    def get_final_results_dict(self) -> dict:
        """
        description: getter for final result report on weather in form of dictionary
        parameter:
        return: dictionary with weather data
                    "city": info about city of weather measures
                    "condition": general description of weather conditions
                    "temperature": average temperature in Celsius degrees
                    "max temp": max temperature in Celsius degrees
                    "min temp": min temperature in Celsius degrees
                    "pressure": pressure in hPa
                    "humidity": humidity in %
                    "wind": wind speed in m/s
                    "sunrise": time of sunrise
                    "sunset": time of sunset
        """
        return self.dict_final_data

    def get_geocode(self, new_city: str = None) -> None:
        """
        description: getter for geocode coordinates for given city
        parameter: new_city - parameter used to change city of weather measure - default: None
        return: None
        """
        if new_city:
            backup_name = self.city_name
            self.city_name = new_city

        api = "http://api.openweathermap.org/geo/1.0/direct?q=" + self.city_name + "&limit=1&appid=" + appid
        json_data = requests.get(api).json()

        if json_data:
            self.city_name = json_data[0]['name']
            self.latitude = json_data[0]['lat']
            self.longitude = json_data[0]['lon']
        else:
            self.city_name = backup_name
            print("Chosen city was not recognized, so city stays default")

    def get_weather(self, name=None) -> None:
        """
        description: method downloads weather info for given city through Open Weather API
        parameter: name: Any - default=None
        return: None
        """
        if None not in [self.city_name, self.latitude, self.longitude]:
            api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(self.latitude) + "&lon=" + str(self.longitude) + "&appid=" + appid + "&units=metric"
        else:
            api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + appid + "&units=metric"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'])
        max_temp = int(json_data['main']['temp_max'])
        min_temp = int(json_data['main']['temp_min'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 79200))
        sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 79200))

        self.general_final_info = "City: " + self.city_name + '\nCondition: ' + condition + "\nTemperature: " + str(temp) + "[C]"
        self.specific_final_data = "\nMax temp: " + str(max_temp) + "[C]" + \
                     "\nMin temp: " + str(min_temp) + "[C]" + \
                     "\nPressure: " + str(pressure) + "[hPa]" + \
                     "\nHumidity: " + str(humidity) + "[%]" + \
                     "\nWind speed: " + str(wind) + "[m/s]" + \
                     "\nSunrise: " + str(sunrise) + \
                     "\nSunset: " + str(sunset)

        self.dict_final_data = {"city": self.city_name, "condition": condition, "temperature": temp, "max temp": max_temp,
                                "min temp": min_temp, "pressure": pressure, "humidity": humidity, "wind": wind,
                                "sunrise": sunrise, "sunset": sunset}

    def set_city(self, name: str) -> None:
        """
        description: setter for city of weather measurement
        parameter: name - name of new city - str
        return: None
        """
        self.get_geocode(new_city=name)
