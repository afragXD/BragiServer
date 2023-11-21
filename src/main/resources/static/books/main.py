import shutil
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from multiprocessing import Pool
import os
#import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth


def OneG(driver) -> list[str]:
    li: list[str] = []
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="arrticle"]'))
    )
    for div in element:
        li.append(div.text)
    return li


def Anti(driver, base_url: str):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div'))
    ).click()


def Description(driver) -> str:
    des = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fs-info"]/div[1]/div/div'))
    ).text
    return des


def src_url(driver) -> str:
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="dle-content"]/article/main/div[1]/div/div[1]/div[2]/div[1]/a/img'))).get_attribute(
        "src")
    return elem


def get_count_change(driver) -> int:
    chapters_count = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fs-info"]/div[2]/ul[1]/li[4]/span/span'))).text
    if chapters_count.isdigit():
        return (int(chapters_count))
    else:
        return 0


# opts.add_argument("window-size=1400,600")

d = {
    # "a-will-eternal":
    # [
    # "https://ranobes.com/chapters/a-will-eternal/246198-golossarij.html",1315
    # ],
     "Tales_of_Herding_Gods":
     [
         "https://ranobes.com/ranobe/53844-tales-of-herding-gods.html",1735
     ],
    # "Player who returned":[
    #   "https://ranobes.com/chapters/player-who-returned-10000-years-later/50777-prolog.html",521
    # ],
    # "Outside Of Time": [
    #     "https://ranobes.com/ranobe/354130-outside-of-time.html", 1482
    # ],
    #"Renegade Immortal":[
    #    "https://ranobes.com/ranobe/799-renegade-immortal.html",2092,
    #]
    # "Against the Gods":[
    #     "https://ranobes.com/chapters/against-the-gods/100834-nprolog.html",2036,
    # ]
}


def get_data(n):
    try:
        global d
        URL = d[n][0]
        # count = d[n][1]
        opts = Options()
        ua = UserAgent()
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option('useAutomationExtension', False)
        user_agent = ua.random
        # opts.add_argument('--headless')
        opts.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(opts)
        driver.set_script_timeout(30)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win64",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        # обход анти-бота
        Anti(driver, URL)
        # description
        text_description = Description(driver)
        print(text_description)
        # img Novel
        elem = src_url(driver)
        print(elem)

        # count chapters-scroll-list
        count = get_count_change(driver)
        # переход на первую главу
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fs-chapters"]/div/div[3]/a[1]'))
        ).click()
        if not (n in os.listdir(path=".")):
            os.mkdir(n)
        else:
            try:
                 file = open(f"{n}\\URL_END.txt", "r")
            except IOError as e:
                print(u'не удалось открыть файл')
                file = open(f"{n}\\URL_END.txt", "w")
                x = '//*[@id="next"]'
                ######
                #driver.find_element(By.XPATH, x).click()
                for i in range(1, count + 1):
                    li: list[str] = OneG(driver)
                    with open(f"{n}\\{i}.txt", "w", encoding='utf-8') as f:
                        f.writelines('\n'.join(li))
                    if i == count:
                        URL = driver.current_url
                        print(URL)
                        print(count, URL, file=file)
                    else:
                        driver.find_element(By.XPATH, x).click()
                        URL = driver.current_url
                        print(URL)
            else:
                with file:
                    print(u'делаем что-то с файлом')
                    content = file.read()
            meta=content.split(" ")

            save_count=int(meta[0])
            if count>save_count:
                driver.get(meta[1])
                x = '//*[@id="next"]'
                driver.find_element(By.XPATH, x).click()
                for i in range(save_count+1, count + 1):
                    li: list[str] = OneG(driver)
                    with open(f"{n}\\{i}.txt", "w", encoding='utf-8') as f:
                        f.writelines('\n'.join(li))

                    if i == count:
                        URL = driver.current_url
                        print(URL)
                        with open(f"{n}\\URL_END.txt", "w", encoding='utf-8') as f1:
                            print(count, URL, file=f1)
                    else:
                        driver.find_element(By.XPATH, x).click()
                        URL = driver.current_url
                        print(URL)
            else:
                print("актуал")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    p = Pool(processes=len(d))

    p.map(get_data, d)
