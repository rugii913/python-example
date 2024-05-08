# 문자열 str 타입

## 문자열을 다루는 여러 메서드들
### upper(), lower(): 소문자 <-> 대문자
str1 = "Hello world!"
str2 = str1.upper()
str3 = str1.lower()

print(str2)
print(str3)

### replace(): 문자열 일부 바꾸기
str4 = "오늘 날씨는 흐림"
str5 = str4.replace("흐림", "맑음")
print(str5)

### find(): 문자열 위치 찾기, 찾는 문자열이 없으면 -1 return
index1 = str1.find("wor")
print(index1)

### count(): 문자열 개수
str6 = "Good cat is kitcat"
count1 = str6.count("cat")
print(count1)

### split(): 문자열 분리(split) # 크롤링할 때 중요
list1 = "신발 265 a1234 80000".split()
print(list1)

list2 = "신발:265:a1234:80000".split(":") # 구분자 sep 지정 가능 - 지정하지 않을 경우 whitespace character로 구분
print(list2)

### join(): 문자열 연결(join)
str7 = "".join(list1) # 구분자에 대해서 호출해야한다는 점이 특이함
print(str7)

str8 = ":".join(list1)
print(str8)

### strip(): 공백 삭제
str9 = "     Hello wor  l d!     "
print(str9.lstrip()) # 왼쪽 공백 없애기
print(str9.rstrip()) # 오른쪽 공백 없애기
print(str9.strip()) # 양쪽 공백 없애기

# ---------------------------------------- #

## 문자열 포매팅: 여러 가지 데이터들을 조합하여 문자열 만들어내기
data1 = "pen"
data2 = "pineapple"
data3 = "apple"

### format 메서드 - [인덱스]}와 format에 넘기는 인자들 사용
formatted_str1 = "hi {0} {1} {2} {0}".format(data1, data2, data3)
print(formatted_str1)

# formatted_str2 = "{} {} {} {}".format(data1, data2, data3) # 인덱스를 생략할 경우, 개수가 안 맞으면 index out of range 예외 발생
formatted_str2 = "hi {} {} {}".format(data1, data2, data3)
print(formatted_str2)

### f-string - f""와 {[변수명]} 사용
formatted_str3 = f"hi {data1} {data2} {data3} {data1}"
print(formatted_str3)
