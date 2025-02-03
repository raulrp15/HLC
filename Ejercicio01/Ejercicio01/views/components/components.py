import reflex as rx

def link_list_item(title:str, url:str, ext:bool) -> rx.Component:
    return rx.list_item(rx.link(title, href=url, is_external=ext, id=title))

def header(t:str) -> rx.Component:
    return rx.vstack(rx.text(t, size="9"))

def return_button() -> rx.Component:
    return rx.link("Volver", href="/", is_external=False, id="Volver")