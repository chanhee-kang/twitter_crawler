from selenium import webdriver
import time
import re

        
def aa(v,nameoff):
    num=re.compile('[0-9]*')
    driver = webdriver.Firefox()
    driver.get(v)
    time.sleep(2)
    counts=driver.find_element_by_class_name('u_cbox_count')
    counts=int(counts.text.replace(",",""))
    nums=int(counts/20)

    for i in range(nums):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_class_name("u_cbox_page_more").click()
            time.sleep(1)
        except:
            continue
            print("err")


    a=driver.find_elements_by_class_name('u_cbox_btn_reply')

    for i in a:
        if int(re.findall(num,str(i.text))[3]) > 0:
            i.click()


    a=driver.find_elements_by_class_name('u_cbox_contents')
    f=open(nameoff+"-"+str(counts)+".txt",'w', encoding='UTF-8')
    errof=0
    numoff=0
    for i in a:
        try:
            numoff+=1
            f.write(str(i.text)+'\n')
        except:
            errof+=1
            continue
    print(errof)
    print(numoff)
    f.close()

    driver.quit()

listof=[]
f1=open('링크수정.txt','r')
while True:
    line=f1.readline()
    if not line:
        break
    listof.append(line)
nux=0
for i in listof:
    nux+=1
    i=i.strip()
    print(i)
    if i=='번':
        continue
    else:
        aa(i,'file-'+str(nux))
