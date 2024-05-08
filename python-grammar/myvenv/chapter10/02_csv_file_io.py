# csv(comma-separated values): 데이터가 ,(comma)로 구부된 텍스트 파일 형식(주로 표 형태 데이터)

## csv 파일 쓰기
import csv # 내장 모듈 csv 사용

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 32],
]

file = open("./myvenv/chapter10/student.csv", "w", newline = "", encoding="utf-8-sig") # Windows 사용할 경우 자동으로 한 줄 씩 개행 문자가 들어가서 이를 막기위해 newline = ""를 줌
writer = csv.writer(file)

for datum in data:
    writer.writerow(datum) # writerow() 리스트로 저장된 데이터를 한 줄 씩 저장

file.close()

## csv 파일 읽기
with open("./myvenv/chapter10/student.csv", "r", encoding="utf-8-sig") as read_file:
    reader = csv.reader(read_file)
    for datum in reader:
        print(datum)
