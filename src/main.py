from flask import Flask
import platform
from modules.datemodule import greets, display_date_in_webapp
from modules.mathmodule import exponent, hypothenuse
from modules.utils import print_sep, play_with_lists, play_with_array, play_with_dictionaries
from modules.ioutils import writeinFile, viewfile
from modules.classmanipulator import play_with_classes, call_do_process

app = Flask(__name__)


@app.route("/")
def index():
    return """
           <br/><a href='/os'>/os</a>
           <br/><a href='/greets'>/greets</a>
           <br/><a href='/hypothenuse/5/3'>/hypothenuse/5/3</a>
           """


@app.route("/os")
def get_system_info():
    return f"os.name : <b>{platform.system()} - {platform.platform()}</b>"


@app.route("/greets")
def display_greets():
    return f"today we are <b>{display_date_in_webapp()}</b>"


@app.route("/hypothenuse/<int:a>/<int:b>")
def calculate_hypothenuse(a, b):
    return f"hypothenuse of [{a}, {b}] is <b>{hypothenuse(a, b)}</b>"


if __name__ == '__main__':
    app.run()

greets()

a = 5
b = 2

print(f"{a} exponent {b} equals {exponent(a, b)}")
print(f"hypothenuse [{a}, {b}] is {hypothenuse(a, b)}")

print_sep()

a = 3
b = 3
exponent(a, b)
print(f"{a} exponent {b} equals {exponent(a, b)}")

print_sep()

play_with_array()

print_sep()

play_with_lists()

print_sep()

play_with_dictionaries()

print_sep()

writeinFile("gap.txt")

viewfile("gap.txt")

play_with_classes()
