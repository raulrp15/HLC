from Portfolio.Pages.Index import index
import reflex as rx

from rxconfig import config

config.title = "Portfolio"
app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Sono:wght@200..800&display=swap"]
)
app.add_page(index)
