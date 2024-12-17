import reflex as rx

def home_header() -> rx.Component:
    return rx.vstack(
        rx.text("Bienvenido a mi portfolio", size="3", weight="bold", color="white"),
    )