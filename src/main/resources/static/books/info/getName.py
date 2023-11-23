from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def name(driver) -> str:
    name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/article/main/div[1]/div/div[1]/h1'))
    ).text
    return name.split('\n')[0]

def nameEn(driver) -> str:
    name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/article/main/div[1]/div/div[1]/h1'))
    ).text
    return name.split('\n')[1].split('•')[0].rstrip()