import os
from gui import WeatherGui

def main():
    if not os.path.exists("api.key"):
        print("Create an api key and put it inside a file called 'api.key'")
        
    with open("api.key", "r") as file:
        api_key = file.read()
        
    WeatherGui(api_key)

if __name__ == "__main__":
    main()
