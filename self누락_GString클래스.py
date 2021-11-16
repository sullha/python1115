#전역변수
str = "Not Class Member"
#클래스 정의
class GString:
    #클래스 멤버 변수(서로다른 인스턴스가 공유해야할따)
    str = ""
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
        GString.str ="클래스 멤버"
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

g = GString()
g.set("First Message")
g.print()
