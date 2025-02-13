import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.heading("Formulario de registro - Mi Web", id="titulo"),
            rx.form(
                rx.hstack(
                    rx.text("Nombre:", id="lname"),
                    rx.input(placeholder="Ingrese su nombre", id="iname", type="text"),
                ),
                rx.hstack(
                    rx.text("Apellidos:", id="lsurname"),
                    rx.input(placeholder="Ingrese su apellido", id="isurname", type="text"),
                ),
                rx.radio_group(
                        [
                            "Hombre",
                            "Mujer",
                        ],
                        name="radio_choice",
                        direction="row",
                    ),
                rx.hstack(
                    rx.text("Email:", id="lemail"),
                    rx.input(placeholder="Ingrese su email", id="iemail", type="text"),
                ),
                rx.checkbox(
                    "Deseo recibir información sobre novedades y ofertas.",
                    checked=True,
                    id="icheck",
                ),
                rx.checkbox(
                    "Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre protección de datos",
                    id="icheck2",
                )
            ),
        )
    )