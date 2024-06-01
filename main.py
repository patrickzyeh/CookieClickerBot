from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium Driver Setup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

COOKIE_CLICKER_URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(COOKIE_CLICKER_URL)

# Finds cookie element

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

# Autoclick & autoupgrade bot

upgrade_options = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrade_options = [option.get_attribute("id") for option in upgrade_options]
upgrade_options.pop(-1)

upgrade_interval = time.time() + 5
timer = time.time() + 300

while True:

    cookie.click()

    if time.time() > timer:
        cps = driver.find_element(By.ID, value="cps").text
        print(cps)
        break

    if time.time() > upgrade_interval:
        money = int(driver.find_element(By.CSS_SELECTOR, value="#money").text.replace(",", ""))

        # Obtain list of upgrade prices

        upgrade_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        upgrade_prices.pop(-1)
        upgrade_prices = [int(price.text.split("-")[1].strip().replace(",", ""))
                          for price in upgrade_prices]

        for i in range(len(upgrade_prices)):
            if upgrade_prices[i] <= money <= upgrade_prices[i+1]:
                most_expensive_id = upgrade_options[i]
                driver.find_element(By.ID, value=most_expensive_id).click()

                break

        upgrade_interval = time.time() + 5
