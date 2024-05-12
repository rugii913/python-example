# re 모듈 및 match 객체
import re

## re 모듈의 메서드: match(), search(), findall(), finditer(), fullmatch()
str1 = "love people around you, love your work, love yourself"

### 1) match(): 문자열의 처음부터 검색 - return 1개의 match 객체
result1_1 = re.match("love", str1)
print(result1_1)

result1_2 = re.match("work", str1)
print(result1_2)

### 2) search(): 문자열의 전체를 검색 - return 1개의 match 객체
result1_3 = re.search("work", str1)
print(result1_3)

### 3) findall(): 문자열의 전체를 검색 - return 문자열 리스트
result1_4 = re.findall("love", str1)
print(result1_4)

### 4) finditer(): 문자열의 전체를 검색 - return match 객체 iterator
result1_5 = re.finditer("love", str1)
print(result1_5)
for result in result1_5:
    print(result)

### 5) fullmatch(): 패턴과 문자열이 완벽하게 일치하는지
result1_6 = re.fullmatch("love people around you, love your work, love yourself", str1)
print(result1_6)

result1_7 = re.fullmatch("love", str1)
print(result1_7)

result1_8 = re.fullmatch("love[a-z,\s]*self", str1)
print(result1_8)

## match 객체의 메서드: group(), start(), end(), span()
result2 = re.search("people", str1)

### 1) group(): 매칭된 문자열을 반환
print(result2.group())

### 2) start(): 매칭된 문자열의 시작 위치 반환
print(result2.start())

### 3) end(): 매칭된 문자열의 끝 위치 반환
print(result2.end())

### 4) span(): 매칭된 문자열의 (시작, 끝) 위치 튜플 반환
print(result2.span())

## 예제 - 전화번호 형식을 검사하는 정규표현식 - cf. 연습 사이트 https://regexr.com/63bls
### 1-1) group 하나만 매칭
str3 = "010-1234-5678"
result3 = re.match("\d{2,3}-(\d{3,4})-(\d{4})$", str3)
print(result3.group())
print(result3.group(0)) # 아무것도 적지 않은 것과 같음
print(result3.group(1))
print(result3.group(2))

### 1-2) group 여러 개 매칭
str4 = "010-1234-5671,010-1234-5672,010-1234-5673,010-1234-5674,010-1234-5675,010-1234-5676"
result4 = re.finditer("\d{2,3}-\d{3,4}-(\d{4})(?=,|$)", str4)
for idx, result in enumerate(result4, 1):
    print(f"{idx}: {result.group(1)}")

### 2) substitution(교체)
str5 = "010-1234-5678"
# result5 = re.sub("(?<=\d{2,3}-\d{3,4}-)\d{4}", "****", str5) # cf. 후방 탐색 시 범위는 고정이어야 함(fixed width), 전방 탐색 시에는 변동 범위 고정어도 됨
result5 = re.sub("(?<=\d{3}-\d{4}-)\d{4}", "****", str5)
print(result5)

## 예제 - YYYY/MM/DD 형식 날짜 검사, 연도는 4자리 숫자, 월은 01~12, 일은 01~31까지 가능
## - cf. 연습 사이트 https://regexr.com/63cii
data1 = [
    "2022/08/08",
    "1000/01/01",
    "9999/12/31",
    "900/02/02",
    "12000/10/26",
    "2021/13/01",
    "2023/2/02",
    "2024/06/3",
    "2023/06/35",
]

regex1 = "^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"

for datum in data1:
    matchObj = re.match(regex1, datum)
    result = (lambda x: True if x != None else False)(matchObj)
    print(f"{datum} {result}")

## 예제
## - 이메일 형식 검사
##   - 이메일은 ID@host 형식
##   - ID 파트는 영문 대소문자, 숫자, 특수문자(-_)만 가능
##   - host 파트는 영문 대소문자, 숫자, 특수문자(-)만 가능
##   - host 파트는 2개 이상의 도메인으로 구성될 수 있음(ex. co.kr)
## - cf. 연습 사이트 https://regexr.com/63ckh
data2 = [
    "startcoding@maver.com",
    "start-coding@maver.com",
    "start_coding@maver.co.kr",
    "startcoding@k-mail.com",
    "@maver.com",
    "startcoding?@k-mail.com",
    "startcoding@k-mail",
    "startcoding@maver",
]

# 이전 예제에서는 이런 방식으로 했지만, for 안에서 정규표현식 패턴을 넘기면 매번 컴파일해야함
# - 따라서 미리 컴파일 해주는 것이 좋다
# regex2 = "^[\w\-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# for datum in data2:
#     matchObj = re.match(regex2, datum)
#     result = (lambda x: True if x != None else False)(matchObj)
#     print(f"{datum} {result}")

regex2 = re.compile("^[\w\-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

for datum in data2:
    matchObj = regex2.match(datum)
    result = (lambda x: True if x != None else False)(matchObj)
    print(f"{datum} {result}")
