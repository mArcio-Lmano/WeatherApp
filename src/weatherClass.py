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
        url_today = f"https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.countryCode}&limit={self.limit}&appid={self.apiKey}"
        r = requests.get(url=url_today)
        data = r.json()
        self.temperatures = []
        self.processTemperatureData([data])


    def getWeather5Days(self):
        url_5days= f"https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.countryCode}&limit={self.limit}&appid={self.apiKey}"    
        r = requests.get(url=url_5days)
        data = r.json()

        self.temperatures = []
  
        data = data["list"]
        self.processTemperatureData(data)

    

    def processTemperatureData(self, data):
        for info in data:
            try:
                try:
                    date = self.convertToMachineUTC(info["dt_txt"])
                except KeyError as e:
                    print(f"Error: Key 'dt_txt' not found in temperature data")
                    date = self.convertToMachineUTC(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

                temperature_info = info["main"]
                min_temperature  = self.convertKelvin(temperature_info["temp_min"])
                max_temperature  = self.convertKelvin(temperature_info["temp_max"])
                humidity         = temperature_info["humidity"]

                weather_info        = info["weather"][0]
                weather             = weather_info["main"]
                weather_description = weather_info["description"]
                weather_icon        = weather_info["icon"] + ".png"

                clouds = info["clouds"]["all"]

                wind_info  = info["wind"]
                wind_speed = wind_info["speed"]
                wind_deg   = wind_info["deg"]

                try:
                    sunrise = self.convertToMachineUTC(datetime.utcfromtimestamp(info["sys"]["sunrise"])
                                                    .strftime("%Y-%m-%d %H:%M:%S"))
                    sunset  = self.convertToMachineUTC(datetime.utcfromtimestamp(info["sys"]["sunset"])
                                                    .strftime("%Y-%m-%d %H:%M:%S"))
                except KeyError as e:
                    print(f"Error: Key 'sunrise' or 'sunset' not found in temperature data")
                    sunrise = None
                    sunset  = None

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
                    "wind_deg": wind_deg,
                    "sunrise": sunrise,
                    "sunset": sunset
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


