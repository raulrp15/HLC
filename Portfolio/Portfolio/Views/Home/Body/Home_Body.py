import reflex as rx

def home_body() -> rx.Component:
    return rx.vstack(
        rx.text("", size="3", weight="bold", color="white"),
    )