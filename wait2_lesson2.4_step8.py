from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
   
    
    # Говорим Selenium проверять в течении 12 секунд, пока кнопка не станет кликабельной
    # Нажимаем на кнопку бронь "Book" в тот момент, когда цена падает до 100$
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    # Ищем значения для элемента Х
    x_element = browser.find_element_by_id("input_value")
    # Передаём 
    y = calc(x_element.text)
    # передадим полученное значение в оконную
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # нажимаем на кнопку Submit
    button = browser.find_element_by_id("solve").click()
    
    # Переключаемся на всплывающее окно
    alert = browser.switch_to.alert
    # получаем текст из всплывающего окна
    alert_text = alert.text
    # нажимаем на кнопку "Ок", т.е. accept
    alert.accept()
    # используя pyperclip, копируем текст из alert в буфер обмена
    # также получаем последний элемент из строки с текстом,
    # разбивая её и переводя в массив с помощью метода split (JS) и регулярного выражения (https://javascript.ru/string/split)
    addToClipBoard = alert_text.split(': ')[-1] # magic
    pyperclip.copy(addToClipBoard)
    
except Exception as error:
    print(f'Произошла ошибка, вот её трейсбэк: {error}')

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
