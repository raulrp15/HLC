"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from Portfolio.Views.Home.Body.Home_Body import home_body
from Portfolio.Views.Home.Footer.Home_Footer import home_footer
from Portfolio.Views.Home.Header.Home_Header import home_header
from Portfolio.Views.NavBar.Navbar import navbar
import reflex as rx

from rxconfig import config



def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        home_header(),
        home_body(),
        home_footer(),
        background="radial-gradient(at -20% -20%, white 10px, #1e0022 50%)",
        align="center",
        justify="center",
        height="100%",
    )


app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Sono:wght@200..800&display=swap"]
)
app.add_page(index)
