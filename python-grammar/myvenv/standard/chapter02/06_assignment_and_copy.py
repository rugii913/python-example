# 할당 시 collection에서 발생하는 문제

## 파이썬에서는 데이터도 객체 - 변수가 데이터를 가리킴
## 어떤 객체를 변수 a에도 할당하고 b에도 할당 시, 복사되기 때문에 문제가 되는 경우가 있음
## 예시
x = [1, 2, 3, 4, 5]
y = x
y[2] = 0
print(x)
print(y)
print(id(x)) # id()로 메모리 주소값을 확인할 수 있음
print(id(y))

## 따라서 단순 할당이 아닌 복사가 필요한 경우가 있음
### 리스트 복사 방식
x = [1, 2, 3, 4, 5]
y = x.copy()
y[2] = 0
print(x)
print(y)
print(id(x))
print(id(y))

### 다차원(중첩) 리스트 복사 방식
import copy

x = [[1, 2], [3, 4, 5]]
y = x.copy()
z = copy.deepcopy(x)
y[0][0] = 0
z[1][0] = 0
print(x)
print(y)
print(z)
