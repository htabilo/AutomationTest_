from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(2.5)

#<input type="text" name="my-text">
text_name = driver.find_element(by=By.NAME, value="mi-text")

#<button type="submit">Enviar</button>
presion_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


text_name.send_keys("selenium")
presion_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()