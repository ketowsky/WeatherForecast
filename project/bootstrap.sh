#!/bin/sh
$env:FLASK_APP = "weather_flask.py"
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0