from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome("D:\\chromedriver.exe")
    browser.get(link)

    redirect = browser.find_element_by_xpath("//button")
    redirect.click()

    browser.switch_to.window(browser.window_handles[1])
    
    x = browser.find_element_by_id("input_value").text 
    answer = browser.find_element_by_id("answer")
    submit = browser.find_element_by_xpath("//button")
    
    answer.send_keys(str(calc(x)))
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
