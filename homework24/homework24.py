from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By

user_link = "http://localhost:8000/dz.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(user_link)

# Frame1
driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
input1_frame1 = driver.find_element(By.XPATH, '//*[@id="input1"]')
input1_frame1.send_keys("Frame1_Secret")
button1_frame1 = driver.find_element(By.XPATH, '/html/body/button')
button1_frame1.click()
alert = Alert(driver)
assert 'Верифікація пройшла успішно!' == alert.text
alert.accept()

# Main Frame
driver.switch_to.default_content()

# Frame2
driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
input2_frame2 = driver.find_element(By.XPATH, '//*[@id="input2"]')
input2_frame2.send_keys("Frame2_Secret")
button2_frame2 = driver.find_element(By.XPATH, '/html/body/button')
button2_frame2.click()
alert = Alert(driver)
assert 'Верифікація пройшла успішно!' == alert.text
