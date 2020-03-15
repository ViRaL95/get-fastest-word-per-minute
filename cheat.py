from pprint import pprint
from time import sleep, time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def get_text():
    t_end = time() + 60
    while time() < t_end:
        web_elements = driver.find_elements(By.XPATH, f'//*[@id="app"]/div/div[2]/div/span/div[2]/span/div/div[2]/div/span[1]')
        for web_element in web_elements:
            ActionChains(driver).send_keys(web_element.text + " ").perform()
            pprint(web_element.text + "\n")
            sleep(.1)


driver = webdriver.Firefox()
driver.get("https://www.livechatinc.com/typing-speed-test/#/")

get_text()

action_chains = ActionChains(driver)

sleep(80)

driver.quit()
