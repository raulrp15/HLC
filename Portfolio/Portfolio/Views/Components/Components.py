from logging import config
import reflex as rx

def navbar_link(t:str, url:str) -> rx.Component:
    return rx.link(t, href=url)