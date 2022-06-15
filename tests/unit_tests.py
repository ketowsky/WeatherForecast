from project.getWeather import Weather


def test_Krakow_is_default_city():
    """
    description: test case checks if default city for weather forecast report is Krakow
    """
    weather_obj = Weather()

    weather_obj.get_weather()
    assert weather_obj.get_final_results_dict()['city'] == 'Krakow'


def test_default_has_all_fields():
    """
    description: test case checks if report for default city is gathered and has all designed fields
    """
    weather_obj = Weather()

    weather_obj.get_weather()
    assert len(weather_obj.get_final_results_dict()) == 10
    assert list(weather_obj.get_final_results_dict().keys()) == ["city", "condition", "temperature", "max temp", "min temp",
                                                                 "pressure", "humidity", "wind", "sunrise", "sunset"]


def test_default_has_all_fields_not_empty():
    """
    description: test case checks if report for default city is gathered and all designed fields have values
    """
    weather_obj = Weather()

    weather_obj.get_weather()
    assert len(weather_obj.get_final_results_dict()) == 10
    assert None not in weather_obj.get_final_results_dict().values()


def test_set_city():
    """
    description: test case checks if setter for a different city works properly and after setting city as 'Tarnow'
                 app gathers weather report for given city
    """
    weather_obj = Weather()

    weather_obj.set_city("Tarnow")
    weather_obj.get_weather()

    assert weather_obj.get_final_results_dict()['city'] == 'Tarnów'


def test_set_city_has_all_fields_not_empty():
    """
    description: test case checks if after setting city as 'Tarnow' app gathers weather report for given city and
                 data in report are valid
    """
    weather_obj = Weather()

    weather_obj.set_city("Tarnow")
    weather_obj.get_weather()

    assert len(weather_obj.get_final_results_dict()) == 10
    assert list(weather_obj.get_final_results_dict().keys()) == ["city", "condition", "temperature", "max temp", "min temp",
                                                                 "pressure", "humidity", "wind", "sunrise", "sunset"]
    assert None not in weather_obj.get_final_results_dict().values()


def test_set_city_is_empty_and_city_stays_default():
    """
    description: test case checks if after faulty setting city as empty string app gathers weather report for default city
    """
    weather_obj = Weather()

    weather_obj.set_city("")
    weather_obj.get_weather()

    assert weather_obj.get_final_results_dict()['city'] == 'Krakow'


def test_set_city_fails_and_city_stays_default():
    """
    description: test case checks if after faulty setting city as incorrect string app gathers weather report for default city
    """
    weather_obj = Weather()

    weather_obj.set_city("rrr")
    weather_obj.get_weather()

    assert weather_obj.get_final_results_dict()['city'] == 'Krakow'
