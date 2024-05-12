# decorator

## decorator: 함수의 앞, 뒤로 부가적인 기능을 적용 → ex. 로깅, 권한 체크, ...
## decorator 작성 방법
## - closure를 이용하여 생성
## - 적용하고 싶은 함수 앞에 @[decorator] 
## - cf. 앞서 @staticmethod, @abstractmethod에서도 사용했었음

# ------------------------------------------------------------ #

## decorator 예시 1 - decorator를 사용하지 않았을 때와 비교, parameter가 없는 케이스
### decorator를 사용하지 않은 경우
def print_hello():
    print("함수 시작")
    print("hello hello")
    print("함수 끝")

def print_bye():
    print("함수 시작")
    print("bye bye")
    print("함수 끝")

### decorator를 사용하는 경우 - 중복 로직 제거에 도움이 됨
def logger(func):
    def wrapper():
        print("함수 시작")
        func() # 대상 함수 실행
        print("함수 끝")
    return wrapper

@logger
# decorator로 지정된 함수를 찾은 뒤, decorator가 붙은 함수(여기서는 print_hello2)를 decorator의 인자로 넘김
# decorator가 붙은 함수를 실행할 때 실제로는 decorator에서 return한 함수를 실행함
def print_hello_decorated():
    print("hello hello hello")

# 다음 두 결과를 비교할 것
print(print_hello) # <function print_hello1 at 0x00...>
print(print_hello_decorated) # <function logger.<locals>.wrapper at 0x00...>

@logger
def print_bye_decorated():
    print("bye bye bye")

print_hello_decorated()
print_bye_decorated()

# ------------------------------------------------------------ #

## decorator 예시 2 - parameter가 있는 케이스
def logger_with_parameters(func):
    def wrapper(*args): # parameter가 하나 밖에 없다면 *args가 아니라 arg로 받아도 됨
        print("함수 시작")
        func(*args) # 대상 함수 실행
        print("함수 끝")
    return wrapper

@logger_with_parameters
# decorator로 지정된 함수를 찾은 뒤, decorator가 붙은 함수(여기서는 print_hello2)를 decorator의 인자로 넘김
# decorator가 붙은 함수를 실행할 때 실제로는 decorator에서 return한 함수를 실행함
def print_hello_decorated_with_parameters(name, message):
    print("hello hello hello", name)
    print(message)


@logger_with_parameters
def print_bye_decorated_with_parameters(name, message):
    print("bye bye bye", name)
    print(message)

print_hello_decorated_with_parameters("김이름", "아무 메시지를 넘긴다")
print_bye_decorated_with_parameters("이이름", "두 번째 인자")
