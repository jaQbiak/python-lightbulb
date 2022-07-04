import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for, render_template

from device import Device


load_dotenv()

DEVICE = Device(os.getenv("DEVICE_ID"), os.getenv("IP_ADDRESS"), os.getenv("LOCALE_KEY")).get_device()

application = Flask(__name__)


@application.route("/")
def status():
    turned = DEVICE.status()["dps"]["1"]
    return render_template("index.html", turned=turned)


@application.route("/turn_on")
def turn_on():
    DEVICE.turn_on()
    return redirect(url_for('status'))


@application.route("/turn_off")
def turn_off():
    DEVICE.turn_off()
    return redirect(url_for('status'))


@application.route("/normal")
def normal():
    DEVICE.set_white(brightness=255, colourtemp=255)
    return redirect(url_for('status'))


@application.route("/white")
def white():
    DEVICE.set_hsv(h=0.5, s=0, v=1)
    return redirect(url_for('status'))


@application.route("/change_color/<red>/<green>/<blue>")
def change_color(red: str, green: str, blue: str):
    DEVICE.set_colour(r=int(red), g=int(green), b=int(blue))
    return redirect(url_for('status'))


