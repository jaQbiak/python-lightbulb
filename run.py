import os

from dotenv import load_dotenv
from flask import Flask

from device import Device


load_dotenv()

DEVICE = Device(os.getenv("DEVICE_ID"), os.getenv("IP_ADDRESS"), os.getenv("LOCALE_KEY")).get_device()

application = Flask(__name__)


@application.route("/")
def turn_on():
    DEVICE.turn_on()
    return "Device turned on"


@application.route("/turn_off")
def turn_off():
    DEVICE.turn_off()
    return "Device turned off"


