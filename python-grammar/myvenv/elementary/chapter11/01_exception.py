# 예외 처리

## 필요한 이유: 프로그램 실행 중에 발생하는 에러를 미리 방지

## try - except 구문
## - try: 예외가 발생할 수 있는 코드
## - except: 예외 발생 시 실행할 코드
## - else: 예외 발생하지 않는 경우 실행할 코드 - 자주 사용하지 않음
## - finally: 항상 실행할 코드(리소스 반환 등)

## 예시: 원화 입력, 환율 입력 → 달러 값

won = input("원화 금액을 입력하세요 >>> ")
exchange_rate = input("환율을 입력하세요 >>> ")

try: # 예외 발생 가능 코드
    print(int(won) / int(exchange_rate))
# except:
except ValueError as error: # 잡는 예외 명시 가능
    print("문자열 입력 예외 발생", error)
except ZeroDivisionError: # 여러 예외 처리 구문 지정 가능
    print("0으로 나누기 예외 발생")
else:
    print("예외가 발생하지 않은 경우")
finally: # 주로 리소스 반환 시 사용
    print("예외에 상관 없이 항상 실행되는 코드")

print("프로그램 종료 체크")
