import requests

l = "python"
url_color = "https://raw.githubusercontent.com/ozh/github-colors/master/colors.json"
json_color_raw = requests.get(url_color)
json_color = json_color_raw.json()

for i,k in json_color.items():
    if i.lower() == l.lower():
        print(k['color'])