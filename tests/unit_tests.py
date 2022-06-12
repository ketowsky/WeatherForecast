from project.getWeather import Weather


def test_Krakow_is_default_city():

    weather_obj = Weather()

    weather_obj.get_weather()
    assert weather_obj.get_final_results_dict()['city'] == 'Krakow'


def test_default_has_all_fields():

    weather_obj = Weather()

    weather_obj.get_weather()
    assert len(weather_obj.get_final_results_dict()) == 10
    assert list(weather_obj.get_final_results_dict().keys()) == ["city", "condition", "temperature", "max temp", "min temp",
                                                                 "pressure", "humidity", "wind", "sunrise", "sunset"]


def test_default_has_all_fields_not_empty():

    weather_obj = Weather()

    weather_obj.get_weather()
    assert len(weather_obj.get_final_results_dict()) == 10
    assert None not in weather_obj.get_final_results_dict().values()


def test_set_city():
    weather_obj = Weather()

    weather_obj.set_city("Tarnow")
    weather_obj.get_weather()

    assert weather_obj.get_final_results_dict()['city'] == 'Tarnów'


def test_set_city_has_all_fields_not_empty():
    weather_obj = Weather()

    weather_obj.set_city("Tarnow")
    weather_obj.get_weather()

    assert len(weather_obj.get_final_results_dict()) == 10
    assert list(weather_obj.get_final_results_dict().keys()) == ["city", "condition", "temperature", "max temp", "min temp",
                                                                 "pressure", "humidity", "wind", "sunrise", "sunset"]
    assert None not in weather_obj.get_final_results_dict().values()


def test_set_city_fails_and_city_stays_default():
    weather_obj = Weather()

    weather_obj.set_city("")
    weather_obj.get_weather()

    assert weather_obj.get_final_results_dict()['city'] == 'Krakow'
