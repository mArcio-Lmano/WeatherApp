import os
import tkinter as tk
from tkinter import ttk, PhotoImage
from weatherClass import WeatherApp


class WeatherGui:
    def __init__(self, api_key):
        self.api_key = api_key

        self.app_width = 400
        self.app_height = 200
        self.row = 0
        self.icons = []
        self.weather_window = None
        self.ligth_blue = "#9ea0ea"
        self.ligth_gray = "#d3d3d3"
        self.weather_window_count = 0

        self.createGui()

    def createGui(self):
        self.root = tk.Tk()
        self.root.configure(background=self.ligth_blue, highlightcolor=self.ligth_blue)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.root.title("Weather App")

        self.root.geometry(
            f"{self.app_width}x{self.app_height}+{self.screen_width-self.app_width}+{self.screen_height-self.app_height}"
        )

        s = ttk.Style()
        s.configure("TFrame", background=self.ligth_blue)
        s.configure(
            "TButton", background="white", font=("Helvetica", 9), relief="sunken"
        )

        self.srcoll_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        self.srcoll_frame.grid()

        self.frm = ttk.Frame(self.root, padding=10, style="TFrame")
        self.frm.grid()

        self.loadCities()

        ttk.Label(self.frm, text="Country/City", background=self.ligth_blue).grid(
            column=0, row=self.row, padx=(0, 5)
        )

        self.city_entry = ttk.Entry(self.frm)
        self.city_entry.insert(0, "PT/Braga")
        self.city_entry.grid(column=1, row=self.row, padx=(0, 5))

        retrieve_button = ttk.Button(
            self.frm, text="Retrieve", command=self.retrieveCity
        )
        retrieve_button.grid(column=2, row=self.row)

        self.row += 1

        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(
            column=3, row=self.row
        )
        self.root.mainloop()

    def loadCities(self):
        text = tk.Text(self.srcoll_frame, width=20, height=8)
        text.configure(cursor="arrow", background=self.ligth_gray)
        text.grid(row=0, column=0)

        sb = tk.Scrollbar(self.srcoll_frame, command=text.yview)
        sb.grid(row=0, column=0, sticky="nse")

        text.configure(yscrollcommand=sb.set)

        ttk.Label(
            self.srcoll_frame,
            text="Weather\nApp",
            background=self.ligth_blue,
            font="20pt",
            anchor="center",
        ).grid(column=2, row=0, padx=(20, 20))

        if os.path.exists("../cities.txt"):
            with open("../cities.txt", "r") as file:
                cities = file.read().split("\n")
                for city in cities:
                    if city == "":
                        continue
                    button = tk.Button(
                        text,
                        text=f"{city}",
                        command=lambda c=city: self.chooseCity(c),
                        background="white",
                    )
                    text.window_create("end", window=button)
                    text.insert("end", "\n")

        text.configure(state="disabled")

    def retrieveCity(self):
        city_variable = self.city_entry.get()
        if os.path.exists("../cities.txt"):
            with open("../cities.txt", "r") as file:
                cities = file.read().split("\n")
        else:
            cities = []

        if city_variable and city_variable not in cities:
            with open("../cities.txt", "a") as file:
                file.write(f"{city_variable}\n")
            self.restartGui()

    def chooseCity(self, location):
        country_code, city = location.split("/")
        weather = WeatherApp(apiKey=self.api_key, city=city, countryCode=country_code)
        self.showWeatherInfo(city, weather)

    def showWeatherInfo(self, city, weather):
        if self.weather_window is not None:
            self.weather_window.destroy()

        s = ttk.Style()
        s.configure("TFrame", background=self.ligth_blue)
        s.configure("TLabel", background=self.ligth_blue)

        self.weather_window = tk.Toplevel(self.root)
        self.weather_window.title(f"Weather Information - {city}")
        self.weather_window.configure(background=self.ligth_blue)

        weather_window_width = 400
        weather_window_height = 50
        self.weather_window.geometry(
            f"{weather_window_width}x{weather_window_height}"
            + f"+{self.screen_width-weather_window_width}"
            + f"+{self.screen_height-weather_window_height-200}"
        )

        weather_frame = ttk.Frame(self.weather_window, padding=10)
        weather_frame.grid()

        ttk.Label(weather_frame, text=city).grid(column=0, row=0)

        weather_now_btn = ttk.Button(
            weather_frame,
            text="Weather Now",
            command=lambda w=weather, c=city: self.getWeatherNow(w, c),
        )
        weather_now_btn.grid(column=0, row=1)
        weather_future_btn = ttk.Button(
            weather_frame,
            text="Weather Forecast",
            command=lambda w=weather, c=city: self.getWeatherFor5Days(w, c),
        )
        weather_future_btn.grid(column=1, row=1)

        ttk.Button(
            weather_frame, text="Close", command=self.weather_window.destroy
        ).grid(column=3, row=1)

    def getWeatherNow(self, weather, city):
        weather.getWeatherToday()

        weather_window = tk.Toplevel(self.root)
        weather_window.title(f"Weather Information - {city}")
        weather_window.configure(background=self.ligth_blue)

        weather_window_width = 400
        weather_window_height = 300
        weather_window.geometry(
            f"{weather_window_width}x{weather_window_height}"
            + f"+{self.screen_width-weather_window_width - self.weather_window_count}"
            + f"+{self.screen_height-weather_window_height-250}"
        )

        weather_frame = ttk.Frame(weather_window, padding=10)
        weather_frame.grid()
        self.weather_window_count += weather_window_width

        s = ttk.Style()
        s.configure("TFrame", background=self.ligth_blue)
        s.configure("TLabel", background=self.ligth_blue)

        weather_info = (
            weather.temperatures[0] if len(weather.temperatures) > 0 else None
        )

        if weather_info is None:
            ttk.Label(
                weather_frame, text=f"{city} Not Found", font=("Helviga", 20)
            ).grid(column=0, row=0)
            ttk.Button(
                weather_frame,
                text="Close",
                command=lambda w=weather_window, width=weather_window_width: self.destroyWeeatherWindow(
                    w, width
                ),
            ).grid(column=3, row=100)
        else:
            date = weather_info["date"].strftime("%m/%d/%Y, %H:%M:%S")
            max_temperature = weather_info["max_temperature"]
            min_temperature = weather_info["min_temperature"]
            humidity = weather_info["humidity"]
            weather_type = weather_info["weather"]
            weather_description = weather_info["weather_description"].capitalize()
            weather_icon = weather_info["weather_icon"]
            clouds = weather_info["clouds"]
            wind_speed = weather_info["wind_speed"]
            wind_deg = weather_info["wind_deg"]
            sunrise = weather_info["sunrise"].strftime("%m/%d/%Y, %H:%M:%S")
            sunset = weather_info["sunset"].strftime("%m/%d/%Y, %H:%M:%S")

            # Load the icon image
            icon_path = "../icons/" + weather_icon
            # self.icon = PhotoImage(file=icon_path)
            self.icons += [PhotoImage(file=icon_path)]

            row = 0
            ttk.Label(weather_frame, text=city, font=("Helviga", 12)).grid(
                column=0, row=row
            )
            icon_label = ttk.Label(weather_frame, image=self.icons[-1])
            icon_label.grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Date").grid(column=0, row=row)
            ttk.Label(weather_frame, text=date).grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Max Temperature").grid(column=0, row=row)
            ttk.Label(weather_frame, text=f"{max_temperature} \N{DEGREE SIGN}C").grid(
                column=1, row=row
            )
            row += 1

            ttk.Label(weather_frame, text="Min Temperature").grid(column=0, row=row)
            ttk.Label(weather_frame, text=f"{min_temperature} \N{DEGREE SIGN}C").grid(
                column=1, row=row
            )
            row += 1

            ttk.Label(weather_frame, text="Humidity").grid(column=0, row=row)
            ttk.Label(weather_frame, text=f"{humidity}%").grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Weather").grid(column=0, row=row)
            ttk.Label(
                weather_frame, text=f"{weather_type}: {weather_description}"
            ).grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Cloudiness").grid(column=0, row=row)
            ttk.Label(weather_frame, text=f"{clouds}%").grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Wind").grid(column=0, row=row)
            ttk.Label(
                weather_frame,
                text=f"Speed: {wind_speed}m/s, Direction: {wind_deg}\N{DEGREE SIGN}",
            ).grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Sunrise").grid(column=0, row=row)
            ttk.Label(weather_frame, text=sunrise).grid(column=1, row=row)
            row += 1

            ttk.Label(weather_frame, text="Sunset").grid(column=0, row=row)
            ttk.Label(weather_frame, text=sunset).grid(column=1, row=row)
            row += 1

            ttk.Button(
                weather_frame,
                text="Close",
                command=lambda w=weather_window, width=weather_window_width: self.destroyWeeatherWindow(
                    w, width
                ),
            ).grid(column=3, row=100)

    def getWeatherFor5Days(self, weather, city):
        weather.getWeather5Days()

        weather_window = tk.Toplevel(self.root)
        weather_window.title(f"Weather Information - {city}")
        weather_window.configure(background=self.ligth_blue)

        weather_window_width = 400
        weather_window_height = 80
        weather_window.geometry(
            f"{weather_window_width}x{weather_window_height}"
            + f"+{self.screen_width-weather_window_width }"
            + f"+{self.screen_height-weather_window_height-250}"
        )

        days = {}
        for day in weather.temperatures:
            date = day["date"].date()
            days[date] = {}

        for i in range(len(weather.temperatures)):
            day = weather.temperatures[i]
            date = day["date"].date()

            hour = day["date"].time()
            days[date][hour] = {}

            days[date][hour] = {
                "min_temperature": day["min_temperature"],
                "max_temperature": day["max_temperature"],
                "humidity": day["humidity"],
                "weather": day["weather"],
                "weather_description": day["weather_description"],
                "weather_icon": day["weather_icon"],
                "clouds": day["clouds"],
                "wind_speed": day["wind_speed"],
                "wind_deg": day["wind_deg"],
            }

        srcoll_frame = ttk.Frame(weather_window, padding=10, style="TFrame")
        srcoll_frame.grid()

        text = tk.Text(srcoll_frame, width=20, height=4)
        text.configure(cursor="arrow", background=self.ligth_gray)
        text.grid(row=0, column=1)

        sb = tk.Scrollbar(srcoll_frame, command=text.yview)
        sb.grid(row=0, column=2, sticky="nse")

        text.configure(yscrollcommand=sb.set)

        ttk.Label(
            srcoll_frame,
            text="Select a Day",
            background=self.ligth_blue,
            font="20pt",
            anchor="center",
        ).grid(column=0, row=0, padx=(20, 20))

        for day in days:
            # weatherOneDay(self, day, date, city):
            button = tk.Button(
                text,
                text=f"{day}",
                command=lambda d=days[day], da=day, c=city: self.weatherOneDay(
                    d, da, c
                ),
                background="white",
            )
            text.window_create("end", window=button)
            text.insert("end", "\n")

        text.configure(state="disabled")

        ttk.Button(srcoll_frame, text="Close", command=weather_window.destroy).grid(
            column=3, row=0, padx=(10, 0)
        )

    def weatherOneDay(self, day, date, city):
        s = ttk.Style()
        s.configure("TFrame", background=self.ligth_blue)
        s.configure("TLabel", background=self.ligth_blue)

        weather_window = tk.Toplevel(self.root)
        weather_window.title(f"Weather Information - {city}")
        weather_window.configure(background=self.ligth_blue)

        weather_window_width = 1800
        weather_window_height = 400
        weather_window.geometry(
            f"{weather_window_width}x{weather_window_height}"
            + f"+{self.screen_width-weather_window_width}"
            + f"+{self.screen_height-weather_window_height-330}"
        )

        if not day:
            ttk.Label(
                weather_window, text=f"{city} Not Found", font=("Helvetica", 20)
            ).grid(row=0, column=0)
            ttk.Button(
                weather_window, text="Close", command=weather_window.destroy
            ).grid(row=100, column=100)
            return

        ttk.Label(weather_window, text=city, font=("Helvetica", 12)).grid(
            row=0, column=0
        )

        column_index = 0
        row_index = 1
        for hour, info in day.items():
            frame = ttk.Frame(weather_window, padding=10)
            frame.grid(
                row=row_index, column=column_index, pady=10, padx=10, sticky="nsew"
            )

            max_temperature = info["max_temperature"]
            min_temperature = info["min_temperature"]
            humidity = info["humidity"]
            weather_type = info["weather"]
            weather_description = info["weather_description"].capitalize()
            weather_icon = info["weather_icon"]
            clouds = info["clouds"]
            wind_speed = info["wind_speed"]
            wind_deg = info["wind_deg"]

            icon_path = "../icons/" + weather_icon
            self.icons += [PhotoImage(file=icon_path)]

            ttk.Label(frame, image=self.icons[-1]).grid(
                column=0, row=0, rowspan=8, padx=10
            )

            ttk.Label(frame, text="Date").grid(column=1, row=0)
            ttk.Label(frame, text=date).grid(column=2, row=0)

            ttk.Label(frame, text="Hour").grid(column=1, row=1)
            ttk.Label(frame, text=hour).grid(column=2, row=1)

            ttk.Label(frame, text="Max Temperature").grid(column=1, row=2)
            ttk.Label(frame, text=f"{max_temperature} \N{DEGREE SIGN}C").grid(
                column=2, row=2
            )

            ttk.Label(frame, text="Min Temperature").grid(column=1, row=3)
            ttk.Label(frame, text=f"{min_temperature} \N{DEGREE SIGN}C").grid(
                column=2, row=3
            )

            ttk.Label(frame, text="Humidity").grid(column=1, row=4)
            ttk.Label(frame, text=f"{humidity}%").grid(column=2, row=4)

            ttk.Label(frame, text="Weather").grid(column=1, row=5)
            ttk.Label(frame, text=f"{weather_type}: {weather_description}").grid(
                column=2, row=5
            )

            ttk.Label(frame, text="Cloudiness").grid(column=1, row=6)
            ttk.Label(frame, text=f"{clouds}%").grid(column=2, row=6)

            ttk.Label(frame, text="Wind").grid(column=1, row=7)
            ttk.Label(
                frame,
                text=f"Speed: {wind_speed}m/s, Direction: {wind_deg}\N{DEGREE SIGN}",
            ).grid(column=2, row=7)

            column_index += 1
            if column_index == 4:
                column_index = 0
                row_index += 1

        frame = ttk.Frame(weather_window, padding=10)
        frame.grid(row=row_index + 1, column=0, pady=10, padx=10, sticky="nsew")
        ttk.Button(frame, text="Close", command=weather_window.destroy).grid(
            column=2, row=8
        )

    def destroyWeeatherWindow(self, weather_window, window_width):
        weather_window.destroy()
        self.weather_window_count -= window_width

    def restartGui(self):
        self.root.destroy()
        self.weather_window = None
        self.createGui()
