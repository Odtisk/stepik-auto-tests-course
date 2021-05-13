from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome("D:\\chromedriver.exe")
    browser.get(link)

    book = browser.find_element_by_id("book")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    book.click()
    
    x = browser.find_element_by_id("input_value").text 
    answer = browser.find_element_by_id("answer")
    submit = browser.find_element_by_id("solve")
    
    answer.send_keys(str(calc(x)))
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
