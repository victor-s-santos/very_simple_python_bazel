from flask import Flask
from random import randint

from projects.calculator.calculator import Calculator

app = Flask(__name__)
my_calc = Calculator()

@app.route('/')
def hello_world():
    n1 = randint(0, 100)
    n2 = randint(-100, 0)
    message = f"Bingo!: {n1} + {n2} == {my_calc.add(n1, n2)}"
    return message


if __name__ == "__main__":
    print("It works!")
    app.run()