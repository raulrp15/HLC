from Portfolio.Routes import Ruta
from Portfolio.Views.Components.Components import bg_cursor
from Portfolio.Views.Home.Body.Home_Body import home_body
from Portfolio.Views.Home.Footer.Home_Footer import home_footer
from Portfolio.Views.Home.Header.Home_Header import home_header
from Portfolio.Views.NavBar.Navbar import navbar
import reflex as rx

rx.page(
    route=Ruta.INDEX.value,
    title="Home",
    description="sisi",
    meta=[
        {"name": "og:title", "content": "Home"},
        {"name": "og:description", "content": "sisi"}
    ]
)
def script() -> rx.Component:
    return rx.script(src="Portfolio/Scripts/my_script.js")


def index() -> rx.Component:
    return rx.vstack(
        script(),
        bg_cursor("white"),
        navbar(),
        home_header(),
        home_body(),
        home_footer(),
        background="purple",
        align="center",
        justify="center",
        height="100%",
    )