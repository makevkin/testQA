import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_page(Base):   # класс login_page стал потомком класса Base



     def __init__(self, driver):
         super().__init__(driver)  # указываем, что это потомок нашего класса Base
         self.driver = driver

    # Locator

     location = "//select[@class='select fromLocation']"
     country = "//select[@class='select toCountry']"
     package = "//select[@class='select package']"
     date_of_departure = "//input[@class='pgs-dropdown__label tourDate start datepick']"
     next_mounth = "//span[@class='ui-icon ui-icon-circle-triangle-e']"
     date_of_departure_1 = "//input[@class='pgs-dropdown__label tourDate end datepick']"
     duration = "//select[@class='select tourDuration tourStartDuration small']"
     duration_1 = "//select[@class='select tourDuration tourEndDuration small']"
     adults = "//select[@class='select adults small']"
     date = "(//td[@data-month='4'])[17]"
     date_1 = "(//td[@data-month='4'])[24]"
     button_search = "//input[@class='main-button pegasys_search_button']"
     means_ai = "//input[@value='6890']"
     categoria_hotel = "//input[@value='3579161']"
     booking = "//*[@id='hotel_wrap']/label[3]/input"
     currency = "//*[@id='content_wrapper']/div/div[3]/form/div[3]/div/div[1]/div[2]/label[1]/input"
     search = "//a[@class='page-header__dropdown-link']"

     # Getors

     def get_location(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location)))

     def get_country(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country)))

     def get_package(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.package)))

     def get_date_of_departure(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_of_departure)))

     def get_date_of_departure_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_of_departure_1)))

     def get_duration(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.duration)))

     def get_duration_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.duration_1)))

     def get_adults(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adults)))

     def get_next_mounth(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_mounth)))

     def get_date(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date)))

     def get_date_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_1)))

     def get_duration(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.duration)))

     def get_duration_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.duration_1)))

     def get_button_search(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search)))

     def get_means_ai(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.means_ai)))

     def get_categoria_hotel(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.categoria_hotel)))

     def get_booking(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.booking)))

     def get_currency(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.currency)))

     def get_price(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content_wrapper']/div/div[3]/div[3]/div/div[6]/div[7]/div[3]/button")))


     # Actions

     """ВВодим город отправления"""
     def input_location(self, location):
         self.get_location().send_keys(location)
         print("Input Location")

     """Вводим страну"""
     def input_country(self, country):
         self.get_country().send_keys(country)
         print("Input Country")

     """Воодим тип тура"""
     def input_packege(self, package):
         self.get_package().send_keys(package)
         print("Input package")

     # def input_packege(self):
     #     self.get_package().send_keys(Keys.ARROW_DOWN*2)
     #     print("Input package")

     """Выбо периода вылета"""
     def date_choice(self):
         self.get_date_of_departure().click()
         self.get_next_mounth().click()
         self.get_date().click()
         self.get_date_of_departure_1().click()
         self.get_date_1().click()

     """Выбор продолжительности тура"""
     def duration_choice(self):
         self.get_duration().click()
         self.get_duration().send_keys('7')
         self.get_duration().send_keys(Keys.RETURN)
         self.get_duration_1().click()
         self.get_duration_1().send_keys('10')
         self.get_duration_1().send_keys(Keys.RETURN)

         print("Input Date")

   #  def scroll_to_button(self):
   #       action = ActionChains(driver)
   #       action.move_to_element()


         # Metods

     def search_online_booking(self):

         self.get_current_url()
         self.input_location("Москва")
         time.sleep(2)
         self.input_country("Турция")
         time.sleep(2)
         self.input_packege("Antalya (Moscow)")
         self.date_choice()
         self.duration_choice()
         self.get_means_ai().click()
         print("AI")
         self.get_categoria_hotel().click()
         print("Yes")
         qqq = self.get_booking()

         if not qqq.is_selected():      # проверка нажат чекбокс "Нет остановки продаж"
             self.get_booking().click()

         currency_active = self.get_currency()

         if not currency_active.is_selected():   # проверка нажат чекбокс Валюта рубли
             self.get_currency().click()

         self.get_button_search().click()      # нажимаем кнопку Найти
         time.sleep(2)

         self.get_price().click()    # выбор отеля для бронирования

     # self.driver.execute_script("window.scrollTo(0, 700)")  # прокрутка страницы на 500 пикселей вниз



     # self.assert_word(self.get_main_word(), 'Products')





