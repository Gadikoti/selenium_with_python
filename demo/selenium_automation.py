print("Hello world of selenium python.")
from selenium import webdriver
driver =webdriver.chrome()
driver.get("https:www.ecoders.in")
time.sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()


