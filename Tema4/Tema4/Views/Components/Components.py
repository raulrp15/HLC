import reflex as rx

def link_button(text: str, url: str, c: str = "") -> rx.Component:
    return rx.link(
        rx.button(text, bg=c),
        href=url,
        is_external=True,
    )