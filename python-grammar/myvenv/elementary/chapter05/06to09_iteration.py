# cf. 시퀀스 자료형: 순서가 있는 자료형
# - 리스트, 문자열, range 객체, 튜플, 딕셔너리

## range 명령어: 순서열 데이터를 만들 때 사용
range(10) # 끝 인덱스(exclusive)만 명시한 경우
range(1, 10, 2) # 시작 인덱스, 끝 인덱스(exclusive), step(단계)를 명시한 경우

# 반복문: 반복해서 명령을 사용하고 싶을 때 사용

## for statement
### 사용법
### for [변수] in [시퀀스 자료형]:
### [들여쓰기][명령문]

### 리스트 사용 예시
integers = [1, 2, 3, 4]

for integer in integers:
    print(integer)

### 문자열 사용 예시
message = "hello world!"

for letter in message:
    print(letter)

### range 객체 사용 예시
for i in range(10):
    print(i)

for i in range(5, 8):
    print(i)

## while statement
### 사용법(초기식과 증감식이 있는 경우)
### [초기식]
### while [조건식]:
### [들여쓰기][반복할 명령]
### [증감식]

### 사용법(무한 루프)
### while True:
### [들여쓰기][반복문]
### [들여쓰기]if [조건식]:
### [들여쓰기][들여쓰기]break # break는 가장 가까운 반복문에서 탈출하게 함
while True:
    x = input("종료하려면 exit를 입력하세요. >>> ")
    if (x == "exit"):
        break
