import  datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    # получаем текущую url

    def get_current_url(self):
        get_url = self.driver.current_url
        print(get_url)


    # Метод сравнения слов
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good word")

    # Метод Скриншот

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\makev\\PycharmProjects\\mains_project\\screen\\' + name_screenshot)

        # Метод сравнения url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good url")

        # переключение между окнами

    def new_window(self):
        original_window = self.driver.current_window_handle
        lll = self.driver.window_handles
        self.driver.switch_to.window(lll[1])



