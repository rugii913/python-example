# 람다 함수

## 람다 함수 정의 방법
### 람다 함수
lambda a: a-1

### 기존 함수와 비교
def minus_one_original(a):
    return a-1

# ---------------------------------- #

## 람다 함수 호출 방법
### (1) 함수 자체를 호출
result1 = (lambda a: a-1)(10)
print(result1)

### (2) 람다 함수를 변수에 담은 후 호출
minus_one = lambda a: a-1
result2 = minus_one(100)
print(result2)

# ---------------------------------- #

## if가 있는 lambda 함수 정의 및 호출
## - cf. 람다 함수에서 if를 쓸 경우 항상 else까지 같이 적어야 함
result3 = (lambda a: True if a > 0 else False)(-1)
print(result3)

is_positive = lambda a: True if a > 0 else False
result4 = is_positive(1)
print(result4)
