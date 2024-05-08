# 입력과 자료형 변환

## 입력 함수
## - input() 실행 시 입력을 기다림
## - input의 argument는 prompt 메시지임
x = input("첫번째 숫자를 입력하세요 >>> ")
y = input("두번째 숫자를 입력하세요 >>> ")
print(x + y) # 문자열 간 연산이 됨
print(type(x))

## 자료형 변환 예시: 문자열 자료형을 숫자형으로 변환
intX = int(x)
intY = int(y)
result = intX + intY
print(result)
print(type(intX))
