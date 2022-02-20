from tkinter import Button, colorchooser, Scale
from tkinter.constants import HORIZONTAL
from dotenv import load_dotenv

import tinytuya
import tkinter
import math
import os


load_dotenv()


def connect_to_device():
    device_id = os.getenv('DEVICE_ID')
    ip_address = os.getenv('IP_ADDRESS')
    locale_key = os.getenv('LOCALE_KEY')
    device = tinytuya.BulbDevice(device_id, ip_address, locale_key)
    device.set_version(3.3)
    return device


def get_color():
    device = connect_to_device()
    device.status()


def change_color(red, green, blue):
    device = connect_to_device()
    device.set_colour(red, green, blue)


def choose_color():
    color = colorchooser.askcolor()
    red = math.floor(color[0][0])
    green = math.floor(color[0][1])
    blue = math.floor(color[0][2])
    change_color(red, green, blue)


def white():
    device = connect_to_device()
    device.set_white(255, 255)


def change_brightness():
    device = connect_to_device()
    device.set_brightness(brightness_slider.get())


def turn_on():
    device = connect_to_device()
    device.turn_on()   


def turn_off():
    device = connect_to_device()
    device.turn_off()   


root = tkinter.Tk()
root.geometry('200x200')
Button(root, text="Choose color", command=choose_color).pack()
Button(root, text="White", command=white).pack()
brightness_slider = Scale(root, from_=25, to=255, orient=HORIZONTAL)
brightness_slider.pack()
Button(root, text="Change brightness", command=change_brightness).pack()
Button(root, text="On", command=turn_on).pack()
Button(root, text="Off", command=turn_off).pack()
root.mainloop()
    