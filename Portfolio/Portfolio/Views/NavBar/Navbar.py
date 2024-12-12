import reflex as rx

from Portfolio.Views.Components.Components import navbar_link

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.icon(),
            navbar_link("Home", "/"),
            navbar_link("Projects", "/projects"),
            navbar_link("Contact", "/contact"),
            navbar_link("Resume", "/resume"),
            navbar_link("About Me", "/about"),
        )
    )