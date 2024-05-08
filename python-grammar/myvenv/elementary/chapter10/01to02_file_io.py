# 파일 입출력

## 사용이유
## - input(), print()로는 부족하다
## - 외부 파일로부터 데이터를 불러와야하거나 데이터를 파일 형태로 저장해야한다면?

## 파일 열기 모드
## - w(쓰기 모드: 덮어 쓰기), a(추가 모드: 이어 쓰기), r(읽기 모드)
## - 과정: 파일 열기 → 파일 작업 → 파일 닫기

## 파일 쓰기
my_file = open("./myvenv/elementary/chapter10/my-data.txt", "w", encoding = "utf8") # open()으로 열게 되면 객체 형태로 불러옴 # 절대 경로를 안 잡아주면 프로젝트 루트 디렉토리를 기준으로 함
my_file.write("Python 공부")
my_file.close()

## 파일 추가(이어 쓰기)
my_file = open("./myvenv/elementary/chapter10/my-data.txt", "a", encoding = "utf8")
my_file.write("\nDjango 공부")
my_file.close()

## 파일 읽기
my_file = open("./myvenv/elementary/chapter10/my-data.txt", "r", encoding = "utf8")

### 파일 전체 읽기 read()
data = my_file.read()
print(data)
my_file.close()

### 파일 한 줄 씩 읽기 readline()
my_file = open("./myvenv/elementary/chapter10/my-data.txt", "r", encoding = "utf8")
while True:
    data = my_file.readline()
    print(data, end="")
    if data == "": # readline() 결과가 "" 공백 문자라는 것은 파일의 끝을 의미함
        break
my_file.close()

#----------------------------------#

# pickle 모듈, with 구문 및 실습
## pickle 모듈 - Python 내장 모듈
## - 파일에 Python 객체 binary data 저장 및 읽기 위해 사용

## with 구문
## - 자동으로 close 할 수 있게 해줌

## 실습
### Python 객체를 pickle로 저장
import pickle

original_data = {
    "목표1": "Python 공부",
    "목표2": "Django 공부"
}

pickle_file = open("./myvenv/elementary/chapter10/my-pickle.pickle", "wb") # wb: binary로 쓰기 # 확장자는 pickle, p, pic 가능
pickle.dump(original_data, pickle_file)
pickle_file.close()

### pickle 파일을 Python으로 가져오기

# pickled_data: dict[str, str]
# pickled_file = open("./myvenv/chapter10/my-pickle.pickle", "rb")
# pickled_data = pickle.load(pickled_file)
# print(pickled_data)
# pickle_file.close()

with open("./myvenv/elementary/chapter10/my-pickle.pickle", "rb") as pickled_file: # with 구문을 사용하면 간결
    # pickled_data = pickled_file.read() # pickle 파일은 read로 읽으면 원하는 결과를 얻지 못함 - pickle.dump()와 pickle.load()를 사용해야함
    pickled_data = pickle.load(pickled_file)
    print(pickled_data)
