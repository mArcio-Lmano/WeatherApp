import os

from tkinter import *
from tkinter import ttk
from weatherClass import WeatherApp

class WeatherGui:
    def __init__(self):
        self.create_gui()

    def restart_gui(self):
        self.root.destroy()  # Destroy the current GUI window
        self.create_gui()    # Recreate the GUI window

    def create_gui(self):
        self.root = Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        app_width = 400
        app_height = 200

        self.root.title("Weather App")
        self.root.geometry(f"{app_width}x{app_height}+{screen_width-400}+{screen_height-200}")

        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        if os.path.exists(os.path.join(os.getcwd(), "cities.txt")):
            with open("cities.txt", "r") as file:
                cities = file.read()

        self.row = 0
        if cities != "":
            cities = cities.split("\n")
            for city in cities:
                ttk.Button(self.frm, text=f"{city}").grid(column=0, row=self.row)
                self.row+=1

        ttk.Label(self.frm, text="Add City: ").grid(column=0, row=self.row)
        self.city_entry = ttk.Entry(self.frm)
        self.city_entry.grid(column=1, row=self.row)

        retrieve_button = ttk.Button(self.frm, text="Retrieve", command=self.retrieve_city)
        retrieve_button.grid(column=2, row=self.row)

        self.row+=1

        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=3, row=self.row)
        self.root.mainloop()

    def retrieve_city(self):
        city_variable = self.city_entry.get()
        with open("cities.txt", "a") as file:
            file.write(f"\n{city_variable}")
        self.restart_gui()

WeatherGui()