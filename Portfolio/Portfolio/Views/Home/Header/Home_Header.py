import reflex as rx
from Portfolio.Views.NavBar.Navbar import State
from Portfolio.Views.Styles.Styles import size

def home_header() -> rx.Component:
    return rx.hstack(
        rx.avatar(src="https://media.licdn.com/dms/image/v2/D4E03AQGvxLLKJGMOxQ/profile-displayphoto-shrink_200_200/B4EZSrywC2HgAY-/0/1738048996527?e=1743638400&v=beta&t=Yd7mmzy2kVSoj2J3qch_xMIWE6I2dcmjitSszejbKYg", 
                alt="Raul Romera Pavón", style={"width":"10%", "height":"10%"}, radius="full"),
        rx.text("Raul Romera Pavón", size=size.LARGE.value, weight="bold", color=State.text_color, font_family="Sono", as_="div"),
    )