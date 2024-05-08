# raise 구문
# 예외 계층 구조 - 예외 클래스 간 상속 관계
# 예외 클래스 만들기 - Exception을 상속

class PositiveNumberInputException(Exception):
    def __init__(self):
        super().__init__("양수 입력 불가") # 에러 메시지 지정 가능

try:
    num = int(input("음수를 입력해주세요 >>> "))
    if num >= 0:
        raise PositiveNumberInputException
except PositiveNumberInputException as error:
    print("에러 발생!", error)
