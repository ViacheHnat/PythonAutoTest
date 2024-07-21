from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

# XPATH
driver.find_element(By.XPATH, "//div[@class='header_inner d-flex justify-content-between align-items-center']")
driver.find_element(By.XPATH, "//button[@appscrollto='aboutSection']")
driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[1]/div/div/div[1]/div/p[1]")
driver.find_element(By.XPATH, "//div[@class='hero-descriptor']/button[text()='Sign up']")
driver.find_element(By.XPATH, "//div//button[text()='Sign In']")
driver.find_element(By.XPATH, "//div[@class='hero-descriptor']")
driver.find_element(By.XPATH, "//img[@src='/assets/images/homepage/info_2.jpg']")
driver.find_element(By.XPATH, "//a[@class='socials_link']//span[@class='socials_icon icon icon-telegram']")
driver.find_element(By.XPATH, "//p[@class='about-block_title h2' and text()='Log fuel expenses']")
driver.find_element(By.XPATH,"//p[@class='about-block_descr lead' and text()='Watch over 100 instructions and repair your car yourself.']")
driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/app-footer/footer/div/div/div[1]/p[1]")
time.sleep(1)

# CSS
driver.find_element(By.CSS_SELECTOR, "div.header_inner.d-flex")
driver.find_element(By.CSS_SELECTOR, "button[appscrollto=aboutSection]")
driver.find_element(By.CSS_SELECTOR, "#aboutSection > div > div > div:nth-child(1) > div > p.about-block_title.h2")
driver.find_element(By.CSS_SELECTOR, "div.hero-descriptor")
driver.find_element(By.CSS_SELECTOR, "div .header_signin")
driver.find_element(By.CSS_SELECTOR, "div .hero-descriptor")
driver.find_element(By.CSS_SELECTOR, ".mt-md-5 img.about-picture_img")
driver.find_element(By.CSS_SELECTOR, ".icon-telegram")
driver.find_element(By.CSS_SELECTOR, ".mt-3 .about-block_title")
driver.find_element(By.CSS_SELECTOR, ".mt-3 .about-block .lead")
driver.find_element(By.CSS_SELECTOR, "body > app-root > app-global-layout > div > app-footer > footer > div > div > div.col-7.d-flex.flex-column.justify-content-center.footer_item.-left > p:nth-child(1)")
