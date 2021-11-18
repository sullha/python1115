# web1.py

from bs4 import BeautifulSoup

#페이지를 로딩: 연속으로 메서드 체인, 함수 체인
page = open("C:\\work\\test01.html","rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체를 보여달라~
#print(soup.prettify())

#<p>를 몽땅 검색 ==> List형식으로 리턴
#print( soup.find_all("p") )

#첫번째 <p> 검색
#print( soup.find("p"))

#필터링:<p class="outer-text">
#파이썬에서 클래스를 정의하는 키워드가 class이므로 겹치니까 언더바를붙엿음
print( soup.find_all("p", class_="outer-text") )