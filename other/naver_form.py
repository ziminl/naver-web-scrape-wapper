


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()



driver.get("https://form.office.naver.com/form/responseViewMobile.cmd?formkey=YTg5YjExZjgtNGYyOC00ODRlLTg3ZmEtZGU4OGE3MTgzMjBh")



wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

def scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
  
time.sleep(5)

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/div[1]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[4]/div/div[3]/div/div[4]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[6]/div/div[3]/div/div[1]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[7]/div/div[3]/div/div[2]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[8]/div/div[3]/div/div[1]/div/div/div[2]/span"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

element_xpath = "/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/div/button[3]"
element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
scroll_into_view(element)
element.click()

time.sleep(5)
driver.quit()


