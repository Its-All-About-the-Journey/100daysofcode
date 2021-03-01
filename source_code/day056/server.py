from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def root():
    return render_template(("index.html"))


@app.route("/images.html")
def image():
    return render_template(("images.html"))


if __name__ == '__main__':
    app.run(debug=True)
