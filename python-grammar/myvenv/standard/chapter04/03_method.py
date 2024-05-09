# 메서드

## 인스턴스 메서드
## - 인스턴스 속성에 접근
## - 항상 첫번째 파라미터가 self

## 클래스 메서드
## - 클래스 속성에 접근
## - 클래스를 의미하는 cls를 파라미터로 받음
## - 데코레이터 @classmethod로 표시

## 정적 메서드
## - 인스턴스를 만들 필요가 없는 메서드
## - 파라미터 self, cls 같은 것을 쓸 필요 없음
## - 메서드가 인스턴스 유무 관계 없이 독립적으로 사용될 때
## - 데코레이터 @staticmethod로 표시

## 매직 메서드
## - 클래스 안에 정의할 수 있는 특별한 메서드
## - 특별한 상황에 호출
## - __이름__ 형태  cf. __init__()도 매직 메서드

import time

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
    
    def check_title_is_not_empty(self):
        return len(self.title) > 0

    def check_content_length_is_longer_than_10(self):
        return len(self.title) > 10
    
    @classmethod # @classmethod를 붙이지 않으면, argument가 없는 꼴이 되므로 Post.print_count() 이런 식으로 호출할 수 없음
    def get_post_count(cls):
        return cls.count

    @staticmethod
    def get_current_time():
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

post1 = Post("제목1", "제목2")
print(post1.check_title_is_not_empty())
print(post1.check_content_length_is_longer_than_10())
print(Post.get_post_count())
print(Post.get_current_time())
print(dir(post1)) # dir() 객체의 멤버들 확인 가능
print(post1.__dir__())
