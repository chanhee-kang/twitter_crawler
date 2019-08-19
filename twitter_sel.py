# -*- coding: cp949 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import time
def sel(v):
    listof=[]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
    driver = webdriver.Firefox(firefox_options=chrome_options)
   
    try:
        driver.get(v)
    except:
        print(v)
        return 0
    
    for i in range(200):
        try:       
            if driver.find_element_by_class_name("SearchEmptyTimeline-emptyTitle"):
                driver.quit()
                return []
        except:
            pass
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #print(driver.get_window_position())
        time.sleep(0.2)
        
        
    content = driver.find_elements_by_class_name('TweetTextSize.js-tweet-text.tweet-text')
    name = driver.find_elements_by_class_name("fullname.show-popup-with-id")
    time2 = driver.find_elements_by_class_name("_timestamp.js-short-timestamp")
    time3 = driver.find_elements_by_class_name("_timestamp.js-short-timestamp.js-relative-timestamp")
    num=0
    time3.extend(time2)
    for i in content:
        li=[]
        li.append(time3[num].text)
        li.append(i.text)
        li.append(name[num].text)
        
        
        num+=1
        listof.append(li)
    driver.quit()
    return listof

#<button style="display: inline-block;" type="button" class="btn-link back-to-top hidden">위로 가기 ↑</button>
#<span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1467296560" data-time-ms="1467296560000" data-long-form="true">6월 30일</span>
#sel('https://twitter.com/search?q=%EC%98%A4%ED%94%BC&src=typd')
