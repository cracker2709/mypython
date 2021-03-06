import datetime
import time

from flask import Flask, render_template
import platform
import os
from modules.datemodule import greets, display_date_in_webapp, display_date_from_timestamp
from modules.mathmodule import exponent, hypothenuse
from modules.utils import print_sep, play_with_lists, play_with_array, play_with_dictionaries
from modules.ioutils import writeinFile, viewfile
from modules.classmanipulator import play_with_classes, call_do_process
from modules.mongoutils import get_movies_json, get_movies_html, get_nb_movies
from ansible_vault import Vault

import json

from src.objects.my_vault import MyVault

app = Flask(__name__)

system_info = ""


@app.route("/")
@app.route("/index.html")
@app.route("/statics/img/html")
def index():
    system_info = f"{platform.system()} - {platform.platform()}"
    return render_template('index.html', system_info=system_info, logo="static/images/python-logo.png",
                           wallpaper="static/images/wallpaper.jpg")


@app.route("/os")
def get_system_info():
    sys_infos = {"uname" : platform.uname(),
                 "system" : platform.system(),
                 "node" : platform.node(),
                 "release" : platform.release(),
                 "machine" : platform.machine(),
                 "processor": platform.processor()}
    # Serializing json
    sys_json_object = json.dumps(sys_infos, indent = 4)
    return sys_json_object


@app.route("/greets")
def display_greets():
    return f"today we are <b>{display_date_in_webapp()}</b>"

@app.route("/vault")
def display_vault():
    my_vault = MyVault()
    return my_vault.load_raw(file="foo.yml")


@app.route("/hypothenuse/<int:a>/<int:b>")
def calculate_hypothenuse(a, b):
    return f"hypothenuse of [{a}, {b}] is <b>{hypothenuse(a, b)}</b>"

@app.route("/mongojson")
def mongo_movies_json():
    return get_movies_json()

@app.route("/mongohtml")
def mongo_movies_html():
    return render_template('mongo.html',
                           nb_movies=get_nb_movies(),
                           movies=get_movies_html(),
                           logo="static/images/python-logo.png",
                           mongo="static/images/mongodb.png",
                           wallpaper="static/images/wallpaper.jpg")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

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

val=1610526618487

calc=val/1000

ts = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(ts)


