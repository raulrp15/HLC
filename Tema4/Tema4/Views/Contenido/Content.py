import reflex as rx

from Tema4.Views.Components.Components import link_button

def content_view() -> rx.Component:
    return rx.vstack(
        link_button("Instagram", "https://www.instagram.com/raulromerap/", "radial-gradient(circle at 20% 110%, #FCB045, #FD1D1D 50.00%, #833AB4)"),
        link_button("Youtube", "https://www.youtube.com/@el_trajeado168", "Red"),
        link_button("Twitch", "https://www.twitch.tv/el_trajeado", "#6441a5"),
        align="center"
    )