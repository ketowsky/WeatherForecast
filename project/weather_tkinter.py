import tkinter as tk
import requests
import time

from project.resources.constants import appid
from project.resources.constants import lat
from project.resources.constants import lon


def get_geocode(name):
    city = textfield.get()
    print(city)
    # api = "http://api.openweathermap.org/geo/1.0/direct?q=" + "Krakow" + "&limit=1&appid=" + appid
    api = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=1&appid=" + appid
    json_data = requests.get(api).json()

    city_name = json_data[0]['local_names']['pl']
    latitude = json_data[0]['lat']
    longitude = json_data[0]['lon']

    return city_name, latitude, longitude


def get_weather(name=None):
    # city = get_geocode()

    city = textfield.get()
    print(city)
    # api = "http://api.openweathermap.org/geo/1.0/direct?q=" + "Krakow" + "&limit=1&appid=" + appid
    api = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=1&appid=" + appid
    json_data = requests.get(api).json()

    city_name = json_data[0]['local_names']['pl']
    latitude = json_data[0]['lat']
    longitude = json_data[0]['lon']

    city = city_name, latitude, longitude

    # api = "https://api.openweathermap.org/data/2.5/weather?city=" + city + "&appid=" + appid + "&units=metric"
    if len(city) == 3:
        api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(city[1]) + "&lon=" + str(city[2]) + "&appid=" + appid  # + "&units=metric"
    else:
        api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + appid #+ "&units=metric"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 79200))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 79200))

    final_info = city[0] + '\n' + condition + "\n" + str(temp) + "[C]"
    final_data = "\nMax temp: " + str(max_temp) + \
                 "\nMin temp: " + str(min_temp) + \
                 "\nPressure: " + str(pressure) + \
                 "\nHumidity: " + str(humidity) + \
                 "\nWind speed: " + str(wind) + \
                 "\nSunrise: " + str(sunrise) + \
                 "\nSunset: " + str(sunset)

    label1.config(text=final_info)
    label2.config(text=final_data)
    # return final_info, final_data


# result = get_weather()
# print(result[0], result[1])


canvas = tk.Tk()

canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', get_weather)

canvas.mainloop()
