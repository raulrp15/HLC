from logging import config
import reflex as rx

def navbar_link(t:str, url:str, txtColor:str) -> rx.Component:
    return rx.link(t, href=url, font_family="Sono", color=txtColor, high_contrast=True)