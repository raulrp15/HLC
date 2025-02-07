import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.heading("Formulario de registro", id="titulo"),
            rx.form(
                rx.hstack(
                    rx.text("Nombre:", id="lname"),
                    rx.input(placeholder="Ingrese su nombre", id="iname"),
                ),
                rx.hstack(
                    rx.text("Apellidos:", id="lsurname"),
                    rx.input(placeholder="Ingrese su apellido", id="isurname"),
                ),
            ),
        )
    )