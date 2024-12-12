import reflex as rx

def navbar_link(t:str, url:str) -> rx.Component:
    return rx.link(text=t, href=url, color="white", text_decoration="none")