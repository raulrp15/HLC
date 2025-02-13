from selenium import webdriver
from selenium.webdriver.common.by import By



url = "http://localhost:3000"
def test_formulario_1():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        title = driver.find_element(By.ID,"titulo").text
    finally:
        driver.quit()
    
    assert title == "Formulario de registro - Mi Web"

def test_formulario_2():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        label_text = driver.find_element(By.ID,"lname").text
    finally:
        driver.quit()
    
    assert label_text == "Nombre:"

def test_formulario_3():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        input = driver.find_element(By.ID,"iname").tag_name
    finally:
        driver.quit()
    
    assert input == "input"

def test_formulario_4():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        label_text = driver.find_element(By.ID,"lsurname").text
    finally:
        driver.quit()
    
    assert label_text == "Apellidos:"

def test_formulario_5():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        input = driver.find_element(By.ID,"isurname").tag_name
    finally:
        driver.quit()
    
    assert input == "input"

def test_formulario_6():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        radio_buttons = driver.find_elements(By.XPATH, "//*[@role='radio']")
        radio_hombre = radio_buttons[0].get_attribute("value")
        radio_mujer = radio_buttons[1].get_attribute("value")
    finally:
        driver.quit()
    
    assert radio_hombre == "Hombre" and radio_mujer == "Mujer"

def test_formulario_7():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        email = driver.find_element(By.ID,"iemail").tag_name
    finally:
        driver.quit()
    
    assert email == "input"

def test_formulario_8():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        checkbox = driver.find_element(By.ID,"icheck").get_attribute("type")
        checkbox_checked = driver.find_element(By.ID,"icheck").get_attribute("aria-checked")
    finally:
        driver.quit()
    
    assert checkbox == "button" and checkbox_checked == "true"

def test_formulario_9():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        checkbox = driver.find_element(By.ID,"icheck2").get_attribute("type")
    finally:
        driver.quit()
    
    assert checkbox == "button"