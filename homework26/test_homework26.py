
from selenium.webdriver.common.by import By

class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button").click()
    def enterName(self):
        self.driver.find_element(By.XPATH, "//*[@id='signupName']").send_keys("NameSs")

    def enterLastName(self):
            self.driver.find_element(By.XPATH, '//*[@id="signupLastName"]').send_keys('qwety')

    def enterEmail(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupEmail"]').send_keys("qwetyass2131@fd.hg")
    def enterPassword(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupPassword"]').send_keys("qwerty2#$QWE")
    def enterPasswordAgain(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupRepeatPassword"]').send_keys("qwerty2#$QWE")

    def clickRegistration(self):
        self.driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button').click()

    def current_url(self):
        return self.driver.current_url
