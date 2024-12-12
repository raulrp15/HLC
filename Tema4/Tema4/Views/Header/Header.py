import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
            src="https://cdn-icons-png.flaticon.com/512/4792/4792929.png",
            size="7"
            ),
            rx.text("Raúl Romera"),
            align="center",
        ),
        rx.text("Aqui va la descripcion de este matao")
    )