from dotenv import load_dotenv
import flet as ft
from flet import Switch, IconButton
from flet.icons import LIGHTBULB, LIGHTBULB_OUTLINE

from device import Device


load_dotenv()

DEVICE = Device(
    device_id="ID OF YOUR DEVICE",
    ip_address="IP OF YOUR DEVICE",
    locale_key="LOCALE KEY OF YOUR DEVICE",
).get_device()

def main(page: ft.Page):
    page.title = "Smart light"
    page.vertical_alignment = "center"
    page.window_width = 250
    page.window_height = 200

    def turn_on():
        DEVICE.turn_on()
        page.update()

    def turn_off():
        DEVICE.turn_off()
        page.update()

    def get_status():
        return DEVICE.status()["dps"]["1"]

    def normal(e):
        DEVICE.set_white(brightness=255, colourtemp=255)
        page.update()

    def white(e):
        DEVICE.set_hsv(h=0.5, s=0, v=1)
        page.update()

    def red(e):
        DEVICE.set_colour(r=255, g=0, b=0)
        page.update()

    def green(e):
        DEVICE.set_colour(r=0, g=255, b=0)
        page.update()

    def blue(e):
        DEVICE.set_colour(r=0, g=0, b=255)
        page.update()

    buttons = [
        IconButton(icon=LIGHTBULB, style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=white),
        IconButton(icon=LIGHTBULB, style=ft.ButtonStyle(color=ft.colors.YELLOW), on_click=normal),
        IconButton(icon=LIGHTBULB, style=ft.ButtonStyle(color=ft.colors.RED), on_click=red),
        IconButton(icon=LIGHTBULB, style=ft.ButtonStyle(color=ft.colors.GREEN), on_click=green),
        IconButton(icon=LIGHTBULB, style=ft.ButtonStyle(color=ft.colors.BLUE), on_click=blue),
    ]

    def switch(e):
        if get_status():
            turn_off()
            for button in buttons:
                button.disabled = True
                button.icon = LIGHTBULB_OUTLINE
        else:
            turn_on()
            for button in buttons:
                button.disabled = False
                button.icon = LIGHTBULB
            page.update()
        page.update()

    if get_status():
        switch = Switch(label="Turn on/off", value=True, on_change=switch)
        for button in buttons:
            button.disabled = False
            button.icon = LIGHTBULB
    else:
        switch = Switch(label="Turn on/off", value=False, on_change=switch)
        for button in buttons:
            button.disabled = True
            button.icon = LIGHTBULB_OUTLINE

    page.add(
        ft.Row(
            [
                switch
            ],
            alignment="center",
        )
    )
    page.add(
        ft.Row(
            buttons,
            alignment="center",
        )
    )

ft.app(target=main)
