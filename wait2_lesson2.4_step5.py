from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicity_wait(5)
    button = browser.find_element_by_id("verify").click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

except Exception as error:
    print(f'Произошла ошибка, вот её трейсбэк: {error}')

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
