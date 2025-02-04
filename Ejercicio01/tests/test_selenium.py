from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "http://localhost:3000"

def test_busquedas():
    driver.get("http://localhost:3000")
    bsq = driver.find_element(By.ID, "Buscadores").get_attribute('href')
    bsq == "http://localhost:3000/buscadores/"
    driver.quit()

def test_redes():
    driver.get("http://localhost:3000")
    red = driver.find_element(By.ID, "Redes Sociales").get_attribute('href')
    red == "http://localhost:3000/redes-sociales/"
    driver.quit()

def test_volver():
    driver.get("http://localhost:3000/buscadores/")
    driver.find_element(By.ID, "Volver").click()
    inicio = driver.current_url
    inicio == "http://localhost:3000/"
    driver.quit()
