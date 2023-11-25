from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def chapterName(driver) -> str:
    chapterName = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dle-content"]/article/div[2]/h1'))
    ).text

    chapterName = chapterName.split('\n')[0]

    return chapterName