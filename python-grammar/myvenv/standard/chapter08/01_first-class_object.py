# 일급 객체
## - 다음을 만족하는 객체: (1) 데이터처럼 사용 가능 (2) 매개변수로 넘길 수 있음 (3) return으로 줄 수 있음
## - Python에서는 함수도 일급 객체

## (1) 데이터처럼 사용 가능
### - 함수를 변수에 할당 가능
def function1(x, y):
    return x + y

add = function1
print(add(3,4))

### - 리스트, 튜플, 딕셔너리 등에 할당 가능
def mul(x, y):
    return x * y

def div(x, y):
    return x / y

calculator = [mul, div]
print(calculator[0](5,6))
print(calculator[1](6,3))

## (2) 매개변수로 넘길 수 있음
def inputData():
    data = input("데이터 입력 >>> ")
    return data

def start(func):
    print("입력한 데이터는", func())

start(inputData)

## (3) return으로 줄 수 있음
def plusTen(a):
    return a + 10

def func():
    return plusTen

print(func()(5))
