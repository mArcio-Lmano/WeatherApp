import os
from gui import WeatherGui


def main():
    api_key_path = "../api.key"
    if not os.path.exists(api_key_path):
        print("Create an api key and put it inside a file called 'api.key'")

    with open(api_key_path, "r") as file:
        api_key = file.read()

    WeatherGui(api_key)


if __name__ == "__main__":
    main()
