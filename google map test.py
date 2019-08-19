from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()

url="https://www.google.com/maps/place/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90+%EC%9E%A0%EC%8B%A4%EC%A0%90/@37.5112827,127.0985472,16z/data=!4m10!1m2!2m1!1z66Gv642w67Cx7ZmU7KCQ!3m6!1s0x357ca5a0b19fcc6d:0x1ee7a2171ae06bca!8m2!3d37.5122103!4d127.0994592!9m1!1b1"
actions = ActionChains(driver)


driver.get(url)

time.sleep(5)
element= driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')

element.click()
element.send_keys(Keys.PAGE_DOWN)

time.sleep(5)

driver.close()
