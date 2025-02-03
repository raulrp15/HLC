import reflex as rx

from Ejercicio01.routes import ruta
from Ejercicio01.views.buscadores_view.body import body
from Ejercicio01.views.components.components import header

rx.page(
    route=ruta.BUSCADORES.value,
    title="Buscadores",
    description="sisi",
    meta=[
        {"name": "og:title", "content": "Buscadores"},
        {"name": "og:description", "content": "sisi"}
    ]
)

def buscadores() -> rx.Component:
    return rx.container(
        header("Buscadores"),
        body()
    )