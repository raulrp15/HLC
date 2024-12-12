import datetime
import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.icon("hand-metal"),
        rx.text(datetime.date.today().year),
        rx.link("Made with ❤️ by Raul Romera", href="https://github.com/raulrp15")
    )