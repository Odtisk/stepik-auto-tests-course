from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome("D:\\chromedriver.exe")
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    lastname = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    file = browser.find_element_by_name("file")
    submit = browser.find_element_by_xpath("//button")

    name.send_keys('roma')
    lastname.send_keys('porkhanov')
    email.send_keys('r6om@ya.ru')
    file.send_keys('D:\\Vegas Pro 18\\gnsdk_license.txt')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
