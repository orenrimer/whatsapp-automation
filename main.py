from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import config
from time import sleep
import schedule


BASE_URL = "https://web.whatsapp.com/"
options = webdriver.ChromeOptions()
options.add_argument(config.CHROME_PROFILE_PATH)


def main():
    driver = Chrome(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(config.WAIT_TIME)
    sleep(10)
    CONTACT = "//span[contains(text(),'{0}')][1]"
    contact = driver.find_element_by_xpath(CONTACT.format(''))
    contact.click()

    msg = "Good Morning"
    INPUT_FIELD = '//div[@contenteditable="true"][@data-tab="6"]'
    input_field = driver.find_element_by_xpath(INPUT_FIELD)
    ActionChains(driver).click(input_field).send_keys(msg).send_keys(Keys.ENTER).perform()
    sleep(5)
    driver.close()

schedule.every().day.at("10:00").do(main)

while True:
    schedule.run_pending()
    sleep(20)