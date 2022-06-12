from getWeather import Weather

print("Welcome to our weather forecast!\n")

weather_obj = Weather()

weather_obj.get_weather()
results = weather_obj.get_final_results()
print(results[0], results[1])

print(weather_obj.get_final_results_dict().keys())
print(weather_obj.get_final_results_dict().values())
print(len(weather_obj.get_final_results_dict()))

print("============================================================================\n")
weather_obj.set_city("Tarnow")
weather_obj.get_weather()
results = weather_obj.get_final_results()
print(results[0], results[1])

name = weather_obj.get_final_results_dict()['city']
cond = weather_obj.get_final_results_dict()['condition']
temp = weather_obj.get_final_results_dict()['temperature']
print(name, cond, temp)



