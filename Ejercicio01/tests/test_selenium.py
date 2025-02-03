from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://localhost:3001")

def test_completo(first_link:str, second_link:str):
    driver.find_element(By.ID, first_link).click()
    sleep(2)
    driver.find_element(By.ID, second_link).click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    driver.find_element(By.ID, "Volver").click()
    sleep(2)
    driver.quit()

if __name__ == "__main__":
    test_completo('Redes Sociales', 'Instagram')