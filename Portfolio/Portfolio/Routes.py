import reflex as rx
from enum import Enum

MAX_WIDTH = "600px"

class Ruta(Enum):
    INDEX= "/"
    PROJECTS= "/projects"
    CONTACT= "/contact"
    RESUME= "/resume"
    ABOUT= "/about"