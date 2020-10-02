from flask import Flask, render_template
import platform
from modules.datemodule import greets, display_date_in_webapp
from modules.mathmodule import exponent, hypothenuse
from modules.utils import print_sep, play_with_lists, play_with_array, play_with_dictionaries
from modules.ioutils import writeinFile, viewfile
from modules.classmanipulator import play_with_classes, call_do_process

app = Flask(__name__)

system_info = ""


@app.route("/")
@app.route("/index.html")
@app.route("/statics/img/html")
def index():
    system_info = get_system_info()
    return render_template('index.html', system_info=system_info, logo="static/images/python-logo.png")


@app.route("/os")
def get_system_info():
    return f"{platform.system()} - {platform.platform()}"


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
