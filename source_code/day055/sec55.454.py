from flask import Flask


app = Flask(__name__)


def make_bold_decorator(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper
        


def make_emphasis_decorator(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underlined_decorator(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/")
@make_emphasis_decorator
@make_bold_decorator
@make_underlined_decorator
def root():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)