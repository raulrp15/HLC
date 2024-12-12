import reflex as rx

from Tema4.Views.Contenido.Content import content_view
from Tema4.Views.Footer.Footer import footer

from .Views.Header.Header import header
from .Views.Navbar.NavBar import barra_navegacion
from rxconfig import config


class State(rx.State):

    ...

def index() -> rx.Component:
    return rx.vstack(
        barra_navegacion(),
        header(),
        content_view(),
        footer(),
        align="center",
        )
app = rx.App()
app.add_page(index)
app._compile()
