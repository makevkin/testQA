
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):   # класс login_page стал потомком класса Base

     url = 'https://pegast.ru/'

     def __init__(self, driver):
         super().__init__(driver)  # указываем, что это потомок нашего класса Base
         self.driver = driver

    # Locator

     online_booking = "//button[@class='menu-dropdown__toggler el-popover__reference']"
     search = "//a[@class='page-header__dropdown-link']"



     # Getors


     def get_online_booking(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.online_booking)))


     def get_search(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))


     # Actions

     """Активация вспомогательного меню Онлайн-бронировани"""
     def click_online_booking(self):
         self.get_online_booking().click()
         print("Click online booking")

     """Выбираем пункт меню Найти тур"""
     def click_search(self):
         self.get_search().click()
         print("Click search")



         # Metods

     def select_online_booking(self):

         self.driver.get(self.url)
         self.driver.maximize_window()
         self.get_current_url()
         self.click_online_booking()
         self.click_search()

        # self.assert_word(self.get_main_word(), 'Products')





