import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.booking_page import Booking_page
from pages.main_page import Main_page
from pages.search_page import Search_page


def test_select_product():

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service('C:\\Users\\makev\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")

    mp = Main_page(driver)
    mp.select_online_booking()

    sp = Search_page(driver)
    sp.search_online_booking()

    lll = driver.window_handles
    print(lll)
    driver.switch_to.window(lll[1])


    time.sleep(3)
    qqq = driver.current_url
    print(qqq)


    bp = Booking_page(driver)
    bp.input_tourist()
    bp.input_tourist_1()
    bp.finish_info()



    # time.sleep(5)
    # driver.quit()








