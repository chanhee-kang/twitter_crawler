import threading
import twitter_sel as tw
import datesp
import queue
from selenium import webdriver
import time
import exel
class news(threading.Thread):

    q2=queue.Queue()
    listof=[]
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            try:
                v=news.q2.get_nowait()
                news.listof.extend(tw.sel(v))
            except queue.Empty:
                break

            
def main(sday,eday,sword,lan,filen):
    
    q2=queue.Queue()        
    a=datesp.datesp(sday,eday)
    
    days=datesp.oned(a.main())
    
    count=len(days)
    num=0
    th=[]
    
    for i in range(count):
        num+=1
        
        try:
            iv="https://twitter.com/search?q="+sword+"%20lang%3A"+lan+"%20since%3A"+days[i]+"%20until%3A"+days[i+1]+"&src=typd"
        except:
            break
        q2.put_nowait(iv)
        
    news.q2=q2


    for v in range(5):
        
        t=news()
        th.append(t)
        t.start()
        time.sleep(2)
        
    for av in th:
        
        av.join()

    print(len(news.listof))
    exel.ex(filen,news.listof)
        

    
#<button style="display: inline-block;" type="button" class="btn-link back-to-top hidden">위로 가기 ↑</button>
#엑셀만들기
#30일마다 끊어서 저장하기
#시간일때에 저장
