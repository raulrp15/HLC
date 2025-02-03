import reflex as rx

from Ejercicio01.routes import ruta
from Ejercicio01.views.components.components import header
from Ejercicio01.views.index_view.body import body

rx.page(
    route=ruta.INDEX.value,
    title="Home",
    description="sisi",
    meta=[
        {"name": "og:title", "content": "Home"},
        {"name": "og:description", "content": "sisi"}
    ]
)

def index() -> rx.Component:
    return rx.container(
            header("Enlaces Favoritos"),
            body(),
    )