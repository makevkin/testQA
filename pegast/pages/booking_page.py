import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Booking_page(Base):   # класс login_page стал потомком класса Base

     def __init__(self, driver):
         super().__init__(driver)  # указываем, что это потомок нашего класса Base
         self.driver = driver

    # Locator

     tourist = "//a[@class='link-popup person_popup_link']"
     tourist_1 = "//*[@id='persons-container']/div/div/table/tr[3]/td[2]/a"
     female = "//input[@id='female']"
     male = "//input[@id='male']"
     surname = "//input[@id='surname']"
     name = "//input[@id='name']"
     birthdate = "//input[@id='birthdate']"
     passport_number = "//input[@id='passport_number']"
     passport_due = "//input[@id='passport_due']"
     passport_where = "//input[@id='passport_where']"
     passport_who = "//input[@id='passport_who']"
     button_save = "//div[@class='main-button save_person']"
     accept_control = "//*[@id='booking-accept-control']"
     submit = "//input[@type='submit']"


     # Getors

     def get_tourist(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tourist)))

     def get_male(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.male)))

     def get_surname(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname)))

     def get_name(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

     def get_birthdate(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.birthdate)))

     def get_passport_number(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passport_number)))

     def get_passport_due(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passport_due)))

     def get_passport_where(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passport_where)))

     def get_passport_who(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.passport_who)))

     def get_button_save(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_save)))

     def get_tourist_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tourist_1)))

     def get_female(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.female)))

     def get_accept_control(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_control)))

     def get_submit(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit)))

     # Actions


     def click_tourist(self):
         self.get_tourist().click()
         print("Click tourist")

     def click_male(self):
         self.get_male().click()
         print("Male")

     def input_surname(self, surname):
         self.get_surname().send_keys(surname)
         print("Surname")

     def input_name(self, name):
         self.get_name().send_keys(name)
         print("Name")

     def input_birthdate(self, birthdate):
         self.get_birthdate().send_keys(birthdate)
         self.get_birthdate().send_keys(Keys.RETURN)
         print("Birthdate")

     def input_passport_number(self, passport_number):
         self.get_passport_number().send_keys(passport_number)
         print("Pasport number")

     def input_passport_due(self, passport_due):
         self.get_passport_due().send_keys(passport_due)
         print("Passport due")

     def input_passport_where(self, passport_where):
         self.get_passport_where().send_keys(passport_where)
         print("Pasport where")

     def input_passport_who(self, passport_who):
         self.get_passport_who().send_keys(passport_who)
         print("Pasport who")

     def click_button_save(self):
         self.get_button_save().click()

     def click_tourist_1(self):
         self.get_tourist_1().click()
         print("Click tourist_1")

     def click_female(self):
         self.get_female().click()
         print("FeMale")

     def click_accept_control(self):
         self.get_accept_control().click()

     def click_submit(self):
         self.get_submit().click()
         print("Submit")


         # Metods

     """Заполняем данные 1 туриста"""
     def input_tourist(self):
         self.click_tourist()
         self.click_male()
         self.input_surname("Ivanov")
         self.input_name("Ivan")
         self.input_birthdate("12.04.1977")
         self.input_passport_number("752324351")
         self.input_passport_due("24.01.2025")
         self.input_passport_where("24.01.2015")
         self.input_passport_who("MVD 64001")
         self.click_button_save()
         time.sleep(2)

     """Заполняем данные 2 туриста"""
     def input_tourist_1(self):
         self.click_tourist_1()
         self.click_female()
         self.input_surname("Ivanova")
         self.input_name("Elena")
         self.input_birthdate("24.11.1977")
         self.input_passport_number("752173651")
         self.input_passport_due("24.01.2025")
         self.input_passport_where("24.01.2015")
         self.input_passport_who("MVD 64001")
         self.click_button_save()

     """Заполняем оставшиеся данные для бронирования тура"""
     def finish_info(self):
         self.click_accept_control()
         self.click_submit()






        # self.assert_word(self.get_main_word(), 'Products')





