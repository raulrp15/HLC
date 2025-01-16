import reflex as rx
from Portfolio.Views.NavBar.Navbar import State
from Portfolio.Views.Styles.Styles import size

def home_header() -> rx.Component:
    return rx.vstack(
        rx.image(src="Portfolio/Images/fotillo.png", width="100", height="100"),
        rx.text("Raul Romera Pavón", size=size.LARGE.value, weight="bold", color=State.text_color, font_family="Sono", as_="div"),
    )