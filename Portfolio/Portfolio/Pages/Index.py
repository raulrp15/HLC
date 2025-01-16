from Portfolio.Routes import Ruta
from Portfolio.Views.Home.Body.Home_Body import home_body
from Portfolio.Views.Home.Footer.Home_Footer import home_footer
from Portfolio.Views.Home.Header.Home_Header import home_header
from Portfolio.Views.NavBar.Navbar import navbar
import reflex as rx

rx.page(
    route=Ruta.INDEX,
    title="Home",
    description="sisi",
    meta=[
        {"name": "og:title", "content": "Home"},
        {"name": "og:description", "content": "sisi"}
    ]
)

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