## 트위터 크롤러
트워터의 크롤링을 진행하기 위해서는 트위터 API를 발급받아야하며 크롤링에 제한을 둡니다.<br><br>
따라서 본 크롤러는 별도의 트위터 API를 발급 받지않아도 원하는 검색어 및 날짜를 설정하여 크롤링을 진행하게 하여줍니다 <br><br>

### 설치
트위터 크롤러는 파이썬3를 통해 작성되었으며 셀레늄 패키지를 활용하였습니다.<br><br>
먼저 해당 프로그램을 git clone을 통해 다운로드 해줍니다.
```
$git clone https://github.com/ck992/twitter_crawler.git
```
그후, 해당 프로그램을 사용하기 위해서는 최신 개코드라이버가 필요합니다.<br><br>
개코드라이버 다운로드는 다음 링크를 통해 설치가 가능합니다. https://www.guru99.com/gecko-marionette-driver-selenium.html <br><br>
또한, 아나콘다(Anaconda)환경에서 제작되어서 아나콘다내 파이썬 내장 패키지외 추가 패키지를 터미널에서 pip 명령어를통해 설치 해주어야 합니다
```
$pip install selenium
$pip install beautifulsoup
```

### 실행
start.py 파일을 열어 주시면 아래의 코드가 열립니다
```
import main
# 시작 날짜, 끝나는 날짜, 단어, 언어(한국어는 ko, 영어는 en), 저장될 파일 날짜
# 끝나는 날짜는 하루 더 추가 하셔야 합니다.

# 한국어의 경우
main.main("2010-01-01","2018-12-31",'검색어',"ko","저장될 파일명")

# 영어의 경우
main.main("2010-01-01","2018-12-31",'검색어',"en","저장될 파일명")
```
자신이 원하는 검색어 및 날짜를 지정해주시면됩니다. <br><br>
코드를 실행시켜 주시면 Selenium을 통한 크롤링이 진행됩니다.

### Contact
If you have any requests, please contact: [https://ck992.github.io/](https://ck992.github.io/).

