from flask import Flask, render_template
import requests


response = requests.get("https://api.npoint.io/f64e88a13a4b081fea8d")

if response.status_code != 200:
    print("Could not retrieve data, exiting")
    exit()

posts = response.json()


app = Flask(__name__)


@app.route('/')
def home():    
    return render_template("index.html", posts=posts)


@app.route("/blog/<int:index>")
def get_post(index):
    if index >= len(posts):
        return "Error rendering page"

    return render_template("post.html", title=posts[index]["title"], body=posts[index]["body"])


if __name__ == "__main__":
    app.run(debug=True)
