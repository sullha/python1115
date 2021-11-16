# Function3.py

x=1
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    #지역변수(LGB)
    x=2
    return a+x

#호출
print(func2(1))

#기본값 세팅
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(3))
print(times(3,4))

#키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("naver.com", "80"))
print(connectURI(port="80", server="naver.com"))

#가변인자(다양한 상황)
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#정의되지 않은 인자
def userURIBuilder(sever, port, **user):
    strURL = "http://"+sever+":"+port+"/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBuilder("naver.com","80", id="kim", passwd="1234"))
print(userURIBuilder("naver.com","80", id="kim", passwd="1234",\
    name="mike"))

#람다함수(간결한 함수 표현식: 익명함수)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x)(3) )
print(globals())
