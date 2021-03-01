import datetime
import random


from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def root():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", number=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(f"https://api.genderize.io?name={name}")
    age = requests.get(f"https://api.agify.io?name={name}")

    if gender.status_code != 200 or age.status_code != 200:
        return "Error rendering page"

    year = datetime.datetime.now().year
    return render_template("index.html", age=age.json()["age"], gender=gender.json()["gender"], year=year)

if __name__ == '__main__':
    app.run(debug=True)
