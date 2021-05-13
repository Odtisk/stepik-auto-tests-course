from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome("D:\\chromedriver.exe")
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    form = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radiobutton = browser.find_element_by_id("robotsRule")
    submit = browser.find_element_by_xpath("//button")

    form.send_keys(calc(x))
    checkbox.click()
    radiobutton.click()
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
