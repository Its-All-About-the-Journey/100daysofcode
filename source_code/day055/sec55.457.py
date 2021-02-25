import random

from flask import Flask

LOW = 0
HIGH = 9
answer = random.randint(LOW, HIGH)


app = Flask(__name__)


@app.route("/")
def root():
    return f"Guess a number between {LOW} and {HIGH}"


@app.route("/<int:number>")
def guess(number):
    if number < answer:
        return "Too low"
    
    elif number > answer:
        return "Too high"
    
    return "You got it!"


if __name__ == "__main__":
    app.run(debug=True)    

