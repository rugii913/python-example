# list 타입
fruits = ["apple", "orange", "mango", "pineapple", "melon", "watermelon", "kiwi"]

## list를 다루는 여러 메서드들
### 리스트 데이터 추가
fruits.append("strawberry")
print(fruits)

### 리스트에 리스트 데이터를 추가
fruits.append(["blueberry", "guava"]) # 이게 왜 가능한지는 모르겠음...
print(fruits)

### 리스트 데이터 삭제
#### pop() 기본적인 방법
fruits.pop()
print(fruits)

#### pop([인덱스]) 인덱스를 이용한 삭제
fruits.pop(1)
print(fruits)

#### remove([데이터]) 데이터를 이용한 삭제
fruits.remove("pineapple")
print(fruits)

#### del 키워드를 이용한 삭제
del fruits[2]
print(fruits)

### 리스트 특정 값의 인덱스 구하기
orange_index = fruits.index("apple")
print(orange_index)

### 리스트 모든 요소 삭제
fruits.clear()
print(fruits)

### 리스트 정렬
numbers = [5, 1, 2, 3, 9, 7]

numbers.reverse() # cf. reverse(): 역순 정렬이 아닌 단순 뒤집기
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True) # 역순 정렬
print(numbers)

### 리스트 for .. in .. 반복문에서 인덱스 함께 출력 - enumerate([Iterable 타입]) 사용
fruits = ["apple", "orange", "mango"]

index = 1
for fruit in fruits:
    print(index, fruit)
    index = index + 1

for index, fruit in enumerate(fruits, 1): # enumerate에서 시작 index 지정 가능
    print(index, fruit)

## 리스트 내포(comprehension): for, if 등으로 리스트를 간편하게 만드는 방법
### 방법
### [[표현식] [for 변수 in 순회가능한 데이터] [if 조건식]]
### [[표현식] [else를 포함한 if문] [for 변수 in 순회가능한 데이터]]

### 예제1
word_list = ["apple", "watch", "apolo", "star", "abocado"]
result = [i for i in word_list if i[0] == "a"]
print(result)

### 예제2
items = ["오메가3", None, "비타민C500", None, "홍삼절편"]
result = [i if i != None else "" for i in items] # else가 있다면 if를 for보다 먼저 적어줘야 함
print(result)
