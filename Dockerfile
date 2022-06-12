FROM python:3.6.8-alpine3.8

# Install libraries
RUN pip install Flask
RUN pip install requests

# Set up working directory
WORKDIR /usr/src/app

# Copy app data into working directory
RUN mkdir -p /usr/src/app/project
COPY project/__init__.py ./project
COPY project/weather_flask.py ./project
COPY project/getWeather.py ./project
COPY project/resources ./project/resources

# Run app on Flask
ENV FLASK_APP project/weather_flask.py

EXPOSE 5000

CMD flask run -h 0.0.0.0

