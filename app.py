from flask import Flask, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():

    language = ""
    if request.method == 'POST':
        language = request.form.get("search")
    else:
        language = request.args.get("search")

    if language.lower() == "c#":
        language = "Csharp"

    request_raw = ""
    json = ""

    if language != None:
        url = "https://api.github.com/search/repositories?q=language:"+language+"&sort=stars&page=1"
        request_raw = requests.get(url)
        
        if request_raw.status_code != 200:
            return render_template("error.html")
        
        json = request_raw.json()
        
        color = ""
        url_color = "https://raw.githubusercontent.com/ozh/github-colors/master/colors.json"
        json_color_raw = requests.get(url_color)
        json_color = json_color_raw.json()

        for i,k in json_color.items():
            if i.lower() == language.lower():
                color=k['color']
        
    return render_template("index.html", language=language, json=json, color=color)

if __name__ == "__main__":
    app.run()