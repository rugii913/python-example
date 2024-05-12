# map: 기존 리스트를 수정해서 새로운 리스트를 만들 때
## 사용 방법
### - map([함수], [시퀀스 자료형])
###   - 시퀀스 자료형의 각 element을 인자로 함수가 동작
###   - return은 함수가 동작한 결과물을 element로 하는 map object - 이 map object를 list 같은 것으로 바꿔주면 됨
### - cf. 시퀀스 자료형: list, tuple, dictionary, range 객체 등


## 사용 예시 - 리스트 모든 요소의 공백 제거
### for문 사용
items1 = [" 마우스  ", "    키보드  "]
for i in range(len(items1)):
    items1[i] = items1[i].strip()

print(items1)

### map 사용
items2 = [" 마우스  ", "    키보드  "]
result2 = list(map(lambda x: x.strip(), items2))

print(result2)

# ------------------------------- #

# filter: 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때
## 사용 방법
### - filter([함수], [시퀀스 자료형])
###   - 시퀀스 자료형의 각 element을 인자로 함수가 동작
###   - return은 함수가 동작한 결과물을 element로 하는 filter object - 이 filter object를 list 같은 것으로 바꿔주면 됨

## 사용 예시 - 리스트에서 길이가 3 이하인 문자들만 필터링
animals = ["cat", "tiger", "dog", "bird", "monkey"]

### for문 사용
result1 = []
for animal in animals:
    if len(animal) <= 3:
        result1.append(animal)

print(result1)

### filter 사용
result2 = list(filter(lambda x: len(x) <= 3, animals))
print(result2)
