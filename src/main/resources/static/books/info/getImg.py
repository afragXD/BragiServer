from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def src_url(driver) -> str:
    img = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="dle-content"]/article/main/div[1]/div/div[1]/div[2]/div[1]/a/img'))).get_attribute(
        "src")
    return img