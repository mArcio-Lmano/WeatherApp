import time
import pytz
import requests
from datetime import datetime


class WeatherApp:
    def __init__(self, apiKey, city, countryCode, limit = 5):
        self.apiKey = apiKey
        self.city = city
        self.countryCode = countryCode
        self.limit = 5
        self.temperatures = []


    def getWeatherToday(self):
       
        # r = requests.get(url=url_today)
        # data = r.json
        # print(r.text)
        # print(data)


        

        self.processTemperatureData([data])
        print(self.temperatures)

        # self.temperature = data["main"]["temp"]
        # self.humidity = data["main"]["humidity"]

        # self.convertKelvin()
        # self.prettyPrint()


    def getWeather4Days(self):
       
        # r = requests.get(url=url_4days)
        # print(r.text)
        # print(data)

   

        data = data["list"]
        self.processTemperatureData(data)

        print(self.temperatures)
    

    def processTemperatureData(self, data):
        # try:
        #     temperatures = data["list"]
        # except KeyError:
        #     print("Error: 'list' key not found in data")
        #     return

        for info in data:
            try:
                try:
                    date = self.convertToMachineUTC(info["dt_txt"])
                except KeyError as e:
                    print(f"Error: Key 'dt_txt' not found in temperature data")
                    date = self.convertToMachineUTC(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
                    # 2024-04-01 18:00:00

                temperature_info = info["main"]
                min_temperature = self.convertKelvin(temperature_info["temp_min"])
                max_temperature = self.convertKelvin(temperature_info["temp_max"])
                humidity = temperature_info["humidity"]

                weather_info = info["weather"][0]
                weather = weather_info["main"]
                weather_description = weather_info["description"]
                weather_icon = weather_info["icon"] + ".png"

                clouds = info["clouds"]["all"]

                wind_info = info["wind"]
                wind_speed = wind_info["speed"]
                wind_deg = wind_info["deg"]

                self.temperatures.append({
                    "date": date,
                    "min_temperature": min_temperature,
                    "max_temperature": max_temperature,
                    "humidity": humidity,
                    "weather": weather,
                    "weather_description": weather_description,
                    "weather_icon": weather_icon,
                    "clouds": clouds,
                    "wind_speed": wind_speed,
                    "wind_deg": wind_deg
                })

            except KeyError as e:
                print(f"Error: Key '{e.args[0]}' not found in temperature data")
                
    def convertKelvin(self, temperature):
        kelvinConstant = -273.15
        return round(temperature + kelvinConstant,2)

    def convertToMachineUTC(self, date):
        date = datetime.fromisoformat(date)
        local_tz = pytz.timezone("Europe/Lisbon")  
        now_local = pytz.utc.localize(date).astimezone(local_tz)
        return now_local

    def prettyPrint(self):
        printString = f"""
        City: {self.city}
        Temperature: {self.temperature}C
        Humidity: {self.humidity}%
"""
        print(printString)


    

def main():
    apiKey = "a3d23475d1415dd9e8b765d7efe21473"

    weather = WeatherApp(apiKey=apiKey, city="Barcelos", countryCode="PT")
    # weather.getWeatherToday()
    # weather.getWeather4Days()
    # weather.convertToMachineUTC()


if __name__ =="__main__":
    main()