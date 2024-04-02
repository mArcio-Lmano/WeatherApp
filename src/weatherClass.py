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
        url_today = f"https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.countryCode}&limit={self.limit}&appid={self.apiKey}"
        r = requests.get(url=url_today)
        data = r.json()
        self.temperatures = []
        self.processTemperatureData([data])


    def getWeather4Days(self):
        # url_4days= f"https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.countryCode}&limit={self.limit}&appid={self.apiKey}"    
        # r = requests.get(url=url_4days)
        # print(r.text)
        # print(data)

        self.temperatures = []
        data = {
            "cod":"200",
            "message":0,
            "cnt":40,
            "list":[
                {
                    "dt":1711994400,
                    "main":{
                        "temp":286.46,
                        "feels_like":285.73,
                        "temp_min":285.28,
                        "temp_max":286.46,
                        "pressure":1014,
                        "sea_level":1014,
                        "grnd_level":1003,
                        "humidity":72,
                        "temp_kf":1.18
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":83
                    },
                    "wind":{
                        "speed":4.4,
                        "deg":210,
                        "gust":8.12
                    },
                    "visibility":10000,
                    "pop":0.98,
                    "rain":{
                        "3h":0.14
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-01 18:00:00"
                },
                {
                    "dt":1712005200,
                    "main":{
                        "temp":284.34,
                        "feels_like":283.71,
                        "temp_min":282.99,
                        "temp_max":284.34,
                        "pressure":1015,
                        "sea_level":1015,
                        "grnd_level":1004,
                        "humidity":84,
                        "temp_kf":1.35
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":51
                    },
                    "wind":{
                        "speed":3.57,
                        "deg":167,
                        "gust":6.71
                    },
                    "visibility":10000,
                    "pop":0.2,
                    "rain":{
                        "3h":0.24
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-01 21:00:00"
                },
                {
                    "dt":1712016000,
                    "main":{
                        "temp":283.02,
                        "feels_like":280.94,
                        "temp_min":283.02,
                        "temp_max":283.02,
                        "pressure":1015,
                        "sea_level":1015,
                        "grnd_level":1004,
                        "humidity":92,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":67
                    },
                    "wind":{
                        "speed":4.11,
                        "deg":149,
                        "gust":9.28
                    },
                    "visibility":10000,
                    "pop":0.36,
                    "rain":{
                        "3h":0.29
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-02 00:00:00"
                },
                {
                    "dt":1712026800,
                    "main":{
                        "temp":283.76,
                        "feels_like":283.12,
                        "temp_min":283.76,
                        "temp_max":283.76,
                        "pressure":1014,
                        "sea_level":1014,
                        "grnd_level":1003,
                        "humidity":86,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":5.13,
                        "deg":159,
                        "gust":13.16
                    },
                    "visibility":10000,
                    "pop":0.03,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-02 03:00:00"
                },
                {
                    "dt":1712037600,
                    "main":{
                        "temp":284.83,
                        "feels_like":284.22,
                        "temp_min":284.83,
                        "temp_max":284.83,
                        "pressure":1013,
                        "sea_level":1013,
                        "grnd_level":1002,
                        "humidity":83,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":5.64,
                        "deg":162,
                        "gust":13.56
                    },
                    "visibility":10000,
                    "pop":0.2,
                    "rain":{
                        "3h":0.13
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-02 06:00:00"
                },
                {
                    "dt":1712048400,
                    "main":{
                        "temp":285.15,
                        "feels_like":284.73,
                        "temp_min":285.15,
                        "temp_max":285.15,
                        "pressure":1013,
                        "sea_level":1013,
                        "grnd_level":1001,
                        "humidity":89,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":8.54,
                        "deg":168,
                        "gust":14.21
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":0.72
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-02 09:00:00"
                },
                {
                    "dt":1712059200,
                    "main":{
                        "temp":284.68,
                        "feels_like":284.29,
                        "temp_min":284.68,
                        "temp_max":284.68,
                        "pressure":1011,
                        "sea_level":1011,
                        "grnd_level":1000,
                        "humidity":92,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":501,
                            "main":"Rain",
                            "description":"moderate rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":8.25,
                        "deg":164,
                        "gust":17.39
                    },
                    "visibility":6437,
                    "pop":1,
                    "rain":{
                        "3h":3.21
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-02 12:00:00"
                },
                {
                    "dt":1712070000,
                    "main":{
                        "temp":286.5,
                        "feels_like":286.35,
                        "temp_min":286.5,
                        "temp_max":286.5,
                        "pressure":1011,
                        "sea_level":1011,
                        "grnd_level":1000,
                        "humidity":94,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":502,
                            "main":"Rain",
                            "description":"heavy intensity rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":8.79,
                        "deg":208,
                        "gust":14.11
                    },
                    "visibility":8707,
                    "pop":1,
                    "rain":{
                        "3h":14.28
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-02 15:00:00"
                },
                {
                    "dt":1712080800,
                    "main":{
                        "temp":286.59,
                        "feels_like":286.39,
                        "temp_min":286.59,
                        "temp_max":286.59,
                        "pressure":1013,
                        "sea_level":1013,
                        "grnd_level":1001,
                        "humidity":92,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":501,
                            "main":"Rain",
                            "description":"moderate rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":99
                    },
                    "wind":{
                        "speed":5.68,
                        "deg":234,
                        "gust":10.74
                    },
                    "visibility":4635,
                    "pop":1,
                    "rain":{
                        "3h":3.69
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-02 18:00:00"
                },
                {
                    "dt":1712091600,
                    "main":{
                        "temp":285.69,
                        "feels_like":285.51,
                        "temp_min":285.69,
                        "temp_max":285.69,
                        "pressure":1015,
                        "sea_level":1015,
                        "grnd_level":1004,
                        "humidity":96,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":80
                    },
                    "wind":{
                        "speed":3.79,
                        "deg":223,
                        "gust":8.66
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":1.66
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-02 21:00:00"
                },
                {
                    "dt":1712102400,
                    "main":{
                        "temp":284.75,
                        "feels_like":284.45,
                        "temp_min":284.75,
                        "temp_max":284.75,
                        "pressure":1016,
                        "sea_level":1016,
                        "grnd_level":1005,
                        "humidity":95,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":55
                    },
                    "wind":{
                        "speed":3.12,
                        "deg":222,
                        "gust":7
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":1.49
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-03 00:00:00"
                },
                {
                    "dt":1712113200,
                    "main":{
                        "temp":284.78,
                        "feels_like":284.53,
                        "temp_min":284.78,
                        "temp_max":284.78,
                        "pressure":1017,
                        "sea_level":1017,
                        "grnd_level":1005,
                        "humidity":97,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":65
                    },
                    "wind":{
                        "speed":2.58,
                        "deg":219,
                        "gust":5.13
                    },
                    "visibility":8043,
                    "pop":1,
                    "rain":{
                        "3h":0.74
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-03 03:00:00"
                },
                {
                    "dt":1712124000,
                    "main":{
                        "temp":285.08,
                        "feels_like":284.86,
                        "temp_min":285.08,
                        "temp_max":285.08,
                        "pressure":1017,
                        "sea_level":1017,
                        "grnd_level":1005,
                        "humidity":97,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":78
                    },
                    "wind":{
                        "speed":2.53,
                        "deg":178,
                        "gust":4.46
                    },
                    "visibility":7317,
                    "pop":1,
                    "rain":{
                        "3h":0.55
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-03 06:00:00"
                },
                {
                    "dt":1712134800,
                    "main":{
                        "temp":286.52,
                        "feels_like":286.39,
                        "temp_min":286.52,
                        "temp_max":286.52,
                        "pressure":1019,
                        "sea_level":1019,
                        "grnd_level":1007,
                        "humidity":95,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":85
                    },
                    "wind":{
                        "speed":3.75,
                        "deg":167,
                        "gust":7.54
                    },
                    "visibility":8931,
                    "pop":1,
                    "rain":{
                        "3h":0.9
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-03 09:00:00"
                },
                {
                    "dt":1712145600,
                    "main":{
                        "temp":288.22,
                        "feels_like":288.11,
                        "temp_min":288.22,
                        "temp_max":288.22,
                        "pressure":1018,
                        "sea_level":1018,
                        "grnd_level":1007,
                        "humidity":89,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":90
                    },
                    "wind":{
                        "speed":5.99,
                        "deg":184,
                        "gust":9.26
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":0.9
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-03 12:00:00"
                },
                {
                    "dt":1712156400,
                    "main":{
                        "temp":289.56,
                        "feels_like":289.14,
                        "temp_min":289.56,
                        "temp_max":289.56,
                        "pressure":1018,
                        "sea_level":1018,
                        "grnd_level":1007,
                        "humidity":72,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":77
                    },
                    "wind":{
                        "speed":6,
                        "deg":203,
                        "gust":9.6
                    },
                    "visibility":10000,
                    "pop":0.23,
                    "rain":{
                        "3h":0.2
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-03 15:00:00"
                },
                {
                    "dt":1712167200,
                    "main":{
                        "temp":287.5,
                        "feels_like":287.26,
                        "temp_min":287.5,
                        "temp_max":287.5,
                        "pressure":1018,
                        "sea_level":1018,
                        "grnd_level":1007,
                        "humidity":87,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":803,
                            "main":"Clouds",
                            "description":"broken clouds",
                            "icon":"04d"
                        }
                    ],
                    "clouds":{
                        "all":80
                    },
                    "wind":{
                        "speed":3.94,
                        "deg":191,
                        "gust":9.71
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-03 18:00:00"
                },
                {
                    "dt":1712178000,
                    "main":{
                        "temp":285.56,
                        "feels_like":285.34,
                        "temp_min":285.56,
                        "temp_max":285.56,
                        "pressure":1019,
                        "sea_level":1019,
                        "grnd_level":1008,
                        "humidity":95,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":95
                    },
                    "wind":{
                        "speed":3.47,
                        "deg":158,
                        "gust":6.67
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-03 21:00:00"
                },
                {
                    "dt":1712188800,
                    "main":{
                        "temp":286.13,
                        "feels_like":285.91,
                        "temp_min":286.13,
                        "temp_max":286.13,
                        "pressure":1019,
                        "sea_level":1019,
                        "grnd_level":1007,
                        "humidity":93,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":97
                    },
                    "wind":{
                        "speed":3.65,
                        "deg":157,
                        "gust":8.25
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-04 00:00:00"
                },
                {
                    "dt":1712199600,
                    "main":{
                        "temp":286.12,
                        "feels_like":285.87,
                        "temp_min":286.12,
                        "temp_max":286.12,
                        "pressure":1017,
                        "sea_level":1017,
                        "grnd_level":1006,
                        "humidity":92,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":4.23,
                        "deg":169,
                        "gust":9.9
                    },
                    "visibility":10000,
                    "pop":0.39,
                    "rain":{
                        "3h":0.13
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-04 03:00:00"
                },
                {
                    "dt":1712210400,
                    "main":{
                        "temp":285.84,
                        "feels_like":285.49,
                        "temp_min":285.84,
                        "temp_max":285.84,
                        "pressure":1016,
                        "sea_level":1016,
                        "grnd_level":1005,
                        "humidity":89,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":3.12,
                        "deg":145,
                        "gust":8.21
                    },
                    "visibility":10000,
                    "pop":0.08,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-04 06:00:00"
                },
                {
                    "dt":1712221200,
                    "main":{
                        "temp":288.12,
                        "feels_like":287.6,
                        "temp_min":288.12,
                        "temp_max":288.12,
                        "pressure":1016,
                        "sea_level":1016,
                        "grnd_level":1005,
                        "humidity":74,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04d"
                        }
                    ],
                    "clouds":{
                        "all":95
                    },
                    "wind":{
                        "speed":3.24,
                        "deg":159,
                        "gust":7.4
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-04 09:00:00"
                },
                {
                    "dt":1712232000,
                    "main":{
                        "temp":290.36,
                        "feels_like":289.7,
                        "temp_min":290.36,
                        "temp_max":290.36,
                        "pressure":1015,
                        "sea_level":1015,
                        "grnd_level":1003,
                        "humidity":60,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04d"
                        }
                    ],
                    "clouds":{
                        "all":97
                    },
                    "wind":{
                        "speed":5.02,
                        "deg":189,
                        "gust":8.57
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-04 12:00:00"
                },
                {
                    "dt":1712242800,
                    "main":{
                        "temp":289.96,
                        "feels_like":289.37,
                        "temp_min":289.96,
                        "temp_max":289.96,
                        "pressure":1014,
                        "sea_level":1014,
                        "grnd_level":1002,
                        "humidity":64,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":4.9,
                        "deg":200,
                        "gust":10.29
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-04 15:00:00"
                },
                {
                    "dt":1712253600,
                    "main":{
                        "temp":287.87,
                        "feels_like":287.43,
                        "temp_min":287.87,
                        "temp_max":287.87,
                        "pressure":1012,
                        "sea_level":1012,
                        "grnd_level":1001,
                        "humidity":78,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":3.86,
                        "deg":172,
                        "gust":11.68
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-04 18:00:00"
                },
                {
                    "dt":1712264400,
                    "main":{
                        "temp":285.82,
                        "feels_like":285.21,
                        "temp_min":285.82,
                        "temp_max":285.82,
                        "pressure":1012,
                        "sea_level":1012,
                        "grnd_level":1000,
                        "humidity":79,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":4.1,
                        "deg":159,
                        "gust":9.21
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-04 21:00:00"
                },
                {
                    "dt":1712275200,
                    "main":{
                        "temp":285.93,
                        "feels_like":285.2,
                        "temp_min":285.93,
                        "temp_max":285.93,
                        "pressure":1010,
                        "sea_level":1010,
                        "grnd_level":999,
                        "humidity":74,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":4.44,
                        "deg":154,
                        "gust":12.37
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-05 00:00:00"
                },
                {
                    "dt":1712286000,
                    "main":{
                        "temp":288.04,
                        "feels_like":286.89,
                        "temp_min":288.04,
                        "temp_max":288.04,
                        "pressure":1008,
                        "sea_level":1008,
                        "grnd_level":997,
                        "humidity":50,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":6.26,
                        "deg":166,
                        "gust":14.88
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-05 03:00:00"
                },
                {
                    "dt":1712296800,
                    "main":{
                        "temp":288.34,
                        "feels_like":287.12,
                        "temp_min":288.34,
                        "temp_max":288.34,
                        "pressure":1006,
                        "sea_level":1006,
                        "grnd_level":995,
                        "humidity":46,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":5.89,
                        "deg":163,
                        "gust":15.08
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-05 06:00:00"
                },
                {
                    "dt":1712307600,
                    "main":{
                        "temp":287.08,
                        "feels_like":286.36,
                        "temp_min":287.08,
                        "temp_max":287.08,
                        "pressure":1007,
                        "sea_level":1007,
                        "grnd_level":996,
                        "humidity":70,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":7.53,
                        "deg":184,
                        "gust":16.48
                    },
                    "visibility":7938,
                    "pop":0.91,
                    "rain":{
                        "3h":0.63
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-05 09:00:00"
                },
                {
                    "dt":1712318400,
                    "main":{
                        "temp":287.21,
                        "feels_like":286.73,
                        "temp_min":287.21,
                        "temp_max":287.21,
                        "pressure":1006,
                        "sea_level":1006,
                        "grnd_level":994,
                        "humidity":79,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":6.64,
                        "deg":183,
                        "gust":15.16
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":1.51
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-05 12:00:00"
                },
                {
                    "dt":1712329200,
                    "main":{
                        "temp":288.52,
                        "feels_like":288.38,
                        "temp_min":288.52,
                        "temp_max":288.52,
                        "pressure":1003,
                        "sea_level":1003,
                        "grnd_level":992,
                        "humidity":87,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":5.97,
                        "deg":179,
                        "gust":17.12
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":2.62
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-05 15:00:00"
                },
                {
                    "dt":1712340000,
                    "main":{
                        "temp":289.98,
                        "feels_like":289.6,
                        "temp_min":289.98,
                        "temp_max":289.98,
                        "pressure":1000,
                        "sea_level":1000,
                        "grnd_level":989,
                        "humidity":72,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":6.7,
                        "deg":158,
                        "gust":16.12
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":0.62
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-05 18:00:00"
                },
                {
                    "dt":1712350800,
                    "main":{
                        "temp":292.15,
                        "feels_like":291.52,
                        "temp_min":292.15,
                        "temp_max":292.15,
                        "pressure":999,
                        "sea_level":999,
                        "grnd_level":988,
                        "humidity":54,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":804,
                            "main":"Clouds",
                            "description":"overcast clouds",
                            "icon":"04n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":9.19,
                        "deg":172,
                        "gust":19.6
                    },
                    "visibility":10000,
                    "pop":0,
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-05 21:00:00"
                },
                {
                    "dt":1712361600,
                    "main":{
                        "temp":288.28,
                        "feels_like":287.89,
                        "temp_min":288.28,
                        "temp_max":288.28,
                        "pressure":998,
                        "sea_level":998,
                        "grnd_level":987,
                        "humidity":78,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":10.47,
                        "deg":179,
                        "gust":20.64
                    },
                    "visibility":10000,
                    "pop":0.47,
                    "rain":{
                        "3h":0.53
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-06 00:00:00"
                },
                {
                    "dt":1712372400,
                    "main":{
                        "temp":284.93,
                        "feels_like":284.67,
                        "temp_min":284.93,
                        "temp_max":284.93,
                        "pressure":1001,
                        "sea_level":1001,
                        "grnd_level":990,
                        "humidity":96,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":501,
                            "main":"Rain",
                            "description":"moderate rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":7.81,
                        "deg":217,
                        "gust":12.85
                    },
                    "visibility":3776,
                    "pop":1,
                    "rain":{
                        "3h":10.52
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-06 03:00:00"
                },
                {
                    "dt":1712383200,
                    "main":{
                        "temp":284.08,
                        "feels_like":283.63,
                        "temp_min":284.08,
                        "temp_max":284.08,
                        "pressure":1005,
                        "sea_level":1005,
                        "grnd_level":994,
                        "humidity":92,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":501,
                            "main":"Rain",
                            "description":"moderate rain",
                            "icon":"10n"
                        }
                    ],
                    "clouds":{
                        "all":92
                    },
                    "wind":{
                        "speed":5.16,
                        "deg":185,
                        "gust":11.29
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":10.75
                    },
                    "sys":{
                        "pod":"n"
                    },
                    "dt_txt":"2024-04-06 06:00:00"
                },
                {
                    "dt":1712394000,
                    "main":{
                        "temp":286.16,
                        "feels_like":285.87,
                        "temp_min":286.16,
                        "temp_max":286.16,
                        "pressure":1008,
                        "sea_level":1008,
                        "grnd_level":997,
                        "humidity":90,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":87
                    },
                    "wind":{
                        "speed":7.25,
                        "deg":177,
                        "gust":12.24
                    },
                    "visibility":10000,
                    "pop":0.29,
                    "rain":{
                        "3h":0.27
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-06 09:00:00"
                },
                {
                    "dt":1712404800,
                    "main":{
                        "temp":286.31,
                        "feels_like":285.95,
                        "temp_min":286.31,
                        "temp_max":286.31,
                        "pressure":1010,
                        "sea_level":1010,
                        "grnd_level":998,
                        "humidity":87,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":93
                    },
                    "wind":{
                        "speed":7.29,
                        "deg":185,
                        "gust":12.92
                    },
                    "visibility":10000,
                    "pop":0.47,
                    "rain":{
                        "3h":0.24
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-06 12:00:00"
                },
                {
                    "dt":1712415600,
                    "main":{
                        "temp":287.72,
                        "feels_like":287.5,
                        "temp_min":287.72,
                        "temp_max":287.72,
                        "pressure":1010,
                        "sea_level":1010,
                        "grnd_level":999,
                        "humidity":87,
                        "temp_kf":0
                    },
                    "weather":[
                        {
                            "id":500,
                            "main":"Rain",
                            "description":"light rain",
                            "icon":"10d"
                        }
                    ],
                    "clouds":{
                        "all":100
                    },
                    "wind":{
                        "speed":4.62,
                        "deg":207,
                        "gust":6.82
                    },
                    "visibility":10000,
                    "pop":1,
                    "rain":{
                        "3h":1.56
                    },
                    "sys":{
                        "pod":"d"
                    },
                    "dt_txt":"2024-04-06 15:00:00"
                }
            ],
            "city":{
                "id":2742416,
                "name":"Barcelos",
                "coord":{
                    "lat":41.5388,
                    "lon":-8.6151
                },
                "country":"PT",
                "population":19085,
                "timezone":3600,
                "sunrise":1711952209,
                "sunset":1711997958
            }
        }
        
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

                sunrise = self.convertToMachineUTC(datetime.utcfromtimestamp(info["sys"]["sunrise"])
                                                   .strftime("%Y-%m-%d %H:%M:%S"))
                sunset  = self.convertToMachineUTC(datetime.utcfromtimestamp(info["sys"]["sunset"])
                                                   .strftime("%Y-%m-%d %H:%M:%S"))

                        #      "sys":{"type":2,              # Internal parameter
                        # "id":2021760,         # Internal parameter
                        # "country":"PT",       # Country code (GB, JP etc.)
                        # "sunrise":1711952209, # Sunrise time, unix, UTC
                        # "sunset":1711997958},

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

    def prettyPrint(self):
        printString = f"""
        City: {self.city}
        Temperature: {self.temperature}C
        Humidity: {self.humidity}%
"""
        print(printString)

