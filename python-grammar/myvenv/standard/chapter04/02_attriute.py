# 속성

## 별도 참고  https://076923.github.io/posts/Python-37/  https://good.oopy.io/clean-code/property-and-attributes
## - 파이썬의 멤버 변수, 멤버 함수는 attribute(속성)라 하는 듯함, property와는 다름

## 인스턴스 속성: 객체마다 다르게 가지는 속성

## 클래스 속성: 모든 객체가 공유하는 속성

## 비공개 속성: 클래스 안에서만 접근 가능한 속성

## 예시
class Post:
    count = 0

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.title_and_content = title + content
        self.__private_attribute = "비공개 속성" # 비공개 속성은 앞에 _ 두 개를 붙임
        Post.count += 1

    def __str__(self):
        return f"제목: {self.title}, 내용: {self.content}"

post1 = Post("제목1", "내용1")
print(post1)
print(Post.count)

### 인스턴스 속성 수정
post1.title = "제목 수정"
print(post1)
print(Post.count)

post2 = Post("제목2", "내용2")
print(post2)
print(Post.count)

### 비공개 속성에는 보통의 방법으로 접근할 수 없음
# print(post2.__private_attribute) → AttributeError: 'Post' object has no attribute '__private_attribute'. Did you mean: '_Post__private_attribute'?
### - name mangling: 하지만 Python에서는 비공개 속성이라고 해도 접근할 수 있음, 네임 맹글링을 통해 접근하기 귀찮게 만들어둔 것뿐임
print(post2._Post__private_attribute)
post2._Post__private_attribute = "말만 비공개 속성이지 사실 접근(조회, 수정) 가능하다"
print(post2._Post__private_attribute)
