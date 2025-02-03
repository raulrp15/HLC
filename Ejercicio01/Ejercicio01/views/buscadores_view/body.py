import reflex as rx

from Ejercicio01.views.components.components import link_list_item, return_button

def body() -> rx.Component:
    return rx.vstack(
        rx.unordered_list(
            link_list_item("Google", "https://www.google.com/", True),
            link_list_item("Bing", "https://www.bing.com/", True),
            link_list_item("Baidu", "https://www.baidu.com/", True),
        ),
        return_button()
    )