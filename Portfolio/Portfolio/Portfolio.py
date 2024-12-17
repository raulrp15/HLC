"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from Portfolio.Views.Home.Header.Home_Header import home_header
from Portfolio.Views.NavBar.Navbar import navbar
import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    ...


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        home_header(),
        background="radial-gradient(at -20% -20%, white 10px, #1e0022 50%)",
        align="center",
        justify="center",
    )


app = rx.App()
app.add_page(index)
