Application based on Current Weather Data API by OpenWeatherMap.org is desigend to provide current weather forecast for given city. 

Author: Ketowsky


To run application recommended way is to build it with Docker and run as container.
1. Clone repo.
2. Go to root application directory.
3. Run: 
        <cmd> docker build -t weather .  
        <cmd> docker run --name weather -d -p 5000:5000 weather
4. To verify if app is running check:
        cmd> docker logs weather
