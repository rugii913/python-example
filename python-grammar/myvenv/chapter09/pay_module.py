# 결제 정보, 관리 모듈
## 변수
version = 2.0

## 함수
def printAuthor():
    print("작성자")


## 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"
    
## 해당 파일을 직접 실행했을 때에만 실행되도록 하는 코드
## - 직접 실행할 경우 __name__ == "__main__"
if __name__ == "__main__":
    print("pay module 실행")

print(__name__)
