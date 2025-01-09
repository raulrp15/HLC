import reflex as rx

def home_header() -> rx.Component:
    return rx.vstack(
        rx.text("Bienvenido a mi portfolio", size="9", weight="bold", color="white", font_family="Sono", as_="div"),
    )