import reflex as rx

from Portfolio.Views.NavBar.Navbar import State
from Portfolio.Views.Styles.Styles import size

def home_footer() -> rx.Component:
    return rx.vstack(
        rx.text("Visita mis redes sociales", size=size.MEDIUM.value, font_family="Sono", color=State.text_color),
        rx.hstack(
            rx.link(
                rx.icon(
                    "github",
                    color=rx.color("purple", 12),
                    size=35),
                    href="https://github.com/raulrp15", is_external=True),
            rx.link(
                rx.icon(
                    "twitter",
                    color=rx.color("purple", 12),
                    size=35),
                    href="https://x.com/el_trajeado", is_external=True),
                    rx.link(
                rx.icon(
                    "twitter",
                    color=rx.color("purple", 12),
                    size=35),
                    href="https://x.com/el_trajeado", is_external=True),
            rx.icon("linkedin", color=rx.color("purple", 12), size=35),
            rx.icon("dribbble", color=rx.color("purple", 12), size=35),
        ),
        align="center",
    )