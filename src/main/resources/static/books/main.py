
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from multiprocessing import Pool
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth

from database.DTO import BookDTO
from database.DTO import ChapterDTO


from database.db import getConnection, inseriFromParse, inseriChapter, getIdFromName

from info.getDescription import description
from info.getName import name
from info.getName import nameEn
from info.getImg import src_url
from info.getRating import rating
from info.getStatus import status
from info.getChapters import chapters
from info.getYear import year
from info.getAuthor import author
from info.getChapterName import chapterName


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


def get_count_change(driver) -> int:
    chapters_count = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fs-info"]/div[2]/ul[1]/li[4]/span/span'))).text
    if chapters_count.isdigit():
        return (int(chapters_count))
    else:
        return 0


d = [
    #"https://ranobes.com/ranobe/53844-tales-of-herding-gods.html",
    #"https://ranobes.com/ranobe/50776-player-who-returned-10000-years-later-1.html",
    #"https://ranobes.com/ranobe/20314-solo-leveling.html",
    #"https://ranobes.com/ranobe/668-warlock-of-the-magus-world.html",
    #"https://ranobes.com/ranobe/5951-a-will-eternal.html",
    #"https://ranobes.com/ranobe/4-overlord.html",
    #"https://ranobes.com/ranobe/151884-the-beginning-after-the-end.html",
    #"https://ranobes.com/ranobe/206754-falling-in-love-with-the-villainess.html",
    #"https://ranobes.com/ranobe/231996-coeus.html",
    #"https://ranobes.com/ranobe/347562-combat-continent.html",
    #"https://ranobes.com/ranobe/134618-lord-of-the-mysteries.html",
    #"https://ranobes.com/ranobe/401486-grandson-of-the-holy-emperor-is-a-necromancer.html",
    #"https://ranobes.com/ranobe/363293-immortal-in-the-magic-world.html",
]

def get_data(n):
    try:
        URL = n
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
        # info
        dto = BookDTO(
            name = name(driver),
            en_name = nameEn(driver),
            image = src_url(driver),
            description = description(driver),
            rating = rating(driver),
            status = status(driver),
            chapters = chapters(driver),
            year = year(driver),
            author = author(driver)
        )



        connection = getConnection()
        inseriFromParse(dto, connection)

        id = getIdFromName(dto.en_name, connection)

        # count chapters-scroll-list
        count = get_count_change(driver)
        # переход на первую главу
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fs-chapters"]/div/div[3]/a[1]'))
        ).click()

        dto2 = ChapterDTO(
            chapter_number= 1,
            chapter_name=chapterName(driver),
            book_id= id
        )
        inseriChapter(dto2, connection)

        if not (dto.en_name in os.listdir(path="res\\novel\\")):
            os.mkdir('res\\novel\\'+dto.en_name)
        try:
             file = open(f"res\\novel\\{dto.en_name}\\URL_END.txt", "r")
        except IOError as e:
            print(u'не удалось открыть файл')
            file = open(f"res\\novel\\{dto.en_name}\\URL_END.txt", "w")
            x = '//*[@id="next"]'
            ######
            #driver.find_element(By.XPATH, x).click()
            for i in range(1, count + 1):
                li: list[str] = OneG(driver)
                with open(f"res\\novel\\{dto.en_name}\\{i}.txt", "w", encoding='utf-8') as f:
                    f.writelines('\n'.join(li))
                if i == count:
                    URL = driver.current_url
                    print(URL)
                    print(count, URL, file=file)
                else:
                    driver.find_element(By.XPATH, x).click()
                    dto2 = ChapterDTO(
                        chapter_number=i,
                        chapter_name=chapterName(driver),
                        book_id=id
                    )
                    inseriChapter(dto2, connection)
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
                with open(f"res\\novel\\{dto.en_name}\\{i}.txt", "w", encoding='utf-8') as f:
                    f.writelines('\n'.join(li))

                if i == count:
                    URL = driver.current_url
                    print(URL)
                    with open(f"res\\novel\\{dto.en_name}\\URL_END.txt", "w", encoding='utf-8') as f1:
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
