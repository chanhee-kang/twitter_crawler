#encoding:utf-8
import urllib.request
import re


req = urllib.request.Request('https://www.google.co.kr/search?q=pokemon+go&biw=1159&bih=779&tbm=nws&ei=uDhPWKq0Hoef8QXv05OoCg&start=0&sa=N&dpr=1.25')
req.add_header('User-agent', 'Mozilla/5.0')
req.add_header('Accept', 'text/html')
 
res = urllib.request.urlopen(req)
text = res.read().decode("utf8")

contents=re.compile('<a href="\/url\?q=(.+?)&amp;sa=U&amp')

a=contents.findall(text)


print(len(a))
