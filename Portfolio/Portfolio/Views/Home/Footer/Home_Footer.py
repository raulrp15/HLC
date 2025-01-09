import reflex as rx

def home_footer() -> rx.Component:
    return rx.vstack(
        rx.text("Visita mis redes sociales", size="3", font_family="Sono", color="white"),
        rx.hstack(
            rx.icon("github", color=rx.color("purple", 12), size=35,),
            rx.icon("twitter", color=rx.color("purple", 12), size=35),
            rx.icon("linkedin", color=rx.color("purple", 12), size=35),
            rx.icon("dribbble", color=rx.color("purple", 12), size=35),
        ),
        align="center",
    )