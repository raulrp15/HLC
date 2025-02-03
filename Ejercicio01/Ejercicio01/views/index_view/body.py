import reflex as rx
from Ejercicio01.routes import ruta
from Ejercicio01.views.components.components import link_list_item

def body() -> rx.Component:
    return rx.vstack(
        rx.unordered_list(
            link_list_item("Buscadores", ruta.BUSCADORES.value, False),
            link_list_item("Redes Sociales", ruta.RRSS.value, False),
        )
    )