import os
import requests
from bs4 import BeautifulSoup


def download_icon(icon_name, icon_url):
    r = requests.get(icon_url)
    if r.status_code == 200:
        with open(f"icons/{icon_name}", "wb") as f:
            f.write(r.content)
        print(f"Icon '{icon_name}' downloaded successfully.")
    else:
        print(f"Failed to download icon '{icon_name}'.")


def main():
    url = "https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2"
    r = requests.get(url=url)
    if r.status_code != 200:
        print("Some problem occurred retrieving the link information.")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    possibleIcons = soup.find_all("td")
    icons = {}

    if not os.path.exists(os.path.join(os.getcwd(), "icons")):
        os.makedirs(os.path.join(os.getcwd(), "icons"))

    for possibleIcon in possibleIcons:
        iconImg = possibleIcon.find("img", class_="icon-img")
        if iconImg:
            iconName = possibleIcon.text.strip()
            icons[iconName] = iconImg["src"]

    for icon in icons:
        download_icon(icon_name=icon, icon_url=icons[icon])

    return 0


if __name__ == "__main__":
    main()

