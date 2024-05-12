# generator

## generator? iterator를 간편하게 만드는 함수 - 클래스를 이용해 만들 필요가 없음
### 생성 방법: 함수에서 yield를 사용
### 특징
### - 함수 안에 yield를 사용(return과 비교)
### - generator 표현식 사용 가능 - list 내포(comprehension)와 유사
### - 효율적인 메모리 사용 → 대용량 데이터 처리에서 사용하기 좋음

# ------------------------------------ #

## generator 예시 1
def season_generator(*args):
    for arg in args:
        yield arg # yield는 return을 지연된 상태로 두다가 __next__()를 호출하면 하나 씩 꺼내줌

generator1 = season_generator("spring", "summer", "autumn", "winter")
print(generator1) # 출력 결과 <generator object season_generator at 0x00...>
# generator는 특수한 iterator로 볼 수 있음 → __iter__와 __next__를 가짐
print(generator1.__iter__)
print(generator1.__next__)
print(generator1.__next__())
print(generator1.__next__())
print(generator1.__next__())
print(generator1.__next__())
# print(generator1.__next__()) # StopIteration 에러

# ------------------------------------ #

## generator 예시 2
def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번째 작업 중...")
    yield 2
    
    print("세번째 작업 중...")
    yield 3

generator2 = func()
print(generator2.__next__())
generator2.__next__()
generator2.__next__()
# print(generator2.__next__()) # StopIteration

# ------------------------------------ #

## generator 표현식 - list comprehension과 유사
list_comprehension_ex = [i * 2 for i in range(1,10)]
print(list_comprehension_ex)

generator3 = (i * 2 for i in range(1,10))
print(generator3)

# ------------------------------------ #

## generator를 이용한 효율적인 메모리 사용
## - list vs. generator 비교

import sys

list_data = [i * 3 for i in range(1, 10_000 + 1)]
generator_data = (i * 3 for i in range(1, 10_000 + 1))

print(sys.getsizeof(list_data)) # 데이터 저장에 필요한 메모리를 모두 사용
print(sys.getsizeof(generator_data))
# 데이터를 미리 계산하지 않고 __next__()가 호출될 때마다 값을 내놓음
# → 대용량 데이터를 처리하는 데이터 분석, 인공 지능 분야에서는 generator를 필수적으로 사용함
