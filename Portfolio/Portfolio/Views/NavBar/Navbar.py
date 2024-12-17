import reflex as rx

from Portfolio.Views.Components.Components import navbar_link

class State(rx.State):
    value: bool = False

    @rx.event
    def toggle(self, value: bool):
        self.value = value

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.icon("menu", display={"base": "block", "md": "none"}),
            navbar_link("Home", "/"),
            navbar_link("Projects", "/projects"),
            navbar_link("Contact", "/contact"),
            navbar_link("Resume", "/resume"),
            navbar_link("About Me", "/about"),
            rx.switch(
                on_change=State.toggle,
                name="Change Theme",
                color_scheme="gray",
            ),
            bg="rgba(20, 20, 20, 0.5)",
            
        ),
    )