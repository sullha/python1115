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
