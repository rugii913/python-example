# 딕셔너리
## 딕셔너리의 특징
## - 시퀀스 자료형
## - 키와 데이터를 가짐

## 딕셔너리 만들기
stock = {
    "삼성전자": 50_000,
    "LG전자": 150_000,
}

## 딕셔너리 접근하기
print(stock["삼성전자"])

## 딕셔너리 수정하기
stock["삼성전자"] = 50_100
print(stock)

## 딕셔너리 삭제하기
del stock["삼성전자"]
print(stock)

## 딕셔너리 함수
### 키와 데이터 쌍
print(stock.items())
for item in stock.items():
    print(item)

### 키
print(stock.keys())
for key in stock.keys():
    print(key)

### 데이터
print(stock.values())
for value in stock.values():
    print(value)
