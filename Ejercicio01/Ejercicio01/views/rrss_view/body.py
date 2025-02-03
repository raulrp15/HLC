import reflex as rx

from Ejercicio01.views.components.components import link_list_item, return_button


def body() -> rx.Component:
    return rx.vstack(
        rx.unordered_list(
            link_list_item("Instagram", "https://www.instagram.com/", True),
            link_list_item("TikTok", "https://www.tiktok.com/", True),
            link_list_item("Facebook", "https://www.facebook.com/", True),
        ),
        return_button()
    )