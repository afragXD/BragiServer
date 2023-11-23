from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def author(driver) -> str:
    author = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fs-info"]/div[2]/ul[1]/li[7]/span/a'))
    ).text
    return author