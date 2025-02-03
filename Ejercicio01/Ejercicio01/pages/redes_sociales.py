import reflex as rx

from Ejercicio01.routes import ruta
from Ejercicio01.views.components.components import header
from Ejercicio01.views.rrss_view.body import body

rx.page(
    route=ruta.RRSS.value,
    title="Redes_Sociales",
    description="sisi",
    meta=[
        {"name": "og:title", "content": "Buscadores"},
        {"name": "og:description", "content": "sisi"}
    ]
)

def redes_sociales() -> rx.Component:
    return rx.container(
        header("Redes Sociales"),
        body()
    )