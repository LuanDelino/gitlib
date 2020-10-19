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

    request_raw = ""
    json = ""

    if language != None:
        url = "https://api.github.com/search/repositories?q=language:"+language+"&sort=stars&page=1"
        request_raw = requests.get(url)
        json = request_raw.json()

    return render_template("index.html", language=language, json=json)



if __name__ == "__main__":
    app.run()