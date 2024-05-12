# 다양한 매개변수 종류
## 위치 매개변수 positional parameter
## - 함수 호출 시 순서대로 인자를 넘기는 것, 다른 매개변수와 쓸 때는 항상 맨 앞에 써야 함

## 기본 매개변수 default parameter
## - 매개변수의 기본적인 값을 지정한 것

## 키워드 매개변수 keyword parameter
## - 함수 호출 시 키워드를 붙여 호출, 매개변수 순서를 지키지 않아도 됨

def my_function(author: str, category: str, title: str, content="내용 없음"):
    print(author, category, title, content)

# my_function("작성자명", category="자유게시판", "아무제목") # 위치 인자가 키워드 인자 뒤에 나올 수 없기 때문에 안 됨
my_function("작성자명", category="자유게시판", title="아무제목")

# ------------------------------- #

## 가변 매개변수: 개수가 정해지지 않은 매개변수

### 위치 가변 매개변수(positional variable length parameter)
### - 매개변수 앞에 *가 붙음(튜플형)
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits("apple", "orange", "mango", "grape")

### 키워드 가변 매개변수(keyword variable length parameter)
### - 매개변수 앞에 **가 붙음(딕셔너리형)
def comment_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

comment_info(name="작성자", content="감사합니다")

# ------------------------------- #

# 매개변수 작성 순서
## 위치 - 기본 - 위치 가변 - 키워드 혹은 기본 - 키워드 가변
## - 외운다기보다는 자연스럽게 익숙해질 것, 이를 따르지 않으면 호출하는 쪽에서 오류가 발생
