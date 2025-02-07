from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "http://localhost:3000"
def test_formulario_1():
    driver.get(url)
    try:
        title = driver.find_element(By.ID,"titulo").text
    finally:
        driver.quit()
    
    assert title == "Formulario de registro"

def test_formulario_2():
    driver.get(url)
    try:
        label_text = driver.find_element(By.ID,"lname").text
    finally:
        driver.quit()
    
    assert label_text == "Nombre:"

def test_formulario_3():
    driver.get(url)
    try:
        input = driver.find_element(By.ID,"iname").tag_name
    finally:
        driver.quit()
    
    assert input == "input"

def test_formulario_4():
    driver.get(url)
    try:
        label_text = driver.find_element(By.ID,"lsurname").text
    finally:
        driver.quit()
    
    assert label_text == "Apellidos:"

def test_formulario_5():
    driver.get(url)
    try:
        input = driver.find_element(By.ID,"isurname").tag_name
    finally:
        driver.quit()
    
    assert input == "input"