import reflex as rx

from Portfolio.Views.NavBar.Navbar import State
from Portfolio.Views.Styles.Styles import size

def home_body() -> rx.Component:
    return rx.vstack(
        rx.text("", size=size.SMALL.value, weight="bold", color=State.text_color, font_family="Sono", as_="div"),
    )