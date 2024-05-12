# closure: 종료되어도 자원(함수 안의 변수)을 사용할 수 있는 함수
## 내부 함수: 함수 안에서 정의되는 함수
def outer(name):
    def inner():
        print(name, "님 안녕하세요!")
    
    return inner

function1 = outer("startcoding") # outer()는 inner()를 반환하고 종료됐지만, __closure__ 라는 공간에 name을 갖고 있음
function1()

## closure가 되는 세 가지 조건
### - (1) 내부 함수 (2) 외부 함수의 변수를 참조 (3) 외부 함수가 내부 함수를 반환
def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요!", sep="")
        print("나이:", age) # cf. 내부 함수에서 참조하지 않는 경우 closure tuple에 해당 변수를 위한 cell도 없음
        print("성별:", gender)
    
    return inner

function2 = greeting("김이름", 30, "남")
function2()
print(dir(function2)) # 여기서 확인한 것 중 __closure__를 이용

closure_of_function2 = function2.__closure__
print(type(closure_of_function2)) # closure_of_function2는 tuple 타입
for item in closure_of_function2:
    print(dir(item)) # 여기서 확인한 것 중 cell_contents를 이용
    print(item.cell_contents)

## 왜 사용하는가?
### - closure는 전역 변수로 대체할 수도 있겠으나,
###   식별자 중복 문제, 스코프 문제 등을 고려하여 전역 변수의 사용을 최소화해야 함
### - 하지만 데이터를 저장하는 용도로는 class 기반으로 코드를 작성하는 게 더 간편할 것
### - 그러면 왜...?
###   iterator, generator, decorator 등을 이해하는 기반이 됨
