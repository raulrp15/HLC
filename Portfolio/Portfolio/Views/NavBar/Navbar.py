import reflex as rx

from Portfolio.Views.Components.Components import navbar_link

class State(rx.State):
    value: bool = False
    rgba_val: str = "#1e0022"
    text_color = "white"
    card_color = "rgba(20, 20, 20, 0.3)"
    back_color = ""

    @rx.event
    def toggle(self, value: bool):
        self.value = value
        self.text_color = "black" if value else "white"
        self.card_color = "rgba(255, 255, 255, 0.3)" if value else "rgba(20, 20, 20, 0.3)"

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.hstack(
                rx.icon("menu", display={"base": "block", "md": "none"}, color=State.text_color),
                navbar_link("Home", "/", State.text_color),
                navbar_link("Projects", "/projects", State.text_color),
                navbar_link("Contact", "/contact", State.text_color),
                navbar_link("Resume", "/resume", State.text_color),
                navbar_link("About Me", "/about", State.text_color),
            ),
            rx.switch(
                on_change=State.toggle,
                name="Change Theme",
                color_scheme="gray",
            ),
            
            bg=State.card_color,
            
        ),
    )