from project.getWeather import Weather
from flask import Flask, request, jsonify


app = Flask(__name__)
diff_cites = ["Tarnow"]
custom_rule = ["default"]


@app.route("/", methods=['POST', 'GET'])
def weather():
    if request.method == 'GET':
        weather_obj = Weather()
        weather_obj.get_weather()
        if custom_rule[-1] == 'default':
            return weather_obj.get_final_results_dict()
        elif custom_rule[-1] == 'essential':
            name = weather_obj.get_final_results_dict()['city']
            cond = weather_obj.get_final_results_dict()['condition']
            temp = weather_obj.get_final_results_dict()['temperature']
            return jsonify({"city": name, 'condition': cond, 'temperature': temp})
        else:
            return weather_obj.get_final_results_dict()
    elif request.method == 'POST':
        rule = request.full_path.split("=")[1]
        custom_rule.append(rule)
        return '', 204


@app.route("/different-city", methods=['POST', 'GET'])
def diff_city_weather():
    if request.method == "GET":
        weather_obj = Weather()
        weather_obj.set_city(diff_cites[-1])
        weather_obj.get_weather()
        return weather_obj.get_final_results_dict()
    elif request.method == "POST":
        city = request.full_path.split("=")[1]
        diff_cites.append(city)
        return '', 204


if __name__ == "__main__":
    app.run()
