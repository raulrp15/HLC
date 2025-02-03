from Ejercicio01.pages.buscadores import buscadores
from Ejercicio01.pages.index import index
import reflex as rx

from Ejercicio01.pages.redes_sociales import redes_sociales
from rxconfig import config

config.title = "Ejercicio01"

app = rx.App()
app.add_page(index)
app.add_page(buscadores)
app.add_page(redes_sociales)