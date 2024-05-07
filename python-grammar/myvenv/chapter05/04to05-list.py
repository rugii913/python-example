# 리스트 자료형
# - array 지원하지 않음, 아마도 Python의 리스트는 ArrayList 자료구조 형태인 듯함(확인 필요)

## 리스트 만들기: 리스트명 = [데이터, ..., 데이터] → 빈 리스트도 만들 수 있음
emptyList = []
animalList = ["가물치", "벼메뚜기", "비단뱀", "도룡뇽"]

## 데이터 접근하기: 인덱스 이용
print(animalList[0])
print(animalList[-1]) # 가장 마지막 데이터
print(animalList[-2])

## 데이터 조작하기
### 추가: 리스트명.append(데이터)
animalList.append("고라니")
print(animalList)

### 수정: 리스트명[인덱스] = 데이터
animalList[1] = "청개구리"
print(animalList)

### 삭제: del 리스트명[인덱스] → del이라는 키워드를 이용
del animalList[0]
print(animalList)

### 슬라이싱: 리스트명[시작:끝 + 1] → endIndex는 exclusive
#### cf. string formatting 혹은 f-strings https://www.freecodecamp.org/korean/news/python-print-string-variable/
slicedAnimalList = animalList[0:2]
print("slicedAnimalList >>> {}".format(slicedAnimalList))
print("animalList >>> {}".format(animalList))
print(f"animalList[:] >>> {animalList[:]}") # 전체
print(f"animalList[:3] >>> {animalList[:3]}") # 시작 인덱스 생략 시 자동으로 0부터
print(f"animalList[1:] >>> {animalList[1:]}") # 끝 인덱스 생략 시 자동으로 마지막까지

### 리스트 길이: len(리스트명)
print(len(slicedAnimalList))
print(len(animalList))

### 리스트 정렬: 리스트명.sort()
slicedAnimalList.sort() # sort()의 반환값은 None임에 유의
animalList.sort(reverse=True) # 내림차순 정렬
print(slicedAnimalList)
print(animalList)
