import reflex as rx

def barra_navegacion() -> rx.Component:
    return rx.hstack(
        rx.link("Home", href="#", size="7", text_decoration="none", color="white"),
        rx.link("About", href="#", size="7", text_decoration="none", color="white"),
        position="sticky",
        align="center",
    )